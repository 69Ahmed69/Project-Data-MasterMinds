# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(900, 600)
        Main.setStyleSheet(u"\n"
"QMainWindow {\n"
"	background-color:#1e1d23;\n"
"	color: #ffffff\n"
"}\n"
"QDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"	background-color:#1e1d23;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"	selection-background-color:#007b50;\n"
"	background-color:#1e1d23;\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"	background-color: #101019;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: inset;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-width: 1px;\n"
"	color: #a9b7c6;\n"
""
                        "	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-bottom: 2px;\n"
"	backgr"
                        "ound-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #37efba;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #37efba;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #808086;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding-bottom: 1px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	padding: 0 8px;\n"
"	color: #a9b7c6;\n"
"	background:#1e1d23;\n"
"	selection-background-color:#007b50;\n"
"	selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"	color: #a9b7c6;\n"
"}\n"
"QLCDNumb"
                        "er {\n"
"	color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(58, 58, 58);\n"
"	border-style: inset;\n"
"	background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: #04b97f;\n"
"	border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"	color: #a9b7c6;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"  	background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background:#1e1d23;\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: #04b97f;\n"
"	border-bottom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #FFFFFF;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"	border-st"
                        "yle: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #a9b7c6;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"	background-color: #242432;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(77,77,77);\n"
"		background-color:#1e1d23;\n"
"		border-style: solid;\n"
"		border-width: 1px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	border-style: solid;\n"
"	color: #808086;\n"
"	padding: 3px;\n"
"	margin-left:3px;\n"
"	background-color: #242432;\n"
""
                        "}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: #04b97f;\n"
"	border-bottom-width: 2px;\n"
"	border-style: solid;\n"
"	color: #FFFFFF;\n"
"	padding-left: 3px;\n"
"	padding-bottom: 2px;\n"
"	margin-left:3px;\n"
"	background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #a9b7c6;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
""
                        "	background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #04b97f;\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
""
                        "QTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QComboBox:editable {\n"
"	background: #1e1d23;\n"
"	color: #a9b7c6;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"	selection-color: #FFFFFF;\n"
"	selection-background-color: #1e1d23;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	color: #a9b7c6;	\n"
"	background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"	color: #a9b7c6;	\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QScr"
                        "ollArea {\n"
"	color: #FFFFFF;\n"
"	background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	width: 14px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"	border: 1px solid #5c5c5c;\n"
"	height: 14px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}\n"
"")
        self.actionDark_Mode = QAction(Main)
        self.actionDark_Mode.setObjectName(u"actionDark_Mode")
        self.actionDark_Mode.setCheckable(False)
        self.actionLight_Mode = QAction(Main)
        self.actionLight_Mode.setObjectName(u"actionLight_Mode")
        self.actionLight_Mode.setCheckable(False)
        self.actionConsole_Mode = QAction(Main)
        self.actionConsole_Mode.setObjectName(u"actionConsole_Mode")
        self.actionConsole_Mode.setCheckable(False)
        self.actionAqua_Mode = QAction(Main)
        self.actionAqua_Mode.setObjectName(u"actionAqua_Mode")
        self.Mainwidget = QWidget(Main)
        self.Mainwidget.setObjectName(u"Mainwidget")
        self.gridLayout_2 = QGridLayout(self.Mainwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.current_user = QLabel(self.Mainwidget)
        self.current_user.setObjectName(u"current_user")
        self.current_user.setMinimumSize(QSize(200, 0))
        self.current_user.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(12)
        font.setBold(True)
        self.current_user.setFont(font)

        self.gridLayout_2.addWidget(self.current_user, 0, 0, 1, 1)

        self.access_right = QLabel(self.Mainwidget)
        self.access_right.setObjectName(u"access_right")
        self.access_right.setMinimumSize(QSize(200, 30))
        self.access_right.setMaximumSize(QSize(200, 16777215))
        self.access_right.setFont(font)

        self.gridLayout_2.addWidget(self.access_right, 0, 1, 1, 1)

        self.toolBox = QToolBox(self.Mainwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(200, 0))
        self.toolBox.setMaximumSize(QSize(300, 5000))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setItalic(True)
        font1.setKerning(True)
        self.toolBox.setFont(font1)
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setStyleSheet(u"")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 200, 257))
        self.page_6.setMaximumSize(QSize(16777215, 888888))
        self.page_6.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout = QVBoxLayout(self.page_6)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.new_user_button = QPushButton(self.page_6)
        self.new_user_button.setObjectName(u"new_user_button")
        self.new_user_button.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(12)
        self.new_user_button.setFont(font2)
        self.new_user_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_user_button.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.new_user_button)

        self.delete_user_button = QPushButton(self.page_6)
        self.delete_user_button.setObjectName(u"delete_user_button")
        self.delete_user_button.setMinimumSize(QSize(0, 50))
        self.delete_user_button.setFont(font2)
        self.delete_user_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_user_button.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.delete_user_button)

        self.modify_button = QPushButton(self.page_6)
        self.modify_button.setObjectName(u"modify_button")
        self.modify_button.setMinimumSize(QSize(0, 50))
        self.modify_button.setMaximumSize(QSize(16777215, 16777215))
        self.modify_button.setFont(font2)
        self.modify_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.modify_button.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.modify_button)

        self.change_password_button = QPushButton(self.page_6)
        self.change_password_button.setObjectName(u"change_password_button")
        self.change_password_button.setMinimumSize(QSize(0, 50))
        self.change_password_button.setFont(font2)
        self.change_password_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_password_button.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.change_password_button)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.toolBox.addItem(self.page_6, u"Users")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 200, 257))
        self.page_5.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.addItem(self.page_5, u"Dashboard")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 200, 257))
        self.toolBox.addItem(self.page, u"Professors")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 200, 257))
        self.toolBox.addItem(self.page_2, u"Students")

        self.gridLayout_2.addWidget(self.toolBox, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.Mainwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(600, 0))
        self.tabWidget.setMaximumSize(QSize(5000, 16777215))
        self.tabWidget.setStyleSheet(u"border-radius: 20")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift"])
        font3.setPointSize(25)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setVerticalSpacing(30)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 0, 5, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 4, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.password2_read = QLineEdit(self.tab_2)
        self.password2_read.setObjectName(u"password2_read")
        self.password2_read.setMinimumSize(QSize(200, 50))
        self.password2_read.setMaximumSize(QSize(600, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setItalic(True)
        self.password2_read.setFont(font4)
        self.password2_read.setEchoMode(QLineEdit.Password)
        self.password2_read.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.password2_read, 2, 5, 1, 1)

        self.show_button = QPushButton(self.tab_2)
        self.show_button.setObjectName(u"show_button")
        self.show_button.setMinimumSize(QSize(0, 40))
        self.show_button.setMaximumSize(QSize(50, 16777215))
        self.show_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_button.setStyleSheet(u"border: none")
        icon = QIcon()
        icon.addFile(u"Icons/65000.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"Icons/Your paragraph text.png", QSize(), QIcon.Active, QIcon.On)
        self.show_button.setIcon(icon)
        self.show_button.setIconSize(QSize(32, 32))
        self.show_button.setCheckable(True)
        self.show_button.setChecked(False)
        self.show_button.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.show_button, 1, 4, 1, 1)

        self.access_right_read = QComboBox(self.tab_2)
        self.access_right_read.addItem("")
        self.access_right_read.addItem("")
        self.access_right_read.addItem("")
        self.access_right_read.addItem("")
        self.access_right_read.setObjectName(u"access_right_read")
        self.access_right_read.setMinimumSize(QSize(0, 50))
        self.access_right_read.setMaximumSize(QSize(600, 16777215))
        self.access_right_read.setFont(font4)
        self.access_right_read.setCursor(QCursor(Qt.PointingHandCursor))
        self.access_right_read.setToolTipDuration(3)
        self.access_right_read.setStyleSheet(u"border: none; border-radius: 0")
        self.access_right_read.setEditable(False)
        self.access_right_read.setInsertPolicy(QComboBox.NoInsert)
        self.access_right_read.setDuplicatesEnabled(False)
        self.access_right_read.setFrame(True)

        self.gridLayout_4.addWidget(self.access_right_read, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.password_read = QLineEdit(self.tab_2)
        self.password_read.setObjectName(u"password_read")
        self.password_read.setMinimumSize(QSize(200, 50))
        self.password_read.setMaximumSize(QSize(600, 16777215))
        self.password_read.setFont(font4)
        self.password_read.setEchoMode(QLineEdit.Password)
        self.password_read.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.password_read, 1, 5, 1, 1)

        self.register_button = QPushButton(self.tab_2)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setMinimumSize(QSize(200, 50))
        self.register_button.setMaximumSize(QSize(300, 50))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.register_button.setFont(font5)
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.register_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"Icons/new-registration-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.register_button.setIcon(icon1)
        self.register_button.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.register_button, 3, 3, 1, 1)

        self.username_read = QLineEdit(self.tab_2)
        self.username_read.setObjectName(u"username_read")
        self.username_read.setMinimumSize(QSize(200, 50))
        self.username_read.setMaximumSize(QSize(600, 16777215))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.username_read.setFont(font6)
        self.username_read.setClearButtonEnabled(True)

        self.gridLayout_4.addWidget(self.username_read, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 6, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.delete_user_button_2 = QPushButton(self.tab_3)
        self.delete_user_button_2.setObjectName(u"delete_user_button_2")
        self.delete_user_button_2.setMinimumSize(QSize(200, 50))
        self.delete_user_button_2.setMaximumSize(QSize(200, 50))
        font7 = QFont()
        font7.setFamilies([u"Bahnschrift"])
        font7.setPointSize(15)
        self.delete_user_button_2.setFont(font7)
        self.delete_user_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_user_button_2.setStyleSheet(u"border-radius: 20px")
        icon2 = QIcon()
        icon2.addFile(u"Icons/3405244.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_user_button_2.setIcon(icon2)
        self.delete_user_button_2.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.delete_user_button_2, 4, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.user_delete_read = QLineEdit(self.tab_3)
        self.user_delete_read.setObjectName(u"user_delete_read")
        self.user_delete_read.setMinimumSize(QSize(200, 50))
        self.user_delete_read.setMaximumSize(QSize(400, 50))
        font8 = QFont()
        font8.setFamilies([u"Bahnschrift Condensed"])
        font8.setPointSize(15)
        self.user_delete_read.setFont(font8)
        self.user_delete_read.setStyleSheet(u"")

        self.gridLayout.addWidget(self.user_delete_read, 3, 0, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setFamilies([u"Bahnschrift"])
        font9.setPointSize(20)
        self.label_2.setFont(font9)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignBottom)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_14 = QGridLayout(self.tab_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setVerticalSpacing(30)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.modify_button_2 = QPushButton(self.tab_4)
        self.modify_button_2.setObjectName(u"modify_button_2")
        self.modify_button_2.setEnabled(False)
        self.modify_button_2.setMinimumSize(QSize(200, 50))
        self.modify_button_2.setMaximumSize(QSize(200, 50))
        self.modify_button_2.setFont(font7)
        self.modify_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.modify_button_2.setStyleSheet(u"border-radius: 20px")
        icon3 = QIcon()
        icon3.addFile(u"Icons/4889110.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"Icons/488911000.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon3.addFile(u"Icons/488911000.png", QSize(), QIcon.Disabled, QIcon.On)
        icon3.addFile(u"Icons/48891100.png", QSize(), QIcon.Active, QIcon.On)
        self.modify_button_2.setIcon(icon3)
        self.modify_button_2.setIconSize(QSize(32, 32))
        self.modify_button_2.setAutoRepeat(False)
        self.modify_button_2.setAutoExclusive(False)

        self.gridLayout_14.addWidget(self.modify_button_2, 6, 1, 1, 1)

        self.access_right_read_3 = QComboBox(self.tab_4)
        self.access_right_read_3.addItem("")
        self.access_right_read_3.addItem("")
        self.access_right_read_3.addItem("")
        self.access_right_read_3.addItem("")
        self.access_right_read_3.setObjectName(u"access_right_read_3")
        self.access_right_read_3.setEnabled(False)
        self.access_right_read_3.setMinimumSize(QSize(300, 50))
        self.access_right_read_3.setMaximumSize(QSize(300, 16777215))
        self.access_right_read_3.setFont(font4)
        self.access_right_read_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.access_right_read_3.setToolTipDuration(3)
        self.access_right_read_3.setStyleSheet(u"border: none; border-radius: 0")
        self.access_right_read_3.setEditable(False)
        self.access_right_read_3.setInsertPolicy(QComboBox.NoInsert)
        self.access_right_read_3.setDuplicatesEnabled(False)
        self.access_right_read_3.setFrame(True)

        self.gridLayout_14.addWidget(self.access_right_read_3, 5, 1, 1, 1)

        self.access_label_2 = QLabel(self.tab_4)
        self.access_label_2.setObjectName(u"access_label_2")
        self.access_label_2.setEnabled(False)
        self.access_label_2.setMinimumSize(QSize(400, 50))
        self.access_label_2.setMaximumSize(QSize(400, 50))
        self.access_label_2.setFont(font9)

        self.gridLayout_14.addWidget(self.access_label_2, 1, 1, 1, 1)

        self.access_label = QLabel(self.tab_4)
        self.access_label.setObjectName(u"access_label")
        self.access_label.setEnabled(False)
        self.access_label.setMinimumSize(QSize(300, 50))
        self.access_label.setMaximumSize(QSize(400, 50))
        self.access_label.setFont(font9)

        self.gridLayout_14.addWidget(self.access_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.search_user_read = QLineEdit(self.tab_4)
        self.search_user_read.setObjectName(u"search_user_read")
        self.search_user_read.setMinimumSize(QSize(250, 50))
        self.search_user_read.setMaximumSize(QSize(300, 50))
        self.search_user_read.setFont(font8)
        self.search_user_read.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.search_user_read, 4, 0, 1, 1)

        self.search_user_button = QPushButton(self.tab_4)
        self.search_user_button.setObjectName(u"search_user_button")
        self.search_user_button.setMinimumSize(QSize(200, 50))
        self.search_user_button.setMaximumSize(QSize(200, 50))
        self.search_user_button.setFont(font7)
        self.search_user_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_user_button.setStyleSheet(u"border-radius: 20px;")
        icon4 = QIcon()
        icon4.addFile(u"Icons/people.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_user_button.setIcon(icon4)
        self.search_user_button.setIconSize(QSize(32, 32))

        self.gridLayout_14.addWidget(self.search_user_button, 5, 0, 1, 1, Qt.AlignVCenter)

        self.new_user_read = QLineEdit(self.tab_4)
        self.new_user_read.setObjectName(u"new_user_read")
        self.new_user_read.setEnabled(False)
        self.new_user_read.setMinimumSize(QSize(250, 50))
        self.new_user_read.setMaximumSize(QSize(300, 50))
        self.new_user_read.setFont(font8)
        self.new_user_read.setStyleSheet(u"")

        self.gridLayout_14.addWidget(self.new_user_read, 4, 1, 1, 1)

        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(200, 50))
        self.label_9.setMaximumSize(QSize(200, 50))
        self.label_9.setFont(font9)

        self.gridLayout_14.addWidget(self.label_9, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_2 = QVBoxLayout(self.tab_9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.access_label_5 = QLabel(self.tab_9)
        self.access_label_5.setObjectName(u"access_label_5")
        self.access_label_5.setEnabled(False)
        self.access_label_5.setMinimumSize(QSize(400, 50))
        self.access_label_5.setMaximumSize(QSize(400, 50))
        self.access_label_5.setFont(font9)

        self.verticalLayout_2.addWidget(self.access_label_5, 0, Qt.AlignHCenter)

        self.username_read_3 = QLineEdit(self.tab_9)
        self.username_read_3.setObjectName(u"username_read_3")
        self.username_read_3.setMinimumSize(QSize(400, 50))
        self.username_read_3.setMaximumSize(QSize(600, 16777215))
        self.username_read_3.setFont(font4)
        self.username_read_3.setEchoMode(QLineEdit.Normal)
        self.username_read_3.setReadOnly(False)
        self.username_read_3.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.username_read_3, 0, Qt.AlignHCenter)

        self.old_password = QLineEdit(self.tab_9)
        self.old_password.setObjectName(u"old_password")
        self.old_password.setMinimumSize(QSize(400, 50))
        self.old_password.setMaximumSize(QSize(600, 16777215))
        self.old_password.setFont(font4)
        self.old_password.setEchoMode(QLineEdit.Password)
        self.old_password.setReadOnly(False)
        self.old_password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.old_password, 0, Qt.AlignHCenter)

        self.new_password = QLineEdit(self.tab_9)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setMinimumSize(QSize(400, 50))
        self.new_password.setMaximumSize(QSize(600, 16777215))
        self.new_password.setFont(font4)
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.new_password, 0, Qt.AlignHCenter)

        self.new_password2 = QLineEdit(self.tab_9)
        self.new_password2.setObjectName(u"new_password2")
        self.new_password2.setMinimumSize(QSize(400, 50))
        self.new_password2.setMaximumSize(QSize(600, 16777215))
        self.new_password2.setFont(font4)
        self.new_password2.setEchoMode(QLineEdit.Password)
        self.new_password2.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.new_password2, 0, Qt.AlignHCenter)

        self.change_password_button_2 = QPushButton(self.tab_9)
        self.change_password_button_2.setObjectName(u"change_password_button_2")
        self.change_password_button_2.setEnabled(True)
        self.change_password_button_2.setMinimumSize(QSize(200, 50))
        self.change_password_button_2.setMaximumSize(QSize(200, 50))
        self.change_password_button_2.setFont(font7)
        self.change_password_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_password_button_2.setStyleSheet(u"border-radius: 20px")
        icon5 = QIcon()
        icon5.addFile(u"Icons/488911000.png", QSize(), QIcon.Normal, QIcon.Off)
        self.change_password_button_2.setIcon(icon5)
        self.change_password_button_2.setIconSize(QSize(32, 32))
        self.change_password_button_2.setAutoRepeat(False)
        self.change_password_button_2.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.change_password_button_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.tabWidget.addTab(self.tab_9, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)

        Main.setCentralWidget(self.Mainwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 25))
        self.menubar.setMinimumSize(QSize(0, 25))
        font10 = QFont()
        font10.setPointSize(10)
        self.menubar.setFont(font10)
        self.menubar.setDefaultUp(False)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuSettings.setMinimumSize(QSize(100, 0))
        self.menuThemes = QMenu(self.menuSettings)
        self.menuThemes.setObjectName(u"menuThemes")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menuSettings.addAction(self.menuThemes.menuAction())
        self.menuThemes.addSeparator()
        self.menuThemes.addAction(self.actionDark_Mode)
        self.menuThemes.addAction(self.actionLight_Mode)
        self.menuThemes.addAction(self.actionConsole_Mode)
        self.menuThemes.addAction(self.actionAqua_Mode)

        self.retranslateUi(Main)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(30)
        self.tabWidget.setCurrentIndex(4)
        self.access_right_read.setCurrentIndex(0)
        self.access_right_read_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.actionDark_Mode.setText(QCoreApplication.translate("Main", u"Dark Mode", None))
        self.actionLight_Mode.setText(QCoreApplication.translate("Main", u"Light Mode", None))
        self.actionConsole_Mode.setText(QCoreApplication.translate("Main", u"Console Mode", None))
        self.actionAqua_Mode.setText(QCoreApplication.translate("Main", u"Aqua Mode", None))
        self.current_user.setText(QCoreApplication.translate("Main", u"   Current user:", None))
        self.access_right.setText(QCoreApplication.translate("Main", u"Acess right:", None))
        self.new_user_button.setText(QCoreApplication.translate("Main", u"Add a new user", None))
        self.delete_user_button.setText(QCoreApplication.translate("Main", u"Delete a user", None))
        self.modify_button.setText(QCoreApplication.translate("Main", u"Modify User", None))
        self.change_password_button.setText(QCoreApplication.translate("Main", u"Change password", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("Main", u"Users", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("Main", u"Dashboard", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Main", u"Professors", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Main", u"Students", None))
        self.label.setText(QCoreApplication.translate("Main", u"Welcome to today's work sesssion<br>Goodluck!!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main", u"Tab 1", None))
        self.password2_read.setPlaceholderText(QCoreApplication.translate("Main", u"Confirm Password...", None))
        self.show_button.setText("")
        self.access_right_read.setItemText(0, QCoreApplication.translate("Main", u"1: Read only", None))
        self.access_right_read.setItemText(1, QCoreApplication.translate("Main", u"2: Insert", None))
        self.access_right_read.setItemText(2, QCoreApplication.translate("Main", u"3: Modify", None))
        self.access_right_read.setItemText(3, QCoreApplication.translate("Main", u"4: Delete", None))

#if QT_CONFIG(tooltip)
        self.access_right_read.setToolTip(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.access_right_read.setStatusTip(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.access_right_read.setWhatsThis(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(whatsthis)
        self.access_right_read.setCurrentText(QCoreApplication.translate("Main", u"1: Read only", None))
#if QT_CONFIG(tooltip)
        self.password_read.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.password_read.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.password_read.setPlaceholderText(QCoreApplication.translate("Main", u"Password...", None))
        self.register_button.setText("")
        self.username_read.setPlaceholderText(QCoreApplication.translate("Main", u"Username...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Tab 2", None))
        self.delete_user_button_2.setText("")
        self.user_delete_read.setPlaceholderText(QCoreApplication.translate("Main", u"Username...", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Delete user permanantly:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Page", None))
        self.modify_button_2.setText("")
        self.access_right_read_3.setItemText(0, QCoreApplication.translate("Main", u"1: Read only", None))
        self.access_right_read_3.setItemText(1, QCoreApplication.translate("Main", u"2: Insert", None))
        self.access_right_read_3.setItemText(2, QCoreApplication.translate("Main", u"3: Modify", None))
        self.access_right_read_3.setItemText(3, QCoreApplication.translate("Main", u"4: Delete", None))

#if QT_CONFIG(tooltip)
        self.access_right_read_3.setToolTip(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.access_right_read_3.setStatusTip(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.access_right_read_3.setWhatsThis(QCoreApplication.translate("Main", u"Access Right...", None))
#endif // QT_CONFIG(whatsthis)
        self.access_right_read_3.setCurrentText(QCoreApplication.translate("Main", u"1: Read only", None))
        self.access_label_2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>Change to:</p></body></html>", None))
        self.access_label.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>Current Access Right:</p></body></html>", None))
        self.search_user_read.setPlaceholderText(QCoreApplication.translate("Main", u"Username...", None))
        self.search_user_button.setText("")
        self.new_user_read.setPlaceholderText(QCoreApplication.translate("Main", u"New Username...", None))
        self.label_9.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>Find User:</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Main", u"Page", None))
        self.access_label_5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p>Change password for:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.username_read_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.username_read_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.username_read_3.setPlaceholderText(QCoreApplication.translate("Main", u"Username:", None))
#if QT_CONFIG(tooltip)
        self.old_password.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.old_password.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.old_password.setPlaceholderText(QCoreApplication.translate("Main", u"Old password...", None))
#if QT_CONFIG(tooltip)
        self.new_password.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.new_password.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.new_password.setPlaceholderText(QCoreApplication.translate("Main", u"New password...", None))
        self.new_password2.setPlaceholderText(QCoreApplication.translate("Main", u"Confirm New Password...", None))
        self.change_password_button_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("Main", u"Page", None))
        self.menuFile.setTitle(QCoreApplication.translate("Main", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("Main", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("Main", u"View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("Main", u"Settings", None))
        self.menuThemes.setTitle(QCoreApplication.translate("Main", u"Themes", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Main", u"Help", None))
        self.menuExit.setTitle(QCoreApplication.translate("Main", u"Exit", None))
    # retranslateUi

