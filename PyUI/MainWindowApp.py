
"""!!!Файл взаимодействия главного окна с дочерними окнами!!!"""


import sys
import re
import os
import comtypes.client
import time

from PyQt5 import QtCore, QtGui, QtWidgets

"""Импорт файлов интерфейса"""
from UI.PPSEditor import Ui_PPSReference
from UI.MainWindow import Ui_MainWindow
from UI.UPSelector import Ui_UPSelection
from UI.UPEditor import Ui_UPReference
from UI.TeacherSelector import Ui_TeacherSelection
from UI.GNEditor import Ui_GNReference
from UI.AudienceDB_Edit import *
from UI.KODB_Editor import *

from Sorting import SelSortAud
from Sorting import SelSortPPS

from SaveAndLoad import writeCSV
from SaveAndLoad import PPSreadCSV
from SaveAndLoad import AUDreadCSV

#Импорт функций генерации документов
import DocxGeneratingDef
#Импорт функции для конвертации файла
import convertDocxToPDF
#Импорт валидатора
import Validator

"""Инициализация классов интерфейса для их вызова в приложении"""

#Класс выбора преподавателя и дисциплины
class TeacherSelectorWindow(QtWidgets.QWidget, Ui_TeacherSelection):
    def __init__(self,parent=None):
        super(TeacherSelectorWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent=parent
        #Работа кнопок
        self.pb_SaveTeacher.clicked.connect(self.closeEvent)
        self.pb_editTeacher.clicked.connect(self.openPPSEditor)
    #Обаботка сигнала закрытия окна (закрывается дочернее окно, открывается родительское)
    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()
    
    def openPPSEditor(self):
        self.PPSEditingWindow=PPSEditorWindow()
        self.PPSEditingWindow.show()
        self.hide()


#Класс редактора аудиторий
class AudienceEditorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AudienceEditorWindow, self).__init__()
        self.records = []
        self.record={}
        self.index = 0
        self.Aaud = ""

        self.counter=0

        self.ui=Ui_Audience_Editor()


        self.ANDialogUi=AudNameDialog()
        self.ANDialogUi.setupUi(self)

        self.ANMDialogUi=AudNaimDialog()
        self.ANMDialogUi.setupUi(self)

        self.ATDialogUi=AudTODialog()
        self.ATDialogUi.setupUi(self)

        self.APDialogUi=AudPODialog()
        self.APDialogUi.setupUi(self)


        self.ui.setupUi(self)

        self.tableRecords()
        self.ui.pb_Save.clicked.connect(self.saveRecord)
        self.ui.pb_Add.clicked.connect(self.addRecord)
       # self.ui.pb_Add.clicked.connect(self.validation)
        self.ui.pb_Delete.clicked.connect(self.delRecord)
        self.ui.pb_Edit.clicked.connect(self.editRecord)

        self.ui.tb_Audience.cellClicked.connect(self.ShowRecord)
        #if self.ui.tb_Audience.cellClicked(self.ui.tb_Audience.currentRow(), self.ui.tb_Audience.currentColumn()):
            #self.ui.pb_Edit.setEnabled(True)
        #else:
            #self.ui.pb_Edit.setEnabled(False)

    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()

    #Валидатор полей справочника аудиторий
    def validation(self):
        self.AudValid=Validator.AudienceValidator()

        self.AudName=self.ui.le_AudienceName.text()

        self.AudNaim=self.ui.tE_Naimen.toPlainText()
        self.AudTO=self.ui.tE_AudienceTO.toPlainText()
        self.AudPO=self.ui.tE_PO.toPlainText()

        if (self.AudValid.AudNameValid(self.AudName))==True:
            if (self.AudValid.AudNaimenValid(self.AudNaim))==True:
                if (self.AudValid.AudTOValid(self.AudTO))==True:
                    if (self.AudValid.AudPOValid(self.AudPO))==True:
                        return True
                    else:
                        self.APDialogUi.show()
                        return False
                else:
                     self.ATDialogUi.show()
                     return False
            else:
                self.ANMDialogUi.show()
                return False
        else:
            self.ANDialogUi.show()
            return False
        
        
    #Добавить запись
    def addRecord(self):
        if self.validation()==True:
            self.xName = str(self.ui.le_AudienceName.text())
            self.yName = str(self.ui.tE_AudienceTO.toPlainText())
            self.wName = str(self.ui.tE_Naimen.toPlainText())
            self.zName = str(self.ui.tE_PO.toPlainText())
            self.record = {'AudienceName': self.xName, 'AudiencePO' : self.yName, 'AudienceTO': self.wName, 'AudienceNaimenovanie' : self.zName }
            self.records.append(self.record)
            if len(self.records)>1:
                SelSortAud(self.records)
            writeCSV("AUDDB.csv",self.records)
            self.tableRecords()



    def tableRecords(self):
        self.records=AUDreadCSV("AUDDB.csv")
        if self.records:
            self.ui.tb_Audience.setRowCount(0)
            self.index = len(self.records)
            for i in range(0, self.index):
                self.rowCount= i
                self.ui.tb_Audience.insertRow(self.rowCount)
                self.ui.tb_Audience.setItem(self.rowCount, 0, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('AudienceName')))
                self.ui.tb_Audience.setItem(self.rowCount, 1, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('AudienceNaimenovanie')))
                self.ui.tb_Audience.setItem(self.rowCount, 2, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('AudienceTO')))
                self.ui.tb_Audience.setItem(self.rowCount, 3, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('AudiencePO')))

        
    def delRecord(self):
        self.ui.tb_Audience.removeRow(self.ui.tb_Audience.currentRow())
        self.row=self.ui.tb_Audience.currentRow()  
        self.ui.tb_Audience.setCurrentCell(self.row-1,0)
        self.records.pop(self.row)
        writeCSV("AUDDB.csv",self.records)
        
    def editRecord(self):
        self.ui.pb_Save.setEnabled(True)
        self.ui.pb_Add.setEnabled(False)
        self.ui.pb_Delete.setEnabled(False)
        self.ui.pb_Edit.setEnabled(False)
        

    def saveRecord(self):
        self.delRecord()
        self.addRecord()
        self.ui.pb_Save.setEnabled(False)
        self.ui.pb_Delete.setEnabled(True)
        self.ui.pb_Add.setEnabled(True)
        self.ui.pb_Edit.setEnabled(True)

    def ShowRecord(self,row,column):
        self.ui.le_AudienceName.setText(self.records[row].get("AudienceName"))
        self.ui.tE_AudienceTO.setPlainText(self.records[row].get("AudienceTO"))
        self.ui.tE_Naimen.setPlainText(self.records[row].get("AudienceNaimenovanie"))
        self.ui.tE_PO.setPlainText(self.records[row].get("AudiencePO"))

