# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 02:21:30 2022

@author: OVENGA DAVID KEVIN
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from eleg import Ui_Form
from tard import Ui_Form


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
Di.label.setText("informations enregistrer")  
sys.exit(app.exec_())