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

class Detect():
 
    def __init__(self, filename):
        self.filename = filename
        self.img=None
        self.thresIm = None;
        self.objectCollection = []
        
    def detectedImage(self,movie):
         self.img = movie.returnImageBasedOnSlider()
         M, N, channel = self.img.shape
         
         U, V = np.meshgrid(np.arange(0, N, 1), np.arange(0, M, 1))
         D= np.sqrt((U-(N+1)/2)**2+(V-(M+1)/2)**2)
        
         D0= np.array([2]);
         n= np.array([2]); 
         one=np.ones((M,N),np.float);
       
         
         H = 1//(one+(D//D0)**(2*n))
         #pdb.set_trace()
         out = np.double(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)) -np.real(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)))*H)))
         currentSnippedImage = np.uint8((255.0/(np.amax(out)-np.amin(out)))*(out-np.amin(out)))
        
         th2 = cv2.adaptiveThreshold(currentSnippedImage,1,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,int(np.min(2*np.floor(np.divide(H.shape,16))+1)),-12)
         nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(th2, connectivity=8)
         sizes = stats[1:, -1]; nb_components = nb_components - 1
         min_size = 40  
         max_size = 120
         img2 = np.zeros((output.shape))
         for i in range(0, nb_components):
            if max_size >= sizes[i] >= min_size :
               img2[output == i + 1] = 255
               self.objectCollection.append(np.array([stats[i+1, cv2.CC_STAT_LEFT],
                        stats[i+1, cv2.CC_STAT_TOP], 
                        stats[i+1, cv2.CC_STAT_WIDTH], 
                        stats[i+1, cv2.CC_STAT_HEIGHT]]))
         #QImage newImage = img2
         #np
         
        
         bytesPerLine = 3*N#int(totalBytes/N)
         #return QImage(img2, img2.shape[1], img2.shape[0],bytesPerLine, QImage.Format_Grayscale8)                                                                                                                                                                 
        
         #return img2
         bytesPerLine =  3*N
         cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB, self.img)   
         color_img = cv2.cvtColor(np.uint8(img2), cv2.COLOR_GRAY2RGB)
         self.threshIm = color_img
         #return QImage(self.img, N, M, bytesPerLine,QImage.Format_RGB888)                   
         return QImage(color_img.data, N, M, bytesPerLine,QImage.Format_RGB888)
         #return cv2.imread(self.filename)  
         #return QImage(self.img.data, N, M, bytesPerLine, QImage.Format_RGB888)
        # return QImage.fromData(self.img.data)    
     #return QImage(img2.data, N, M, bytesPerLine,QImage.Format_Grayscale8)

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

#imgFile = cv2.imread(r"C:\Users\Sid\Desktop\pythonLearn\guiml\demo\demo.jpg")

#cv2.imshow('dst_rt', imgFile)
# =============================================================================
# =============================================================================
# # #cv2.waitKey(0)
# # #cv2.destroyAllWindows()

# newDetect = Detect(r'C:\Users\Sid\Desktop\pythonLearn\guiml\demo\a.jpg')    
# cv2.imshow( "Display window", newDetect.detectedImage())
# cv2.waitKey(3000)
# =============================================================================
# # cv2.destroyAllWindows()
# 
# for i in range(0, 20):
#      newDetect = Detect(r'C:\Users\Sid\Desktop\pythonLearn\guiml\demo\a.jpg')    
#      newDetect.detectedImage()
#      cv2.imshow( "Display window", newDetect.returnSingleObject(i))
#      cv2.waitKey(3000)
#      cv2.destroyAllWindows()
# 
# for i in range(0, 20):
#       newDetect = Detect(r'C:\Users\Sid\Desktop\pythonLearn\guiml\demo\a.jpg')    
#       newDetect.detectedImage()
#       cv2.imshow( "Display window", newDetect.showImageWithHighlight(i))
#       cv2.waitKey(3000)
#       cv2.destroyAllWindows()
