import os
from datetime import datetime


class FileRenamer:
    def __init__(self, workpath=input("Enter your path: ")):
        self.workpath = workpath

    def add_the_date(self, path):
        creation_date = datetime.fromtimestamp(os.path.getctime(path))
        formatted = datetime.strftime(creation_date, "%Y.%m.%d")
        return formatted

    def change_the_name(self):
        for ele in os.listdir(self.workpath):
            path_to_ele = os.path.join(self.workpath, ele)
            if os.path.isfile(path_to_ele):
                file_name, file_extension = os.path.splitext(path_to_ele)
                new_name = f"{file_name} {self.add_the_date(path_to_ele)}{file_extension}"
                os.rename(path_to_ele, new_name)


if __name__ == "__main__":
    renamer = FileRenamer()
    renamer.change_the_name()