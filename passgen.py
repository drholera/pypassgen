# Python Password Generator
# Version 1.2

import random, string, sys
from datetime import datetime
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class Password:
    """Build unique password"""

    today = datetime.now()
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    current_date = today.strftime("%Y/%m/%d %H:%M:%S")

    def __init__(self, pass_len):
        self.pass_len = pass_len
        self.new_pass = ''.join(random.choice(self.pass_chars) for _ in range(self.pass_len))


class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow constructor"""

        super().__init__()

        # Setup window title and size
        self.setWindowTitle("PyPassGen")
        # self.resize(400, 200) << REVISE

        # Setup Layout
        layout = qtw.QHBoxLayout()
        self.setLayout(layout)

        # Create Widgets
        pass_label = qtw.QLabel('Enter Password Lenght:', self)
        pass_len = qtw.QLineEdit(self, clearButtonEnabled=True, maxLength=20)
        pass_gen_btn = qtw.QPushButton('Generate', self)


        # Add Widgets to Layout
        layout.addWidget(pass_label)
        layout.addWidget(pass_len)
        layout.addWidget(pass_gen_btn)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec()) 