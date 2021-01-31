from PIL import Image

# An RGB pixel is a tuple of 3 numbers each in the range [0, 255]
MAX_PIXEL_VALUE = 255
# The characters in this string are ordered from thinnest to boldest, which
# means darkest to brightest for white text on a dark terminal background
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# Now we reverse the ASCII_CHARS string to be lightest to darkest
# ASCII_CHARS = ASCII_CHARS[::-1]
# Track the width & height of the image
width, height = 0, 0

def load_image(filename='images/plane.jpg') -> Image:
    img = Image.open(filename)
    global width, height
    width, height = img.size  # plane.jpg is 640 x 480
    # Reduce image size 16x to ensure fit on terminal screen
    width, height = width // 4, height // 4
    img = img.resize((width, height))
    # print('Successfully loaded image!')
    # print('Image size: {} x {}'.format(*img.size))
    return img


def get_pixel_matrix(img):
    # width, height = img.size
    pixels = list(img.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    # print('Successfully constructed pixel matrix!')
    # print('Pixel matrix size: {} x {}'.format(len(pixels[0]), len(pixels)))
    # print('First 10 cells in matrix:\n', pixels[0][:10])
    return pixels


def get_pixel_brightness_matrix(pixel_matrix):
    """
    Convert each RGB tuple of a pixel matrix into a brightness number matrix.

    Parameters:
            pixel_matrix (list): A 2D matrix of RGB tuples

    Returns:
            pixel_brightness_matrix (list): A 2D matrix of brightness values

    There are numerous ways to convert RGB to brightness, all generating a
    slightly different style of transformed image. Here are 3 examples:
    Average (average the R, G and B values):
        -> (R + G + B) / 3
    Lightness (average the maximum and minimum values out of R, G and B):
        -> max(R, G, B) + min(R, G, B) / 2
    Luminosity (take weighted average of RGB to account for human perception):
        ->  0.2126 * R + 0.7152 * G + 0.0722 * B

    More information can be found here:
    https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color
    """
    def get_pixel_brightness(rgb_tuple):
        # Use Luminosity
        r, g, b = rgb_tuple
        # return (r + g + b) / 3
        # return (max(r, g, b) + min(r, g, b)) / 2
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    pixel_brightness_matrix = [list(map(get_pixel_brightness, row)) for row in pixel_matrix]
    # print('Successfully constructed pixel brightness matrix. First row:')
    # print(pixel_brightness_matrix[0])
    return pixel_brightness_matrix


def normalize_brightness_matrix(brightness_matrix):
    normalized_brightness_matrix = []
    min_pixel = min(map(min, brightness_matrix))
    max_pixel = max(map(max, brightness_matrix))
    brightness_range = float(max_pixel - min_pixel)
    for row in brightness_matrix:
        normalized_row = []
        for p in row:
            new_p = MAX_PIXEL_VALUE * ((p - min_pixel) / brightness_range)
            normalized_row.append(new_p)
        normalized_brightness_matrix.append(normalized_row)

    return normalized_brightness_matrix


def get_ascii_matrix(brightness_matrix):
    ascii_matrix = [[None] * width for _ in range(height)]

    for x in range(height):
        for y in range(width):
            idx = round((brightness_matrix[x][y] / MAX_PIXEL_VALUE) * len(ASCII_CHARS))
            idx -= 1 if idx >= 1 else 0
            ascii_matrix[x][y] = ASCII_CHARS[idx]
    # print('Successfully constructed ascii character matrix. First row:')
    # print(ascii_matrix[0])
    return ascii_matrix


def print_ascii_art(ascii_matrix):
    for x in range(height):
        for y in range(width):
            # The height of terminal characters is 3 times the width.
            # So print the char 2x or 3x times to reasonably fit the screen.
            char = ascii_matrix[x][y]
            print(char+char, sep='', end='')
        print()


def main():
    # Load image using Pillow
    img = load_image('images/plane.jpg')
    # Load the image's pixel data into a 2D array
    pixel_matrix = get_pixel_matrix(img)

    # Now convert the RGB tuple (pixel) matrix into a pixel brightness matrix
    pixel_brightness_matrix = get_pixel_brightness_matrix(pixel_matrix)
    # Normalize the pixel brightness values
    pixel_brightness_matrix = normalize_brightness_matrix(pixel_brightness_matrix)

    # Now convert the pixel brightness matrix to an ascii character matrix
    ascii_matrix = get_ascii_matrix(pixel_brightness_matrix)
    # Print ascii art to the terminal
    print_ascii_art(ascii_matrix)


if __name__ == '__main__':
    main()
