import logging as logger
import os


class StructureBuilder:
    """
    includes functions, filenames and directorynames
    to create
    """

    def __init__(self):
        self._directory_list = [
            "src",
            "tests",
            "data/raw",
            "data/interim",
            "data/external",
            "data/processed",
            "output",
            "reports/figures",
            "references",
            "docs",
        ]
        self._file_list = [
            ".gitignore",
            "README.md",
            "main.py",
            "LICENSE",
            "setup.py",
            "setup.cfg",
            "pyproject.toml",
            "MANIFEST.in",
            "requirements.txt",
            ".env",
        ]

    def initialize_structure(self):
        cdir = os.getcwd()
        for directory in self._directory_list:
            if os.path.exists(os.path.join(cdir, directory)):
                continue
            else:
                os.makedirs(os.path.join(cdir, directory))
                f = open(os.path.join(cdir, directory, ".gitadd"), "w+")
                f.close()
        file_dir = os.path.dirname(os.path.realpath(__file__))
        for file in self._file_list:
            if os.path.exists(os.path.join(cdir, file)):
                continue
            else:
                text_file = (
                    f"{file.strip('.').split('.')[0]}_text.py"
                    if not file.startswith("setup")
                    else f"{file}_text.py"
                )
                try:
                    logger.debug("reading text")
                    text = open(os.path.join(file_dir, text_file), "r").read()
                    text = text.strip('"""').strip("\n")
                except Exception:
                    logger.info(f"no default text set for {file}")
                    text = ""
                f = open(os.path.join(cdir, file), "w+")
                f.write(text)
                f.close()

    @staticmethod
    def mirror_project_structure(project_path: str) -> list:
        """reads the structure of a project on the main and second level of directories  

        Args:
            project_path (str): path to project to copy structure from 

        Returns:
            list, list: lists containing main level files and directories 
        """
        directories = []
        files = []
        important_files = ["__init__.py", "__main__.py"]

        if os.path.exists(project_path):
            included = os.listdir(project_path)

            # reading main level directories and files
            files = [os.path.isfile(os.path.join(project_path),f) for f in included]
            directories = [os.path.isdir(os.path.join(project_path),d) for d in included]

            # iteration over every directory to read files and directory beneath
            for directory in directories:
                dir_ = os.path.join(project_path, directory)
                included = os.listdir(dir_)
                for k in included:
                    if os.path.isdir(os.path.join(dir_, k)):
                        directories.append(f"{directory}/{k}")
                    elif os.path.isfile(os.path.join(dir_, k)) and k in important_files:
                        files.append(f"{directory}/{k}")

        return directories, files

    @property
    def directory_list(self):
        """getter method for list which contains all directories, that should be created.

        Returns:
            list: list of directories
        """
        return self._directory_list

    @directory_list.setter
    def directory_list(self, dl):
        """setter method for directory list

        Args:
            dl (list): new list of directories to be created
        """
        self._directory_list = dl

    @directory_list.deleter
    def directory_list(self):
        """deleter of directory list"""
        del self._directory_list

    @property
    def file_list(self):
        """getter method for list of files to create"""
        return self._file_list

    @file_list.setter
    def file_list(self, fl: list):
        """setter method for list of files to create

        Args:
            fl (list): new lit of files to create when calling class
        """
        self._file_list = fl

    @file_list.deleter
    def file_list(self):
        """delter method for list of files to create"""
        del self._file_list
