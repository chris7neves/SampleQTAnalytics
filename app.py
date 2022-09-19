import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# Only 1 QApplication instance is needed per application
app = QApplication(sys.argv)

# Creates and displays the window.
# In Qt, any widget can be a window
#window = QWidget()
window2 = QPushButton("Push Me")
# With Qt you can nest widgets inside an empty QWidget using layouts
# Qt already has something called the QMainWindow, its a pre-made widget
# that comes included with many standard window features that are 
# commonly used

# Widgets without a parent are by default invisible. This is why we call show.
# Application will by default exit when the last window is closed.
# Every application needs at least 1 window.
#window.show()
window2.show()

# Starts the event loop. Ends when app is exited
app.exec()
print("App exited successfully.")