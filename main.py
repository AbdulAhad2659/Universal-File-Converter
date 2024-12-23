import sys
from PyQt5.QtWidgets import QApplication
from gui import FileConverterApp  # Import the FileConverterApp class from gui.py

def main():
    """
    Main function to create and run the File Converter application.
    """
    app = QApplication(sys.argv)
    ex = FileConverterApp()
    ex.show()  # Make sure the window is shown
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    