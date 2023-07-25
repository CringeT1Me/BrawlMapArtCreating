# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import GUI_res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1250, 967)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/assets/showdown/brown_crate.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"font-family: 12pt \"Century Schoolbook\";\n"
"font: 12pt \"Century Schoolbook\";\n"
"background-color: rgb(23, 22, 22);\n"
"border-radius: 20px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1118, 626))
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ImageBoard = QLabel(self.centralwidget)
        self.ImageBoard.setObjectName(u"ImageBoard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ImageBoard.sizePolicy().hasHeightForWidth())
        self.ImageBoard.setSizePolicy(sizePolicy1)
        self.ImageBoard.setMinimumSize(QSize(600, 600))
        self.ImageBoard.setMaximumSize(QSize(1000, 1000))
        self.ImageBoard.setSizeIncrement(QSize(100, 900))
        self.ImageBoard.setBaseSize(QSize(700, 700))
        self.ImageBoard.setMouseTracking(False)
        self.ImageBoard.setLayoutDirection(Qt.LeftToRight)
        self.ImageBoard.setStyleSheet(u"padding: 10px;\n"
"height: width;\n"
"\n"
"")
        self.ImageBoard.setPixmap(QPixmap(u":/image/assets/Map.png"))
        self.ImageBoard.setScaledContents(True)
        self.ImageBoard.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.ImageBoard.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.ImageBoard)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_new_image = QPushButton(self.centralwidget)
        self.btn_new_image.setObjectName(u"btn_new_image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_new_image.sizePolicy().hasHeightForWidth())
        self.btn_new_image.setSizePolicy(sizePolicy2)
        self.btn_new_image.setMinimumSize(QSize(232, 0))
        self.btn_new_image.setMaximumSize(QSize(10000, 60))
        self.btn_new_image.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"font-size: 24pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/image_new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_image.setIcon(icon1)
        self.btn_new_image.setIconSize(QSize(20, 20))
        self.btn_new_image.setFlat(False)

        self.verticalLayout.addWidget(self.btn_new_image)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_map_cells = QCheckBox(self.centralwidget)
        self.checkBox_map_cells.setObjectName(u"checkBox_map_cells")
        sizePolicy2.setHeightForWidth(self.checkBox_map_cells.sizePolicy().hasHeightForWidth())
        self.checkBox_map_cells.setSizePolicy(sizePolicy2)
        self.checkBox_map_cells.setMaximumSize(QSize(250, 60))
        self.checkBox_map_cells.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 spacing: 10px;\n"
"}\n"
"QCheckBox:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QCheckBox:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/map_cells.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_map_cells.setIcon(icon2)
        self.checkBox_map_cells.setIconSize(QSize(25, 25))
        self.checkBox_map_cells.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_map_cells, 0, Qt.AlignLeft)

        self.checkBox_grid = QCheckBox(self.centralwidget)
        self.checkBox_grid.setObjectName(u"checkBox_grid")
        sizePolicy2.setHeightForWidth(self.checkBox_grid.sizePolicy().hasHeightForWidth())
        self.checkBox_grid.setSizePolicy(sizePolicy2)
        self.checkBox_grid.setMaximumSize(QSize(250, 60))
        self.checkBox_grid.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 spacing: 10px;\n"
"}\n"
"QCheckBox:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QCheckBox:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_grid.setIcon(icon3)
        self.checkBox_grid.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.checkBox_grid)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_save_image = QPushButton(self.centralwidget)
        self.btn_save_image.setObjectName(u"btn_save_image")
        sizePolicy2.setHeightForWidth(self.btn_save_image.sizePolicy().hasHeightForWidth())
        self.btn_save_image.setSizePolicy(sizePolicy2)
        self.btn_save_image.setMinimumSize(QSize(0, 0))
        self.btn_save_image.setMaximumSize(QSize(1000, 60))
        self.btn_save_image.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 font-size: 24pt;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,50);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/image_save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_image.setIcon(icon4)
        self.btn_save_image.setIconSize(QSize(20, 20))
        self.btn_save_image.setFlat(False)

        self.verticalLayout.addWidget(self.btn_save_image)

        self.verticalSpacer = QSpacerItem(20, 700, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 14pt")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Brawl Stars Map Art Creator 1.0", None))
        self.ImageBoard.setText("")
        self.btn_new_image.setText(QCoreApplication.translate("MainWindow", u"New Image", None))
        self.checkBox_map_cells.setText(QCoreApplication.translate("MainWindow", u"Use map cells", None))
        self.checkBox_grid.setText(QCoreApplication.translate("MainWindow", u"Show grid", None))
        self.btn_save_image.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created by CringeT1Me\n"
"on GitHub", None))
    # retranslateUi

