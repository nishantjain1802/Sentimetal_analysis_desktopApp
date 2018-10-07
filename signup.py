# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
import sqlite3
import ibm_db
import ibmdbpy


class Ui_SignUp(object):
    conn = ""

    def cloudConnectiontwo():
        print("called")
        dsn_driver = "IBM DB2 ODBC DRIVER"
        dsn_databases = "BLUDB"
        dsn_hostname = 'dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net'
        dsn_port = "50000"
        dsn_protocal = "TCPIP"
        dsn_uid = 'wkg83160'
        dsn_pwd = "8g2kgt18+2tljbrb"
        dsn = ("DRIVER={{IBM DB2 ODBC DRIVER}};"
               "DATABASE={0};"
               "HOSTNAME = {1};"
               "PORT = {2};"
               "PROTOCOL = TCPIP;"
               "UID={3};"
               "pwd ={4};").format(dsn_databases, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)
        global conn
        conn = ibm_db.connect(dsn, "", "")
        print("cloud connected")

    def insertData(self):
        Ui_SignUp.cloudConnectiontwo()
        username = self.unameInp.text()
        password = self.pswdInp.text()
        email = self.emailInp.text()
        conatct = int(self.contactInp.text())
        query = "insert into WKG83160.USERS1(username, pasd, email, contact) values('%s','%s','%s','%s')" % (
        username, password, email, conatct)
        stmt = ibm_db.exec_immediate(conn, query)
        self.clickLogin()

    def clickLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.uilogin = Ui_Login()
        self.uilogin.setupUiLogin(self.window)
        self.window.show()

    def setupUiSignUp(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QtCore.QSize(960, 640))
        MainWindow.setMaximumSize(QtCore.QSize(960, 640))
        MainWindow.setStyleSheet("background-image:url(:/newPrefix/watsonLogo.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.unameLbl = QtWidgets.QLabel(self.centralwidget)
        self.unameLbl.setGeometry(QtCore.QRect(260, 200, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.unameLbl.setFont(font)
        self.unameLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameLbl.setScaledContents(False)
        self.unameLbl.setWordWrap(False)
        self.unameLbl.setOpenExternalLinks(False)
        self.unameLbl.setObjectName("unameLbl")
        self.signupLbl = QtWidgets.QLabel(self.centralwidget)
        self.signupLbl.setGeometry(QtCore.QRect(420, 90, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.signupLbl.setFont(font)
        self.signupLbl.setStyleSheet("color:rgb(255, 255, 255);")
        self.signupLbl.setObjectName("signupLbl")
        self.unameInp = QtWidgets.QLineEdit(self.centralwidget)
        self.unameInp.setGeometry(QtCore.QRect(420, 210, 231, 25))
        self.unameInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.unameInp.setText("")
        self.unameInp.setObjectName("unameInp")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(220, 500, 112, 34))
        #######################login button clicked############
        self.loginBtn.clicked.connect(self.clickLogin)
        #######################################################
        font = QtGui.QFont()
        font.setPointSize(15)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginBtn.setObjectName("loginBtn")
        self.submitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitBtn.setGeometry(QtCore.QRect(410, 500, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.submitBtn.setFont(font)
        self.submitBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.submitBtn.setAutoDefault(True)
        self.submitBtn.setDefault(False)
        self.submitBtn.setFlat(False)
        self.submitBtn.setObjectName("submitBtn")
        ############################# insert data ##################
        self.submitBtn.clicked.connect(self.insertData)
        ############################################################
        self.pswdLbl = QtWidgets.QLabel(self.centralwidget)
        self.pswdLbl.setGeometry(QtCore.QRect(260, 250, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pswdLbl.setFont(font)
        self.pswdLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswdLbl.setObjectName("pswdLbl")
        self.pswdInp = QtWidgets.QLineEdit(self.centralwidget)
        self.pswdInp.setGeometry(QtCore.QRect(420, 270, 231, 25))
        self.pswdInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.pswdInp.setText("")
        self.pswdInp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswdInp.setObjectName("pswdInp")
        self.emailLbl = QtWidgets.QLabel(self.centralwidget)
        self.emailLbl.setGeometry(QtCore.QRect(260, 320, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.emailLbl.setFont(font)
        self.emailLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.emailLbl.setScaledContents(False)
        self.emailLbl.setWordWrap(False)
        self.emailLbl.setOpenExternalLinks(False)
        self.emailLbl.setObjectName("emailLbl")
        self.contactInp = QtWidgets.QLineEdit(self.centralwidget)
        self.contactInp.setGeometry(QtCore.QRect(420, 390, 231, 25))
        self.contactInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.contactInp.setText("")
        self.contactInp.setObjectName("contactInp")
        self.emailInp = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInp.setGeometry(QtCore.QRect(420, 330, 231, 25))
        self.emailInp.setStyleSheet("color: rgb(255, 255, 255);")
        self.emailInp.setObjectName("emailInp")
        self.contactLbl = QtWidgets.QLabel(self.centralwidget)
        self.contactLbl.setGeometry(QtCore.QRect(260, 370, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.contactLbl.setFont(font)
        self.contactLbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.contactLbl.setObjectName("contactLbl")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(590, 500, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resetBtn.setFont(font)
        self.resetBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.resetBtn.setAutoDefault(True)
        self.resetBtn.setDefault(False)
        self.resetBtn.setFlat(False)
        self.resetBtn.setObjectName("resetBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 60, 121, 111))
        self.label.setStyleSheet("background-image:url(:/newPrefix/User-Login-128.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signup"))
        self.unameLbl.setText(_translate("MainWindow", "USERNAME"))
        self.signupLbl.setText(_translate("MainWindow", "SIGNUP"))
        self.unameInp.setPlaceholderText(_translate("MainWindow", "username"))
        self.loginBtn.setText(_translate("MainWindow", "LOGIN"))
        self.submitBtn.setText(_translate("MainWindow", "SUBMIT"))
        self.pswdLbl.setText(_translate("MainWindow", "PASSWORD"))
        self.pswdInp.setPlaceholderText(_translate("MainWindow", "password"))
        self.emailLbl.setText(_translate("MainWindow", "EMAIL ID"))
        self.contactInp.setPlaceholderText(_translate("MainWindow", "contact"))
        self.emailInp.setPlaceholderText(_translate("MainWindow", "email"))
        self.contactLbl.setText(_translate("MainWindow", "CONTACT"))
        self.resetBtn.setText(_translate("MainWindow", "RESET"))


import picsIBM_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setupUiSignUp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
