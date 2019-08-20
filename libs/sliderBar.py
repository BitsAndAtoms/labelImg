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
      
   def setMovie(self,movie):
      self.movie = movie
      
   def value_changed(self):
       
       self.parent().parent().movie.setCurrentImageNum(self.sl.value())
       self.parent().parent().detectedImages.detectedImage(self.parent().parent().movie)
       self.parent().parent().loadFile( self.parent().parent().fname)
       
   def setDetect(self,detect):
       self.detect = movie