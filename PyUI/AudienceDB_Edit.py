# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\f0kes\Desktop\ACCR\PyUI\AudienceDB_Edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Audience_Editor(object):
    def setupUi(self, Audience_Editor):
        Audience_Editor.setObjectName("Audience_Editor")
        Audience_Editor.resize(893, 582)
        self.centralwidget = QtWidgets.QWidget(Audience_Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tb_Audience = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_Audience.setMinimumSize(QtCore.QSize(435, 0))
        self.tb_Audience.setObjectName("tb_Audience")
        self.tb_Audience.setColumnCount(4)
        self.tb_Audience.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        item.setFont(font)
        self.tb_Audience.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Audience.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tb_Audience.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_Audience.setHorizontalHeaderItem(3, item)
        self.tb_Audience.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.tb_Audience, 0, 0, 1, 1)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.le_AudienceName = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.le_AudienceName.setObjectName("le_AudienceName")
        self.verticalLayout.addWidget(self.le_AudienceName)
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tE_AudienceTO = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_AudienceTO.setObjectName("tE_AudienceTO")
        self.verticalLayout.addWidget(self.tE_AudienceTO)
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tE_Naimen = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_Naimen.setObjectName("tE_Naimen")
        self.verticalLayout.addWidget(self.tE_Naimen)
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tE_PO = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_PO.setObjectName("tE_PO")
        self.verticalLayout.addWidget(self.tE_PO)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridFrame_2 = QtWidgets.QFrame(self.verticalGroupBox)
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_Save = QtWidgets.QPushButton(self.gridFrame_2)
        self.pb_Save.setObjectName("pb_Save")
        self.gridLayout.addWidget(self.pb_Save, 0, 5, 1, 1)
        self.pb_Edit = QtWidgets.QPushButton(self.gridFrame_2)
        self.pb_Edit.setObjectName("pb_Edit")
        self.gridLayout.addWidget(self.pb_Edit, 0, 3, 1, 1)
        self.pb_Add = QtWidgets.QPushButton(self.gridFrame_2)
        self.pb_Add.setObjectName("pb_Add")
        self.gridLayout.addWidget(self.pb_Add, 0, 1, 1, 1)
        self.pb_Delete = QtWidgets.QPushButton(self.gridFrame_2)
        self.pb_Delete.setObjectName("pb_Delete")
        self.gridLayout.addWidget(self.pb_Delete, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.gridFrame_2)
        self.gridLayout_2.addWidget(self.verticalGroupBox, 0, 1, 1, 1)
        Audience_Editor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Audience_Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 21))
        self.menubar.setObjectName("menubar")
        Audience_Editor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Audience_Editor)
        self.statusbar.setObjectName("statusbar")
        Audience_Editor.setStatusBar(self.statusbar)

        self.retranslateUi(Audience_Editor)
        QtCore.QMetaObject.connectSlotsByName(Audience_Editor)

    def retranslateUi(self, Audience_Editor):
        _translate = QtCore.QCoreApplication.translate
        Audience_Editor.setWindowTitle(_translate("Audience_Editor", "MainWindow"))
        self.tb_Audience.setSortingEnabled(True)
        item = self.tb_Audience.horizontalHeaderItem(0)
        item.setText(_translate("Audience_Editor", "Аудитория"))
        item = self.tb_Audience.horizontalHeaderItem(1)
        item.setText(_translate("Audience_Editor", "Наименование"))
        item = self.tb_Audience.horizontalHeaderItem(2)
        item.setText(_translate("Audience_Editor", "Тех. оснащение"))
        item = self.tb_Audience.horizontalHeaderItem(3)
        item.setText(_translate("Audience_Editor", "ПО"))
        self.label.setText(_translate("Audience_Editor", "Аудитория:"))
        self.label_2.setText(_translate("Audience_Editor", "Техническое оснащение аудитории:"))
        self.label_3.setText(_translate("Audience_Editor", "Наименование:"))
        self.label_4.setText(_translate("Audience_Editor", "Лицензионное ПО:"))
        self.pb_Save.setText(_translate("Audience_Editor", "Сохранить"))
        self.pb_Edit.setText(_translate("Audience_Editor", "Редактировать"))
        self.pb_Add.setText(_translate("Audience_Editor", "Добавить"))
        self.pb_Delete.setText(_translate("Audience_Editor", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Audience_Editor = QtWidgets.QMainWindow()
    ui = Ui_Audience_Editor()
    ui.setupUi(Audience_Editor)
    Audience_Editor.show()
    sys.exit(app.exec_())
