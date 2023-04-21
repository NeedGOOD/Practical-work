from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint,  QTimer
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPixmap, QIcon, QImage
from PyQt5.QtWidgets import QColorDialog, QFileDialog
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 431)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(0, 40, 481, 371))
        self.canvas.setStyleSheet("background: rgb(255, 255, 255);")
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.fill_objects = QtWidgets.QCheckBox(self.centralwidget)
        self.fill_objects.setGeometry(QtCore.QRect(180, 0, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fill_objects.setFont(font)
        self.fill_objects.setObjectName("fill_objects")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.brush_size = QtWidgets.QMenu(self.menubar)
        self.brush_size.setObjectName("brush_size")
        self.brush_color = QtWidgets.QMenu(self.menubar)
        self.brush_color.setObjectName("brush_color")
        self.menu_figure = QtWidgets.QMenu(self.menubar)
        self.menu_figure.setObjectName("menu_figure")
        MainWindow.setMenuBar(self.menubar)
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.actionclear_screen = QtWidgets.QAction(MainWindow)
        self.actionclear_screen.setObjectName("actionclear_screen")
        self.five_px = QtWidgets.QAction(MainWindow)
        self.five_px.setObjectName("five_px")
        self.twelve_px = QtWidgets.QAction(MainWindow)
        self.twelve_px.setObjectName("twelve_px")
        self.twenty_px = QtWidgets.QAction(MainWindow)
        self.twenty_px.setObjectName("twenty_px")
        self.twenty_five_px = QtWidgets.QAction(MainWindow)
        self.twenty_five_px.setObjectName("twenty_five_px")
        self.black_color = QtWidgets.QAction(MainWindow)
        self.black_color.setObjectName("black_color")
        self.green_color = QtWidgets.QAction(MainWindow)
        self.green_color.setObjectName("green_color")
        self.yellow_color = QtWidgets.QAction(MainWindow)
        self.yellow_color.setObjectName("yellow_color")
        self.blue_color = QtWidgets.QAction(MainWindow)
        self.blue_color.setObjectName("blue_color")
        self.actionChose = QtWidgets.QAction(MainWindow)
        self.actionChose.setObjectName("actionChose")
        self.square_figure = QtWidgets.QAction(MainWindow)
        self.square_figure.setObjectName("square_figure")
        self.cyrcle_figure = QtWidgets.QAction(MainWindow)
        self.cyrcle_figure.setObjectName("cyrcle_figure")
        self.line = QtWidgets.QAction(MainWindow)
        self.line.setObjectName("line")
        self.clear = QtWidgets.QAction(MainWindow)
        self.clear.setObjectName("clear")
        self.pen = QtWidgets.QAction(MainWindow)
        self.pen.setObjectName("pen")
        self.file.addAction(self.save)
        self.file.addAction(self.clear)
        self.brush_size.addAction(self.five_px)
        self.brush_size.addAction(self.twelve_px)
        self.brush_size.addAction(self.twenty_px)
        self.brush_size.addAction(self.twenty_five_px)
        self.brush_color.addAction(self.black_color)
        self.brush_color.addAction(self.green_color)
        self.brush_color.addAction(self.yellow_color)
        self.brush_color.addAction(self.blue_color)
        self.menu_figure.addAction(self.square_figure)
        self.menu_figure.addAction(self.cyrcle_figure)
        self.menu_figure.addAction(self.line)
        self.menu_figure.addAction(self.pen)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.brush_size.menuAction())
        self.menubar.addAction(self.brush_color.menuAction())
        self.menubar.addAction(self.menu_figure.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pixmap = QPixmap(self.canvas.width(), self.canvas.height())
        self.Pen = QPainter(self.pixmap)
        self.obj = ""

        self.pre_points = QPoint()
        self.Color = QColor()
        self.pen_Size = 5

        self.connect()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paint"))
        self.fill_objects.setText(_translate("MainWindow", "filling"))
        self.file.setTitle(_translate("MainWindow", "File"))
        self.brush_size.setTitle(_translate("MainWindow", "Brush size"))
        self.brush_color.setTitle(_translate("MainWindow", "Brush color"))
        self.menu_figure.setTitle(_translate("MainWindow", "Figure"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.actionclear_screen.setText(_translate("MainWindow", "clear screen"))
        self.five_px.setText(_translate("MainWindow", "5px"))
        self.twelve_px.setText(_translate("MainWindow", "12px"))
        self.twenty_px.setText(_translate("MainWindow", "20px"))
        self.twenty_five_px.setText(_translate("MainWindow", "25px"))
        self.black_color.setText(_translate("MainWindow", "Black"))
        self.green_color.setText(_translate("MainWindow", "Green"))
        self.yellow_color.setText(_translate("MainWindow", "Yellow"))
        self.blue_color.setText(_translate("MainWindow", "Blue"))
        self.actionChose.setText(_translate("MainWindow", "Chose"))
        self.square_figure.setText(_translate("MainWindow", "Square □"))
        self.cyrcle_figure.setText(_translate("MainWindow", "Cyrcle o"))
        self.line.setText(_translate("MainWindow", "Line /"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.pen.setText(_translate("MainWindow", "Pen"))

    def connect(self):
        self.pixmap.fill(Qt.white)

        self.canvas.mouseMoveEvent = self.drawing
        self.canvas.mousePressEvent = self.mousepressevent
        self.canvas.mouseReleaseEvent = self.obj_Draw

        self.yellow_color.triggered.connect(lambda: setattr(self, 'Color', Qt.yellow))
        self.blue_color.triggered.connect(lambda: setattr(self, 'Color', Qt.blue))
        self.black_color.triggered.connect(lambda: setattr(self, 'Color', Qt.black))
        self.green_color.triggered.connect(lambda: setattr(self, 'Color', Qt.green))

        self.clear.triggered.connect(self.clear_screen)

        self.five_px.triggered.connect(lambda: setattr(self, 'pen_Size', 5))
        self.twelve_px.triggered.connect(lambda: setattr(self, 'pen_Size', 12))
        self.twenty_px.triggered.connect(lambda: setattr(self, 'pen_Size', 20))
        self.twenty_five_px.triggered.connect(lambda: setattr(self, 'pen_Size', 25))

        self.cyrcle_figure.triggered.connect(lambda: setattr(self, 'obj', "Cyrcle"))
        self.square_figure.triggered.connect(lambda: setattr(self, 'obj', "Square"))
        self.line.triggered.connect(lambda: setattr(self, 'obj', "Line"))
        self.pen.triggered.connect(lambda: setattr(self, 'obj', ""))

        self.save.triggered.connect(self.save_file)

    def obj_Draw(self, event):
        # Визначаємо дистанцію x та y
        X = event.x() - self.pre_points.x()
        Y = event.y() - self.pre_points.y()
        preX, preY = self.pre_points.x(), self.pre_points.y()

        self.Pen.setPen(QPen(self.Color, self.pen_Size))

        # Перевірка чек-боксу, якщо він true, тоді малюємо фігуру заповнену, якщо ні - пусту
        if not self.fill_objects.checkState(): self.Pen.setBrush(Qt.NoBrush)
        else: self.Pen.setBrush(QBrush(self.Color))

        if self.obj != "" and event.button() == Qt.LeftButton:
            match self.obj:
                case "Cyrcle": self.Pen.drawEllipse(preX, preY, X, Y)
                case "Square": self.Pen.drawRect(preX, preY, X, Y)
                case "Line": self.Pen.drawLine(self.pre_points, event.pos())
            self.canvas.setPixmap(self.pixmap)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(QtWidgets.QWidget(), "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if file_path == "":
            return
        self.pixmap.save(file_path)

    def clear_screen(self):
        self.pixmap.fill(Qt.white)
        self.canvas.setPixmap(self.pixmap)

    def mousepressevent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.pre_points = event.pos()

    def drawing(self, event):
        if event.buttons() == Qt.LeftButton and self.obj == "":
            self.Pen.setPen(QPen(self.Color, self.pen_Size))

            self.Pen.drawLine(self.pre_points, event.pos())

            self.pre_points = event.pos()
            self.canvas.setPixmap(self.pixmap)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())