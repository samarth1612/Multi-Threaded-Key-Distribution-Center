# Import the required libraries
import sys
from PyQt5.QtWidgets import *

from ClientGUI import ClientUI


# Main driver function for the client
def fileIOClient():
    # Start a Qt application
    app = QApplication(sys.argv)
    # Initialize the file dialog class
    ex = ClientUI()
    # Show the file dialog window
    ex.show()
    # Exit the application, on click of close
    sys.exit(app.exec_())


if __name__ == '__main__':
    fileIOClient()
