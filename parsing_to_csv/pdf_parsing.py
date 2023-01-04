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

