from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
import random
import time
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 530)
        MainWindow.setMinimumSize(QtCore.QSize(710, 530))
        MainWindow.setMaximumSize(QtCore.QSize(710, 530))
        MainWindow.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 10, 125, 250))
        self.btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photo/1.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_1.setIcon(icon)
        self.btn_1.setIconSize(QtCore.QSize(124, 246))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(150, 10, 125, 250))
        self.btn_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photo/2.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_2.setIcon(icon1)
        self.btn_2.setIconSize(QtCore.QSize(124, 246))
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(290, 10, 125, 250))
        self.btn_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("photo/3.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_3.setIcon(icon2)
        self.btn_3.setIconSize(QtCore.QSize(124, 246))
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(430, 10, 125, 250))
        self.btn_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("photo/4.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_4.setIcon(icon3)
        self.btn_4.setIconSize(QtCore.QSize(124, 246))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(570, 10, 125, 250))
        self.btn_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("photo/5.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.btn_5.setIcon(icon4)
        self.btn_5.setIconSize(QtCore.QSize(124, 246))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(10, 270, 125, 250))
        self.btn_6.setText("")
        self.btn_6.setIcon(icon)
        self.btn_6.setIconSize(QtCore.QSize(124, 246))
        self.btn_6.setObjectName("btn_6")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(290, 270, 125, 250))
        self.btn_8.setText("")
        self.btn_8.setIcon(icon2)
        self.btn_8.setIconSize(QtCore.QSize(124, 246))
        self.btn_8.setObjectName("btn_8")
        self.btn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_10.setGeometry(QtCore.QRect(570, 270, 125, 250))
        self.btn_10.setText("")
        self.btn_10.setIcon(icon4)
        self.btn_10.setIconSize(QtCore.QSize(124, 246))
        self.btn_10.setObjectName("btn_10")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(150, 270, 125, 250))
        self.btn_7.setText("")
        self.btn_7.setIcon(icon1)
        self.btn_7.setIconSize(QtCore.QSize(124, 246))
        self.btn_7.setObjectName("btn_7")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(430, 270, 125, 250))
        self.btn_9.setText("")
        self.btn_9.setIcon(icon3)
        self.btn_9.setIconSize(QtCore.QSize(124, 246))
        self.btn_9.setObjectName("btn_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.work()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game"))

    def work(self):
            self.first_names = [ "1", "2", "3", "4", "5",
                                "1", "2", "3", "4", "5" ]
            self.button_images = [ self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5,
                                self.btn_6, self.btn_7, self.btn_8, self.btn_9, self.btn_10 ]
            self.cards = []
            self.pair = 0
            self.not_pair = 0
            
            random.shuffle(self.first_names)

            for i in range(0, 10):
                self.button_images[i].setIcon(QIcon(f"photo/back.png"))

            self.show_cards()
            self.btn_1.clicked.connect(lambda: self.flippingCards(0))
            self.btn_2.clicked.connect(lambda: self.flippingCards(1))
            self.btn_3.clicked.connect(lambda: self.flippingCards(2))
            self.btn_4.clicked.connect(lambda: self.flippingCards(3))
            self.btn_5.clicked.connect(lambda: self.flippingCards(4))
            self.btn_6.clicked.connect(lambda: self.flippingCards(5))
            self.btn_7.clicked.connect(lambda: self.flippingCards(6))
            self.btn_8.clicked.connect(lambda: self.flippingCards(7))
            self.btn_9.clicked.connect(lambda: self.flippingCards(8))
            self.btn_10.clicked.connect(lambda: self.flippingCards(9))

    def show_cards(self):
        for i, name in enumerate(self.first_names):
            self.button_images[i].setIcon(QIcon(f"photo/{name}.png"))
        QTimer.singleShot(2000, self.hide_cards)

    def hide_cards(self):
        for i in range(10):
            self.button_images[i].setIcon(QIcon(f"photo/back.png"))
            self.button_images[i].show()

    def flippingCards(self, Card_num):
        if len(self.cards) == 1 and self.cards[0][1] == Card_num:
            self.button_images[Card_num].setIcon(QIcon(f"photo/back.png"))
            self.cards = []
            return

        self.button_images[Card_num].setIcon(QIcon(f"photo/{self.first_names[Card_num]}.png"))

        self.cards.append([self.first_names[Card_num], Card_num])

        if len(self.cards) == 2:
            MainWindow.repaint()
            time.sleep(1)
            if self.cards[0][0] == self.cards[1][0]:
                self.button_images[self.cards[0][1]].setEnabled(False)
                self.button_images[self.cards[1][1]].setEnabled(False)
                self.pair += 1
            else:
                self.button_images[self.cards[0][1]].setIcon(QIcon(f"photo/back.png"))
                self.button_images[self.cards[1][1]].setIcon(QIcon(f"photo/back.png"))
                self.not_pair += 1
            self.winOrLose()
            self.cards = []

    def winOrLose(self):
        box = QMessageBox()
        if self.pair == 5:
            box.setWindowTitle("Перемога")
            box.setText("Ви перемогли!")
            box.setStandardButtons(QMessageBox.Retry|QMessageBox.Close)
            box.button(QMessageBox.Retry).setText("Перезапустити")
            box.button(QMessageBox.Close).setText("Вийти")
            click = box.exec_()
            if click == QMessageBox.Retry:
                self.pair = 0
                self.not_pair = 0
                self.cards = []
                for i in self.button_images:
                    i.setEnabled(True)
                random.shuffle(self.first_names)
                self.show_cards()
            elif click == QMessageBox.Close:
                sys.exit()
        elif self.not_pair == 5:
            box.setWindowTitle("Програш")
            box.setText("Ви програли!")
            box.setStandardButtons(QMessageBox.Retry|QMessageBox.Close)
            box.button(QMessageBox.Retry).setText("Перезапустити")
            box.button(QMessageBox.Close).setText("Вийти")
            click = box.exec_()
            if click == QMessageBox.Retry:
                self.pair = 0
                self.not_pair = 0
                self.cards = []
                for i in self.button_images:
                    i.setEnabled(True)
                random.shuffle(self.first_names)
                self.show_cards()
            elif click == QMessageBox.Close:
                sys.exit()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())