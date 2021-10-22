# text-extracter
a very simple python script will extract the text from photos

## installation
!pip install pytesseract

## useage
Copy your photo, and edit the main.py file, 
change this line for whatever you need, back to your photo name: 
image_file = 'test.jpg'
then, run the main file... 
python main.py
## important thing
I can't remember how many plugins was installed, but try these things: 
in this line: 
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
have the path for Tesseract-OCR, cinclude your instalation directory, , then the ext file after, like i did above. 

and, this line will extract the english text: 
print(pytesseract.image_to_string(Image.open(image_file), lang='eng').replace(' ', ''))
change lang='eng' to anytrhing you want.please back to this thing: 
TO know the language list will be found from this code: 
print(pytesseract.get_languages(config=''))
