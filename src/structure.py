import logging as logger
import os


class StructureBuilder:
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
            "requirements.txt",
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

        for file in self._file_list:
            if os.path.exists(os.path.join(cdir, file)):
                continue
            else:
                text_file = f"{file.strip('.').split('.')[0]}_text.txt"
                try:
                    text = open(os.path.join("data", "raw", text_file), "r").read()
                    f = open(os.path.join(cdir, file), "w+")
                except Exception as e:
                    logger.warning(f"reading text for {file} failed with error: {e}")
                    text = ""
                f.write(text)
                f.close()

    @property
    def directory_list(self):
        return self._directory_list

    @directory_list.setter
    def directory_list(self, dl):
        self._directory_list = dl

    @directory_list.deleter
    def directory_list(self):
        del self._directory_list

    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, fl):
        self._file_list = fl

    @file_list.deleter
    def file_list(self):
        del self._file_list
