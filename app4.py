# Widgets
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        # We'll start with a simple label widget
        widget1 = QLabel("Hello")
        # To change the font of the widget, we need to first get the font from the widget
        # then change it. This ensures that the other font properties remain as the desktop defaults
        font = widget1.font()
        font.setPointSize(30)
        widget1.setFont(font)
        # we can use the pipe here necause the alignments are non
        # overlapping bitmasks. We can use only one H and V alignments at a time.
        widget1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # The alignment flags can be found in the documentation

        # A QLabel is also capable of holding an image in the form of a QPixmap
        # widget.setPixmap(QPixmap('filename.jpg'))
        # To make the image scale to fit the window completely we do
        # widget.setScaledContents(True)

        self.setCentralWidget(widget1)

        # Many more widgets are explained here https://www.pythonguis.com/tutorials/pyqt-basic-widgets/
        # but i don't think its beneficial to go through all of them right now

        # Some general notes:
        # - check boxed can be set to Qt.PartiallyChecked so that they can be part of a hierarchical checking scheme
        # (eg. other checkboxes become checkable if another is checked). You can also do .setTriState(True)
        # - QComboBox is a generic drop down list. Qt provides some specific drop down lists, line one made purposefully
        # for fonts (QFontComboBox). Items are added by passing a list of strings to .addItems().

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
