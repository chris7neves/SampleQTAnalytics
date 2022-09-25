from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")
        # Create the label widget
        self.label = QLabel()

        # Create the input widget
        self.input = QLineEdit()

        # Connect the signal from input to trigger the label's setText function.
        self.input.textChanged.connect(self.label.setText)

        # Add the widgets to a layout. This is covered in detail later
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # Wrap the layout in a container widget
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Note, slots and signals can be found in the documentation for each widget. Eg:
        # https://doc.qt.io/qt-5/qlabel.html#setMovie

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
