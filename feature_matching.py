from flask import Flask, jsonify 
import cv2
import os
import difflib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import urllib.request

def feature_matching(url1, url2, flag):
    def dl_jpg(urlt, file_name):
        full_path = file_name + '.jpg'
        urllib.request.urlretrieve(urlt, full_path)

    def match_image(img1, img2):
        text1 = pytesseract.image_to_string(img1, lang='eng')
        text2 = pytesseract.image_to_string(img2, lang='eng')
        pwt = difflib.SequenceMatcher(None,text1,text2).ratio()
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)              #clicked image
        kp2, des2 = orb.detectAndCompute(img2, None)              #database image
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        matches = bf.match(des1, des2)
        val1 = len(kp1)
        val3 = len(matches)
        pct = (val3/val1)*100 
        if(pct>50 or pwt>80):
            return True
        else:
            return False

    dl_jpg(url1, 'img1')
    img1 = cv2.imread('img1.jpg', 0)
    img1 = cv2.resize(img1, (500,500))
    dl_jpg(url2, 'img2')
    img2 = cv2.imread('img2.jpg', 0)
    img2 = cv2.resize(img2, (500,500))
    if(match_image(img1, img2)):
        flag=1
    else:
        flag=0
    os.remove('img2.jpg')
    os.remove('img1.jpg')
    if(flag == 0):
        return False
    else:
        return True
