# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emprunt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_emprun(object):
    def setupUi(self, emprun):
        emprun.setObjectName("emprun")
        emprun.resize(455, 376)
        self.label = QtWidgets.QLabel(emprun)
        self.label.setGeometry(QtCore.QRect(90, 0, 261, 31))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(emprun)
        self.widget.setGeometry(QtCore.QRect(0, 60, 281, 131))
        self.widget.setStyleSheet("background-color: rgb(231, 220, 225);")
        self.widget.setObjectName("widget")
        self.nom = QtWidgets.QTextEdit(self.widget)
        self.nom.setGeometry(QtCore.QRect(100, 50, 171, 21))
        self.nom.setObjectName("nom")
        self.filiere = QtWidgets.QTextEdit(self.widget)
        self.filiere.setGeometry(QtCore.QRect(100, 80, 111, 21))
        self.filiere.setObjectName("filiere")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_3.setObjectName("label_3")
        self.matri = QtWidgets.QTextEdit(self.widget)
        self.matri.setGeometry(QtCore.QRect(80, 20, 141, 21))
        self.matri.setObjectName("matri")
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.matri.raise_()
        self.nom.raise_()
        self.filiere.raise_()
        self.label_5 = QtWidgets.QLabel(emprun)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 141, 20))
        self.label_5.setStyleSheet("background-color: rgb(255, 116, 74);\n"
"color: rgb(32, 16, 255);")
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(emprun)
        self.widget_3.setGeometry(QtCore.QRect(0, 210, 451, 101))
        self.widget_3.setStyleSheet("background-color: rgb(231, 220, 225);")
        self.widget_3.setObjectName("widget_3")
        self.nom_3 = QtWidgets.QTextEdit(self.widget_3)
        self.nom_3.setGeometry(QtCore.QRect(110, 30, 171, 21))
        self.nom_3.setObjectName("nom_3")
        self.filiere_3 = QtWidgets.QTextEdit(self.widget_3)
        self.filiere_3.setGeometry(QtCore.QRect(120, 60, 161, 21))
        self.filiere_3.setObjectName("filiere_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.label_12.setObjectName("label_12")
        self.widget_2 = QtWidgets.QWidget(emprun)
        self.widget_2.setGeometry(QtCore.QRect(290, 60, 161, 131))
        self.widget_2.setStyleSheet("background-color: rgb(231, 220, 225);\n"
"background-color: rgb(128, 204, 255);")
        self.widget_2.setObjectName("widget_2")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_7.setObjectName("label_7")
        self.matri_2 = QtWidgets.QTextEdit(self.widget_2)
        self.matri_2.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.matri_2.setObjectName("matri_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.label_8.setObjectName("label_8")
        self.nom_2 = QtWidgets.QTextEdit(self.widget_2)
        self.nom_2.setGeometry(QtCore.QRect(10, 100, 141, 21))
        self.nom_2.setObjectName("nom_2")
        self.label_6 = QtWidgets.QLabel(emprun)
        self.label_6.setGeometry(QtCore.QRect(330, 0, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(emprun)
        self.label_13.setGeometry(QtCore.QRect(320, 50, 61, 20))
        self.label_13.setStyleSheet("background-color: rgb(253, 255, 82);\n"
            "color: rgb(32, 16, 255);")
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(emprun)
        self.label_9.setGeometry(QtCore.QRect(180, 200, 141, 20))
        self.label_9.setStyleSheet("background-color: rgb(255, 116, 74);\n"
              "color: rgb(32, 16, 255);")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(emprun)
        self.pushButton.setGeometry(QtCore.QRect(170, 330, 151, 31))
        self.pushButton.setStyleSheet("color: rgb(17, 80, 255);\n"
         "background-color: rgb(255, 235, 11);\n"
         "font: 16pt \"Perpetua\";\n"
         "font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(emprun)
        QtCore.QMetaObject.connectSlotsByName(emprun)

    def retranslateUi(self, emprun):
        _translate = QtCore.QCoreApplication.translate
        emprun.setWindowTitle(_translate("emprun", "Form"))
        self.label.setText(_translate("emprun", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Gestion des Emprunts</span></p></body></html>"))
        self.label_4.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Filière :</span></p></body></html>"))
        self.label_2.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Matricule :</span></p></body></html>"))
        self.label_3.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Nom/Prenom :</span></p></body></html>"))
        self.label_5.setText(_translate("emprun", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Info de l\'étuduiant/Adéran</span></p></body></html>"))
        self.label_10.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Auteur du livre :</span></p></body></html>"))
        self.label_12.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Titre du livre :</span></p></body></html>"))
        self.label_7.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Date d\'emprunt :</span></p></body></html>"))
        self.label_8.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Date de remise :</span></p></body></html>"))
        self.label_6.setText(_translate("emprun", "<html><head/><body><p><span style=\" font-size:12pt;\">Filière :</span></p></body></html>"))
        self.label_13.setText(_translate("emprun", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Delai</span></p></body></html>"))
        self.label_9.setText(_translate("emprun", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Info de l\'étuduiant/Adéran</span></p></body></html>"))
        self.pushButton.setText(_translate("emprun", "Sauvegarder"))
        self.pushButton.clicked.connect(self.saisirTexte)
        
    def saisirTexte(self):
        self.textEditValue = self.nom.toPlainText()
        self.textEditValue_2 = self.filiere.toPlainText()
        self.textEditValue_3 =  self.matri.toPlainText()
        self.textEditValue_4 =  self.matri_2.toPlainText()
        self.textEditValue_5 =  self.nom_2.toPlainText()
        self.textEditValue_6 =  self.nom_3.toPlainText()
        self.textEditValue_7 = self.filiere_3.toPlainText()
        print(self.textEditValue)
        print(self.textEditValue_2)
        print(self.textEditValue_3)
        print(self.textEditValue_4)
        print(self.textEditValue_5)
        print(self.textEditValue_6)
        print(self.textEditValue_7)
        
        
        
        
       
       


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form =QtWidgets.QWidget()
    ui = Ui_emprun()
    ui.setupUi(Form)
    
    
    # afficher la fenetre
    Form.show()
    
    
    sys.exit(app.exec_())