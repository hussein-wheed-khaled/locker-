import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import os
import winsound
import time


class MainWindow(QDialog):
    global password
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("locker.ui",self)
        self.pushButton.clicked.connect(self.browsefiles)
        self.pushButton_2.clicked.connect(self.savepassword)
        self.pushButton_4.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.exit)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
    def exit(self):
        sys.exit(app.exec_())


    def browsefiles(self):
        global fname
        global saving
        fname=QFileDialog.getOpenFileName(self, 'select file','exe files (.exe)')
        self.lineEdit.setText(fname[0])


    def savepassword(self):
        global password
        global saving
        password=self.lineEdit_2.text()
        with open("C:\ProgramData\password locker pro\password.txt","w") as saving:
            saving.write(password)



        if fname == "":
            msg1 = QMessageBox()
            msg1.setWindowTitle("Enter path file")
            msg1.setFixedWidth(20)
            msg1.setFixedHeight(20)
            msg1.setText("Please select file you want to lock by click browse ")
            msg1.show()
            winsound.PlaySound("run.wav", winsound.SND_FILENAME)

            x = msg1.exec_()

        elif password == "":
            msg2 = QMessageBox()
            msg2.setWindowTitle("Enter password")
            msg2.setText("Please Enter password before click save ")
            msg2.setFixedWidth(30)
            msg2.setFixedHeight(30)
            msg2.show()
            winsound.PlaySound("run.wav", winsound.SND_FILENAME)

            x = msg2.exec_()

        elif len(password) <=4:
            msg3 = QMessageBox()
            msg3.setWindowTitle("Error ")
            msg3.setFixedWidth(60)
            msg3.setFixedHeight(60)
            msg3.setText(" password most be more than 4 letters ")
            msg3.show()
            x = msg3.exec_()



        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warring !!")

            msg.setText("you almost locked the file selected in :\n" + str(fname[0])+"\n Are you sure want to continue?")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.setFixedWidth(170)
            msg.setFixedHeight(190)

            msg.setDefaultButton(QMessageBox.Ok)
            msg.show()
            msg.buttonClicked.connect(self.lock)
            winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
            x = msg.exec_()


    def lock(self,i):
             global change

             ii = QMessageBox()
             ii.setWindowTitle("successfully done")
             ii.setText("you are successfully lock the program in path :\n" + str(fname[0]))
             ii.show()
             x = ii.exec_()
             change = str(fname[0]).replace("exe", "lock")
             os.rename(str(fname[0]), change)
















    def login(self):

        newwindow=MainWindow2()
        widget.addWidget(newwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow2(QDialog):


    def __init__(self):

      super(MainWindow2, self).__init__()
      loadUi("password.ui", self)
      self.pushButton2.clicked.connect(self.ok)
      self.button.clicked.connect(self.back)
      self.pushButtonb.clicked.connect(self.open)
      self.lineEdit3.setEchoMode(QtWidgets.QLineEdit.Password)
    def open(self):
        global fpath
        fpath = QFileDialog.getOpenFileName(self, 'select file', 'lock files (.lock)')
        self.lineEdit2.setText(fpath[0])

    def ok(self):
        with open("C:\ProgramData\password locker pro\password.txt","r+") as q:
            read=q.read()


        if self.lineEdit3.text() == read :

            unlock = str(fpath[0]).replace("lock", "exe")
            os.rename(fpath[0], unlock)
            un=QMessageBox()
            un.setWindowTitle("successfully unlock ")
            un.setText("your program now is unlocked enjoy :)")
            winsound.PlaySound("true.wav", winsound.SND_FILENAME)
            un.show()
            x=un.exec_()


        else:
            q=QMessageBox()
            q.setWindowTitle("Error")
            q.setText("password Error try again")
            winsound.PlaySound("passworderror.wav", winsound.SND_FILENAME)
            q.show()
            x=q.exec_()




    def back(self):
        newwindow = MainWindow()
        widget.addWidget(newwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)





















app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(530)
widget.setFixedHeight(450)
widget.show()
sys.exit(app.exec_())

