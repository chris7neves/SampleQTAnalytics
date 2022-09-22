# Events

# The way to change the way widgets handle events is by subclassing a widget, and overriding the
# event handlers.

# Events are objects what are passed to event handlers. EG a mouseclick is part of QMouseEvent.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # If mouse tracking is disabled, then the window only receives events when one of the mouse buttons are pressed
        # If it is enabled, then the window will receive mouse move events even if no buttons are pressed
        self.setMouseTracking(True) # enabling this doesnt actually seem to change any behaviour though

        self.label = QLabel("Click in this Window")
        self.setCentralWidget(self.label)

        # Typically when you want to handle a click from a user, you should watch for both
        # the mouse click and release events

        # Lower down in this example, we intercepted the context menu event. However, we can also open a context menu
        # using the signal-slot approach

        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        # Notice that here we don't use Global Pos, we instead need to map the pos passed to the slot
        # to the global position of the window.
        context.exec(self.mapToGlobal(pos))

    # Events in QT are a collection of parameters that help characterize the event.
    # For example, QMouseEvent object has the following accessor methods:

    # .button() - specific button that triggered the event
    # .buttons() - state of all the mouse buttons
    # .globalPos() - application global position as a QPoint
    # .globalX() - x coord of application global pos
    # .globalY() - y pos
    # .pos() - widget relative position as a QPoint in integer
    # .posF() - widget relative position as a QPointF, float

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

    def contextMenuEvent(self, e) -> None:
        """
        When a context menu is *about* to appear, the QContextMenuEvent is fired.
        To intercept the event and handle it our way, we override the contextMenuEvent handler
        just like we did for the mouse buttons.
        """
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        # Create the menu at the position the event was fired at.
        # The position is relative to the parent that was used in its constructor
        # we passed self, this is why we can do globalPos
        context.exec(e.globalPos())

    # Lets say you want to simply intercept an event, add in some non-interfering behaviour, then continue with the
    # default functionality. We can do this by intercepting the event, adding our code, then calling the parent class
    # functionality

    # def mousePressEvent(self, e):
    #     print("Mouse pressed!")
    #     super(self, MainWindow).contextMenuEvent(e)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# Note: use .parent() to access the parent of a widget. Events will hit the uppermost widget first, then bubble up the
# hierarchy is they arent handled or accepted.

# Calling event.ignore() on an event in a custom event handler will bubble the event up the hierarchy