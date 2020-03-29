# Python Password Generator
# Version 1.2

import password as ps
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    # Generate Button Clicked
    def generate_pass(self):
        try:
            user_pass_len = int(self.pass_len.text())
            if user_pass_len > 0:
                user_new_password = ps.Password(user_pass_len)
                self.pass_list.addItem(user_new_password.new_pass)
            else:
                return
        except ValueError:
            return
    
    def clear_list(self):
        self.pass_list.clear()

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
        self.pass_clear_btn.clicked.connect(self.clear_list)

        # Styling
        self.setStyleSheet(open('styles.css').read())

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
