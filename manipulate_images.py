from PIL import ImageColor
from PIL import Image

# manipulating images in python
# section 1: getting image details
# section 2: cropping an image
# section 3: create a simple image 
# section 4: rotate and flip images
# https://automatetheboringstuff.com/2e/chapter19/ 

print(ImageColor.getcolor('red', 'RGBA'))
print(ImageColor.getcolor('RED', 'RGBA'))
print(ImageColor.getcolor('Black', 'RGBA'))
print(ImageColor.getcolor('chocolate', 'RGBA'))
print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
# Color details are available here: https://nostarch.com/automatestuff2/

image_open = Image.open('peacock.jpeg')
print(image_open.size)
width_image, height_image = image_open.size

# section 1: image details
print('width and height of image  ', width_image, height_image)
print('image filename  ',image_open.filename)
print(image_open.format)
print(image_open.format_description)

# section 2: cropping an image 
croppedIm = image_open.crop((70, 30, 210, 150))
croppedIm.save('cropped.png')

# section 3: creating simple images 
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (120, 20))
im2.save('transparentImage.png')

# section 4: rotate and flip images 
image_zebra = Image.open('zebra.jpg')

image_zebra.rotate(6).save('zebra_rotated6.png')
image_zebra.rotate(-16, expand=True).save('zebra_rotated6_expanded.png')


image_zebra.transpose(Image.FLIP_LEFT_RIGHT).save('zebra_horizontal_flip.png')
image_zebra.transpose(Image.FLIP_TOP_BOTTOM).save('zebra_vertical_flip.png')

print('Done')