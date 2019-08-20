try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

class SliderBar(QWidget):
   def __init__(self, parent = None):
      super(SliderBar, self).__init__(parent)
      layout = QHBoxLayout()
      self.l1 = QLCDNumber(self)
      #self.l1.setAlignment(Qt.AlignCenter)
      layout.addWidget(self.l1)
      self.sl = QSlider(Qt.Horizontal)
      self.sl.setMinimum(10)
      self.sl.setMaximum(30)
      self.sl.setValue(20)
      self.sl.setTickPosition(QSlider.TicksBelow)
      self.sl.setTickInterval(5)
      layout.addWidget(self.sl)
      self.sl.valueChanged.connect(self.l1.display)
      self.setLayout(layout)
      self.setWindowTitle("SpinBox demo")

   def valuechange(self):
      size = self.sl.value()
      self.l1.set_text(QLabel("dfsdf"))