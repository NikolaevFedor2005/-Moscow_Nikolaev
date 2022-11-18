from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import random

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('календарь.ui', self)
        self.events = []

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.listWidget.clear()
        self.events.append(
            (self.calendarWidget.selectedDate().toString('yyyy-MM-dd'),
             self.timeEdit.time().toString(),
             self.lineEdit.text())
        )
        self.listWidget.addItems(['; '.join(item) for item in sorted(self.events)])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())