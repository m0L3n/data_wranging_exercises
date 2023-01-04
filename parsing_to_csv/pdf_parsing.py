import os
from pdf2image import convert_from path
import glob
import cv2
import pztesseract

#source data from:
# https://files.stlouisfed.org/files/htdocs/publications/page1-econ/2020/12/01/ \unemployment-insurance-a-tried-and-true-safety-net_SE.pdf

name_pdf='SafeyNet'
source_pdf= 'data/'+name_pdf+'.pdf'

# if folder with the same name does not exist, create on.
if os.path.isdir(name_pdf) == False:
    target_folder = os.mkdir(name_pdf)

# store all the pages of the PDF in a variable
pages = convert_from_path(source_pdf, 300)
# loop through all the  pages, enumerating them so that the page number can be used to label the resulting images
for page_num, page in enumerate(pages):
    # create filenames for each page image, combining the folder name and the page number
    filename = os.path.join(name_pdf, "p" + str(page_num) + ".png")
    # save the image of the page in system
    page.save(filename, 'PNG')

#loop throw all files with .png
for img_file in glob.glob(os.path.join(name_pdf, '*.png')):
    # replace the slash in the image's filename with a dot
    temp_n = img_file.replace("/",".")
    # pull the unique page name from the `temp_name`
    text_filename = temp_n.split(".")[1]
    # create output file with name of the image as .txt
    output_file = open(os.path.join(name_pdf,text_filename+".txt"), "w")
    # use the `cv2` library to interpret image
    img = cv2.imread(img_file)
    # create a new variable to hold the results of pytesseract's `image_to_string()` function
    converted_text = pytesseract.image_to_string(img)
    # write text to our output file
    output_file.write(converted_text)
    # close
    output_file.close()
