# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'total.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Deuxieme_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(367, 196)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 70, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "VOS INFORMATIONS ONT ETE ENREGISTRER" ))
        
        
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 270, 56, 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 20))
        self.label.setStyleSheet("font: 16pt \"Mongolian Baiti\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 35, 10))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 35, 10))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 35, 10))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 60, 291, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 110, 291, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 160, 291, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(80, 210, 291, 41))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton_2.setText(_translate("Form", "Effacer"))
        self.label.setText(_translate("Form", "FORMULAIRE D\'INSCRIPTION"))
        self.label_2.setText(_translate("Form", "Nom"))
        self.label_3.setText(_translate("Form", "Prenom"))
        self.label_4.setText(_translate("Form", "Matricule"))
        self.label_5.setText(_translate("Form", "Genre"))
        self.pushButton_2.clicked.connect(self.Effacer)
        self.pushButton.setText(_translate("Form", "Valider"))
        # création de l'évenement à attacher sur la méthode de la deuxième fenêtre' 
        self.pushButton.clicked.connect(self.deuxiemeFenetre)
        self.pushButton.clicked.connect(Form.close)
        
    # C'est ici que je crée la méthode permettant d'ouvrir la seconde interface
    # c'est pareil que dans la méthode main sauf qu'on utilise le self    
    def deuxiemeFenetre(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Deuxieme_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        
    
       

    def Effacer(self):
        self.textEdit.setText("")        
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_4.setText("")
        
    def Saisirtexte(self):
        self.textEditValue = self.textEdit.toPlainText()
        self.textEditValue_2 = self.textEdit_2.toPlainText()
        self.textEditValue_3 = self.textEdit_3.toPlainText() 
        self.textEditValue_4 = self.textEdit_4.toPlainText() 
         
        print(self.textEditValue)
        print(self.textEditValue_2)
        print(self.textEditValue_3)
        print(self.textEditValue_4)

        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())    



