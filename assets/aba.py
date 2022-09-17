# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\AndroidBatteryAnalyst\ABA.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import win32api
import win32con
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / 2, win32api.GetSystemMetrics(win32con.SM_CYSCREEN) / 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 5, 2, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout.addWidget(self.stopButton, 5, 3, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 4, 0, 1, 4)
        self.linkLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkLineEdit.sizePolicy().hasHeightForWidth())
        self.linkLineEdit.setSizePolicy(sizePolicy)
        self.linkLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.linkLineEdit.setObjectName("linkLineEdit")
        self.gridLayout.addWidget(self.linkLineEdit, 3, 0, 1, 4)
        self.pairButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pairButton.sizePolicy().hasHeightForWidth())
        self.pairButton.setSizePolicy(sizePolicy)
        self.pairButton.setObjectName("pairButton")
        self.gridLayout.addWidget(self.pairButton, 2, 0, 1, 4)
        self.pairLineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pairLineEdit_2.sizePolicy().hasHeightForWidth())
        self.pairLineEdit_2.setSizePolicy(sizePolicy)
        self.pairLineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pairLineEdit_2.setObjectName("pairLineEdit_2")
        self.gridLayout.addWidget(self.pairLineEdit_2, 1, 0, 1, 4)
        self.pairLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pairLineEdit.sizePolicy().hasHeightForWidth())
        self.pairLineEdit.setSizePolicy(sizePolicy)
        self.pairLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pairLineEdit.setObjectName("pairLineEdit")
        self.gridLayout.addWidget(self.pairLineEdit, 0, 0, 1, 4)
        self.adbInfo = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adbInfo.sizePolicy().hasHeightForWidth())
        self.adbInfo.setSizePolicy(sizePolicy)
        self.adbInfo.setObjectName("adbInfo")
        self.gridLayout.addWidget(self.adbInfo, 6, 0, 1, 4)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout.addWidget(self.refreshButton, 5, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(6, 9)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 3, 1)
        self.widget_3 = QChartView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)
        self.widget_4 = QChartView(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2.addWidget(self.widget_4, 1, 1, 1, 1)
        self.csvButton = QtWidgets.QPushButton(self.centralwidget)
        self.csvButton.setObjectName("csvButton")
        self.gridLayout_2.addWidget(self.csvButton, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 8)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 8)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AndroidChargeAnalyst"))
        self.startButton.setText(_translate("MainWindow", "开始记录"))
        self.stopButton.setText(_translate("MainWindow", "停止记录"))
        self.connectButton.setText(_translate("MainWindow", "连接设备"))
        self.linkLineEdit.setPlaceholderText(_translate("MainWindow", "这里输入连接地址"))
        self.pairButton.setText(_translate("MainWindow", "配对设备"))
        self.pairLineEdit_2.setPlaceholderText(_translate("MainWindow", "这里输入配对码"))
        self.pairLineEdit.setPlaceholderText(_translate("MainWindow", "这里输入配对地址"))
        self.refreshButton.setText(_translate("MainWindow", "显示已连接设备"))
        self.csvButton.setText(_translate("MainWindow", "以CSV文件将数据导出Excel"))
from PyQt5.QtChart import QChartView
