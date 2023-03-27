from PyQt5 import QtCore, QtGui, QtWidgets
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 90, 411, 111))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label_5.setObjectName("label_5")
        self.sex = QtWidgets.QComboBox(self.groupBox)
        self.sex.setGeometry(QtCore.QRect(90, 70, 73, 22))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label_4.setObjectName("label_4")
        self.fullname = QtWidgets.QLineEdit(self.groupBox)
        self.fullname.setGeometry(QtCore.QRect(90, 30, 261, 22))
        self.fullname.setObjectName("fullname")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 240, 401, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.trongRangNum = QtWidgets.QSpinBox(self.groupBox_2)
        self.trongRangNum.setGeometry(QtCore.QRect(230, 130, 42, 22))
        self.trongRangNum.setObjectName("trongRangNum")
        self.niengRangCb = QtWidgets.QCheckBox(self.groupBox_2)
        self.niengRangCb.setGeometry(QtCore.QRect(260, 40, 91, 20))
        self.niengRangCb.setObjectName("niengRangCb")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.tayTrangCb = QtWidgets.QCheckBox(self.groupBox_2)
        self.tayTrangCb.setGeometry(QtCore.QRect(70, 40, 81, 20))
        self.tayTrangCb.setObjectName("tayTrangCb")
        self.nhoRangNum = QtWidgets.QSpinBox(self.groupBox_2)
        self.nhoRangNum.setGeometry(QtCore.QRect(230, 100, 42, 22))
        self.nhoRangNum.setObjectName("nhoRangNum")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.calcBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcBtn.setGeometry(QtCore.QRect(140, 460, 91, 31))
        self.calcBtn.setObjectName("calcBtn")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(250, 461, 171, 31))
        self.total.setObjectName("total")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 470, 55, 20))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # event
        self.calcBtn.clicked.connect(self.calcTotal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ứng dụng tính tiền phòng khám"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG TÍNH TIỀN PHÒNG KHÁM"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_5.setText(_translate("MainWindow", "Giới tính"))
        self.sex.setItemText(0, _translate("MainWindow", "Nam"))
        self.sex.setItemText(1, _translate("MainWindow", "Nữ"))
        self.label_4.setText(_translate("MainWindow", "Họ và tên"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dịch vụ"))
        self.niengRangCb.setText(_translate("MainWindow", "Niền răng"))
        self.label_3.setText(_translate("MainWindow", "Trồng răng"))
        self.tayTrangCb.setText(_translate("MainWindow", "Tẩy trắng"))
        self.label_2.setText(_translate("MainWindow", "Nhổ răng"))
        self.calcBtn.setText(_translate("MainWindow", "Tính tổng"))
        self.label_6.setText(_translate("MainWindow", "vnđ"))

    def calcTotal(self):
        prices = {
            "tayTrang": 100000,
            "niengRang": 200000,
            "nhoRang": 50000,
            "trongRang": 500000,
        }
        sum = (0 if self.tayTrangCb.checkState() == 0 else prices["tayTrang"]) \
            + (0 if self.niengRangCb.checkState() == 0 else prices["niengRang"]) \
            + int(self.nhoRangNum.text()) * prices["nhoRang"] \
            + int(self.trongRangNum.text()) * prices["trongRang"]
        self.total.setText(str(sum))

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Chào {} {}!".format("Ông" if self.sex.currentText() == "Nam" else "Bà", self.fullname.text()))
        msg.setInformativeText(" Tổng chi phí là {}vnđ".format(str(sum)))
        msg.setWindowTitle("Chi phí")
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())