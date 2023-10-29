import sys

from PyQt5 import QtWidgets, uic
from ui import Ui_Dialog
from downloader import downloader


# Класс экранной формы и обработчиков кнопок
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # подключение клик-сигналов
        self.ui.pushButton.clicked.connect(self.run_button)
        self.ui.pushButton_2.clicked.connect(self.browse_start_file_path)
        # self.ui.pushButton_3.clicked.connect(self.browse_result_folder_path)

    # указание директории проверяемого файла
    def browse_start_file_path(self):
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, "Выберите папку")
        self.ui.lineEdit.setText(directory[0][0])

    # # указание директории результирующего файла
    # def browse_result_folder_path(self):
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
    #     self.ui.lineEdit_2.setText(directory)

    def run_button(self):
        # проверка, что путь до проверяемого файла заполнен
        if self.ui.lineEdit.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Внимание")
            msg.setText("Не указан путь до excel файла!")
            msg.exec_()
        else:
            # Директории файлов
            path = self.ui.lineEdit.text()

            downloader(path)

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Внимание")
            msg.setText("Done!")
            msg.exec_()
            sys.exit()
