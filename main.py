from PyQt5 import QtWidgets, uic
from window import MainWindow


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    app.exec()


if __name__ == '__main__':
    main()

# https://raw.githubusercontent.com/ruauka/image-downloader-py/main/dist/main.exe
# pyinstaller --onefile .\main.py --name image_downloader
