import os


class ElementsDeleter:

    def __init__(self, path=input(r"Enter the path: ")):
        self.path = path

    def delete_empty_elements(self):
        for path, directories, files in os.walk(self.path, False):
            for file in files:
                path_to_file = os.path.join(path, file)
                if os.path.getsize(path_to_file) == 0:
                    os.remove(path_to_file)
            for directory in directories:
                path_to_directory = os.path.join(path, directory)
                try:
                    os.rmdir(path_to_directory)
                except OSError:
                    pass
        print("Command fulfilled.")


if __name__ == "__main__":
    elementsdeleter = ElementsDeleter()
    elementsdeleter.delete_empty_elements()
