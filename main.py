import datetime
import os
import sys
from PyQt5 import QtWidgets
import PyQt5.QtChart as QtChart
from PyQt5.QtCore import QTimer

import utils.config
from assets.aba import Ui_MainWindow
from assets.setup import Ui_Dialog
import utils.popUtil as popUtil
import utils.download as download
from utils import unzip


class Chart:
    seri = None
    x = None
    y = None

    def __init__(self, widget, seri_name, x_title_text, y_title_text, x_range, y_range):
        self.seri = QtChart.QLineSeries()
        self.seri.setName(seri_name)
        chart = QtChart.QChart()
        widget.setChart(chart)
        chart.addSeries(self.seri)
        self.x = QtChart.QValueAxis()
        self.x.setRange(0, x_range)
        self.x.setTitleText(x_title_text)
        self.y = QtChart.QValueAxis()
        self.y.setRange(0, y_range)
        self.y.setTitleText(y_title_text)
        chart.setAxisX(self.x, self.seri)
        chart.setAxisY(self.y, self.seri)


class MainApplication(QtWidgets.QMainWindow, Ui_MainWindow, QtWidgets.QWidget):
    config = None
    current = None
    capacity = None
    adbStatus = False
    chart1 = None
    chart2 = None
    dataTemp = "时间/s,电流/mA,电量/%\n"
    t2 = 0
    usedTime = 0
    ix = 1

    def __init__(self):
        super(MainApplication, self).__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.pairButton.clicked.connect(self.adbPair)
        self.connectButton.clicked.connect(self.adbLink)
        self.refreshButton.clicked.connect(self.adbDevices)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.timer.stop)
        self.csvButton.clicked.connect(self.csv)

    def csv(self):
        self.adbStatus = True
        name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        open(".\\" + name + ".csv", "w").write(self.dataTemp)
        self.adbInfo.setText("【System】已保存到程序目录下 " + name + ".csv")

    def adbPair(self):
        self.adbStatus = True
        ip = self.pairLineEdit.text()
        match = self.pairLineEdit_2.text()
        popUtil.popUtil(".\\platform-tools\\adb pair" + " " + ip + " " + match)
        self.adbInfo.setText("【System】配对成功后，您可以在手机的无线调试中看到您的电脑，对于Android11以及以下版本的设备，请直接使用下面的连接")

    def adbLink(self):
        self.adbStatus = True
        ip = self.linkLineEdit.text()
        popUtil.popUtil(".\\platform-tools\\adb connect " + ip)
        self.adbDevices()

    def adbDevices(self):
        self.adbStatus = True
        g = popUtil.popUtil(".\\platform-tools\\adb devices")
        self.adbInfo.setText(g)
        return g

    def start(self):
        self.adbStatus = True
        g = self.adbDevices().replace("List of devices attached", "").strip()
        if g == "":
            self.adbInfo.setText("【System】请连接设备")
        else:
            self.dataTemp = "时间/s,电流/mA,电量/%\n"
            self.timer.timeout.connect(self.setData)
            self.timer.start(1000)
            self.chart1 = Chart(self.widget_3, "电流/mA", "电量/%", "电流/mA", 100, 11000)
            self.chart2 = Chart(self.widget_4, "电流/mA", "时间/min", "电流/mA", self.ix, 11000)
            self.t2 = 0
            self.usedTime = 0
            self.config = utils.config.Config(".\\api.cfig")
            self.current = ".\\platform-tools\\adb shell cat " + self.config.getVar("current")
            self.capacity = ".\\platform-tools\\adb shell cat " + self.config.getVar("capacity")
            if self.current is None or self.current == ".\\platform-tools\\adb shell cat null":
                self.current = ".\\platform-tools\\adb shell cat /sys/class/power_supply/battery/current_now"
            if self.capacity is None or self.capacity == ".\\platform-tools\\adb shell cat null":
                self.capacity = ".\\platform-tools\\adb shell cat /sys/class/power_supply/battery/capacity"

    def setData(self):
        self.adbStatus = True
        cur = popUtil.popUtil(self.current)
        cap = popUtil.popUtil(self.capacity)
        y = 0
        t = 0
        if str(cur).strip() != "" and str(cap).strip() != "":
            y = (eval(cur) / 1000) * -1
            t = eval(cap)
            print("当前电流：{}".format(y), end=" ")
            print("当前电量：{}".format(t))
            if y > 0:
                self.chart2.seri.append(self.usedTime / 60, y)
                self.dataTemp += "{},{},{}\n".format(self.usedTime, y, t)
                if t != self.t2:
                    print(t)
                    print(self.t2)
                    self.chart1.seri.append(t, y)
                if self.usedTime % 60 == 0 and self.usedTime != 0:
                    self.ix += 1
                    self.chart2.x.setRange(0, self.ix)

            else:
                self.adbInfo.setText("【System】未在充电，已停止记录")
                self.timer.stop()
            self.t2 = t
            self.usedTime += 1
        else:
            self.adbInfo.setText("【System】接口有误，请检查接口配置")
            self.timer.stop()

    def closeEvent(self, event):
        if self.adbStatus:
            self.adbStatus = False
            popUtil.popUtil(".\\platform-tools\\adb kill-server")
        event.accept()


class SetupDialog(QtWidgets.QDialog, Ui_Dialog):
    main = None

    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.downButton.clicked.connect(self.download)
        self.main = main

    def download(self):
        download.download("https://dl.google.com/android/repository/platform-tools_r33.0.2-windows.zip?hl=zh-cn",
                          "platform-tools.zip", self.progressBar)
        unzip.unzip("platform-tools.zip", ".\\")
        MainApplication().show()
        self.close()
        self.main.show()


if __name__ == "__main__":

    if os.path.exists(".\\platform-tools"):
        app = QtWidgets.QApplication(sys.argv)
        window = MainApplication()
        window.show()
        sys.exit(app.exec_())
    else:
        setup = QtWidgets.QApplication(sys.argv)
        window = MainApplication()
        dialog = SetupDialog(window)
        dialog.show()
        sys.exit(setup.exec_())
