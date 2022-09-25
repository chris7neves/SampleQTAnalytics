# Toolbars
# QAction is used to avoid repetition of actions common to many toolbars

# In Qt, toolbars are created using the QToolBar class
# We create an instance of that class then call .addToolbar on the mainwindow class
# Passing a string as the first constructor parameter to QToolBar gives a name to the toolbar

# By default, you can remove and move around toolbars. In general, you want to make at least one
# toolbar unremoveable or make a context menu where you can add or remove various toolbars

# The standard way of adding features to the toolbar is to create QActions. This provides a way
# for us to describe an abstract user interface. For example, instead of defining Cut in 3 different
# places, you define it once with a general interface and just add it wherever you want it

import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        toolbar = QToolBar("Utilities")
        self.addToolBar(toolbar)

        button_action = QAction("Your Button", self) # PArent for the action is the final param
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

        # If we wanted to give our action an icon, we would do
        # button_action = QAction(QIcon("bug.png"), "Your Button", self)
        # This replaces the actions text with an icon
        # and if we wanted to set its size
        # toolbar.setIconSize(QSize(16, 16))
        # Sometimes the OS settings will dictate whether actions are displayed via their text or their
        # icon.
        # We can override this by doing self.setToolButtonStyle() and providing it with any of the
        # supplied tags

        # The status bar is what displays a message or a description either of something happening in general,
        # or of what your mouse is hovering over. Status bar text is updated as we hover over our actions
        self.setStatusBar(QStatusBar(self))

        # Now lets add a menu
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)

        # Create a second button
        button_action2 = QAction("Your Button2", self)  # PArent for the action is the final param
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        # Add a menu separator
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        # Add a submenu, this will expand on hover
        sub_menu = file_menu.addMenu("&Sub")
        sub_menu.addAction(button_action)

        # We can also add keyboard shortcuts to actions
        button_action2.setShortcut(QKeySequence("Ctrl+p"))

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignVCenter)
        self.setCentralWidget(label)

        # Note, we can add literally anything to the toolbar including widgets or whatever.

    def onMyToolBarButtonClick(self, s):
        print("click", s)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()