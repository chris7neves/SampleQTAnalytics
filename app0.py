import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt

# Only 1 QApplication instance is needed per application
app = QApplication(sys.argv)

# Creates and displays the window.

# In Qt, any widget can be a window
#window = QWidget()
#window2 = QPushButton("Push Me")

# With Qt you can nest widgets inside an empty QWidget using layouts
# Qt already has something called the QMainWindow, its a pre-made widget
# that comes included with many standard window features that are 
# commonly used

#window = QMainWindow() # The default QMainWindow has no content, we have to enable features
# To create a custom window, the best way to do it is to subclass QMainWindow and then include the setup for the window in the constructor, eg:

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__() # Call QMainWindow constructor, when subclassing Qt widgets, you must always call super to set up the parent class

        self.setWindowTitle("Tutorial App")
        button = QPushButton("Push me")

        # Set the central widget of the window
        self.setCentralWidget(button)

        # If we want to limit the size of the window, we use the QSize object and pass it to the window we just created
        # This makes it so that the window is not resizeable
        self.setFixedSize(QSize(400, 300))

        # You can also use setMinimumSize and setMaximumSize. All of these methods are from the QWidget class, from which 
        # QMainWindow inherits

# Widgets without a parent are by default invisible. This is why we call show.
# Application will by default exit when the last window is closed.
# Every application needs at least 1 window.
window = MainWindow()
window.show()


# Starts the event loop. Ends when app is exited
app.exec()
print("App exited successfully.")