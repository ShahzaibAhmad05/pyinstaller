"""
Entry point file for the whole app.
"""

# pyqt stuff
from PyQt6.QtWidgets import QApplication

# default libs
import sys
from pathlib import Path

# custom modules
from selector.main import SelectorService
from converter.main import ConverterService
from saver.main import SaverService

# custom objects
from objects.project import Project


def main() -> None:
    app: QApplication = QApplication(sys.argv)
    

    # get the project selector
    project: Project = SelectorService.select_project()
    

    # convert the project
    exe_temp_path: Path = ConverterService.convert_to_exe(project)
    

    # select the save path and save the exe
    exe_save_path: Path = SaverService.ask_for_save_path()
    SaverService.save_exe(exe_save_path, exe_temp_path)
    
    
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
    
