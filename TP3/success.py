# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SUCESS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(758, 603)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 200, 531, 71))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "VOS INFORMATIONS ONT BIEN ETE ENREGISTRER"))

    def saisirTexte(self):
        textEditValue=self.textEdit.toPlainText()+self.textEdit_2.toPlainText()+self.textEdit_3.toPlainText()
        self.textEdit_4.toPlainText()
        print(textEditValue)
        