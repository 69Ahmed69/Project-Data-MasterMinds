# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(800, 518)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.user = QLabel(Form)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(200, 60))
        self.user.setMaximumSize(QSize(300, 90))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(21)
        font.setBold(True)
        self.user.setFont(font)
        self.user.setStyleSheet(u"")
        self.user.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.user)

        self.userinput = QLineEdit(Form)
        self.userinput.setObjectName(u"userinput")
        self.userinput.setEnabled(True)
        self.userinput.setMinimumSize(QSize(300, 50))
        self.userinput.setMaximumSize(QSize(450, 60))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        self.userinput.setFont(font1)
        self.userinput.setStyleSheet(u"border-radius: 20px")
        self.userinput.setInputMethodHints(Qt.ImhNone)
        self.userinput.setFrame(False)
        self.userinput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.userinput.setPlaceholderText(u"Enter username...")
        self.userinput.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.userinput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.userinput)

        self.password = QLabel(Form)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 60))
        self.password.setMaximumSize(QSize(200, 60))
        self.password.setFont(font)
        self.password.setLayoutDirection(Qt.LeftToRight)
        self.password.setStyleSheet(u"")
        self.password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.password)

        self.passwordinput = QLineEdit(Form)
        self.passwordinput.setObjectName(u"passwordinput")
        self.passwordinput.setMinimumSize(QSize(300, 50))
        self.passwordinput.setMaximumSize(QSize(450, 60))
        self.passwordinput.setFont(font1)
        self.passwordinput.setStyleSheet(u"border-radius: 20px")
        self.passwordinput.setFrame(False)
        self.passwordinput.setEchoMode(QLineEdit.Password)
        self.passwordinput.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.passwordinput.setReadOnly(False)
        self.passwordinput.setPlaceholderText(u"Enter password...")
        self.passwordinput.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.passwordinput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.passwordinput)

        self.loginbutton = QPushButton(Form)
        self.loginbutton.setObjectName(u"loginbutton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginbutton.sizePolicy().hasHeightForWidth())
        self.loginbutton.setSizePolicy(sizePolicy)
        self.loginbutton.setMinimumSize(QSize(200, 60))
        self.loginbutton.setMaximumSize(QSize(300, 60))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(20)
        self.loginbutton.setFont(font2)
        self.loginbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginbutton.setMouseTracking(False)
        self.loginbutton.setFocusPolicy(Qt.StrongFocus)
        self.loginbutton.setStyleSheet(u"border-radius: 20px")
        self.loginbutton.setCheckable(False)
        self.loginbutton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.loginbutton, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.user.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.userinput.setText("")
        self.password.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.passwordinput.setText("")
        self.loginbutton.setText(QCoreApplication.translate("Form", u"LOG IN", None))
#if QT_CONFIG(shortcut)
        self.loginbutton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

