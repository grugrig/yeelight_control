import sys
import ipaddress
import random

from PyQt5 import QtCore, QtWidgets


lst = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4"]

class MyWindow(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        QtWidgets.QWidget.__init__(self,parent)

        self.btnOn = QtWidgets.QPushButton("&On")
        self.btnOff = QtWidgets.QPushButton("Of&f")

        self.radBtn = QtWidgets.QVBoxLayout()
        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for ip in self.lst:
            btn = QtWidgets.QRadioButton(ip)
            self.radBtn.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[random.randint(
            0, len(self.lst)-1)].setChecked(True)
        
        self.hboxHor = QtWidgets.QHBoxLayout()
        self.hboxHor.addLayout(self.radBtn)

        self.vboxBtn = QtWidgets.QVBoxLayout()
        self.vboxBtn.addWidget(self.btnOn)
        self.vboxBtn.addWidget(self.btnOff)
        self.hboxHor.addLayout(self.vboxBtn)

        self.btnOn.clicked.connect(self.on_btnOn_clicked)
        self.btnOff.clicked.connect(self.on_btnOff_clicked)


        self.setLayout(self.hboxHor)
        self.setGeometry(400, 200, 325, 150)

    def on_btnOn_clicked(self):
        pass

    def on_btnOff_clicked(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(lst)
    window.setWindowTitle("Управление лампами")
    window.show()
    sys.exit(app.exec())