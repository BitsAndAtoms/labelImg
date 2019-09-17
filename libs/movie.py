# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:43:16 2019

@author: drink
"""

# importing OpenCV(cv2) module 

import cv2 
import numpy as np
import pdb
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#from PIL import Image
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from skimage import morphology
from PIL import Image
plt.tight_layout()
plt.show()
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

class Movie():
 
    def __init__(self, filename):
        self.vid = cv2.VideoCapture(filename)
        self.currentImage=None
        self.totalFrames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.vid.get(cv2.CAP_PROP_FPS)
        self.currentImageNum = 0;
        self.currentObjectIndex = None;
    
    
    def returnImageBasedOnMiniSlider(self,index):
        self.vid.set(cv2.CAP_PROP_POS_FRAMES,index)
        ret, frame = self.vid.read()
        return frame
    
    def returnImageBasedOnSlider(self):
         self.vid.set(cv2.CAP_PROP_POS_FRAMES,self.currentImageNum)
         ret, frame = self.vid.read()
         return frame
         #return QImage(self.img.data, N, M, bytesPerLine, QImage.Format_RGB888)
        # return QImage.fromData(self.img.data)    
     #return QImage(img2.data, N, M, bytesPerLine,QImage.Format_Grayscale8)
     
    def returnMovieFinalFrame(self):
         return self.totalFrames

    def returnSingleObject(self,index):
        boundedImg = self.img[self.objectCollection[index][1]:self.objectCollection[index][1]+self.objectCollection[index][3] , self.objectCollection[index][0]:self.objectCollection[index][0]+self.objectCollection[index][2], :]
        
        color_img2 = cv2.cvtColor(boundedImg, cv2.COLOR_BGR2RGB)   
        print(len(self.objectCollection))
        return QImage( color_img2.data, boundedImg.shape[1], boundedImg.shape[0], 3*boundedImg.shape[1], QImage.Format_RGB888)
        #return boundedImg
        
        
    def showImageWithHighlight(self,index):
        threshImCrop = cv2.rectangle(self.threshIm , (self.objectCollection[index][0], self.objectCollection[index][1]), (self.objectCollection[index][0]+self.objectCollection[index][2]-1 , self.objectCollection[index][1]+self.objectCollection[index][3]-1), (255,0,0), 3)
        #return threshImCrop
        return QImage(threshImCrop.data, threshImCrop.shape[1], threshImCrop.shape[0], 3*threshImCrop.shape[1], QImage.Format_RGB888)
    
    def setCurrentImageNum(self,value):
        self.currentImageNum = value
        
    def getCurrentImageNum(self):
        return self.currentImageNum

        