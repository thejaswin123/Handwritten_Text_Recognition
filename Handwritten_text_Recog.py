#!/usr/bin/env python
# coding: utf-8

# In[29]:


from tkinter import *
from tkinter import filedialog
import fpdf
import cv2
import numpy as np

from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pytesseract
# Path of working folder on Disk

def browseFiles():
    py=r"*.png *.jpg *jpeg"
    global result
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("images",py),
                                                                                                ("all files","*.*")))
    if filename == "":
        return
    
    # Read image with opencv
    img = cv2.imread(filename)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    

    # Write the image after apply opencv to do some ...
    cv2.imwrite(filename, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(filename))

    # Remove template file
    label_file_explorer.configure(text=result)
    
    

def pdf():
    global result
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.write(5,result)
    pdf.ln()
    pdf.output("converted.pdf")

window = Tk()
  
# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("700x350")
reg_info = Label(window,text = "Handwritten Text Recognition Using Pytesseract",width='80',height='2',font= ("ariel",12,"bold"),fg = "black",bg='lightgrey')
reg_info.place(x=370,y=18,anchor='center')  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "See the Output Here",font= ("ariel",10,"bold"),
                            width = 90, height = 12,
                            fg = "blue")
  
label_file_explorer.place(x=0,y=35) 

button_explore = Button(window,
                        text = "Browse Files",fg="white",bg="black",font= ("ariel",10,"bold"),width=10,
                        command = browseFiles)
button_explore.place(x=250,y=270)

text=Label(window,text="(Select an image)",bg="white",fg="black",font= ("ariel",8,"bold"))
text.place(x=242,y=300)

button1 = Button(window,
                        text = "convert text to pdf",fg="white",bg="black",font= ("ariel",10,"bold"),width=15,
                        command = pdf)
button1.place(x=370,y=270)

window.mainloop()

from difflib import SequenceMatcher
if result is not None:
    s="We start With good\n\nBecause all businesses should\n\nbe doing something good"
    s1=result
    def similar(a, b):
        return "\nThe accuracy of the model is "+str(SequenceMatcher(None, a, b).ratio()*100)+"%\n"
    print(similar(s,s1))
    result=None


# In[ ]:




