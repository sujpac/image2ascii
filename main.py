from PIL import Image

# Load image using Pillow
img = Image.open('plane.jpg')
print('Successfully loaded image!')
print('Image size: {} x {}'.format(*img.size))  # 640x480

# Load the image's pixel data into a 2D array
width, height = img.size
pixels = list(img.getdata())
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print('Successfully constructed pixel matrix!')
print('Pixel matrix size: {} x {}'.format(len(pixels[0]), len(pixels)))
print('First 10 cells in matrix:\n', pixels[0][:10])

# Now convert the RGB tuple (pixel) matrix into a pixel brightness matrix
def get_pixel_brightness(rgb_tuple):
    """
    This method converts an RGB tuple of the pixel array into a single
    brightness number. There are numerous ways to do this, all resulting in a
    slightly different style of transformed image. Here are 3 examples:
    Average: (for now we will use this)
        Average the R, G and B values
        => (R + G + B) / 3
    Lightness:
        Average the maximum and minimum values out of R, G and B
        => max(R, G, B) + min(R, G, B) / 2
    Luminosity:
        Take a weighted average of the R, G and B values to account for
        human perception
        => 0.21 R + 0.72 G + 0.07 B

    More information can be found here:
    https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color
    """
    return (rgb_tuple[0] + rgb_tuple[1] + rgb_tuple[2]) / 3

pixel_brightness_matrix = [list(map(get_pixel_brightness, row)) for row in pixels]
print('Successfully constructed pixel brightness matrix. First row:')
print(pixel_brightness_matrix[0])

# Now convert the pixel brightness matrix to an ascii character matrix
ascii_matrix = [[None] * width for _ in range(height)]
# The characters in this string are ordered from thinnest to boldest, which
# means darkest to brightest for white text on a dark terminal background
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for x in range(height):
    for y in range(width):
        idx = round((pixel_brightness_matrix[x][y] / 255) * len(ascii_chars)) - 1
        idx = 0 if idx < 0 else idx
        ascii_matrix[x][y] = ascii_chars[idx]
print('Successfully constructed ascii character matrix. First row:')
print(ascii_matrix[0])

# # Print ascii art to the terminal
# for x in range(height):
#     for y in range(width):
#         print(ascii_matrix[x][y], sep='', end='')
#     print()
