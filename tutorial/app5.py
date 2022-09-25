# Layouts

# There are 4 different types of basic layouts in PyQt5
# - QHBoxLayout
# - QVBoxLayout
# - QGridLayout
# - QStackedLayout

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton, QStackedWidget, QStackedLayout, QTabWidget)
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget): # Subclass widget to make custom widget

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True) # Set the widget to automatically fill the background with the window color

        palette = self.palette() # Extract the widgets palette so we can modify it
        palette.setColor(QPalette.Window, QColor(color)) # We set the current palette's window color to a color of our choice
        self.setPalette(palette) # Set the palette of the widget to our new palette


class MainWindowV(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QVBoxLayout")

        layout = QVBoxLayout()

        # In a QVBoxLayout, adding widgets adds them to the bottom of the stack
        # this layout is simply widgets stacked vertically
        # We need to set this layout in a dummy widget before adding it to the main window

        layout.addWidget(Color("red")) # The layout with just one color will have a border around the widget
        # This is called layout spacing and can be modified

        layout.addWidget(Color("blue")) # Layout spacing also handles the spacing between widgets in a layout
        layout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

class MainWindowH(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("H Box Layout")

        layout = QHBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# In order to get more complex window designs, we can nest layouts
class MainWindowN(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested Layout")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        # To set the spacing around the layout use
        layout1.setContentsMargins(0, 0, 0, 0)

        # To set the spacing around the widgets use
        layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

# Sometimes, if we want to layout multiple elements, it would be hard to line them up just by using
# nested layouts. For this, we can use widgets arranged in a grid
# For this, we use QGridLayout. We then specify the widget placement by providing (row, col)
# Grid elements can be left empty

class MainWindowG(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

# Lets say we want to create a window with multiple tabs. The way to do this is by using a stacked
# layout (it imitates tabs) We can use the QStackedWidget in order to add the widget directly to the window
# as a central widget. We use the layout.setCurrentIndex() to choose which of the stacked widgets to show


# The following is an example of building a tab system from scratch using layouts

class TabbedWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Layout for the whole page
        self.page_layout = QVBoxLayout()

        # Layout for the colors
        self.color_layout = QStackedLayout()
        self.color_layout.addWidget(Color("red"))
        self.color_layout.addWidget(Color("blue"))
        self.color_layout.addWidget(Color("green"))

        # Layout for the buttons
        self.button_layout = QHBoxLayout()

        self.button1 = QPushButton("red")
        self.button_layout.addWidget(self.button1)
        self.button1.clicked.connect(self.red_button)

        self.button2 = QPushButton("blue")
        self.button_layout.addWidget(self.button2)
        self.button2.clicked.connect(self.blue_button)

        self.button3 = QPushButton("green")
        self.button_layout.addWidget(self.button3)
        self.button3.clicked.connect(self.green_button)

        # Add the color and button layouts to the page layout
        self.page_layout.addLayout(self.button_layout)
        self.page_layout.addLayout(self.color_layout)

        widget = QWidget()
        widget.setLayout(self.page_layout)
        self.setCentralWidget(widget)

    def red_button(self):
        self.color_layout.setCurrentIndex(0)

    def blue_button(self):
        self.color_layout.setCurrentIndex(1)

    def green_button(self):
        self.color_layout.setCurrentIndex(2)

# Doing the same thing but with the TabWdiget, the built in solution for tabbed windows

class MainWindowTW(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabbed WIdget test")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)




app = QApplication(sys.argv)

#window = MainWindowV() # QVBoxLayout
#window = MainWindowH() #QHBoxLayout
#window = MainWindowN() # Nested layouts
#window = MainWindowG() # Grid layout with some elemts missing
#window = TabbedWindow() # Example of custom tabbed window
window = MainWindowTW() # Tabbed window using the builtin tab widget

window.show()

app.exec()