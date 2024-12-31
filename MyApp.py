import sys
from PyQt6 import QtWidgets
from MainWindowExt import MainWindowExt

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowExt()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
