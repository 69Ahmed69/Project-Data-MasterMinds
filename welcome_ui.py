# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(731, 599)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 100)
        self.welcome = QLabel(Form)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(800, 0))
        self.welcome.setMaximumSize(QSize(800, 16777215))
        font = QFont()
        font.setFamilies([u"Perpetua"])
        font.setPointSize(26)
        self.welcome.setFont(font)
        self.welcome.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.welcome, 4, 0, 1, 1)

        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        self.image.setInputMethodHints(Qt.ImhDigitsOnly)
        self.image.setPixmap(QPixmap(u"../422.png"))
        self.image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.image, 1, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 400))
        self.label.setMaximumSize(QSize(16777215, 400))
        self.label.setPixmap(QPixmap(u"Icons/image(1).png"))

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.welcome.setText(QCoreApplication.translate("Form", u"Welcome to a world where data management <br> is made easy...", None))
        self.image.setText("")
        self.label.setText("")
    # retranslateUi

