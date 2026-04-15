import sys
import ipaddress

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QPushButton,
    QDialog,
    QLineEdit
)

class GetIp(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 425, 150)
        self.setWindowTitle('Получение IP адресов устройств')
        self.line_edits = []
        x = 15
        y = 15
        for i in range(4):
            text = f'Устройство №{i+1}'
            self.label = QLabel(text, self)
            self.label.resize(self.label.sizeHint())
            self.label.move(x, y)

            line_edit = QLineEdit(self)
            line_edit.setObjectName(f"edit_{i}")
            line_edit.resize(150, 20)
            line_edit.move(x+120, y)
            self.line_edits.append(line_edit)
            y += 30

            self.button = QPushButton('Отправить', self)
            self.button.resize(self.button.sizeHint())
            self.button.move(315, 60)
            self.button.clicked.connect(self.run)

    def run(self):
        addresses = []
        for item in self.line_edits:
            if item.text():
                addresses.append(item.text())

        if addresses:
            for i in addresses:
                try:
                    ipaddress.ip_address(i)
                except ValueError:
                    QMessageBox.information(
                        self, 'Message', 'Проверьте адреса!')
                    return
                

        else:
            QMessageBox.information(
                        self, 'Message', 'Вы ничего не ввели!')
            return
        
        # window = MyWindow(addresses)
        # window.setWindowTitle("Управление лампами")
        # self.close()
        # window.exec_()

        print(addresses)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GetIp()
    ex.show()
    sys.exit(app.exec())