#Класс выбора группы
class GNEditorWindow(QtWidgets.QWidget, Ui_GNReference):
    def __init__(self,parent=None):
        super(GNEditorWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent=parent

        self.pb_ExitGN.clicked.connect(self.closeEvent)
        self.pb_SaveGN.clicked.connect(self.closeEvent)

    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()


#Класс редактирования ППС
class PPSEditorWindow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(PPSEditorWindow, self).__init__(parent)
        self.parent=parent
        self.setupUi(self)


    def closeEvent(self,event):
        self.TeacherSelectionWindow=TeacherSelectorWindow()
        self.TeacherSelectionWindow.show()
        self.hide()



#Класс Редактирования КО
class KOEditorWindow(QtWidgets.QMainWindow):
    def __init__(self,):
        super(KOEditorWindow, self).__init__()
        self.ui=Ui_KO_Editor()
        self.counter=0
        self.records = []
        self.record={}
        self.index = 0
        self.ui.setupUi(self)
        
        self.tableRecords()
        self.ui.pb_Save.clicked.connect(self.saveRecord)
        self.ui.pb_Add.clicked.connect(self.addRecord)
        self.ui.pb_Delete.clicked.connect(self.delRecord)
        self.ui.pb_Edit.clicked.connect(self.editRecord)

        self.ui.tb_KO.cellClicked.connect(self.ShowRecord)

        self.FIODialogUi=FIODialog()
        self.FIODialogUi.setupUi(self)

        self.UslPrDialogUI=UslPrDialog()
        self.UslPrDialogUI.setupUi(self)

        self.NaprPodgotovDialogUi=NaprPodgotovDialog()
        self.NaprPodgotovDialogUi.setupUi(self)

        self.EducationDialogUi=EducationDialog()
        self.EducationDialogUi.setupUi(self)

    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()

    def addRecord(self):
        if self.validation()==True:
            if self.ui.chB_State.isChecked()==False and self.ui.chB_Inner.isChecked()==False and self.ui.chB_Deal.isChecked()==False:
                self.UslPrDialogUI.show()
                return False
            else:
                self.fPPS = str(self.ui.le_FIO.text())
            if self.ui.chB_State.isChecked()==True:
                self.state = 1
            else:
                self.state = 0
            if self.ui.chB_Inner.isChecked()==True:
                self.inner = 1
            else:
                self.inner = 0
            if self.ui.chB_Deal.isChecked()==True:
                self.deal = 1
            else:
                self.deal = 0

            self.row=self.ui.tb_KO.currentRow()
            self.Dol = self.ui.cb_Dolzh.currentIndex()
            self.dRank = str(self.ui.cb_Dolzh.currentText())
            self.Step = self.ui.cb_Stepen.currentIndex()
            self.ucRank = str(self.ui.cb_Stepen.currentText())
            self.Zvan = self.ui.cb_zvan.currentIndex()
            self.zRank = str(self.ui.cb_zvan.currentText())
            self.nPPS = str(self.ui.tE_NaprPodgotov.toPlainText())
            self.ePPS = str(self.ui.tE_Education.toPlainText())
            self.record = {'FIO': self.fPPS,'Uslovia': [self.state,self.inner,self.deal], "Dolzhnost": self.Dol, "Stepen": self.Step, "Zvanie": self.Zvan, 'Napravlenie': self.nPPS, 'Education' : self.ePPS }
            self.records.append(self.record)
            if len(self.records)>1:
                SelSortPPS(self.records)
            writeCSV("PPSDB.csv",self.records)
            self.tableRecords()
            

    def tableRecords(self):
        self.records=PPSreadCSV("PPSDB.csv")
        if self.records:
            self.ui.tb_KO.setRowCount(0)
            self.index = len(self.records)
            print(self.index)
            for i in range(0, self.index):
                self.rowCount= i
                self.ui.tb_KO.insertRow(self.rowCount)
                if self.records[self.rowCount].get("Uslovia")[0]==1:     
                    self.c1PPS = str(self.ui.chB_State.text())
                else:
                    self.c1PPS  = str('')
                if self.records[self.rowCount].get("Uslovia")[1]==1:
                    self.c2PPS = str(self.ui.chB_Inner.text())
                else:
                    self.c2PPS  = str('')
                if self.records[self.rowCount].get("Uslovia")[2]==1:
                    self.c3PPS = str(self.ui.chB_Deal.text())
                else:
                    self.c3PPS  = str('')

                self.qboxPPS = self.c1PPS + ' ' + self.c2PPS + ' ' + self.c3PPS

                self.ui.tb_KO.setItem(self.rowCount, 0, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('FIO')))
                self.ui.tb_KO.setItem(self.rowCount, 1, QtWidgets.QTableWidgetItem(self.qboxPPS))
                self.ui.tb_KO.setItem(self.rowCount, 2, QtWidgets.QTableWidgetItem(self.ui.cb_Dolzh.itemText(self.records[self.rowCount].get("Dolzhnost"))))
                self.ui.tb_KO.setItem(self.rowCount, 3, QtWidgets.QTableWidgetItem(self.ui.cb_Stepen.itemText(self.records[self.rowCount].get("Stepen"))))
                self.ui.tb_KO.setItem(self.rowCount, 4, QtWidgets.QTableWidgetItem(self.ui.cb_zvan.itemText(self.records[self.rowCount].get("Zvanie"))))
                self.ui.tb_KO.setItem(self.rowCount, 6, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('Napravlenie')))
                self.ui.tb_KO.setItem(self.rowCount, 7, QtWidgets.QTableWidgetItem(self.records[self.rowCount].get('Education')))


    def delRecord(self):
        self.ui.tb_KO.removeRow(self.ui.tb_KO.currentRow())
        self.row=self.ui.tb_KO.currentRow()
        self.ui.tb_KO.setCurrentCell(self.row-1,0)
        self.records.pop(self.row)
        writeCSV("PPSDB.csv",self.records)
        
    def editRecord(self):
        self.ui.pb_Save.setEnabled(True)
        self.ui.pb_Add.setEnabled(False)
        self.ui.pb_Delete.setEnabled(False)
        self.ui.pb_Edit.setEnabled(False)
        

    def saveRecord(self):
        self.delRecord()
        self.addRecord()
        self.ui.pb_Save.setEnabled(False)
        self.ui.pb_Delete.setEnabled(True)
        self.ui.pb_Add.setEnabled(True)
        self.ui.pb_Edit.setEnabled(True)

    def ShowRecord(self,row,column):
        print(row)
        print(self.records)
        self.ui.le_FIO.setText(self.records[row].get("FIO"))
        if self.records[row].get("Uslovia")[0]==True:
            self.ui.chB_State.setChecked(True)
        else:
            self.ui.chB_State.setChecked(False)
        if self.records[row].get("Uslovia")[1]==True:
            self.ui.chB_Inner.setChecked(True)
        else:
            self.ui.chB_Inner.setChecked(False)
        if self.records[row].get("Uslovia")[2]==True:
            self.ui.chB_Deal.setChecked(True)
        else:
            self.ui.chB_Deal.setChecked(False)
        self.ui.cb_Dolzh.setCurrentIndex(self.records[row].get("Dolzhnost"))
        self.ui.cb_Stepen.setCurrentIndex(self.records[row].get("Stepen"))
        self.ui.cb_zvan.setCurrentIndex(self.records[row].get("Zvanie"))
        self.ui.tE_NaprPodgotov.setPlainText(self.records[row].get("Napravlenie"))
        self.ui.tE_Education.setPlainText(self.records[row].get("Education"))


    #Валидатор полей справочника аудиторий
    def validation(self):
        self.PPSValid=Validator.PPSValidator()

        self.FIO=self.ui.le_FIO.text()

        self.NaprPodgotov=self.ui.tE_NaprPodgotov.toPlainText()
        self.Education=self.ui.tE_NaprPodgotov.toPlainText()

        if (self.PPSValid.FIOValid(self.FIO))==True:
            if (self.PPSValid.NaprPodgotov(self.NaprPodgotov))==True:
                if (self.PPSValid.EducationValid(self.Education))==True:
                    return True
                else:
                    self.EducationDialogUi.show()
                    return False
            else:
                self.NaprPodgotovDialogUi.show()
                return False
        else:
            self.FIODialogUi.show()
            return False

        

        


