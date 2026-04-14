# default libs
from pathlib import Path

# custom objects
from objects.project import Project


class SelectorService:
    def select_project() -> Project:
        return Project(path=Path())
    
