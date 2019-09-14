# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:56:59 2019

@author: Sid
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import distutils.spawn
import os.path
import platform
import re
import sys
import subprocess
import gui_python_hook
import pdb
from functools import partial
from collections import defaultdict
import cv2
import QtGui

class Login(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_dlgLogovanje()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.buttonLogin, QtCore.SIGNAL("clicked()"), self.doLogin)

    def doLogin(self):
        name = str(self.ui.lineKorisnik.text())
        passwd = str(self.ui.lineSifra.text())
        if name == "john" and passwd =="doe":
            self.runIt()
        else:
            QtGui.QMessageBox.warning(self, 'Greška',
        "Bad user or password", QtGui.QMessageBox.Ok)           

    def runIt(self):
        myprogram = Window()        
        myprogram.showMaximized() #myprogram is

class Window(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


if __name__=="__main__":
    program = QtGui.QApplication(sys.argv)
    myprogram = Window()
    if Login().exec_() == QtGui.QDialog.Accepted:       
        sys.exit(program.exec_())