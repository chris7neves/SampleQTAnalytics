# Layouts

# There are 4 different types of basic layouts in PyQt5
# - QHBoxLayout
# - QVBoxLayout
# - QGridLayout
# - QStackedLayout

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")


class Color(QWidget): # Subclass widget to make custom widget

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True) # Set the widget to automatically fill the background with the window color

        palette = self.palette() # Extract the widgets palette so we can modify it
        palette.setColor(QPalette.Window, QColor(color)) # We set the current palette's window color to a color of our choice
        self.setPalette(palette) # Set the palette of the widget to our new palette


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()