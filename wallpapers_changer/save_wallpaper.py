import sys
from PyQt5 import QtWidgets
import design
import os
from pathlib import Path
from shutil import copyfile

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save_image)
        self.pushButton_2.clicked.connect(self.browse_folder)

        self.lineEdit.setText(str(Path("C:\\Users\\Slava\\Pictures\\unsplash_images")))
        self.default_directory = str(Path("C:\\Users\\Slava\\Pictures\\unsplash_images"))
        self.directory = self.default_directory
        self.next_image_name = self.get_next_image_name(os.listdir(self.default_directory))
        self.setWindowTitle("Wallpaper Saver")

    def browse_folder(self):
        self.directory = str(Path(QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")))

        if self.directory == ".":
            self.directory = self.default_directory

        self.lineEdit.setText(self.directory)

    def save_image(self):
        self.label_2.setText("...")
        file_list = os.listdir(self.directory)
        self.next_image_name = self.get_next_image_name(file_list)
        tmp_image_path = Path("C:\\Users\\Slava\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles")
        ready = False
        files = ""
        while not ready or not files:
            try:
                files = os.listdir(tmp_image_path)
                ready = True
            except:
                print("Folder is still not loaded")
        filepath_destination = self.lineEdit.text() + str(Path(f"\\{self.next_image_name}"))
        try:
            filename = files[0]
            ready = True
            filepath_source = Path(f"{tmp_image_path}\\{filename}")
            copyfile(filepath_source, filepath_destination)
            self.label_2.setText(f"OK!\nImage was saved as:\n{filepath_destination}")
            print(f"Image was saved to {filepath_destination}")
        except Exception as e:
            print(f"Error: there are no files in the directory, also {e}")

    def get_next_image_name(self, file_list):
        max = 0
        for file in file_list:
            filename = file.split(".")[0]
            try:
                if int(filename) > max:
                    max = int(filename)
            except:
                print(f"Error: filename of '{file}' cannot be casted to int.")
        return str(max + 1) + ".jpg"


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp() 
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
