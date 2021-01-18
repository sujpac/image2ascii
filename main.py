from PIL import Image

img = Image.open('plane.jpg')
print('Successfully loaded image!')
print('Image size: {} x {}'.format(*img.size))  # 640x480

width, height = img.size
pixels = list(img.getdata())
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print('Successfully constructed pixel matrix!')
print('Pixel matrix size: {} x {}'.format(len(pixels[0]), len(pixels)))
print('First 10 cells in matrix:\n', pixels[0][:10])
