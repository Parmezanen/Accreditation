# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\f0kes\Desktop\ACCR\QtGui\QtGui\PPSReference.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PPSReference(object):
    def setupUi(self, PPSReference):
        PPSReference.setObjectName("PPSReference")
        PPSReference.resize(503, 418)
        self.gridLayout_2 = QtWidgets.QGridLayout(PPSReference)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tb_KOtable = QtWidgets.QTableWidget(PPSReference)
        self.tb_KOtable.setObjectName("tb_KOtable")
        self.tb_KOtable.setColumnCount(0)
        self.tb_KOtable.setRowCount(0)
        self.gridLayout_2.addWidget(self.tb_KOtable, 0, 0, 1, 2)
        self.pb_editPPS = QtWidgets.QPushButton(PPSReference)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_editPPS.setFont(font)
        self.pb_editPPS.setObjectName("pb_editPPS")
        self.gridLayout_2.addWidget(self.pb_editPPS, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(359, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_savePPS = QtWidgets.QPushButton(PPSReference)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_savePPS.setFont(font)
        self.pb_savePPS.setObjectName("pb_savePPS")
        self.gridLayout.addWidget(self.pb_savePPS, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(288, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pb_ExitPPS = QtWidgets.QPushButton(PPSReference)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_ExitPPS.setFont(font)
        self.pb_ExitPPS.setObjectName("pb_ExitPPS")
        self.gridLayout.addWidget(self.pb_ExitPPS, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(PPSReference)
        QtCore.QMetaObject.connectSlotsByName(PPSReference)

    def retranslateUi(self, PPSReference):
        _translate = QtCore.QCoreApplication.translate
        PPSReference.setWindowTitle(_translate("PPSReference", "PPSReference"))
        self.pb_editPPS.setText(_translate("PPSReference", "Редактировать"))
        self.pb_savePPS.setText(_translate("PPSReference", "Сохранить"))
        self.pb_ExitPPS.setText(_translate("PPSReference", "Закрыть"))
