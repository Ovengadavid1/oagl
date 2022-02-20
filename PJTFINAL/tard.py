# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'virage.ui'
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 50, 71, 20))
        self.label.setStyleSheet("font: 16pt \"MS Reference Sans Serif\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 90, 241, 64))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 230, 56, 17))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Login"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton.clicked.connect(self.SaisirTexte)
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
    def SaisirTexte(self):
        self.textEditValue = self.textEdit.toPlainText()
        print(self.textEditValue)
        
            
        
      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())    




