"""
Entry point file for the whole app.
"""

# pyqt stuff
from PyQt6.QtWidgets import QApplication

# default libs
import sys

# custom modules
from ui.pyinstaller import pyinstaller


def main() -> None:
    app: QApplication = QApplication()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
    
