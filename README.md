# HandWritten Text Recognition

## Introduction

This project aims to Extract Handwritten text from an image of any format(png,jpg,jpeg) and project is done using tesseract-OCR, OpenCV and tkinter. Optical Character Recognition (OCR) Systems aim to recognize text and bring it to editable form from the given document image, where the input text can be in machine printed, hand written or hand printed form.

## Dependencies

* [Python 3](https://www.python.org/)
*  [OpenCV](https://opencv.org/)

If you dont have Python installed in your PC ,it can be installed from here [python](https://www.python.org/downloads/).

- Hit the command in CMD/Terminal if you don't have it already installed:

      pip install opencv-python

   (OR)
   
  Install OpenCV via anaconda
  
      conda install -c menpo opencv
    
- Install Tesseract-OCR from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
  The latest installers can be downloaded here:

   - [tesseract-ocr-w32-setup-v5.0.0-alpha.20210506.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0-alpha.20210506.exe) (32 bit) and
   - [tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe) (64 bit) resp.

-  Install fpdf library,a library for PDF document generation
     
       pip install fpdf
 
## How to run the code
1. Clone the Repository and extract the files
2. Make sure the teserract-ocr file set in path `C:\Program Files\Tesseract-OCR\tesseract.exe`
3. Run the code in [jupyter](https://jupyter.org/install) to have better experience

## Outcome:
The outcome the project is :
-	To extract the text from the given input image file  .
-	To display the extracted text from that image with accuracy of 0.7-0.8 .

## Exceptions considered:
-	The accuracy considered is around 0.75 - 0.80 so more than that is model cant predict
-	The language considered for the text extraction is english other than that we cant use any other language.
-	The image should be captured properly without any disturbances.

**You can also try run the code in Colab and link to the notebook is given below**
https://colab.research.google.com/drive/1JOufSBv20vgO3j6FJN6FnhcSzmkBNXn7?usp=sharing

## Output
![image](https://user-images.githubusercontent.com/52855622/123369164-dfb82800-d59a-11eb-9a8b-c108b7568b2e.png)
