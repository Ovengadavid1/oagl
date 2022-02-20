# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:58:29 2022

@author: OVENGA DAVID KEVIN
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from index import Ui_Form
from maxx import Ui_Form


def afficheDialog():
    Dialog.show()

    

import sys
app=QtWidgets.QApplication(sys.argv)
Form=QtWidgets.QWidget()
ui=Ui_Form()
ui.setupUi(Form)


Dialog=QtWidgets.QDialog()
Di=Ui_Form()
Di.setupUi(Dialog)




    #afficher

Form.show()
    #les signaux
ui.pushButton.clicked.connect(afficheDialog) 
sys.exit(app.exec_())