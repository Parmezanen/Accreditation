# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 482)
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tb_ChosenTeacher = QtWidgets.QTableWidget(self.centralWidget)
        self.tb_ChosenTeacher.setObjectName("tb_ChosenTeacher")
        self.tb_ChosenTeacher.setColumnCount(8)
        self.tb_ChosenTeacher.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenTeacher.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tb_ChosenTeacher, 1, 2, 1, 2)
        self.tb_AvailAud = QtWidgets.QTableWidget(self.centralWidget)
        self.tb_AvailAud.setObjectName("tb_AvailAud")
        self.tb_AvailAud.setColumnCount(4)
        self.tb_AvailAud.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailAud.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailAud.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailAud.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailAud.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tb_AvailAud, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.tb_AvailTeacher = QtWidgets.QTableWidget(self.centralWidget)
        self.tb_AvailTeacher.setObjectName("tb_AvailTeacher")
        self.tb_AvailTeacher.setColumnCount(8)
        self.tb_AvailTeacher.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_AvailTeacher.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tb_AvailTeacher, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.tb_ChosenAdu = QtWidgets.QTableWidget(self.centralWidget)
        self.tb_ChosenAdu.setObjectName("tb_ChosenAdu")
        self.tb_ChosenAdu.setColumnCount(4)
        self.tb_ChosenAdu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenAdu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenAdu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenAdu.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_ChosenAdu.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tb_ChosenAdu, 0, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menuBar)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setWindowTitle("")
        self.mainToolBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_SaveAs = QtWidgets.QAction(MainWindow)
        self.action_SaveAs.setObjectName("action_SaveAs")
        self.action_MTOPDF = QtWidgets.QAction(MainWindow)
        self.action_MTOPDF.setObjectName("action_MTOPDF")
        self.action_MTODOCX = QtWidgets.QAction(MainWindow)
        self.action_MTODOCX.setObjectName("action_MTODOCX")
        self.action_KOPDF = QtWidgets.QAction(MainWindow)
        self.action_KOPDF.setObjectName("action_KOPDF")
        self.action_KODOCX = QtWidgets.QAction(MainWindow)
        self.action_KODOCX.setObjectName("action_KODOCX")
        self.action_PPS = QtWidgets.QAction(MainWindow)
        self.action_PPS.setObjectName("action_PPS")
        self.action_UP = QtWidgets.QAction(MainWindow)
        self.action_UP.setObjectName("action_UP")
        self.action_GN = QtWidgets.QAction(MainWindow)
        self.action_GN.setObjectName("action_GN")
        self.action_KOFormul = QtWidgets.QAction(MainWindow)
        self.action_KOFormul.setObjectName("action_KOFormul")
        self.action_TemplateMTO = QtWidgets.QAction(MainWindow)
        self.action_TemplateMTO.setObjectName("action_TemplateMTO")
        self.action_TemplateKO = QtWidgets.QAction(MainWindow)
        self.action_TemplateKO.setObjectName("action_TemplateKO")
        self.action_FulledAudience = QtWidgets.QAction(MainWindow)
        self.action_FulledAudience.setObjectName("action_FulledAudience")
        self.action_FulledStaff = QtWidgets.QAction(MainWindow)
        self.action_FulledStaff.setObjectName("action_FulledStaff")
        self.action_CheckPercent = QtWidgets.QAction(MainWindow)
        self.action_CheckPercent.setObjectName("action_CheckPercent")
        self.action_Audience = QtWidgets.QAction(MainWindow)
        self.action_Audience.setObjectName("action_Audience")
        self.menu.addAction(self.action_Open)
        self.menu.addAction(self.action_Save)
        self.menu.addAction(self.action_SaveAs)
        self.menu_2.addAction(self.action_MTOPDF)
        self.menu_2.addAction(self.action_MTODOCX)
        self.menu_2.addAction(self.action_KOPDF)
        self.menu_2.addAction(self.action_KODOCX)
        self.menu_3.addAction(self.action_Audience)
        self.menu_3.addAction(self.action_PPS)
        self.menu_3.addAction(self.action_GN)
        self.menu_3.addAction(self.action_KOFormul)
        self.menu_4.addAction(self.action_TemplateMTO)
        self.menu_4.addAction(self.action_TemplateKO)
        self.menu_5.addAction(self.action_FulledAudience)
        self.menu_5.addAction(self.action_FulledStaff)
        self.menu_5.addAction(self.action_CheckPercent)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu_6.menuAction())
        self.Help = QtWidgets.QAction(MainWindow)
        self.Help.setObjectName("Help")
        self.menu_6.addAction(self.Help)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtGui"))
        self.Help.setText(_translate("MainWindow","Справка"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Усл. привлечения"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Уч. степень"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Уч. звание"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дисциплины"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Напр. подготовки"))
        item = self.tb_ChosenTeacher.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Доп. образование"))
        item = self.tb_AvailAud.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дисиплина"))
        item = self.tb_AvailAud.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tb_AvailAud.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ТО"))
        item = self.tb_AvailAud.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ПО"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Усл. привлечения"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Уч. степень"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Уч. звание"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дисциплины"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Напр. подготовки"))
        item = self.tb_AvailTeacher.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Доп. образование"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить в DOCX"))
        item = self.tb_ChosenAdu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дисциплина"))
        item = self.tb_ChosenAdu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.tb_ChosenAdu.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ТО"))
        item = self.tb_ChosenAdu.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ПО"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Сгенерировать справку"))
        self.menu_3.setTitle(_translate("MainWindow", "Справочники"))
        self.menu_4.setTitle(_translate("MainWindow", "Шаблон"))
        self.menu_5.setTitle(_translate("MainWindow", "Проверка"))
        self.menu_6.setTitle(_translate("MainWindow", "Справка"))
        self.action_Open.setText(_translate("MainWindow", "Открыть"))
        self.action_Save.setText(_translate("MainWindow", "Сохранить"))
        self.action_SaveAs.setText(_translate("MainWindow", "Сохранить как..."))
        self.action_MTOPDF.setText(_translate("MainWindow", "МТО PDF"))
        self.action_MTODOCX.setText(_translate("MainWindow", "МТО DOCX"))
        self.action_KOPDF.setText(_translate("MainWindow", "КО PDF"))
        self.action_KODOCX.setText(_translate("MainWindow", "КО DOCX"))
        self.action_PPS.setText(_translate("MainWindow", "Справочник ППС"))
        self.action_UP.setText(_translate("MainWindow", "Справочник УП"))
        self.action_GN.setText(_translate("MainWindow", "Справочник УП"))
        self.action_KOFormul.setText(_translate("MainWindow", "Справочник КО формул"))
        self.action_TemplateMTO.setText(_translate("MainWindow", "Загрузить шаблон МТО"))
        self.action_TemplateKO.setText(_translate("MainWindow", "Загрузить шаблон КО"))
        self.action_FulledAudience.setText(_translate("MainWindow", "Заполнены аудитории"))
        self.action_FulledStaff.setText(_translate("MainWindow", "Заполнены кадры"))
        self.action_CheckPercent.setText(_translate("MainWindow", "Проверка %"))
        self.action_Audience.setText(_translate("MainWindow", "Справочник аудиторий"))

class HelpDialog(QtWidgets.QDialog):
    def setupUi(self,Dialog):
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label=QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setText('В данной версии программы можно редактировать такие справочники, как УП, КО, МТО \nДля создания справки наведите в верхней панели на меню "Шаблон",\nзатем выберите интересуюущий вас вид справки и нажмите на кнопку на главном окне "Сохранить"')
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Справка")
        self.pushButton.setText("Понимаю")

    def btnClosed(self):
        self.close()