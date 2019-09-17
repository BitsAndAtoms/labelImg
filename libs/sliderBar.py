try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    
from libs.movie import Movie
from libs.detect import Detect
import pdb
class SliderBar(QWidget):
    
   def __init__(self, parent = None,Minimum = 0,Maximum = 30):
      super(SliderBar, self).__init__(parent)
      layout = QHBoxLayout()
      self.l1 = QLCDNumber(self)
      #self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(Minimum)
      self.sl.setMaximum(Maximum)
      self.sl.setValue(0)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5)
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.l1.display)
      self.sl.valueChanged.connect(self.value_changed)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")
      self.movie = None
      self.detect = None
      

      
   def value_changed(self):
      
       try:
        self.parent().parent().movie.setCurrentImageNum(self.sl.value())
        #self.parent().parent().detectedImages.detectedImagePlainHighlight(self.parent().parent().movie)
        self.parent().parent().loadFile( self.parent().parent().fname)
       except:
        
        returnVal = self.parent().parent().parent().parent().detectedImages.returnSingleObjectMini(self.sl.value(),self.parent().parent().parent().parent().movie) 
        pixmap = QPixmap.fromImage(returnVal).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.parent().parent().parent().parent().canvas2.loadPixmap(pixmap)
         