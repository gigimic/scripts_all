from PIL import ImageColor
from PIL import Image

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
# Color details are available here: https://nostarch.com/automatestuff2/

image_open = Image.open('peacock.jpeg')
print(image_open.size)
width_image, height_image = image_open.size

# image details
print('width and height of image  ', width_image, height_image)
print('image filename  ',image_open.filename)
print(image_open.format)
print(image_open.format_description)

# cropping an image 
croppedIm = image_open.crop((70, 30, 210, 150))
croppedIm.save('cropped.png')

# creating simple images 
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (120, 20))
im2.save('transparentImage.png')

image_zebra = Image.open('zebra.jpg')
image_zebra.transpose(Image.FLIP_LEFT_RIGHT).save('zebra_horizontal_flip.png')
image_zebra.transpose(Image.FLIP_TOP_BOTTOM).save('zebra_vertical_flip.png')

print('Done')