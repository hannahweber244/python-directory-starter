import os


class StructureBuilder:

    def __init__(self):
        self.__directory_list = ["src", "tests", "data", "output", "reports"]
        self.__file_list = [".gitignore", "README.md", "LICENSE", "setup.py"]
      
    def initialize_structure(self):
        cdir = os.getcwd()
        for directory in self.__directory_list:
            if os.path.exists(os.path.join(cdir, directory)):
                continue
            else:
                os.mkdir(os.path.join(cdir, directory))
                f = open(os.path.join(cdir, directory, ".gitadd"), "w+")
                f.close()

        for file in self.__file_list:
            if os.path.exists(os.path.join(cdir, file)):
                continue
            else:
                text_file = f"{file.strip('.').split('.')[0]}_text.txt"
                text = open(os.path.join("data", text_file), "r").read()
                f = open(os.path.join(cdir, file), "w+")
                f.write(text)
                f.close()

    @property
    def directory_list(self):
        return self.__directory_list

    @directory_list.setter
    def directory_list(self, dl):
        self.__directory_list = dl

    @directory_list.deleter
    def directory_list(self):
        del self.__directory_list

    @property
    def file_list(self):
        return self.__file_list

    @file_list.setter
    def directory_list(self, fl):
        self.__file_list = fl

    @file_list.deleter
    def directory_list(self):
        del self.__file_list
    