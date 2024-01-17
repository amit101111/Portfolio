# This Python file uses the following encoding: utf-8
import sys
import pytz

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from datetime import (datetime, date)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def mouseMoveEvent(self, e):
        now = datetime.now(pytz.timezone('Asia/Dhaka'))
        self.ui.currentTime.setText(now.strftime("%H:%M:%S"))

    def mousePressEvent(self, e):
        today = date.today()
        self.ui.currentDate.setText(str(today))

    '''def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
