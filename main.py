import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

from PIL import Image
image_file = 'test.jpg'
print(pytesseract.image_to_string(Image.open(image_file), lang='eng').replace(' ', ''))
