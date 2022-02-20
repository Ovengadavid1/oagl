# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_tp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 341)
        Form.setStyleSheet("background-color: rgb(255, 235, 241);")
        self.emprunts = QtWidgets.QPushButton(Form)
        self.emprunts.setGeometry(QtCore.QRect(30, 130, 191, 51))
        self.emprunts.setStyleSheet("font: 16pt \"Open Sans\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);")
        self.emprunts.setObjectName("emprunts")
        self.liste_livre = QtWidgets.QPushButton(Form)
        self.liste_livre.setGeometry(QtCore.QRect(240, 130, 191, 51))
        self.liste_livre.setStyleSheet("font: 16pt \"Open Sans\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 68, 12);")
        self.liste_livre.setObjectName("liste_livre")
        self.admin = QtWidgets.QPushButton(Form)
        self.admin.setGeometry(QtCore.QRect(140, 220, 191, 51))
        self.admin.setStyleSheet("font: 16pt \"Open Sans\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 127);")
        self.admin.setObjectName("admin")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 271, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 371, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.emprunts.setText(_translate("Form", "Gestion des emprunts"))
        self.liste_livre.setText(_translate("Form", "liste des livres"))
        self.admin.setText(_translate("Form", "Administrateur"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">BIBLIOTHEQUE</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Bibliotéque de la gestion des emprunts de l\'université Adventiste Cosendai (UAC)</span></p></body></html>"))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form =QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    
    
    # afficher la fenetre
    Form.show()
    
    
    sys.exit(app.exec_())