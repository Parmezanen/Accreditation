# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\f0kes\Desktop\ACCR\QtGui\QtGui\StaffEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeacherSelection(object):
    def setupUi(self, TeacherSelection):
        TeacherSelection.setObjectName("TeacherSelection")
        TeacherSelection.resize(400, 200)
        TeacherSelection.setMinimumSize(QtCore.QSize(400, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(TeacherSelection)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.pb_editTeacher = QtWidgets.QPushButton(TeacherSelection)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_editTeacher.setFont(font)
        self.pb_editTeacher.setObjectName("pb_editTeacher")
        self.gridLayout.addWidget(self.pb_editTeacher, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(301, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.pb_SaveTeacher = QtWidgets.QPushButton(TeacherSelection)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pb_SaveTeacher.setFont(font)
        self.pb_SaveTeacher.setAutoRepeatDelay(300)
        self.pb_SaveTeacher.setAutoRepeatInterval(100)
        self.pb_SaveTeacher.setObjectName("pb_SaveTeacher")
        self.gridLayout.addWidget(self.pb_SaveTeacher, 4, 3, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.cb_teacherSelection = QtWidgets.QComboBox(TeacherSelection)
        self.cb_teacherSelection.setObjectName("cb_teacherSelection")
        self.gridLayout.addWidget(self.cb_teacherSelection, 2, 2, 1, 3)
        self.cb_typeOfWorkSelection = QtWidgets.QComboBox(TeacherSelection)
        self.cb_typeOfWorkSelection.setObjectName("cb_typeOfWorkSelection")
        self.gridLayout.addWidget(self.cb_typeOfWorkSelection, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(TeacherSelection)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(TeacherSelection)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(TeacherSelection)
        QtCore.QMetaObject.connectSlotsByName(TeacherSelection)

    def retranslateUi(self, TeacherSelection):
        _translate = QtCore.QCoreApplication.translate
        TeacherSelection.setWindowTitle(_translate("TeacherSelection", "Выбор преподавателя и дисциплины"))
        self.pb_editTeacher.setText(_translate("TeacherSelection", "Редактировать"))
        self.pb_SaveTeacher.setText(_translate("TeacherSelection", "Сохранить"))
        self.label.setText(_translate("TeacherSelection", "Тип занятия"))
        self.label_2.setText(_translate("TeacherSelection", "Преподователь"))

