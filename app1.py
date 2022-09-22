# Signals and Slots

# A signal is emitted by a widget when something happens.
# Signals can also send data to provide more context about what happened
# Custom signals can also be created

# Slots are what Qt uses to receive signals

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked) # clicked is a "signal" member of the QPushButton class
        #button.clicked.connect(self.the_button_was_toggled) # You can connect as many slots as you want to a signal

        self.button.setChecked(self.button_is_checked)

        # Every widget has signals that are pretty extensive, for example, the QMainWindow
        # Something that is very important to note is that not all signals fire when you expect them too
        # and you should be checking the docs to find out when they do.
        # For example, windowTitleChanged does not fire if the new title is the same as the old one.
        # It only fires if the new title is different.
        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Note, without this line, the button just doesnt appear. Which makes sense, its just a local object.
        self.setCentralWidget(self.button)
        

    def the_button_was_clicked(self):
        """
        Custom slot that waits for the button press signal.
        Prints 'Clicked!' to console.
        """
        #print("Clicked!")
        self.button.setText("You already clicked me.")
        #self.button.setEnabled(False) # Greys out and disables the button

        new_window_title = choice(window_titles)
        print("Setting the title to: {}".format(new_window_title))
        self.setWindowTitle(new_window_title)

    def the_button_was_toggled(self, checked):
        
        # You can store the values of widgets in a class member
        self.button_is_checked = checked

        print("Checked?", checked)

    def the_window_title_changed(self, window_title):
        print("Window title changed to: {}".format(window_title))
        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()