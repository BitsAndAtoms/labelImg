# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:50:44 2019

@author: Sid
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
from libs.movie import Movie
plt.tight_layout()
plt.show()
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

class Result():
 
    def __init__(self):
        self.resultCollection = []
        

        
    def intializeFrameWiseResult(self,movie):
         self.resultCollection = [None]*(movie.returnMovieFinalFrame())
         

    def getFrameWiseResult(self ):
         return self.resultCollection
    
    def initalizeResultInSingleFrame(self,value,length):
        self.resultCollection[value] = [None]*length
        
        
    def setUnsetWorm(self,value,index):
            if self.resultCollection[value][index] is None:
             self.resultCollection[value][index] = 1
            elif self.resultCollection[value][index] == 1:
             self.resultCollection[value][index] = 0
            elif self.resultCollection[value][index] == 0:
             self.resultCollection[value][index] = None
              
           