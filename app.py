from google_images_download import google_images_download
import sys
import cv2
import os
import json
from dbr import DynamsoftBarcodeReader
dbr = DynamsoftBarcodeReader()
dbr.initLicense('LICENSE-KEY')


def decodeFile(fileName, templateName=""):
    # 1D, PDF417, QRCODE, DataMatrix, Aztec Code
    barcodeTypes = 0x3FF | 0x2000000 | 0x4000000 | 0x8000000 | 0x10000000
    results = dbr.decodeFile(fileName, barcodeTypes, templateName)

    for result in results:
        print("Format: " + result[0])
        print("Value: " + result[1])


def read_folder(folder):
    for f in os.listdir(folder):
        print("-------------------------------------------------\n")
        print(f)
        decodeFile(os.path.join(folder, f))


if __name__ == "__main__":

    keyword = "barcode on box"
    response = google_images_download.googleimagesdownload()  

    arguments = {"keywords": keyword, "limit": 10, "format": "jpg", "usage_rights": "labeled-for-reuse", "time_range": '{"time_min": "01/01/2010", "time_max": "01/01/2019"}'}  
    paths = response.download(arguments) 

    images = paths[0][keyword]

    for filename in images:
            print("-------------------------------------------------\n")
            print(filename)
            decodeFile(filename)
            
    # read_folder(os.path.join(os.getcwd(), 'downloads', keyword))
