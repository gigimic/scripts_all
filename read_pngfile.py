# tesseract ocr github
# sudo apt-get install tesseract-ocr
# tesseract test.png output.txt  //on the prompt
# PIL: python image library

# pip3 install pillow pytesseract

from PIL import Image
import pytesseract

im = Image.open("test5.jpg")
text =pytesseract.image_to_string(im, lang="eng") 
print(text)
# print(pytesseract.image_to_string(Image.open("test.png"), lang="eng"))
