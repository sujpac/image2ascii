from PIL import Image

img = Image.open('plane.jpg')
print('Successfully loaded image!')
print('Image size: {} x {}'.format(*img.size))
