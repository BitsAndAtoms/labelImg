# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newLoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os 
from subprocess import Popen
import labelImg
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 406)
        MainWindow.setStyleSheet("QPushButton {\n"
"           color: red;\n"
"           background-color: orange;\n"
"           border-style: outset;\n"
"           border-width: 2px;\n"
"           border-radius: 15px;\n"
"           border-color: black;\n"
"           padding: 4px; \n"
"         \n"
"        }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"        background-color: yellow;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(40, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(40, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(197, 140, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(197, 90, 121, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(40, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(157, 40, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 210, 311, 101))
        self.textEdit.setObjectName("textEdit")
        self.commentLabel = QtWidgets.QLabel(self.centralwidget)
        self.commentLabel.setGeometry(QtCore.QRect(40, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.commentLabel.setFont(font)
        self.commentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.commentLabel.setObjectName("commentLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # added value setters
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.timeEdit.setTime(QtCore.QTime.currentTime())
         
        # function calls
        self.retranslateUi(MainWindow)
        app.aboutToQuit.connect(self.closeEvent)
        self.pushButton.clicked.connect(self.submitButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def closeEvent(self):
        
        #Popen('python labelImg.py',shell=True)
        import sys
        sys.exit(0)

    def submitButton(self):
        text_file = open(QtCore.QDateTime.currentDateTime().toString("yyyyMMdd_h_m_s"), "w")
        text_file.write(self.lineEdit.text())
        text_file.write(os.linesep)
        text_file.write(self.textEdit.toPlainText())
        text_file.close()
        
        self.dialog =  labelImg.MainWindow(None,os.path.join(
                         os.path.dirname('python labelImg.py'),
                         'data', 'predefined_classes.txt'),None)
        self.dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Worm Label Tool"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.commentLabel.setText(_translate("MainWindow", "Comment"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
