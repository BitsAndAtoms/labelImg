# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:02:08 2019

@author: Sid
"""

import sys
from PyQt5 import QtWidgets

def catch_exceptions(t, val, tb):
    
    QtWidgets.QMessageBox.critical(None,'An Exception was Raised','Value: {}'.format(val))
    
    sys.excepthook = catch_exceptions