#Класс выбора УП
class UPSelectorWindow(QtWidgets.QWidget, Ui_UPSelection):
    def __init__(self,parent=None):
        super(UPSelectorWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent=parent

        self.pb_saveUP.clicked.connect(self.closeEvent)

    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()


#Класс редактирования УП
class UPEditorWindow(QtWidgets.QWidget, Ui_UPReference):
    def __init__(self,parent=None):
        super(UPEditorWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent=parent

        self.pb_saveUP.clicked.connect(self.closeEvent)
        self.pb_ExitUP.clicked.connect(self.closeEvent)

    def closeEvent(self,event):
        self.MainAppWindowShow=MainAppWindow()
        self.MainAppWindowShow.show()
        self.close()
    

#Класс главного окна
class MainAppWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainAppWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Приложение для генерации справок")

        #Вызов файлового менеджера
        self.action_Open.triggered.connect(self.openFile)
        #Создание файла
        self.action_Save.triggered.connect(self.saveFile)

        """Кнопки вызова дочерних окон"""
        self.pb_KOChange.clicked.connect(self.openTeacherSelector)
        self.action_PPS.triggered.connect(self.openKOEditor)
        self.pb_UPChange.clicked.connect(self.openUPSelector)
        self.action_UP.triggered.connect(self.openUPEditor)
        self.pb_Group.clicked.connect(self.openGNEditor)
        self.pb_MTOChange.clicked.connect(self.openAudienceEditor)
        self.action_Audience.triggered.connect(self.openAudienceEditor)

    #Функция вызова файлового менеджера
    def openFile(self):
        self.filenameDocx = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", os.getcwd(), ".DOCX Файлы (*.docx)")
        directory=str(self.filenameDocx)
        docxDirectory=""
        counter=0
        for i  in range(2,len(directory)):
            if directory[i]=="\'":
                counter+=1
            if counter<1:
                docxDirectory=docxDirectory+directory[i]

        self.filenamePDF = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите файл", os.getcwd(), ".pdf Файлы (*.pdf)")
        directory=str(self.filenamePDF)
        PDFDirectory=""
        counter=0
        for i  in range(2,len(directory)):
            if directory[i]=="\'":
                counter+=1
            if counter<1:
                PDFDirectory=PDFDirectory+directory[i]

        convertDocxToPDF.convertDocxToPdf(docxDirectory,PDFDirectory)

    def saveFile(self):
        self.filename=QtWidgets.QFileDialog.getSaveFileName(self, "Выберите файл", os.getcwd(), ".DOCX Файлы (*.docx)")
        directory=str(self.filename)
        cleanDirectory=""
        counter=0
        for i  in range(2,len(directory)):
            if directory[i]=="\'":
                counter+=1
            if counter<1:
                cleanDirectory=cleanDirectory+directory[i]

        DocxGeneratingDef.allInOne(cleanDirectory)

    """Функции вызова дочерних окон"""
    def openTeacherSelector(self):
        self.TeacherSelectionWindow=TeacherSelectorWindow()
        self.TeacherSelectionWindow.show()
        self.hide()

    def openKOEditor(self):
        self.KOEditor=KOEditorWindow()
        self.KOEditor.show()
        self.hide()
  
    def openUPSelector(self):
        self.UPSelectWindow=UPSelectorWindow()
        self.UPSelectWindow.show()
        self.hide()

    def openUPEditor(self):
        self.UPEditingWindow=UPEditorWindow()
        self.UPEditingWindow.show()
        self.hide()

    def openGNEditor(self):
        self.GNEditingWindow=GNEditorWindow()
        self.GNEditingWindow.show()
        self.hide()

    def openAudienceEditor(self):
        self.AudienceEditingWindow=AudienceEditorWindow()
        self.AudienceEditingWindow.show()
        self.hide()
  
  
    



#Вызов программы
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=MainAppWindow()
    MainWindow.show()
    sys.exit(app.exec_())


