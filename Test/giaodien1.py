# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giaodien.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(675, 614)
        mainWindow.setAcceptDrops(False)
        mainWindow.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
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
        self.fullname = QtWidgets.QLineEdit(self.groupBox)
        self.fullname.setGeometry(QtCore.QRect(90, 30, 261, 22))
        self.fullname.setObjectName("fullname")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label_5.setObjectName("label_5")
        self.sex = QtWidgets.QComboBox(self.groupBox)
        self.sex.setGeometry(QtCore.QRect(90, 70, 73, 22))
        self.sex.setMouseTracking(False)
        self.sex.setTabletTracking(False)
        self.sex.setAcceptDrops(False)
        self.sex.setAutoFillBackground(False)
        self.sex.setEditable(False)
        self.sex.setDuplicatesEnabled(False)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 240, 401, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tayTrangCb = QtWidgets.QCheckBox(self.groupBox_2)
        self.tayTrangCb.setGeometry(QtCore.QRect(70, 40, 81, 20))
        self.tayTrangCb.setObjectName("tayTrangCb")
        self.nienRangCb = QtWidgets.QCheckBox(self.groupBox_2)
        self.nienRangCb.setGeometry(QtCore.QRect(260, 40, 91, 20))
        self.nienRangCb.setObjectName("nienRangCb")
        self.nhoRangNum = QtWidgets.QSpinBox(self.groupBox_2)
        self.nhoRangNum.setGeometry(QtCore.QRect(230, 100, 42, 22))
        self.nhoRangNum.setObjectName("nhoRangNum")
        self.trongRangNum = QtWidgets.QSpinBox(self.groupBox_2)
        self.trongRangNum.setGeometry(QtCore.QRect(230, 130, 42, 22))
        self.trongRangNum.setObjectName("trongRangNum")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(140, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(250, 461, 171, 31))
        self.total.setObjectName("total")
        self.calcBtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcBtn.setGeometry(QtCore.QRect(140, 460, 91, 31))
        self.calcBtn.setObjectName("calcBtn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 470, 55, 20))
        self.label_6.setObjectName("label_6")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 26))
        self.menubar.setObjectName("menubar")
        self.menu_ng_d_ng_t_nh_ti_n_ph_ng_kh_m = QtWidgets.QMenu(self.menubar)
        self.menu_ng_d_ng_t_nh_ti_n_ph_ng_kh_m.setObjectName("menu_ng_d_ng_t_nh_ti_n_ph_ng_kh_m")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_ng_d_ng_t_nh_ti_n_ph_ng_kh_m.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Ứng dụng tính tiền phòng khám"))
        self.label.setText(_translate("mainWindow", "ỨNG DỤNG TÍNH TIỀN PHÒNG KHÁM"))
        self.groupBox.setTitle(_translate("mainWindow", "Thông tin khách hàng"))
        self.label_4.setText(_translate("mainWindow", "Họ và tên"))
        self.label_5.setText(_translate("mainWindow", "Giới tính"))
        self.sex.setItemText(0, _translate("mainWindow", "Nam"))
        self.sex.setItemText(1, _translate("mainWindow", "Nữ"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Dịch vụ"))
        self.tayTrangCb.setText(_translate("mainWindow", "Tẩy răng"))
        self.nienRangCb.setText(_translate("mainWindow", "Niềng răng"))
        self.label_2.setText(_translate("mainWindow", "Nhổ răng"))
        self.label_3.setText(_translate("mainWindow", "Trồng răng"))
        self.calcBtn.setText(_translate("mainWindow", "Tính tổng"))
        self.label_6.setText(_translate("mainWindow", "VND"))
        self.menu_ng_d_ng_t_nh_ti_n_ph_ng_kh_m.setTitle(_translate("mainWindow", "Ứng dụng tính tiền phòng khám"))

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
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())