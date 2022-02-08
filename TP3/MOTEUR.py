# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 08:06:50 2022

@author: OVENGA DAVID KEVIN
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from FORMULAIRE import  Ui_Form
from success import  Ui_Dialog


def afficheDialog():
    Dialog.show()


    

import sys
app=QtWidgets.QApplication(sys.argv)
Form=QtWidgets.QWidget()
ui=Ui_Form()
ui.setupUi(Form)


Dialog=QtWidgets.QDialog()
Di=Ui_Dialog()
Di.setupUi(Dialog)




    #afficher
Form.show()
    #les signaux
ui.pushButton.clicked.connect(afficheDialog)

Di.label.setText("informations enregistrés")  
sys.exit(app.exec_())