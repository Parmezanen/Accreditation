# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\f0kes\Desktop\ACCR\PyUI\KODB_Editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KO_Editor(object):
    def setupUi(self, KO_Editor):
        KO_Editor.setObjectName("KO_Editor")
        KO_Editor.resize(1163, 613)
        self.centralwidget = QtWidgets.QWidget(KO_Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tb_KO = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_KO.setMinimumSize(QtCore.QSize(604, 0))
        self.tb_KO.setMaximumSize(QtCore.QSize(604, 16777215))
        self.tb_KO.setObjectName("tb_KO")
        self.tb_KO.setColumnCount(6)
        self.tb_KO.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_KO.setHorizontalHeaderItem(5, item)
        self.tb_KO.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.tb_KO, 0, 0, 1, 1)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.le_FIO = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.le_FIO.setObjectName("le_FIO")
        self.verticalLayout.addWidget(self.le_FIO)
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.le_Privlech = QtWidgets.QLineEdit(self.verticalGroupBox)
        self.le_Privlech.setObjectName("le_Privlech")
        self.verticalLayout.addWidget(self.le_Privlech)
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tE_Dolzhnost = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_Dolzhnost.setObjectName("tE_Dolzhnost")
        self.verticalLayout.addWidget(self.tE_Dolzhnost)
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.tE_Disciplines = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_Disciplines.setObjectName("tE_Disciplines")
        self.verticalLayout.addWidget(self.tE_Disciplines)
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tE_NaprPodgotov = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_NaprPodgotov.setObjectName("tE_NaprPodgotov")
        self.verticalLayout.addWidget(self.tE_NaprPodgotov)
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.tE_Education = QtWidgets.QPlainTextEdit(self.verticalGroupBox)
        self.tE_Education.setObjectName("tE_Education")
        self.verticalLayout.addWidget(self.tE_Education)
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
        KO_Editor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KO_Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 21))
        self.menubar.setObjectName("menubar")
        KO_Editor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KO_Editor)
        self.statusbar.setObjectName("statusbar")
        KO_Editor.setStatusBar(self.statusbar)

        self.retranslateUi(KO_Editor)
        QtCore.QMetaObject.connectSlotsByName(KO_Editor)

    def retranslateUi(self, KO_Editor):
        _translate = QtCore.QCoreApplication.translate
        KO_Editor.setWindowTitle(_translate("KO_Editor", "MainWindow"))
        self.tb_KO.setSortingEnabled(True)
        item = self.tb_KO.horizontalHeaderItem(0)
        item.setText(_translate("KO_Editor", "Новый столбец"))
        item = self.tb_KO.horizontalHeaderItem(1)
        item.setText(_translate("KO_Editor", "ФИО"))
        item = self.tb_KO.horizontalHeaderItem(2)
        item.setText(_translate("KO_Editor", "Усл. привлечения"))
        item = self.tb_KO.horizontalHeaderItem(3)
        item.setText(_translate("KO_Editor", "Должн., у.с., у.з."))
        item = self.tb_KO.horizontalHeaderItem(4)
        item.setText(_translate("KO_Editor", "Напр. подготовки"))
        item = self.tb_KO.horizontalHeaderItem(5)
        item.setText(_translate("KO_Editor", "Доп. образование"))
        self.label.setText(_translate("KO_Editor", "ФИО преподавателя:"))
        self.label_2.setText(_translate("KO_Editor", "Условия привлечения:"))
        self.label_3.setText(_translate("KO_Editor", "Должность, ученая степень, ученое звание:"))
        self.label_4.setText(_translate("KO_Editor", "Перечень читаемых дисциплин:"))
        self.label_5.setText(_translate("KO_Editor", "Уровень образования, \n"
"наименование специальности, направления подготовки, наименование присвоенной квалификации:"))
        self.label_6.setText(_translate("KO_Editor", "Сведения о дополнительном профессиональном образовании:"))
        self.pb_Save.setText(_translate("KO_Editor", "Сохранить"))
        self.pb_Edit.setText(_translate("KO_Editor", "Редактировать"))
        self.pb_Add.setText(_translate("KO_Editor", "Добавить"))
        self.pb_Delete.setText(_translate("KO_Editor", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KO_Editor = QtWidgets.QMainWindow()
    ui = Ui_KO_Editor()
    ui.setupUi(KO_Editor)
    KO_Editor.show()
    sys.exit(app.exec_())
