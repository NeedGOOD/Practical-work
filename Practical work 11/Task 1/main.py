from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog, QMessageBox
from PyQt5.QtCore import QDir
import os
import sys
import shutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setObjectName("treeView")
        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.contextMenu)
        self.work()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guide"))

    def work(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setSortingEnabled(True)

    def contextMenu(self):
        self.menu = QtWidgets.QMenu()
        create = self.menu.addAction("Створити")
        create.triggered.connect(self.createNewFile)
        delete = self.menu.addAction("Видалення")
        delete.triggered.connect(self.deleteFile)
        rename = self.menu.addAction("Перемейнування")
        rename.triggered.connect(self.renameFile)
        copy = self.menu.addAction("Копіювати")
        copy.triggered.connect(self.copyFile)
        insert = self.menu.addAction("Вставити")
        insert.triggered.connect(self.insertFile)
        cursor = QtGui.QCursor()
        self.menu.exec_(cursor.pos())

    def createNewFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        new_file = QInputDialog.getText(None, "Створення файла", "Введіть назву файлу: ")
        if new_file[1]:
            if os.path.exists(file_path + '/' + new_file[0]):
                if '.' in new_file[0]:
                    error = QMessageBox()
                    error.setWindowTitle("Помилка")
                    error.setText(f"Файл {new_file[0]} уже створено.")
                    error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Помилка")
                    error.setText(f"Папка {new_file[0]} уже створено.")
                    error.exec_()
            else:
                if '.' in new_file[0]:
                    with open(file_path + '/' + new_file[0], "w"):
                        pass
                else:
                    QDir().mkdir(file_path + '/' + new_file[0])

    def deleteFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        if '.' in file_path:
            os.remove(file_path)
        else:
            shutil.rmtree(file_path)

    def renameFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        rename_file = QInputDialog.getText(None, "Перейменування файла", "Введіть нову назву файла: ")
        folder_path = os.path.dirname(file_path)
        rename_file_path = os.path.join(folder_path, rename_file[0])
        if rename_file[1]:
            os.rename(file_path, rename_file_path)

    def copyFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        self.file_path = file_path

    def insertFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        name_file_path = os.path.basename(self.file_path)
        try:
            if '.' in name_file_path:
                shutil.copy(self.file_path, file_path)
            else:
                copy_file_path = os.path.join(file_path, name_file_path)
                shutil.copytree(self.file_path, copy_file_path)
        except FileExistsError:
            error = QMessageBox()
            error.setWindowTitle("Помилка")
            error.setText(f"Папка {name_file_path} находиться в папці.")
            error.exec_()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())