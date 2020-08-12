# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from lib.currencies import get_latest_btc
import random
import json


class Ui_AutoInvest(object):
    def setupUi(self, AutoInvest):
        AutoInvest.setObjectName("AutoInvest")
        AutoInvest.resize(646, 675)
        self.centralwidget = QtWidgets.QWidget(AutoInvest)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setToolTip("")
        self.label_2.setObjectName("label_2")
        self.email_recipient = QtWidgets.QTextEdit(self.centralwidget)
        self.email_recipient.setGeometry(QtCore.QRect(10, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_recipient.setFont(font)
        self.email_recipient.setToolTip("")
        self.email_recipient.setObjectName("email_recipient")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setToolTip("")
        self.label_3.setObjectName("label_3")
        self.email_sender = QtWidgets.QTextEdit(self.centralwidget)
        self.email_sender.setGeometry(QtCore.QRect(60, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_sender.setFont(font)
        self.email_sender.setToolTip("")
        self.email_sender.setStatusTip("")
        self.email_sender.setWhatsThis("")
        self.email_sender.setAccessibleName("")
        self.email_sender.setObjectName("email_sender")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.email_passwd = QtWidgets.QTextEdit(self.centralwidget)
        self.email_passwd.setGeometry(QtCore.QRect(290, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.email_passwd.setFont(font)
        self.email_passwd.setToolTip("")
        self.email_passwd.setStatusTip("")
        self.email_passwd.setWhatsThis("")
        self.email_passwd.setAccessibleName("")
        self.email_passwd.setObjectName("email_passwd")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setToolTip("")
        self.label_6.setObjectName("label_6")
        self.your_btc = QtWidgets.QTextEdit(self.centralwidget)
        self.your_btc.setGeometry(QtCore.QRect(10, 350, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.your_btc.setFont(font)
        self.your_btc.setToolTip("")
        self.your_btc.setObjectName("your_btc")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 410, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setToolTip("")
        self.label_7.setObjectName("label_7")
        self.value = QtWidgets.QTextEdit(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(10, 450, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.value.setFont(font)
        self.value.setToolTip("")
        self.value.setObjectName("value")
        self.currency = QtWidgets.QComboBox(self.centralwidget)
        self.currency.setGeometry(QtCore.QRect(180, 450, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.currency.setFont(font)
        self.currency.setObjectName("currency")
        self.currency.addItem("")
        self.currency.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setToolTip("")
        self.label_8.setObjectName("label_8")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(10, 580, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        AutoInvest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutoInvest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 21))
        self.menubar.setObjectName("menubar")
        AutoInvest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AutoInvest)
        self.statusbar.setObjectName("statusbar")
        AutoInvest.setStatusBar(self.statusbar)

        self.retranslateUi(AutoInvest)
        QtCore.QMetaObject.connectSlotsByName(AutoInvest)

        self.start_btn.clicked.connect(lambda: self.start_clicked(
            self.email_sender.toPlainText(),
            self.email_passwd.toPlainText(),
            self.email_recipient.toPlainText(),
            self.isfloat(self.your_btc.toPlainText()),
            self.isfloat(self.value.toPlainText()),
            str(self.currency.currentText()),
            get_latest_btc(),
        ))

    def retranslateUi(self, AutoInvest):
        _translate = QtCore.QCoreApplication.translate
        AutoInvest.setWindowTitle(_translate("AutoInvest", "AutoInvest"))
        self.label.setText(_translate("AutoInvest", "AutoInvest"))
        self.label_2.setText(_translate("AutoInvest", "Email recipient"))
        self.email_recipient.setHtml(_translate("AutoInvest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.label_3.setText(_translate("AutoInvest", "Email sender"))
        self.email_sender.setHtml(_translate("AutoInvest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("AutoInvest", "Email:"))
        self.label_5.setText(_translate("AutoInvest", "Passwd:"))
        self.email_passwd.setHtml(_translate("AutoInvest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.label_6.setText(_translate("AutoInvest", "Your Bitcoins"))
        self.your_btc.setHtml(_translate("AutoInvest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.label_7.setText(_translate("AutoInvest", "Notify me when BTC value is "))
        self.value.setHtml(_translate("AutoInvest", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.currency.setItemText(0, _translate("AutoInvest", "BTC"))
        self.currency.setItemText(1, _translate("AutoInvest", "EUR"))
        self.label_8.setText(_translate("AutoInvest", "greater"))
        self.start_btn.setText(_translate("AutoInvest", "Start"))

    def start_clicked(self, email_sender, 
                      email_passwd, 
                      email_recipient,
                      your_btc,
                      value, 
                      currency,
                      past_btc_value):

        if email_sender == '' or email_passwd == '' or email_recipient == '' or your_btc == '' or value == '':
            self.show_popup('AutoInvest', 'Looks like you haven\'t entered all values.', QMessageBox.Warning)

        else:
            new_user = {
                'email_sender': email_sender,
                'email_passwd': email_passwd,
                'email_recipient': email_recipient,
                'your_btc': your_btc,
                'value': value,
                'currency': currency,
                'past_btc_value': past_btc_value,
            }

            users = json.load(open('./data/users.json'))
            
            user_id = str(random.randint(100000000000000000000000000000, 999999999999999999999999999999))

            with open('./data/users.json', 'w') as f:
                users[user_id] = new_user
                
                json.dump(users, f, indent=4, sort_keys=True)
            
            self.show_popup('Success!', 'We have now added you to our users.', QMessageBox.Information)
    
    def show_popup(self, title, text, icon):
        msg = QMessageBox()

        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)

        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()
    
    def isfloat(self, value):
        try:
            float(value)
        
        except ValueError:
            self.show_popup('AutoInvest', 'Looks like you haven\'t entered a valid number. Quitting...', QMessageBox.Critical)
            
            exit()

        else:
            return float(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoInvest = QtWidgets.QMainWindow()
    ui = Ui_AutoInvest()
    ui.setupUi(AutoInvest)
    AutoInvest.show()
    sys.exit(app.exec_())
