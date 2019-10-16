# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_launch.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.target_details = QtWidgets.QLineEdit(self.centralwidget)
        self.target_details.setGeometry(QtCore.QRect(190, 40, 201, 20))
        self.target_details.setObjectName("target_details")
        self.sitename = QtWidgets.QLineEdit(self.centralwidget)
        self.sitename.setGeometry(QtCore.QRect(190, 70, 201, 20))
        self.sitename.setObjectName("sitename")
        self.nodes = QtWidgets.QLineEdit(self.centralwidget)
        self.nodes.setGeometry(QtCore.QRect(190, 160, 201, 20))
        self.nodes.setObjectName("nodes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 91, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.launch_btn = QtWidgets.QPushButton(self.centralwidget)
        self.launch_btn.setGeometry(QtCore.QRect(190, 230, 75, 23))
        self.launch_btn.setObjectName("launch_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 40, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 70, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 160, 171, 16))
        self.label_6.setObjectName("label_6")
        self.cancle = QtWidgets.QPushButton(self.centralwidget)
        self.cancle.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.cancle.setObjectName("cancle")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 100, 47, 13))
        self.label_7.setObjectName("label_7")
        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(190, 100, 201, 20))
        self.userid.setObjectName("userid")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 130, 47, 13))
        self.label_9.setObjectName("label_9")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 130, 201, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Launcher"))
        self.label.setText(_translate("MainWindow", "Target server"))
        self.label_2.setText(_translate("MainWindow", "Site Name"))
        self.label_3.setText(_translate("MainWindow", "Nodes"))
        self.launch_btn.setText(_translate("MainWindow", "Launch Test"))
        self.label_4.setText(_translate("MainWindow", "ex(http://server:port)"))
        self.label_5.setText(_translate("MainWindow", "ex(PSFINDMO)"))
        self.label_6.setText(_translate("MainWindow", "ex(PSFT_HR,HRMS)"))
        self.cancle.setText(_translate("MainWindow", "Cancle"))
        self.label_7.setText(_translate("MainWindow", "User ID"))
        self.label_9.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

