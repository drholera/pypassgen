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

    # Generate Button Clicked
    def generate_pass(self):
        user_pass_len = int(self.pass_len.text())
        user_new_password = Password(user_pass_len)
        self.pass_list.addItem(user_new_password.new_pass)
        print("New password was generated")

    def __init__(self):
        """MainWindow constructor"""

        super().__init__()

        # Setup window title and size
        self.setWindowTitle("PyPassGen")
        # self.resize(400, 200) << REVISE

        # Setup Main Layout
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # Setup Top Layout
        top_layout = qtw.QHBoxLayout()
        main_layout.addLayout(top_layout)

        # Setup Bottom Layout
        bottom_layout = qtw.QGridLayout()
        main_layout.addLayout(bottom_layout)

        # Create Widgets
        self.pass_label = qtw.QLabel('Enter Password Lenght:')
        self.pass_len = qtw.QLineEdit(clearButtonEnabled=True, maxLength=20)
        self.pass_gen_btn = qtw.QPushButton('Generate')
        self.pass_list = qtw.QListWidget()
        self.pass_clear_btn = qtw.QPushButton('Clear')


        # Add Widgets to top_layout
        top_layout.addWidget(self.pass_label)
        top_layout.addWidget(self.pass_len)
        top_layout.addWidget(self.pass_gen_btn)

        # Add Widgets to bottom layout
        bottom_layout.addWidget(self.pass_clear_btn,2,1)
        bottom_layout.addWidget(self.pass_list,1,1)

        # Handle Events
        self.pass_gen_btn.clicked.connect(self.generate_pass)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
