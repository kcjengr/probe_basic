# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'probe_basic.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QComboBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QListView, QListWidgetItem, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.containers.stack import VCPStackedWidget
from qtpyvcp.widgets.display_widgets.designer_plugins import VTKBackPlot
from qtpyvcp.widgets.display_widgets.notification_widget import NotificationWidget
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.widgets.hal_widgets.hal_bar_indicator import HalBarIndicator
from qtpyvcp.widgets.hal_widgets.hal_button import HalButton
from qtpyvcp.widgets.hal_widgets.hal_label import HalLabel
from qtpyvcp.widgets.hal_widgets.hal_led import HalLedIndicator
from qtpyvcp.widgets.input_widgets.action_slider import ActionSlider
from qtpyvcp.widgets.input_widgets.file_system import (FileSystemTable, RemovableDeviceComboBox)
from qtpyvcp.widgets.input_widgets.gcode_text_edit import GcodeTextEdit
from qtpyvcp.widgets.input_widgets.jog_increment import JogIncrementWidget
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.mdihistory_widget import MDIHistory
from qtpyvcp.widgets.input_widgets.offset_table import OffsetTable
from qtpyvcp.widgets.input_widgets.recent_file_combobox import RecentFileComboBox
from qtpyvcp.widgets.input_widgets.setting_slider import (VCPSettingsLineEdit, VCPSettingsPushButton, VCPSettingsSlider)
from qtpyvcp.widgets.input_widgets.tool_table import ToolTable
from widgets.conversational.designer_plugins import (FacingWidget, HoleCircleWidget, XYCoordWidget)
import probe_basic_rc
import probe_basic_rc
import probe_basic_rc
import probe_basic_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(1931, 1101)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(274, 50))
        Form.setMaximumSize(QSize(16777215, 1101))
        font = QFont()
        font.setFamilies([u"Bebas Kai"])
        font.setPointSize(11)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/probe_basic_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(-1)
        Form.setStyleSheet(u"Form {\n"
"bottom-margin: 0px;\n"
"}")
        Form.setDocumentMode(False)
        Form.setProperty(u"promptAtExit", False)
        Form.setProperty(u"promot_on_exit", False)
        self.actionExit = QAction(Form)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen = QAction(Form)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(Form)
        self.actionClose.setObjectName(u"actionClose")
        self.actionReload = QAction(Form)
        self.actionReload.setObjectName(u"actionReload")
        self.actionSave_As = QAction(Form)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionHome_X = QAction(Form)
        self.actionHome_X.setObjectName(u"actionHome_X")
        self.actionHome_Y = QAction(Form)
        self.actionHome_Y.setObjectName(u"actionHome_Y")
        self.actionHome_Z = QAction(Form)
        self.actionHome_Z.setObjectName(u"actionHome_Z")
        self.action_EmergencyStop_toggle = QAction(Form)
        self.action_EmergencyStop_toggle.setObjectName(u"action_EmergencyStop_toggle")
        self.action_MachinePower_toggle = QAction(Form)
        self.action_MachinePower_toggle.setObjectName(u"action_MachinePower_toggle")
        self.action_MachinePower_toggle.setProperty(u"_axis", 2)
        self.actionHome_All = QAction(Form)
        self.actionHome_All.setObjectName(u"actionHome_All")
        self.actionRun_Program = QAction(Form)
        self.actionRun_Program.setObjectName(u"actionRun_Program")
        self.actionFile1 = QAction(Form)
        self.actionFile1.setObjectName(u"actionFile1")
        self.actionReport_Actual_Position = QAction(Form)
        self.actionReport_Actual_Position.setObjectName(u"actionReport_Actual_Position")
        self.actionReport_Actual_Position.setCheckable(True)
        self.actionTest = QAction(Form)
        self.actionTest.setObjectName(u"actionTest")
        self.action_Mist_toggle = QAction(Form)
        self.action_Mist_toggle.setObjectName(u"action_Mist_toggle")
        self.action_Mist_toggle.setCheckable(True)
        self.action_Flood_toggle = QAction(Form)
        self.action_Flood_toggle.setObjectName(u"action_Flood_toggle")
        self.action_Flood_toggle.setCheckable(True)
        self.centralwidget = QWidget(Form)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_31 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(-1, -1, 0, 3)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, -1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777214))
        palette = QPalette()
        brush = QBrush(QColor(241, 241, 241, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(129, 133, 132, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(85, 255, 127, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush2)
        brush3 = QBrush(QColor(241, 241, 241, 128))
        brush3.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush2)
        brush4 = QBrush(QColor(241, 241, 241, 128))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        brush5 = QBrush(QColor(145, 141, 126, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush5)
        brush6 = QBrush(QColor(241, 241, 241, 128))
        brush6.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush6)
#endif
        self.tabWidget.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Bebas Kai"])
        font1.setPointSize(15)
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"    Background: rgb(146, 150, 149);\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab {\n"
"    margin-top: 1px;\n"
"    margin-bottom: 2px;\n"
"    min-width: 130px;\n"
"    min-height: 30px;\n"
"    font: 15pt \"bebas kai\";\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setUsesScrollButtons(False)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.horizontalLayout = QHBoxLayout(self.main_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_49 = QWidget(self.main_tab)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_61 = QVBoxLayout(self.widget_49)
        self.verticalLayout_61.setSpacing(12)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 6, 0)
        self.splitter = QSplitter(self.widget_49)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFocusPolicy(Qt.NoFocus)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.gcode_mdi = QStackedWidget(self.splitter)
        self.gcode_mdi.setObjectName(u"gcode_mdi")
        self.Page1gcodeedit = QWidget()
        self.Page1gcodeedit.setObjectName(u"Page1gcodeedit")
        self.verticalLayout_2 = QVBoxLayout(self.Page1gcodeedit)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 0)
        self.widget_6 = QWidget(self.Page1gcodeedit)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 40))
        self.widget_6.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 1, 0, 1)
        self.recentfilecombobox = RecentFileComboBox(self.widget_6)
        self.recentfilecombobox.setObjectName(u"recentfilecombobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.recentfilecombobox.sizePolicy().hasHeightForWidth())
        self.recentfilecombobox.setSizePolicy(sizePolicy2)
        self.recentfilecombobox.setMinimumSize(QSize(147, 32))
        self.recentfilecombobox.setMaximumSize(QSize(16777215, 32))
        self.recentfilecombobox.setFocusPolicy(Qt.NoFocus)
        self.recentfilecombobox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid black;\n"
"	border-radius: 3px;\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	padding: 1px 23px 1px 8px;\n"
"	min-width: 6em;\n"
"	color: #ffffff;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" 	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image: url(:/images/combobox-arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" 	selection-background-color: #999999;\n"
"	selection-color: #4f4f4f;\n"
"}")

        self.horizontalLayout_12.addWidget(self.recentfilecombobox)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy3)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.find_m6_button = QPushButton(self.widget_9)
        self.find_m6_button.setObjectName(u"find_m6_button")
        sizePolicy.setHeightForWidth(self.find_m6_button.sizePolicy().hasHeightForWidth())
        self.find_m6_button.setSizePolicy(sizePolicy)
        self.find_m6_button.setMinimumSize(QSize(80, 32))
        self.find_m6_button.setMaximumSize(QSize(80, 32))
        self.find_m6_button.setFocusPolicy(Qt.NoFocus)
        self.find_m6_button.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid black;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"	color: white;\n"
"    font: 13pt \"Bebas Kai\";\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_14.addWidget(self.find_m6_button)

        self.run_from_line_Num = VCPLineEdit(self.widget_9)
        self.run_from_line_Num.setObjectName(u"run_from_line_Num")
        sizePolicy.setHeightForWidth(self.run_from_line_Num.sizePolicy().hasHeightForWidth())
        self.run_from_line_Num.setSizePolicy(sizePolicy)
        self.run_from_line_Num.setMinimumSize(QSize(80, 32))
        self.run_from_line_Num.setMaximumSize(QSize(80, 32))
        self.run_from_line_Num.setMouseTracking(False)
        self.run_from_line_Num.setFocusPolicy(Qt.NoFocus)
        self.run_from_line_Num.setStyleSheet(u"color: white;\n"
"border-radius: 0px;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"font: 13pt;\n"
"background-color: transparent;")
        self.run_from_line_Num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.run_from_line_Num.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.run_from_line_Num)

        self.run_from_line_Btn = QPushButton(self.widget_9)
        self.run_from_line_Btn.setObjectName(u"run_from_line_Btn")
        self.run_from_line_Btn.setMinimumSize(QSize(80, 32))
        self.run_from_line_Btn.setMaximumSize(QSize(80, 32))
        self.run_from_line_Btn.setFocusPolicy(Qt.NoFocus)
        self.run_from_line_Btn.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    color: white;\n"
"    font: 13pt \"Bebas Kai\";\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1"
                        ":0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.18 rgba(123, 123, 232, 255), stop:0.39 rgba(85, 85, 238, 255), stop:0.61 rgba(85, 85, 238, 255), stop:0.82 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.run_from_line_Btn.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.run_from_line_Btn)


        self.horizontalLayout_12.addWidget(self.widget_9)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.gcodetextedit_2 = GcodeTextEdit(self.Page1gcodeedit)
        self.gcodetextedit_2.setObjectName(u"gcodetextedit_2")
        sizePolicy1.setHeightForWidth(self.gcodetextedit_2.sizePolicy().hasHeightForWidth())
        self.gcodetextedit_2.setSizePolicy(sizePolicy1)
        self.gcodetextedit_2.setStyleSheet(u"")
        self.gcodetextedit_2.setFrameShape(QFrame.NoFrame)
        self.gcodetextedit_2.setFrameShadow(QFrame.Plain)
        self.gcodetextedit_2.setLineWidth(0)
        self.gcodetextedit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.gcodetextedit_2.setTabStopWidth(100)
        self.gcodetextedit_2.setProperty(u"syntaxHighlighting", False)
        self.gcodetextedit_2.setProperty(u"readOnly", True)
        self.gcodetextedit_2.setProperty(u"currentLineBackground", QColor(214, 214, 221))
        self.gcodetextedit_2.setProperty(u"marginBackground", QColor(146, 150, 149))
        self.gcodetextedit_2.setProperty(u"marginCurrentLineBackground", QColor(110, 110, 110))
        self.gcodetextedit_2.setProperty(u"marginColor", QColor(49, 49, 49))
        self.gcodetextedit_2.setProperty(u"marginCurrentLineColor", QColor(255, 255, 255))

        self.verticalLayout_2.addWidget(self.gcodetextedit_2)

        self.gcode_mdi.addWidget(self.Page1gcodeedit)
        self.Page2_mdiedit = QWidget()
        self.Page2_mdiedit.setObjectName(u"Page2_mdiedit")
        self.horizontalLayout_16 = QHBoxLayout(self.Page2_mdiedit)
        self.horizontalLayout_16.setSpacing(30)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(6, 6, 12, 3)
        self.verticalWidget = QWidget(self.Page2_mdiedit)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy4)
        self.verticalWidget.setStyleSheet(u"")
        self.verticalLayout_60 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_60.setSpacing(9)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.mdihistory = MDIHistory(self.verticalWidget)
        self.mdihistory.setObjectName(u"mdihistory")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.mdihistory.sizePolicy().hasHeightForWidth())
        self.mdihistory.setSizePolicy(sizePolicy5)
        self.mdihistory.setMinimumSize(QSize(360, 0))
        self.mdihistory.setStyleSheet(u"MDIHistory {\n"
"    font: 16pt \"Bebas Kai\";\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: black;\n"
"}")
        self.mdihistory.setAlternatingRowColors(False)
        self.mdihistory.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.mdihistory.setViewMode(QListView.ListMode)
        self.mdihistory.setProperty(u"mdiListOrderNatural", True)

        self.verticalLayout_60.addWidget(self.mdihistory)

        self.widget_37 = QWidget(self.verticalWidget)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy4.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy4)
        self.widget_37.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_147 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_147.setSpacing(12)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 1, 0, 1)
        self.btn_del_history_row_mdi = QPushButton(self.widget_37)
        self.btn_del_history_row_mdi.setObjectName(u"btn_del_history_row_mdi")
        sizePolicy2.setHeightForWidth(self.btn_del_history_row_mdi.sizePolicy().hasHeightForWidth())
        self.btn_del_history_row_mdi.setSizePolicy(sizePolicy2)
        self.btn_del_history_row_mdi.setMinimumSize(QSize(58, 50))
        self.btn_del_history_row_mdi.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Bebas Kai"])
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_del_history_row_mdi.setFont(font2)
        self.btn_del_history_row_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_del_history_row_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_147.addWidget(self.btn_del_history_row_mdi)

        self.btn_del_all_mdi = QPushButton(self.widget_37)
        self.btn_del_all_mdi.setObjectName(u"btn_del_all_mdi")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_del_all_mdi.sizePolicy().hasHeightForWidth())
        self.btn_del_all_mdi.setSizePolicy(sizePolicy6)
        self.btn_del_all_mdi.setMinimumSize(QSize(58, 50))
        self.btn_del_all_mdi.setMaximumSize(QSize(16777215, 50))
        self.btn_del_all_mdi.setFont(font2)
        self.btn_del_all_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_del_all_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_147.addWidget(self.btn_del_all_mdi)

        self.btn_clear_queue_mdi = QPushButton(self.widget_37)
        self.btn_clear_queue_mdi.setObjectName(u"btn_clear_queue_mdi")
        sizePolicy2.setHeightForWidth(self.btn_clear_queue_mdi.sizePolicy().hasHeightForWidth())
        self.btn_clear_queue_mdi.setSizePolicy(sizePolicy2)
        self.btn_clear_queue_mdi.setMinimumSize(QSize(58, 50))
        self.btn_clear_queue_mdi.setMaximumSize(QSize(16777215, 50))
        self.btn_clear_queue_mdi.setFont(font2)
        self.btn_clear_queue_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_clear_queue_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_147.addWidget(self.btn_clear_queue_mdi)

        self.btn_pause_mdi = QPushButton(self.widget_37)
        self.btn_pause_mdi.setObjectName(u"btn_pause_mdi")
        sizePolicy2.setHeightForWidth(self.btn_pause_mdi.sizePolicy().hasHeightForWidth())
        self.btn_pause_mdi.setSizePolicy(sizePolicy2)
        self.btn_pause_mdi.setMinimumSize(QSize(58, 50))
        self.btn_pause_mdi.setMaximumSize(QSize(16777215, 50))
        self.btn_pause_mdi.setFont(font2)
        self.btn_pause_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_pause_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")
        self.btn_pause_mdi.setCheckable(True)

        self.horizontalLayout_147.addWidget(self.btn_pause_mdi)

        self.btn_row_up_mdi = QPushButton(self.widget_37)
        self.btn_row_up_mdi.setObjectName(u"btn_row_up_mdi")
        sizePolicy6.setHeightForWidth(self.btn_row_up_mdi.sizePolicy().hasHeightForWidth())
        self.btn_row_up_mdi.setSizePolicy(sizePolicy6)
        self.btn_row_up_mdi.setMinimumSize(QSize(62, 50))
        self.btn_row_up_mdi.setMaximumSize(QSize(62, 50))
        self.btn_row_up_mdi.setFont(font1)
        self.btn_row_up_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_row_up_mdi.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/up_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_row_up_mdi.setIcon(icon1)
        self.btn_row_up_mdi.setIconSize(QSize(25, 25))

        self.horizontalLayout_147.addWidget(self.btn_row_up_mdi)


        self.verticalLayout_60.addWidget(self.widget_37)

        self.widget_39 = QWidget(self.verticalWidget)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy4.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy4)
        self.widget_39.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_150 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_150.setSpacing(12)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 1, 0, 1)
        self.btn_run_from_line_mdi = QPushButton(self.widget_39)
        self.btn_run_from_line_mdi.setObjectName(u"btn_run_from_line_mdi")
        sizePolicy6.setHeightForWidth(self.btn_run_from_line_mdi.sizePolicy().hasHeightForWidth())
        self.btn_run_from_line_mdi.setSizePolicy(sizePolicy6)
        self.btn_run_from_line_mdi.setMinimumSize(QSize(58, 50))
        self.btn_run_from_line_mdi.setFont(font2)
        self.btn_run_from_line_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_run_from_line_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_150.addWidget(self.btn_run_from_line_mdi)

        self.btn_run_selection_mdi = QPushButton(self.widget_39)
        self.btn_run_selection_mdi.setObjectName(u"btn_run_selection_mdi")
        sizePolicy6.setHeightForWidth(self.btn_run_selection_mdi.sizePolicy().hasHeightForWidth())
        self.btn_run_selection_mdi.setSizePolicy(sizePolicy6)
        self.btn_run_selection_mdi.setMinimumSize(QSize(58, 50))
        self.btn_run_selection_mdi.setFont(font2)
        self.btn_run_selection_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_run_selection_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_150.addWidget(self.btn_run_selection_mdi)

        self.btn_copy_to_editor_mdi = QPushButton(self.widget_39)
        self.btn_copy_to_editor_mdi.setObjectName(u"btn_copy_to_editor_mdi")
        sizePolicy6.setHeightForWidth(self.btn_copy_to_editor_mdi.sizePolicy().hasHeightForWidth())
        self.btn_copy_to_editor_mdi.setSizePolicy(sizePolicy6)
        self.btn_copy_to_editor_mdi.setMinimumSize(QSize(58, 50))
        self.btn_copy_to_editor_mdi.setFont(font2)
        self.btn_copy_to_editor_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_copy_to_editor_mdi.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_150.addWidget(self.btn_copy_to_editor_mdi)

        self.btn_row_down_mdi = QPushButton(self.widget_39)
        self.btn_row_down_mdi.setObjectName(u"btn_row_down_mdi")
        sizePolicy.setHeightForWidth(self.btn_row_down_mdi.sizePolicy().hasHeightForWidth())
        self.btn_row_down_mdi.setSizePolicy(sizePolicy)
        self.btn_row_down_mdi.setMinimumSize(QSize(62, 50))
        self.btn_row_down_mdi.setMaximumSize(QSize(62, 50))
        self.btn_row_down_mdi.setFont(font1)
        self.btn_row_down_mdi.setFocusPolicy(Qt.NoFocus)
        self.btn_row_down_mdi.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/down_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_row_down_mdi.setIcon(icon2)
        self.btn_row_down_mdi.setIconSize(QSize(25, 25))

        self.horizontalLayout_150.addWidget(self.btn_row_down_mdi)


        self.verticalLayout_60.addWidget(self.widget_39)


        self.horizontalLayout_16.addWidget(self.verticalWidget)

        self.mdi_button_container_widget = QWidget(self.Page2_mdiedit)
        self.mdi_button_container_widget.setObjectName(u"mdi_button_container_widget")
        self.mdi_button_container_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.mdi_button_container_widget)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 3, 0, 0)
        self.R = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi = QButtonGroup(Form)
        self.btngrpMdi.setObjectName(u"btngrpMdi")
        self.btngrpMdi.addButton(self.R)
        self.R.setObjectName(u"R")
        sizePolicy1.setHeightForWidth(self.R.sizePolicy().hasHeightForWidth())
        self.R.setSizePolicy(sizePolicy1)
        self.R.setMinimumSize(QSize(60, 58))
        self.R.setMaximumSize(QSize(60, 58))
        font3 = QFont()
        font3.setFamilies([u"Bebas Kai"])
        font3.setPointSize(21)
        self.R.setFont(font3)
        self.R.setFocusPolicy(Qt.NoFocus)
        self.R.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.R, 0, 10, 1, 1)

        self.I = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.I)
        self.I.setObjectName(u"I")
        sizePolicy1.setHeightForWidth(self.I.sizePolicy().hasHeightForWidth())
        self.I.setSizePolicy(sizePolicy1)
        self.I.setMinimumSize(QSize(60, 58))
        self.I.setMaximumSize(QSize(60, 58))
        self.I.setFont(font3)
        self.I.setFocusPolicy(Qt.NoFocus)
        self.I.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.I, 0, 5, 1, 1)

        self.NP6 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP6)
        self.NP6.setObjectName(u"NP6")
        sizePolicy1.setHeightForWidth(self.NP6.sizePolicy().hasHeightForWidth())
        self.NP6.setSizePolicy(sizePolicy1)
        self.NP6.setMinimumSize(QSize(60, 58))
        self.NP6.setMaximumSize(QSize(60, 58))
        font4 = QFont()
        font4.setFamilies([u"Bebas Kai"])
        font4.setPointSize(21)
        font4.setBold(False)
        font4.setItalic(False)
        self.NP6.setFont(font4)
        self.NP6.setFocusPolicy(Qt.NoFocus)
        self.NP6.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP6, 4, 9, 1, 1)

        self.A = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.A)
        self.A.setObjectName(u"A")
        sizePolicy1.setHeightForWidth(self.A.sizePolicy().hasHeightForWidth())
        self.A.setSizePolicy(sizePolicy1)
        self.A.setMinimumSize(QSize(60, 58))
        self.A.setMaximumSize(QSize(60, 58))
        self.A.setFont(font3)
        self.A.setFocusPolicy(Qt.NoFocus)
        self.A.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.A, 1, 9, 1, 1)

        self.S = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.S)
        self.S.setObjectName(u"S")
        sizePolicy1.setHeightForWidth(self.S.sizePolicy().hasHeightForWidth())
        self.S.setSizePolicy(sizePolicy1)
        self.S.setMinimumSize(QSize(60, 58))
        self.S.setMaximumSize(QSize(60, 58))
        self.S.setFont(font3)
        self.S.setFocusPolicy(Qt.NoFocus)
        self.S.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.S, 4, 10, 1, 1)

        self.F = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.F)
        self.F.setObjectName(u"F")
        sizePolicy1.setHeightForWidth(self.F.sizePolicy().hasHeightForWidth())
        self.F.setSizePolicy(sizePolicy1)
        self.F.setMinimumSize(QSize(60, 58))
        self.F.setMaximumSize(QSize(60, 58))
        self.F.setFont(font3)
        self.F.setFocusPolicy(Qt.NoFocus)
        self.F.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.F, 2, 10, 1, 1)

        self.J = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.J)
        self.J.setObjectName(u"J")
        sizePolicy1.setHeightForWidth(self.J.sizePolicy().hasHeightForWidth())
        self.J.setSizePolicy(sizePolicy1)
        self.J.setMinimumSize(QSize(60, 58))
        self.J.setMaximumSize(QSize(60, 58))
        self.J.setFont(font3)
        self.J.setFocusPolicy(Qt.NoFocus)
        self.J.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.J, 0, 6, 1, 1)

        self.NP3 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP3)
        self.NP3.setObjectName(u"NP3")
        sizePolicy1.setHeightForWidth(self.NP3.sizePolicy().hasHeightForWidth())
        self.NP3.setSizePolicy(sizePolicy1)
        self.NP3.setMinimumSize(QSize(60, 58))
        self.NP3.setMaximumSize(QSize(60, 58))
        self.NP3.setFont(font4)
        self.NP3.setFocusPolicy(Qt.NoFocus)
        self.NP3.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP3, 6, 9, 1, 1)

        self.NP7 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP7)
        self.NP7.setObjectName(u"NP7")
        sizePolicy1.setHeightForWidth(self.NP7.sizePolicy().hasHeightForWidth())
        self.NP7.setSizePolicy(sizePolicy1)
        self.NP7.setMinimumSize(QSize(60, 58))
        self.NP7.setMaximumSize(QSize(60, 58))
        self.NP7.setFont(font4)
        self.NP7.setFocusPolicy(Qt.NoFocus)
        self.NP7.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP7, 2, 6, 1, 1)

        self.M = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.M)
        self.M.setObjectName(u"M")
        sizePolicy1.setHeightForWidth(self.M.sizePolicy().hasHeightForWidth())
        self.M.setSizePolicy(sizePolicy1)
        self.M.setMinimumSize(QSize(60, 58))
        self.M.setMaximumSize(QSize(60, 58))
        self.M.setFont(font3)
        self.M.setFocusPolicy(Qt.NoFocus)
        self.M.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.M, 4, 5, 1, 1)

        self.NP5 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP5)
        self.NP5.setObjectName(u"NP5")
        sizePolicy1.setHeightForWidth(self.NP5.sizePolicy().hasHeightForWidth())
        self.NP5.setSizePolicy(sizePolicy1)
        self.NP5.setMinimumSize(QSize(60, 58))
        self.NP5.setMaximumSize(QSize(60, 58))
        self.NP5.setFont(font4)
        self.NP5.setFocusPolicy(Qt.NoFocus)
        self.NP5.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP5, 4, 8, 1, 1)

        self.btnMdiSpace = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.btnMdiSpace)
        self.btnMdiSpace.setObjectName(u"btnMdiSpace")
        sizePolicy1.setHeightForWidth(self.btnMdiSpace.sizePolicy().hasHeightForWidth())
        self.btnMdiSpace.setSizePolicy(sizePolicy1)
        self.btnMdiSpace.setMinimumSize(QSize(0, 58))
        self.btnMdiSpace.setMaximumSize(QSize(16777215, 58))
        font5 = QFont()
        font5.setFamilies([u"Bebas Kai"])
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        self.btnMdiSpace.setFont(font5)
        self.btnMdiSpace.setFocusPolicy(Qt.NoFocus)
        self.btnMdiSpace.setStyleSheet(u"font: 18pt \"Bebas Kai\";")

        self.gridLayout_4.addWidget(self.btnMdiSpace, 10, 8, 1, 2)

        self.D = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.D)
        self.D.setObjectName(u"D")
        sizePolicy1.setHeightForWidth(self.D.sizePolicy().hasHeightForWidth())
        self.D.setSizePolicy(sizePolicy1)
        self.D.setMinimumSize(QSize(60, 58))
        self.D.setMaximumSize(QSize(60, 58))
        self.D.setFont(font3)
        self.D.setFocusPolicy(Qt.NoFocus)
        self.D.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.D, 0, 9, 1, 1)

        self.B = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.B)
        self.B.setObjectName(u"B")
        sizePolicy1.setHeightForWidth(self.B.sizePolicy().hasHeightForWidth())
        self.B.setSizePolicy(sizePolicy1)
        self.B.setMinimumSize(QSize(60, 58))
        self.B.setMaximumSize(QSize(60, 58))
        self.B.setFont(font3)
        self.B.setFocusPolicy(Qt.NoFocus)
        self.B.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.B, 1, 10, 1, 1)

        self.Q = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.Q)
        self.Q.setObjectName(u"Q")
        sizePolicy1.setHeightForWidth(self.Q.sizePolicy().hasHeightForWidth())
        self.Q.setSizePolicy(sizePolicy1)
        self.Q.setMinimumSize(QSize(60, 58))
        self.Q.setMaximumSize(QSize(60, 58))
        self.Q.setFont(font3)
        self.Q.setFocusPolicy(Qt.NoFocus)
        self.Q.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.Q, 10, 10, 1, 1)

        self.O = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.O)
        self.O.setObjectName(u"O")
        sizePolicy1.setHeightForWidth(self.O.sizePolicy().hasHeightForWidth())
        self.O.setSizePolicy(sizePolicy1)
        self.O.setMinimumSize(QSize(60, 58))
        self.O.setMaximumSize(QSize(60, 58))
        self.O.setFont(font4)
        self.O.setFocusPolicy(Qt.NoFocus)
        self.O.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.O, 9, 5, 1, 1)

        self.Z = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.Z)
        self.Z.setObjectName(u"Z")
        sizePolicy1.setHeightForWidth(self.Z.sizePolicy().hasHeightForWidth())
        self.Z.setSizePolicy(sizePolicy1)
        self.Z.setMinimumSize(QSize(60, 58))
        self.Z.setMaximumSize(QSize(60, 58))
        self.Z.setFont(font3)
        self.Z.setFocusPolicy(Qt.NoFocus)
        self.Z.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.Z, 1, 8, 1, 1)

        self.NP1 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP1)
        self.NP1.setObjectName(u"NP1")
        sizePolicy1.setHeightForWidth(self.NP1.sizePolicy().hasHeightForWidth())
        self.NP1.setSizePolicy(sizePolicy1)
        self.NP1.setMinimumSize(QSize(60, 58))
        self.NP1.setMaximumSize(QSize(60, 58))
        self.NP1.setFont(font4)
        self.NP1.setFocusPolicy(Qt.NoFocus)
        self.NP1.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP1, 6, 6, 1, 1)

        self.P = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.P)
        self.P.setObjectName(u"P")
        sizePolicy1.setHeightForWidth(self.P.sizePolicy().hasHeightForWidth())
        self.P.setSizePolicy(sizePolicy1)
        self.P.setMinimumSize(QSize(60, 58))
        self.P.setMaximumSize(QSize(60, 58))
        self.P.setFont(font3)
        self.P.setFocusPolicy(Qt.NoFocus)
        self.P.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.P, 9, 10, 1, 1)

        self.NP4 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP4)
        self.NP4.setObjectName(u"NP4")
        sizePolicy1.setHeightForWidth(self.NP4.sizePolicy().hasHeightForWidth())
        self.NP4.setSizePolicy(sizePolicy1)
        self.NP4.setMinimumSize(QSize(60, 58))
        self.NP4.setMaximumSize(QSize(60, 58))
        self.NP4.setFont(font4)
        self.NP4.setFocusPolicy(Qt.NoFocus)
        self.NP4.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP4, 4, 6, 1, 1)

        self.NP8 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP8)
        self.NP8.setObjectName(u"NP8")
        sizePolicy1.setHeightForWidth(self.NP8.sizePolicy().hasHeightForWidth())
        self.NP8.setSizePolicy(sizePolicy1)
        self.NP8.setMinimumSize(QSize(60, 58))
        self.NP8.setMaximumSize(QSize(60, 58))
        self.NP8.setFont(font4)
        self.NP8.setFocusPolicy(Qt.NoFocus)
        self.NP8.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP8, 2, 8, 1, 1)

        self.decimal = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.decimal)
        self.decimal.setObjectName(u"decimal")
        sizePolicy1.setHeightForWidth(self.decimal.sizePolicy().hasHeightForWidth())
        self.decimal.setSizePolicy(sizePolicy1)
        self.decimal.setMinimumSize(QSize(60, 58))
        self.decimal.setMaximumSize(QSize(60, 58))
        self.decimal.setFont(font4)
        self.decimal.setFocusPolicy(Qt.NoFocus)
        self.decimal.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.decimal, 9, 9, 1, 1)

        self.NP9 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP9)
        self.NP9.setObjectName(u"NP9")
        sizePolicy1.setHeightForWidth(self.NP9.sizePolicy().hasHeightForWidth())
        self.NP9.setSizePolicy(sizePolicy1)
        self.NP9.setMinimumSize(QSize(60, 58))
        self.NP9.setMaximumSize(QSize(60, 58))
        self.NP9.setFont(font4)
        self.NP9.setFocusPolicy(Qt.NoFocus)
        self.NP9.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP9, 2, 9, 1, 1)

        self.L = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.L)
        self.L.setObjectName(u"L")
        sizePolicy1.setHeightForWidth(self.L.sizePolicy().hasHeightForWidth())
        self.L.setSizePolicy(sizePolicy1)
        self.L.setMinimumSize(QSize(60, 58))
        self.L.setMaximumSize(QSize(60, 58))
        self.L.setFont(font3)
        self.L.setFocusPolicy(Qt.NoFocus)
        self.L.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../../../../../../../../../../../../Desktop/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.L.setIcon(icon3)
        self.L.setIconSize(QSize(35, 35))

        self.gridLayout_4.addWidget(self.L, 10, 5, 1, 1)

        self.X = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.X)
        self.X.setObjectName(u"X")
        sizePolicy1.setHeightForWidth(self.X.sizePolicy().hasHeightForWidth())
        self.X.setSizePolicy(sizePolicy1)
        self.X.setMinimumSize(QSize(60, 58))
        self.X.setMaximumSize(QSize(60, 58))
        self.X.setFont(font3)
        self.X.setFocusPolicy(Qt.NoFocus)
        self.X.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.X, 1, 5, 1, 1)

        self.H = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.H)
        self.H.setObjectName(u"H")
        sizePolicy1.setHeightForWidth(self.H.sizePolicy().hasHeightForWidth())
        self.H.setSizePolicy(sizePolicy1)
        self.H.setMinimumSize(QSize(60, 58))
        self.H.setMaximumSize(QSize(60, 58))
        self.H.setFont(font3)
        self.H.setFocusPolicy(Qt.NoFocus)
        self.H.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.H, 6, 10, 1, 1)

        self.btnMdiLeft_arrow = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.btnMdiLeft_arrow)
        self.btnMdiLeft_arrow.setObjectName(u"btnMdiLeft_arrow")
        sizePolicy1.setHeightForWidth(self.btnMdiLeft_arrow.sizePolicy().hasHeightForWidth())
        self.btnMdiLeft_arrow.setSizePolicy(sizePolicy1)
        self.btnMdiLeft_arrow.setMinimumSize(QSize(60, 58))
        self.btnMdiLeft_arrow.setMaximumSize(QSize(60, 58))
        self.btnMdiLeft_arrow.setFont(font1)
        self.btnMdiLeft_arrow.setFocusPolicy(Qt.NoFocus)
        self.btnMdiLeft_arrow.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMdiLeft_arrow.setIcon(icon4)
        self.btnMdiLeft_arrow.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.btnMdiLeft_arrow, 12, 5, 1, 1)

        self.enter = QPushButton(self.mdi_button_container_widget)
        self.enter.setObjectName(u"enter")
        sizePolicy1.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy1)
        self.enter.setMinimumSize(QSize(0, 58))
        self.enter.setMaximumSize(QSize(16777215, 58))
        self.enter.setFont(font5)
        self.enter.setFocusPolicy(Qt.NoFocus)
        self.enter.setStyleSheet(u"font: 18pt \"Bebas Kai\";")

        self.gridLayout_4.addWidget(self.enter, 12, 8, 1, 3)

        self.T = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.T)
        self.T.setObjectName(u"T")
        sizePolicy1.setHeightForWidth(self.T.sizePolicy().hasHeightForWidth())
        self.T.setSizePolicy(sizePolicy1)
        self.T.setMinimumSize(QSize(60, 58))
        self.T.setMaximumSize(QSize(60, 58))
        self.T.setFont(font3)
        self.T.setFocusPolicy(Qt.NoFocus)
        self.T.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.T, 6, 5, 1, 1)

        self.btnMdiBksp = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.btnMdiBksp)
        self.btnMdiBksp.setObjectName(u"btnMdiBksp")
        sizePolicy1.setHeightForWidth(self.btnMdiBksp.sizePolicy().hasHeightForWidth())
        self.btnMdiBksp.setSizePolicy(sizePolicy1)
        self.btnMdiBksp.setMinimumSize(QSize(60, 58))
        self.btnMdiBksp.setMaximumSize(QSize(60, 58))
        self.btnMdiBksp.setFont(font1)
        self.btnMdiBksp.setFocusPolicy(Qt.NoFocus)
        self.btnMdiBksp.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/images/backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMdiBksp.setIcon(icon5)
        self.btnMdiBksp.setIconSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.btnMdiBksp, 10, 6, 1, 1)

        self.btnMdiRight_arrow = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.btnMdiRight_arrow)
        self.btnMdiRight_arrow.setObjectName(u"btnMdiRight_arrow")
        sizePolicy1.setHeightForWidth(self.btnMdiRight_arrow.sizePolicy().hasHeightForWidth())
        self.btnMdiRight_arrow.setSizePolicy(sizePolicy1)
        self.btnMdiRight_arrow.setMinimumSize(QSize(60, 58))
        self.btnMdiRight_arrow.setMaximumSize(QSize(60, 58))
        self.btnMdiRight_arrow.setFont(font1)
        self.btnMdiRight_arrow.setFocusPolicy(Qt.NoFocus)
        self.btnMdiRight_arrow.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/images/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMdiRight_arrow.setIcon(icon6)
        self.btnMdiRight_arrow.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.btnMdiRight_arrow, 12, 6, 1, 1)

        self.NP0 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP0)
        self.NP0.setObjectName(u"NP0")
        sizePolicy1.setHeightForWidth(self.NP0.sizePolicy().hasHeightForWidth())
        self.NP0.setSizePolicy(sizePolicy1)
        self.NP0.setMinimumSize(QSize(60, 58))
        self.NP0.setMaximumSize(QSize(60, 58))
        self.NP0.setFont(font4)
        self.NP0.setFocusPolicy(Qt.NoFocus)
        self.NP0.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP0, 9, 8, 1, 1)

        self.G = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.G)
        self.G.setObjectName(u"G")
        sizePolicy1.setHeightForWidth(self.G.sizePolicy().hasHeightForWidth())
        self.G.setSizePolicy(sizePolicy1)
        self.G.setMinimumSize(QSize(60, 58))
        self.G.setMaximumSize(QSize(60, 58))
        self.G.setFont(font3)
        self.G.setFocusPolicy(Qt.NoFocus)
        self.G.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.G, 2, 5, 1, 1)

        self.subtract = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.subtract)
        self.subtract.setObjectName(u"subtract")
        sizePolicy1.setHeightForWidth(self.subtract.sizePolicy().hasHeightForWidth())
        self.subtract.setSizePolicy(sizePolicy1)
        self.subtract.setMinimumSize(QSize(60, 58))
        self.subtract.setMaximumSize(QSize(60, 58))
        font6 = QFont()
        font6.setFamilies([u"Bebas Kai"])
        font6.setPointSize(24)
        font6.setBold(False)
        font6.setItalic(False)
        self.subtract.setFont(font6)
        self.subtract.setFocusPolicy(Qt.NoFocus)
        self.subtract.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(236, 49, 74, 255), stop:0.328042 rgba(236, 49, 74, 255), stop:0.492063 rgba(240, 53, 78, 255), stop:0.703704 rgba(236, 49, 74, 255), stop:0.86 rgba(236, 49, 74, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 24pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(252, 163, 178, 255), stop: 1.0 rgba(255, 173, 188, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop"
                        ":1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.subtract, 9, 6, 1, 1)

        self.K = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.K)
        self.K.setObjectName(u"K")
        sizePolicy1.setHeightForWidth(self.K.sizePolicy().hasHeightForWidth())
        self.K.setSizePolicy(sizePolicy1)
        self.K.setMinimumSize(QSize(60, 58))
        self.K.setMaximumSize(QSize(60, 58))
        self.K.setFont(font3)
        self.K.setFocusPolicy(Qt.NoFocus)
        self.K.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.K, 0, 8, 1, 1)

        self.Y = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.Y)
        self.Y.setObjectName(u"Y")
        sizePolicy1.setHeightForWidth(self.Y.sizePolicy().hasHeightForWidth())
        self.Y.setSizePolicy(sizePolicy1)
        self.Y.setMinimumSize(QSize(60, 58))
        self.Y.setMaximumSize(QSize(60, 58))
        self.Y.setFont(font3)
        self.Y.setFocusPolicy(Qt.NoFocus)
        self.Y.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.15 rgba(60, 121, 212, 255), stop:0.3 rgba(60, 121, 212, 255), stop:0.5 rgba(63, 124, 215, 255), stop:0.7 rgba(60, 121, 212, 255), stop:0.85 rgba(60, 121, 212, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(136, 177, 238, 255), stop: 1.0 rgba(146, 177, 238, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 1"
                        "35, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.Y, 1, 6, 1, 1)

        self.NP2 = QPushButton(self.mdi_button_container_widget)
        self.btngrpMdi.addButton(self.NP2)
        self.NP2.setObjectName(u"NP2")
        sizePolicy1.setHeightForWidth(self.NP2.sizePolicy().hasHeightForWidth())
        self.NP2.setSizePolicy(sizePolicy1)
        self.NP2.setMinimumSize(QSize(60, 58))
        self.NP2.setMaximumSize(QSize(60, 58))
        self.NP2.setFont(font4)
        self.NP2.setFocusPolicy(Qt.NoFocus)
        self.NP2.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.18 rgba(213, 213, 223, 255), stop:0.3 rgba(213, 213, 223, 255), stop:0.5 rgba(213, 213, 223, 255), stop:0.7 rgba(213, 213, 223, 255), stop:0.82 rgba(213, 213, 213, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 21pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 rgba(255, 255, 255, 255), stop: 1.0 rgba(235, 235, 235, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(1"
                        "26, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.gridLayout_4.addWidget(self.NP2, 6, 8, 1, 1)


        self.horizontalLayout_16.addWidget(self.mdi_button_container_widget)

        self.gcode_mdi.addWidget(self.Page2_mdiedit)
        self.splitter.addWidget(self.gcode_mdi)

        self.verticalLayout_61.addWidget(self.splitter)

        self.widget_50 = QWidget(self.widget_49)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 42))
        self.widget_50.setMaximumSize(QSize(16777215, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.mdiEntry = MDIEntry(self.widget_50)
        self.mdiEntry.setObjectName(u"mdiEntry")
        sizePolicy2.setHeightForWidth(self.mdiEntry.sizePolicy().hasHeightForWidth())
        self.mdiEntry.setSizePolicy(sizePolicy2)
        self.mdiEntry.setMinimumSize(QSize(0, 40))
        self.mdiEntry.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setFamilies([u"Bebas Kai"])
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(False)
        self.mdiEntry.setFont(font7)
        self.mdiEntry.setFocusPolicy(Qt.ClickFocus)
        self.mdiEntry.setProperty(u"mdi_history_size", 0)

        self.horizontalLayout_3.addWidget(self.mdiEntry)

        self.widget_54 = QWidget(self.widget_50)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_128 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_128.setSpacing(0)
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.horizontalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.gcode_page = QPushButton(self.widget_54)
        self.gcodemdibtnGroup = QButtonGroup(Form)
        self.gcodemdibtnGroup.setObjectName(u"gcodemdibtnGroup")
        self.gcodemdibtnGroup.addButton(self.gcode_page)
        self.gcode_page.setObjectName(u"gcode_page")
        self.gcode_page.setMinimumSize(QSize(90, 42))
        self.gcode_page.setMaximumSize(QSize(90, 42))
        self.gcode_page.setFocusPolicy(Qt.NoFocus)
        self.gcode_page.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 2px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.gcode_page.setCheckable(True)
        self.gcode_page.setChecked(True)
        self.gcode_page.setAutoExclusive(True)
        self.gcode_page.setProperty(u"page", 0)

        self.horizontalLayout_128.addWidget(self.gcode_page)

        self.mdi_page = QPushButton(self.widget_54)
        self.gcodemdibtnGroup.addButton(self.mdi_page)
        self.mdi_page.setObjectName(u"mdi_page")
        sizePolicy.setHeightForWidth(self.mdi_page.sizePolicy().hasHeightForWidth())
        self.mdi_page.setSizePolicy(sizePolicy)
        self.mdi_page.setMinimumSize(QSize(90, 42))
        self.mdi_page.setMaximumSize(QSize(90, 42))
        self.mdi_page.setFocusPolicy(Qt.NoFocus)
        self.mdi_page.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 2px;\n"
"    border-left-width: 1px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.mdi_page.setCheckable(True)
        self.mdi_page.setAutoExclusive(True)
        self.mdi_page.setProperty(u"page", 1)

        self.horizontalLayout_128.addWidget(self.mdi_page)


        self.horizontalLayout_3.addWidget(self.widget_54)


        self.verticalLayout_61.addWidget(self.widget_50)


        self.horizontalLayout.addWidget(self.widget_49)

        self.widget_7 = QWidget(self.main_tab)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(4)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy7)
        self.widget_7.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.vtk_control_buttons = QWidget(self.widget_7)
        self.vtk_control_buttons.setObjectName(u"vtk_control_buttons")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.vtk_control_buttons.sizePolicy().hasHeightForWidth())
        self.vtk_control_buttons.setSizePolicy(sizePolicy8)
        self.vtk_control_buttons.setMinimumSize(QSize(90, 0))
        self.vtk_control_buttons.setMaximumSize(QSize(90, 16777215))
        self.vtk_control_buttons.setStyleSheet(u".QWidget{\n"
"    background: rgb(32, 36, 37);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.vtk_control_buttons)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 12, 0, 12)
        self.iso_view_button = QPushButton(self.vtk_control_buttons)
        self.iso_view_button.setObjectName(u"iso_view_button")
        sizePolicy.setHeightForWidth(self.iso_view_button.sizePolicy().hasHeightForWidth())
        self.iso_view_button.setSizePolicy(sizePolicy)
        self.iso_view_button.setMinimumSize(QSize(75, 33))
        self.iso_view_button.setMaximumSize(QSize(75, 33))
        self.iso_view_button.setFocusPolicy(Qt.NoFocus)
        self.iso_view_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.iso_view_button)

        self.x_view_button = QPushButton(self.vtk_control_buttons)
        self.x_view_button.setObjectName(u"x_view_button")
        sizePolicy.setHeightForWidth(self.x_view_button.sizePolicy().hasHeightForWidth())
        self.x_view_button.setSizePolicy(sizePolicy)
        self.x_view_button.setMinimumSize(QSize(75, 33))
        self.x_view_button.setMaximumSize(QSize(75, 33))
        self.x_view_button.setFocusPolicy(Qt.NoFocus)
        self.x_view_button.setStyleSheet(u"")
        self.x_view_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.x_view_button)

        self.y_view_button = QPushButton(self.vtk_control_buttons)
        self.y_view_button.setObjectName(u"y_view_button")
        sizePolicy.setHeightForWidth(self.y_view_button.sizePolicy().hasHeightForWidth())
        self.y_view_button.setSizePolicy(sizePolicy)
        self.y_view_button.setMinimumSize(QSize(75, 33))
        self.y_view_button.setMaximumSize(QSize(75, 33))
        self.y_view_button.setFocusPolicy(Qt.NoFocus)
        self.y_view_button.setStyleSheet(u"")
        self.y_view_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.y_view_button)

        self.z_view_button = QPushButton(self.vtk_control_buttons)
        self.z_view_button.setObjectName(u"z_view_button")
        sizePolicy.setHeightForWidth(self.z_view_button.sizePolicy().hasHeightForWidth())
        self.z_view_button.setSizePolicy(sizePolicy)
        self.z_view_button.setMinimumSize(QSize(75, 33))
        self.z_view_button.setMaximumSize(QSize(75, 33))
        self.z_view_button.setFocusPolicy(Qt.NoFocus)
        self.z_view_button.setStyleSheet(u"")
        self.z_view_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.z_view_button)

        self.pan_button = QPushButton(self.vtk_control_buttons)
        self.pan_button.setObjectName(u"pan_button")
        sizePolicy6.setHeightForWidth(self.pan_button.sizePolicy().hasHeightForWidth())
        self.pan_button.setSizePolicy(sizePolicy6)
        self.pan_button.setMinimumSize(QSize(75, 33))
        self.pan_button.setMaximumSize(QSize(75, 33))
        self.pan_button.setFocusPolicy(Qt.NoFocus)
        self.pan_button.setStyleSheet(u"")
        self.pan_button.setCheckable(True)

        self.verticalLayout_8.addWidget(self.pan_button)

        self.zoom_in_button = QPushButton(self.vtk_control_buttons)
        self.zoom_in_button.setObjectName(u"zoom_in_button")
        sizePolicy6.setHeightForWidth(self.zoom_in_button.sizePolicy().hasHeightForWidth())
        self.zoom_in_button.setSizePolicy(sizePolicy6)
        self.zoom_in_button.setMinimumSize(QSize(75, 33))
        self.zoom_in_button.setMaximumSize(QSize(75, 33))
        self.zoom_in_button.setFocusPolicy(Qt.NoFocus)
        self.zoom_in_button.setStyleSheet(u"")
        self.zoom_in_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.zoom_in_button)

        self.zoom_out_button = QPushButton(self.vtk_control_buttons)
        self.zoom_out_button.setObjectName(u"zoom_out_button")
        sizePolicy6.setHeightForWidth(self.zoom_out_button.sizePolicy().hasHeightForWidth())
        self.zoom_out_button.setSizePolicy(sizePolicy6)
        self.zoom_out_button.setMinimumSize(QSize(75, 33))
        self.zoom_out_button.setMaximumSize(QSize(75, 33))
        self.zoom_out_button.setFocusPolicy(Qt.NoFocus)
        self.zoom_out_button.setStyleSheet(u"")
        self.zoom_out_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.zoom_out_button)

        self.program_zoom_button = QPushButton(self.vtk_control_buttons)
        self.program_zoom_button.setObjectName(u"program_zoom_button")
        sizePolicy.setHeightForWidth(self.program_zoom_button.sizePolicy().hasHeightForWidth())
        self.program_zoom_button.setSizePolicy(sizePolicy)
        self.program_zoom_button.setMinimumSize(QSize(75, 33))
        self.program_zoom_button.setMaximumSize(QSize(75, 33))
        self.program_zoom_button.setFocusPolicy(Qt.NoFocus)
        self.program_zoom_button.setStyleSheet(u"")
        self.program_zoom_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.program_zoom_button)

        self.machine_zoom_button = QPushButton(self.vtk_control_buttons)
        self.machine_zoom_button.setObjectName(u"machine_zoom_button")
        sizePolicy.setHeightForWidth(self.machine_zoom_button.sizePolicy().hasHeightForWidth())
        self.machine_zoom_button.setSizePolicy(sizePolicy)
        self.machine_zoom_button.setMinimumSize(QSize(75, 33))
        self.machine_zoom_button.setMaximumSize(QSize(75, 33))
        self.machine_zoom_button.setFocusPolicy(Qt.NoFocus)
        self.machine_zoom_button.setStyleSheet(u"")
        self.machine_zoom_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.machine_zoom_button)

        self.path_button = QPushButton(self.vtk_control_buttons)
        self.path_button.setObjectName(u"path_button")
        sizePolicy.setHeightForWidth(self.path_button.sizePolicy().hasHeightForWidth())
        self.path_button.setSizePolicy(sizePolicy)
        self.path_button.setMinimumSize(QSize(75, 33))
        self.path_button.setMaximumSize(QSize(75, 33))
        self.path_button.setFocusPolicy(Qt.NoFocus)
        self.path_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.path_button)

        self.clear_button = QPushButton(self.vtk_control_buttons)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QSize(75, 33))
        self.clear_button.setMaximumSize(QSize(75, 33))
        self.clear_button.setFocusPolicy(Qt.NoFocus)
        self.clear_button.setStyleSheet(u"")
        self.clear_button.setCheckable(False)

        self.verticalLayout_8.addWidget(self.clear_button)

        self.ortho_button = QPushButton(self.vtk_control_buttons)
        self.mainorthoperspbtnGroup = QButtonGroup(Form)
        self.mainorthoperspbtnGroup.setObjectName(u"mainorthoperspbtnGroup")
        self.mainorthoperspbtnGroup.addButton(self.ortho_button)
        self.ortho_button.setObjectName(u"ortho_button")
        sizePolicy.setHeightForWidth(self.ortho_button.sizePolicy().hasHeightForWidth())
        self.ortho_button.setSizePolicy(sizePolicy)
        self.ortho_button.setMinimumSize(QSize(75, 33))
        self.ortho_button.setMaximumSize(QSize(75, 33))
        self.ortho_button.setFocusPolicy(Qt.NoFocus)
        self.ortho_button.setStyleSheet(u"")
        self.ortho_button.setCheckable(True)
        self.ortho_button.setChecked(True)
        self.ortho_button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.ortho_button)

        self.perspective_button = QPushButton(self.vtk_control_buttons)
        self.mainorthoperspbtnGroup.addButton(self.perspective_button)
        self.perspective_button.setObjectName(u"perspective_button")
        sizePolicy.setHeightForWidth(self.perspective_button.sizePolicy().hasHeightForWidth())
        self.perspective_button.setSizePolicy(sizePolicy)
        self.perspective_button.setMinimumSize(QSize(75, 33))
        self.perspective_button.setMaximumSize(QSize(75, 33))
        self.perspective_button.setFocusPolicy(Qt.NoFocus)
        self.perspective_button.setStyleSheet(u"")
        self.perspective_button.setCheckable(True)
        self.perspective_button.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.perspective_button)


        self.horizontalLayout_10.addWidget(self.vtk_control_buttons)

        self.vtk = VTKBackPlot(self.widget_7)
        self.vtk.setObjectName(u"vtk")
        sizePolicy4.setHeightForWidth(self.vtk.sizePolicy().hasHeightForWidth())
        self.vtk.setSizePolicy(sizePolicy4)
        self.vtk.setStyleSheet(u"VTKBackPlot {\n"
"    border: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"}")
        self.vtk.setProperty(u"backgroundColor", QColor(32, 36, 37))

        self.horizontalLayout_10.addWidget(self.vtk)


        self.horizontalLayout.addWidget(self.widget_7)

        self.tabWidget.addTab(self.main_tab, "")
        self.file_tab = QWidget()
        self.file_tab.setObjectName(u"file_tab")
        self.verticalLayout_5 = QVBoxLayout(self.file_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, 22, 20, 20)
        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setSpacing(15)
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalLayout_120.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.usb_file_frame = QFrame(self.file_tab)
        self.usb_file_frame.setObjectName(u"usb_file_frame")
        self.usb_file_frame.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.usb_file_frame.sizePolicy().hasHeightForWidth())
        self.usb_file_frame.setSizePolicy(sizePolicy8)
        self.usb_file_frame.setMinimumSize(QSize(420, 0))
        self.usb_file_frame.setMaximumSize(QSize(420, 16777215))
        self.usb_file_frame.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.usb_file_frame.setFrameShape(QFrame.StyledPanel)
        self.usb_file_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.usb_file_frame)
        self.verticalLayout_37.setSpacing(9)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalLayout_124.setContentsMargins(5, -1, 5, -1)
        self.device_folder_up_button = QPushButton(self.usb_file_frame)
        self.device_folder_up_button.setObjectName(u"device_folder_up_button")
        sizePolicy.setHeightForWidth(self.device_folder_up_button.sizePolicy().hasHeightForWidth())
        self.device_folder_up_button.setSizePolicy(sizePolicy)
        self.device_folder_up_button.setMinimumSize(QSize(110, 35))
        self.device_folder_up_button.setMaximumSize(QSize(110, 35))
        self.device_folder_up_button.setFocusPolicy(Qt.NoFocus)
        self.device_folder_up_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/images/folder_up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.device_folder_up_button.setIcon(icon7)
        self.device_folder_up_button.setIconSize(QSize(30, 17))

        self.horizontalLayout_124.addWidget(self.device_folder_up_button)

        self.removabledevicecombobox = RemovableDeviceComboBox(self.usb_file_frame)
        self.removabledevicecombobox.setObjectName(u"removabledevicecombobox")
        sizePolicy2.setHeightForWidth(self.removabledevicecombobox.sizePolicy().hasHeightForWidth())
        self.removabledevicecombobox.setSizePolicy(sizePolicy2)
        self.removabledevicecombobox.setMinimumSize(QSize(0, 35))
        self.removabledevicecombobox.setMaximumSize(QSize(16777215, 35))
        self.removabledevicecombobox.setStyleSheet(u"QComboBox::drop-down:button {\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding-left: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_124.addWidget(self.removabledevicecombobox)

        self.device_eject_usb_button = QPushButton(self.usb_file_frame)
        self.device_eject_usb_button.setObjectName(u"device_eject_usb_button")
        sizePolicy.setHeightForWidth(self.device_eject_usb_button.sizePolicy().hasHeightForWidth())
        self.device_eject_usb_button.setSizePolicy(sizePolicy)
        self.device_eject_usb_button.setMinimumSize(QSize(100, 35))
        self.device_eject_usb_button.setMaximumSize(QSize(100, 35))
        self.device_eject_usb_button.setFocusPolicy(Qt.NoFocus)
        self.device_eject_usb_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_124.addWidget(self.device_eject_usb_button)


        self.verticalLayout_37.addLayout(self.horizontalLayout_124)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.filesystemtable_2 = FileSystemTable(self.usb_file_frame)
        self.filesystemtable_2.setObjectName(u"filesystemtable_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.filesystemtable_2.sizePolicy().hasHeightForWidth())
        self.filesystemtable_2.setSizePolicy(sizePolicy9)
        self.filesystemtable_2.setFocusPolicy(Qt.WheelFocus)
        self.filesystemtable_2.setStyleSheet(u"FileSystemTable {\n"
"	color: black;\n"
"   	border: 1px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"	border-radius:none;\n"
"	border-style: none;\n"
"	font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.filesystemtable_2.setAutoScroll(True)
        self.filesystemtable_2.setAutoScrollMargin(20)
        self.filesystemtable_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.filesystemtable_2.setTextElideMode(Qt.ElideRight)
        self.filesystemtable_2.setShowGrid(False)
        self.filesystemtable_2.setSortingEnabled(True)
        self.filesystemtable_2.setProperty(u"fixedNameColumn", True)
        self.filesystemtable_2.setProperty(u"nameColumnsWidth", 250)
        self.filesystemtable_2.horizontalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_125.addWidget(self.filesystemtable_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_125)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setSpacing(12)
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.device_delete_item_button = QPushButton(self.usb_file_frame)
        self.device_delete_item_button.setObjectName(u"device_delete_item_button")
        sizePolicy.setHeightForWidth(self.device_delete_item_button.sizePolicy().hasHeightForWidth())
        self.device_delete_item_button.setSizePolicy(sizePolicy)
        self.device_delete_item_button.setMinimumSize(QSize(100, 35))
        self.device_delete_item_button.setMaximumSize(QSize(100, 35))
        self.device_delete_item_button.setFocusPolicy(Qt.NoFocus)
        self.device_delete_item_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/images/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.device_delete_item_button.setIcon(icon8)
        self.device_delete_item_button.setIconSize(QSize(14, 14))

        self.horizontalLayout_126.addWidget(self.device_delete_item_button)

        self.device_rename_item_button = QPushButton(self.usb_file_frame)
        self.device_rename_item_button.setObjectName(u"device_rename_item_button")
        sizePolicy6.setHeightForWidth(self.device_rename_item_button.sizePolicy().hasHeightForWidth())
        self.device_rename_item_button.setSizePolicy(sizePolicy6)
        self.device_rename_item_button.setMinimumSize(QSize(90, 35))
        self.device_rename_item_button.setMaximumSize(QSize(16777215, 35))
        self.device_rename_item_button.setFocusPolicy(Qt.NoFocus)
        self.device_rename_item_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_126.addWidget(self.device_rename_item_button)

        self.copy_from_usb_2 = QPushButton(self.usb_file_frame)
        self.copy_from_usb_2.setObjectName(u"copy_from_usb_2")
        sizePolicy.setHeightForWidth(self.copy_from_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_from_usb_2.setSizePolicy(sizePolicy)
        self.copy_from_usb_2.setMinimumSize(QSize(100, 35))
        self.copy_from_usb_2.setMaximumSize(QSize(100, 35))
        self.copy_from_usb_2.setFocusPolicy(Qt.NoFocus)
        self.copy_from_usb_2.setLayoutDirection(Qt.RightToLeft)
        self.copy_from_usb_2.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"    padding-right: 4px;\n"
"}")
        self.copy_from_usb_2.setIcon(icon6)

        self.horizontalLayout_126.addWidget(self.copy_from_usb_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_126)


        self.horizontalLayout_120.addWidget(self.usb_file_frame)

        self.main_file_frame = QFrame(self.file_tab)
        self.main_file_frame.setObjectName(u"main_file_frame")
        sizePolicy4.setHeightForWidth(self.main_file_frame.sizePolicy().hasHeightForWidth())
        self.main_file_frame.setSizePolicy(sizePolicy4)
        self.main_file_frame.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.main_file_frame.setFrameShape(QFrame.StyledPanel)
        self.main_file_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.main_file_frame)
        self.verticalLayout_35.setSpacing(9)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.horizontalLayout_121.setContentsMargins(5, -1, 5, -1)
        self.main_folder_up_button = QPushButton(self.main_file_frame)
        self.main_folder_up_button.setObjectName(u"main_folder_up_button")
        sizePolicy.setHeightForWidth(self.main_folder_up_button.sizePolicy().hasHeightForWidth())
        self.main_folder_up_button.setSizePolicy(sizePolicy)
        self.main_folder_up_button.setMinimumSize(QSize(110, 35))
        self.main_folder_up_button.setMaximumSize(QSize(110, 35))
        self.main_folder_up_button.setFocusPolicy(Qt.NoFocus)
        self.main_folder_up_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        self.main_folder_up_button.setIcon(icon7)
        self.main_folder_up_button.setIconSize(QSize(30, 17))

        self.horizontalLayout_121.addWidget(self.main_folder_up_button)

        self.recentfilecombobox_2 = RecentFileComboBox(self.main_file_frame)
        self.recentfilecombobox_2.setObjectName(u"recentfilecombobox_2")
        sizePolicy2.setHeightForWidth(self.recentfilecombobox_2.sizePolicy().hasHeightForWidth())
        self.recentfilecombobox_2.setSizePolicy(sizePolicy2)
        self.recentfilecombobox_2.setMinimumSize(QSize(0, 35))
        self.recentfilecombobox_2.setMaximumSize(QSize(16777215, 35))
        self.recentfilecombobox_2.setStyleSheet(u"QComboBox::drop-down:button {\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding-left: 8px;\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_121.addWidget(self.recentfilecombobox_2)

        self.refresh_folder_button = QPushButton(self.main_file_frame)
        self.refresh_folder_button.setObjectName(u"refresh_folder_button")
        sizePolicy.setHeightForWidth(self.refresh_folder_button.sizePolicy().hasHeightForWidth())
        self.refresh_folder_button.setSizePolicy(sizePolicy)
        self.refresh_folder_button.setMinimumSize(QSize(40, 35))
        self.refresh_folder_button.setMaximumSize(QSize(40, 35))
        self.refresh_folder_button.setFocusPolicy(Qt.NoFocus)
        self.refresh_folder_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/images/cw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_folder_button.setIcon(icon9)
        self.refresh_folder_button.setIconSize(QSize(30, 17))

        self.horizontalLayout_121.addWidget(self.refresh_folder_button)

        self.main_load_gcode_button = QPushButton(self.main_file_frame)
        self.main_load_gcode_button.setObjectName(u"main_load_gcode_button")
        sizePolicy.setHeightForWidth(self.main_load_gcode_button.sizePolicy().hasHeightForWidth())
        self.main_load_gcode_button.setSizePolicy(sizePolicy)
        self.main_load_gcode_button.setMinimumSize(QSize(100, 35))
        self.main_load_gcode_button.setMaximumSize(QSize(100, 35))
        self.main_load_gcode_button.setFocusPolicy(Qt.NoFocus)
        self.main_load_gcode_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_121.addWidget(self.main_load_gcode_button)


        self.verticalLayout_35.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.filesystemtable = FileSystemTable(self.main_file_frame)
        self.filesystemtable.setObjectName(u"filesystemtable")
        self.filesystemtable.setFocusPolicy(Qt.WheelFocus)
        self.filesystemtable.setStyleSheet(u"FileSystemTable {\n"
"	color: black;\n"
"   	border: 1px;\n"
"	border-color: rgb(120, 120, 120);\n"
"	border-style: solid;\n"
"	background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"	color: black;\n"
"    border: none;\n"
"	border-radius:none;\n"
"	border-style: none;\n"
"	font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.filesystemtable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.filesystemtable.setTextElideMode(Qt.ElideRight)
        self.filesystemtable.setShowGrid(False)
        self.filesystemtable.setSortingEnabled(True)
        self.filesystemtable.setProperty(u"fixedNameColumn", True)
        self.filesystemtable.setProperty(u"nameColumnsWidth", 410)
        self.filesystemtable.horizontalHeader().setCascadingSectionResizes(True)
        self.filesystemtable.horizontalHeader().setMinimumSectionSize(18)

        self.horizontalLayout_122.addWidget(self.filesystemtable)


        self.verticalLayout_35.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setSpacing(6)
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.hide_show_usb_button = VCPSettingsPushButton(self.main_file_frame)
        self.hide_show_usb_button.setObjectName(u"hide_show_usb_button")
        self.hide_show_usb_button.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.hide_show_usb_button.sizePolicy().hasHeightForWidth())
        self.hide_show_usb_button.setSizePolicy(sizePolicy6)
        self.hide_show_usb_button.setMinimumSize(QSize(90, 35))
        self.hide_show_usb_button.setMaximumSize(QSize(16777215, 35))
        self.hide_show_usb_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"     background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}")

        self.horizontalLayout_123.addWidget(self.hide_show_usb_button)

        self.copy_to_usb_2 = QPushButton(self.main_file_frame)
        self.copy_to_usb_2.setObjectName(u"copy_to_usb_2")
        sizePolicy6.setHeightForWidth(self.copy_to_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_to_usb_2.setSizePolicy(sizePolicy6)
        self.copy_to_usb_2.setMinimumSize(QSize(90, 35))
        self.copy_to_usb_2.setMaximumSize(QSize(16777215, 35))
        self.copy_to_usb_2.setFocusPolicy(Qt.NoFocus)
        self.copy_to_usb_2.setLayoutDirection(Qt.LeftToRight)
        self.copy_to_usb_2.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"    padding-right: 8px;\n"
"}")
        self.copy_to_usb_2.setIcon(icon4)

        self.horizontalLayout_123.addWidget(self.copy_to_usb_2)

        self.main_delete_item_button = QPushButton(self.main_file_frame)
        self.main_delete_item_button.setObjectName(u"main_delete_item_button")
        sizePolicy6.setHeightForWidth(self.main_delete_item_button.sizePolicy().hasHeightForWidth())
        self.main_delete_item_button.setSizePolicy(sizePolicy6)
        self.main_delete_item_button.setMinimumSize(QSize(90, 35))
        self.main_delete_item_button.setMaximumSize(QSize(16777215, 35))
        self.main_delete_item_button.setFocusPolicy(Qt.NoFocus)
        self.main_delete_item_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        self.main_delete_item_button.setIcon(icon8)
        self.main_delete_item_button.setIconSize(QSize(14, 14))

        self.horizontalLayout_123.addWidget(self.main_delete_item_button)

        self.main_new_file_button = QPushButton(self.main_file_frame)
        self.main_new_file_button.setObjectName(u"main_new_file_button")
        sizePolicy6.setHeightForWidth(self.main_new_file_button.sizePolicy().hasHeightForWidth())
        self.main_new_file_button.setSizePolicy(sizePolicy6)
        self.main_new_file_button.setMinimumSize(QSize(100, 35))
        self.main_new_file_button.setMaximumSize(QSize(16777215, 35))
        self.main_new_file_button.setFocusPolicy(Qt.NoFocus)
        self.main_new_file_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/images/new_file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.main_new_file_button.setIcon(icon10)
        self.main_new_file_button.setIconSize(QSize(12, 16))

        self.horizontalLayout_123.addWidget(self.main_new_file_button)

        self.main_new_folder_button = QPushButton(self.main_file_frame)
        self.main_new_folder_button.setObjectName(u"main_new_folder_button")
        sizePolicy6.setHeightForWidth(self.main_new_folder_button.sizePolicy().hasHeightForWidth())
        self.main_new_folder_button.setSizePolicy(sizePolicy6)
        self.main_new_folder_button.setMinimumSize(QSize(125, 35))
        self.main_new_folder_button.setMaximumSize(QSize(16777215, 35))
        self.main_new_folder_button.setFocusPolicy(Qt.NoFocus)
        self.main_new_folder_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/images/new_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.main_new_folder_button.setIcon(icon11)
        self.main_new_folder_button.setIconSize(QSize(28, 15))

        self.horizontalLayout_123.addWidget(self.main_new_folder_button)

        self.main_rename_item_button = QPushButton(self.main_file_frame)
        self.main_rename_item_button.setObjectName(u"main_rename_item_button")
        sizePolicy6.setHeightForWidth(self.main_rename_item_button.sizePolicy().hasHeightForWidth())
        self.main_rename_item_button.setSizePolicy(sizePolicy6)
        self.main_rename_item_button.setMinimumSize(QSize(90, 35))
        self.main_rename_item_button.setMaximumSize(QSize(16777215, 35))
        self.main_rename_item_button.setFocusPolicy(Qt.NoFocus)
        self.main_rename_item_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_123.addWidget(self.main_rename_item_button)


        self.verticalLayout_35.addLayout(self.horizontalLayout_123)


        self.horizontalLayout_120.addWidget(self.main_file_frame)

        self.frame_36 = QFrame(self.file_tab)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy4.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy4)
        self.frame_36.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_36)
        self.verticalLayout_38.setSpacing(9)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(10, 12, 10, 9)
        self.gcodeeditor_label = QLabel(self.frame_36)
        self.gcodeeditor_label.setObjectName(u"gcodeeditor_label")
        self.gcodeeditor_label.setMinimumSize(QSize(0, 30))
        self.gcodeeditor_label.setMaximumSize(QSize(16777215, 30))
        self.gcodeeditor_label.setStyleSheet(u"font: 16pt \"Bebas Kai\";\n"
"color: white;")
        self.gcodeeditor_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.gcodeeditor_label)

        self.gcodetextedit = GcodeTextEdit(self.frame_36)
        self.gcodetextedit.setObjectName(u"gcodetextedit")
        self.gcodetextedit.setProperty(u"currentLineBackground", QColor(214, 214, 221))
        self.gcodetextedit.setProperty(u"marginBackground", QColor(146, 150, 149))
        self.gcodetextedit.setProperty(u"marginCurrentLineBackground", QColor(110, 110, 110))
        self.gcodetextedit.setProperty(u"marginColor", QColor(49, 49, 49))
        self.gcodetextedit.setProperty(u"marginCurrentLineColor", QColor(255, 255, 255))

        self.verticalLayout_38.addWidget(self.gcodetextedit)

        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.edit_gcode_button = QPushButton(self.frame_36)
        self.edit_gcode_button.setObjectName(u"edit_gcode_button")
        sizePolicy.setHeightForWidth(self.edit_gcode_button.sizePolicy().hasHeightForWidth())
        self.edit_gcode_button.setSizePolicy(sizePolicy)
        self.edit_gcode_button.setMinimumSize(QSize(100, 35))
        self.edit_gcode_button.setMaximumSize(QSize(100, 35))
        self.edit_gcode_button.setFocusPolicy(Qt.NoFocus)
        self.edit_gcode_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")
        self.edit_gcode_button.setCheckable(True)
        self.edit_gcode_button.setChecked(True)

        self.horizontalLayout_129.addWidget(self.edit_gcode_button)

        self.find_replace_button = QPushButton(self.frame_36)
        self.find_replace_button.setObjectName(u"find_replace_button")
        sizePolicy.setHeightForWidth(self.find_replace_button.sizePolicy().hasHeightForWidth())
        self.find_replace_button.setSizePolicy(sizePolicy)
        self.find_replace_button.setMinimumSize(QSize(100, 35))
        self.find_replace_button.setMaximumSize(QSize(100, 35))
        self.find_replace_button.setFocusPolicy(Qt.NoFocus)
        self.find_replace_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_129.addWidget(self.find_replace_button)

        self.save_button = QPushButton(self.frame_36)
        self.save_button.setObjectName(u"save_button")
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QSize(100, 35))
        self.save_button.setMaximumSize(QSize(100, 35))
        self.save_button.setFocusPolicy(Qt.NoFocus)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_129.addWidget(self.save_button)

        self.save_as_button = QPushButton(self.frame_36)
        self.save_as_button.setObjectName(u"save_as_button")
        sizePolicy.setHeightForWidth(self.save_as_button.sizePolicy().hasHeightForWidth())
        self.save_as_button.setSizePolicy(sizePolicy)
        self.save_as_button.setMinimumSize(QSize(100, 35))
        self.save_as_button.setMaximumSize(QSize(100, 35))
        self.save_as_button.setFocusPolicy(Qt.NoFocus)
        self.save_as_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_129.addWidget(self.save_as_button)

        self.undo_button = QPushButton(self.frame_36)
        self.undo_button.setObjectName(u"undo_button")
        sizePolicy.setHeightForWidth(self.undo_button.sizePolicy().hasHeightForWidth())
        self.undo_button.setSizePolicy(sizePolicy)
        self.undo_button.setMinimumSize(QSize(100, 35))
        self.undo_button.setMaximumSize(QSize(100, 35))
        self.undo_button.setFocusPolicy(Qt.NoFocus)
        self.undo_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_129.addWidget(self.undo_button)


        self.verticalLayout_38.addLayout(self.horizontalLayout_129)


        self.horizontalLayout_120.addWidget(self.frame_36)


        self.verticalLayout_5.addLayout(self.horizontalLayout_120)

        self.tabWidget.addTab(self.file_tab, "")
        self.atc_tab = QWidget()
        self.atc_tab.setObjectName(u"atc_tab")
        self.horizontalLayout_36 = QHBoxLayout(self.atc_tab)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 9)
        self.atc_layout = QVBoxLayout()
        self.atc_layout.setObjectName(u"atc_layout")

        self.horizontalLayout_36.addLayout(self.atc_layout)

        self.tabWidget.addTab(self.atc_tab, "")
        self.tool_tab = QWidget()
        self.tool_tab.setObjectName(u"tool_tab")
        self.horizontalLayout_41 = QHBoxLayout(self.tool_tab)
        self.horizontalLayout_41.setSpacing(12)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(20, 22, 20, 20)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.tool_tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setSpacing(9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(16, 20, 16, -1)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, -1)
        self.tool_table = ToolTable(self.frame_13)
        self.tool_table.setObjectName(u"tool_table")
        sizePolicy9.setHeightForWidth(self.tool_table.sizePolicy().hasHeightForWidth())
        self.tool_table.setSizePolicy(sizePolicy9)
        palette1 = QPalette()
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush7)
        brush8 = QBrush(QColor(120, 120, 120, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush8)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush8)
        brush9 = QBrush(QColor(90, 90, 90, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush8)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush7)
#endif
        self.tool_table.setPalette(palette1)
        self.tool_table.setFont(font7)
        self.tool_table.setTabletTracking(False)
        self.tool_table.setFocusPolicy(Qt.NoFocus)
        self.tool_table.setFrameShape(QFrame.StyledPanel)
        self.tool_table.setFrameShadow(QFrame.Sunken)
        self.tool_table.setLineWidth(3)
        self.tool_table.setMidLineWidth(3)
        self.tool_table.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tool_table.setProperty(u"showDropIndicator", True)
        self.tool_table.setAlternatingRowColors(True)
        self.tool_table.setShowGrid(True)
        self.tool_table.setGridStyle(Qt.SolidLine)
        self.tool_table.setSortingEnabled(True)
        self.tool_table.setProperty(u"currentToolColor", QColor(255, 255, 255))
        self.tool_table.setProperty(u"currentToolBackground", QColor(93, 95, 239))
        self.tool_table.horizontalHeader().setMinimumSectionSize(90)
        self.tool_table.horizontalHeader().setDefaultSectionSize(90)
        self.tool_table.horizontalHeader().setHighlightSections(False)
        self.tool_table.horizontalHeader().setStretchLastSection(True)
        self.tool_table.verticalHeader().setVisible(False)
        self.tool_table.verticalHeader().setCascadingSectionResizes(True)
        self.tool_table.verticalHeader().setMinimumSectionSize(35)
        self.tool_table.verticalHeader().setDefaultSectionSize(35)
        self.tool_table.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_38.addWidget(self.tool_table)


        self.verticalLayout_20.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.tool_table_delete_button = QPushButton(self.frame_13)
        self.tool_table_delete_button.setObjectName(u"tool_table_delete_button")
        sizePolicy.setHeightForWidth(self.tool_table_delete_button.sizePolicy().hasHeightForWidth())
        self.tool_table_delete_button.setSizePolicy(sizePolicy)
        self.tool_table_delete_button.setMinimumSize(QSize(160, 33))
        self.tool_table_delete_button.setMaximumSize(QSize(120, 33))
        self.tool_table_delete_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_delete_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_delete_button)

        self.tool_table_add_tool_button = QPushButton(self.frame_13)
        self.tool_table_add_tool_button.setObjectName(u"tool_table_add_tool_button")
        sizePolicy.setHeightForWidth(self.tool_table_add_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_add_tool_button.setSizePolicy(sizePolicy)
        self.tool_table_add_tool_button.setMinimumSize(QSize(160, 33))
        self.tool_table_add_tool_button.setMaximumSize(QSize(120, 33))
        self.tool_table_add_tool_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_add_tool_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_add_tool_button)

        self.tool_table_save_button = QPushButton(self.frame_13)
        self.tool_table_save_button.setObjectName(u"tool_table_save_button")
        sizePolicy.setHeightForWidth(self.tool_table_save_button.sizePolicy().hasHeightForWidth())
        self.tool_table_save_button.setSizePolicy(sizePolicy)
        self.tool_table_save_button.setMinimumSize(QSize(160, 33))
        self.tool_table_save_button.setMaximumSize(QSize(120, 33))
        self.tool_table_save_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_save_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_save_button)

        self.tool_table_reload_button = QPushButton(self.frame_13)
        self.tool_table_reload_button.setObjectName(u"tool_table_reload_button")
        sizePolicy.setHeightForWidth(self.tool_table_reload_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reload_button.setSizePolicy(sizePolicy)
        self.tool_table_reload_button.setMinimumSize(QSize(160, 33))
        self.tool_table_reload_button.setMaximumSize(QSize(140, 33))
        self.tool_table_reload_button.setFocusPolicy(Qt.NoFocus)
        self.tool_table_reload_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_37.addWidget(self.tool_table_reload_button)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)


        self.verticalLayout_19.addWidget(self.frame_13)


        self.horizontalLayout_41.addLayout(self.verticalLayout_19)

        self.widget_56 = QWidget(self.tool_tab)
        self.widget_56.setObjectName(u"widget_56")

        self.horizontalLayout_41.addWidget(self.widget_56)

        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.tool_tab)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setMinimumSize(QSize(0, 58))
        self.frame_28.setMaximumSize(QSize(16777215, 58))
        self.frame_28.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_108 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setSpacing(3)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_56 = QLabel(self.frame_28)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(60, 33))
        self.label_56.setMaximumSize(QSize(60, 33))
        self.label_56.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.label_56.setWordWrap(True)

        self.horizontalLayout_109.addWidget(self.label_56)

        self.tool_length_7 = StatusLabel(self.frame_28)
        self.tool_length_7.setObjectName(u"tool_length_7")
        sizePolicy1.setHeightForWidth(self.tool_length_7.sizePolicy().hasHeightForWidth())
        self.tool_length_7.setSizePolicy(sizePolicy1)
        self.tool_length_7.setMinimumSize(QSize(70, 33))
        self.tool_length_7.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_length_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tool_length_7.setIndent(4)

        self.horizontalLayout_109.addWidget(self.tool_length_7)


        self.horizontalLayout_108.addLayout(self.horizontalLayout_109)


        self.verticalLayout_73.addWidget(self.frame_28)

        self.widget_10 = QWidget(self.tool_tab)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy5.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy5)
        self.widget_10.setMinimumSize(QSize(580, 0))
        self.widget_10.setStyleSheet(u"QFrame{\n"
"border-style: none;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.label_43 = QLabel(self.widget_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(45, 16, 250, 403))
        self.label_43.setStyleSheet(u"image: url(:/images/atc_spindle_tool_dimensioned.png);")
        self.label_43.setPixmap(QPixmap(u":/images/atc_spindle_tool_dimensioned.png"))
        self.label_43.setScaledContents(True)
        self.frame_11 = QFrame(self.widget_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(4, 205, 145, 60))
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QSize(100, 60))
        self.frame_11.setMaximumSize(QSize(16777215, 58))
        self.frame_11.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_98 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QSize(48, 33))
        self.label_48.setMaximumSize(QSize(48, 33))
        self.label_48.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_48.setAlignment(Qt.AlignCenter)
        self.label_48.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_48)

        self.tool_length_5 = StatusLabel(self.frame_11)
        self.tool_length_5.setObjectName(u"tool_length_5")
        sizePolicy4.setHeightForWidth(self.tool_length_5.sizePolicy().hasHeightForWidth())
        self.tool_length_5.setSizePolicy(sizePolicy4)
        self.tool_length_5.setMinimumSize(QSize(70, 33))
        self.tool_length_5.setMaximumSize(QSize(70, 33))
        self.tool_length_5.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_length_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.tool_length_5)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_17)

        self.frame_12 = QFrame(self.widget_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(30, 384, 132, 60))
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QSize(100, 60))
        self.frame_12.setMaximumSize(QSize(16777215, 60))
        self.frame_12.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_99 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_49 = QLabel(self.frame_12)
        self.label_49.setObjectName(u"label_49")
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setMinimumSize(QSize(35, 33))
        self.label_49.setMaximumSize(QSize(35, 33))
        self.label_49.setStyleSheet(u"QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_49.setAlignment(Qt.AlignCenter)
        self.label_49.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.label_49)

        self.tool_diameter_2 = StatusLabel(self.frame_12)
        self.tool_diameter_2.setObjectName(u"tool_diameter_2")
        sizePolicy4.setHeightForWidth(self.tool_diameter_2.sizePolicy().hasHeightForWidth())
        self.tool_diameter_2.setSizePolicy(sizePolicy4)
        self.tool_diameter_2.setMinimumSize(QSize(70, 33))
        self.tool_diameter_2.setMaximumSize(QSize(70, 33))
        self.tool_diameter_2.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_diameter_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.tool_diameter_2)


        self.horizontalLayout_99.addLayout(self.horizontalLayout_18)

        self.tool_length_6 = StatusLabel(self.widget_10)
        self.tool_length_6.setObjectName(u"tool_length_6")
        self.tool_length_6.setGeometry(QRect(180, 165, 50, 33))
        sizePolicy4.setHeightForWidth(self.tool_length_6.sizePolicy().hasHeightForWidth())
        self.tool_length_6.setSizePolicy(sizePolicy4)
        self.tool_length_6.setMinimumSize(QSize(50, 33))
        self.tool_length_6.setMaximumSize(QSize(50, 33))
        self.tool_length_6.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.tool_length_6.setAlignment(Qt.AlignCenter)
        self.frame_17 = QFrame(self.widget_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(320, 18, 250, 250))
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QSize(250, 250))
        self.frame_17.setMaximumSize(QSize(250, 250))
        self.frame_17.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(51, 57, 59);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.verticalLayout_49 = QVBoxLayout(self.frame_17)
        self.verticalLayout_49.setSpacing(5)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(6, -1, 6, 7)
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 2, 0, 2)
        self.machine_column_header_7 = QLabel(self.frame_17)
        self.machine_column_header_7.setObjectName(u"machine_column_header_7")
        self.machine_column_header_7.setMinimumSize(QSize(0, 45))
        self.machine_column_header_7.setMaximumSize(QSize(16777215, 45))
        self.machine_column_header_7.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_78.addWidget(self.machine_column_header_7)


        self.verticalLayout_49.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setSpacing(9)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_79.setContentsMargins(4, 2, 2, 2)
        self.load_spindle_tool_number_2 = VCPLineEdit(self.frame_17)
        self.load_spindle_tool_number_2.setObjectName(u"load_spindle_tool_number_2")
        sizePolicy2.setHeightForWidth(self.load_spindle_tool_number_2.sizePolicy().hasHeightForWidth())
        self.load_spindle_tool_number_2.setSizePolicy(sizePolicy2)
        self.load_spindle_tool_number_2.setMinimumSize(QSize(60, 43))
        self.load_spindle_tool_number_2.setMaximumSize(QSize(16777215, 43))
        self.load_spindle_tool_number_2.setFocusPolicy(Qt.ClickFocus)
        self.load_spindle_tool_number_2.setStyleSheet(u"font: 16pt;")
        self.load_spindle_tool_number_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_79.addWidget(self.load_spindle_tool_number_2)

        self.load_spindle_button_2 = SubCallButton(self.frame_17)
        self.load_spindle_button_2.setObjectName(u"load_spindle_button_2")
        sizePolicy1.setHeightForWidth(self.load_spindle_button_2.sizePolicy().hasHeightForWidth())
        self.load_spindle_button_2.setSizePolicy(sizePolicy1)
        self.load_spindle_button_2.setMinimumSize(QSize(120, 45))
        self.load_spindle_button_2.setMaximumSize(QSize(16777215, 45))
        self.load_spindle_button_2.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_79.addWidget(self.load_spindle_button_2)


        self.verticalLayout_49.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_80.setContentsMargins(2, 2, 2, 2)
        self.remove_tool_2 = SubCallButton(self.frame_17)
        self.remove_tool_2.setObjectName(u"remove_tool_2")
        self.remove_tool_2.setMinimumSize(QSize(125, 45))
        self.remove_tool_2.setMaximumSize(QSize(16777215, 45))
        self.remove_tool_2.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_80.addWidget(self.remove_tool_2)


        self.verticalLayout_49.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_145 = QHBoxLayout()
        self.horizontalLayout_145.setSpacing(9)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(4, 2, 2, 2)
        self.tool_number_entry_tool_page = VCPLineEdit(self.frame_17)
        self.tool_number_entry_tool_page.setObjectName(u"tool_number_entry_tool_page")
        sizePolicy2.setHeightForWidth(self.tool_number_entry_tool_page.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_tool_page.setSizePolicy(sizePolicy2)
        self.tool_number_entry_tool_page.setMinimumSize(QSize(60, 43))
        self.tool_number_entry_tool_page.setMaximumSize(QSize(16777215, 43))
        self.tool_number_entry_tool_page.setSizeIncrement(QSize(0, 40))
        palette2 = QPalette()
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush7)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush10)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush7)
        brush11 = QBrush(QColor(65, 84, 255, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush11)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush7)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush7)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush10)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush10)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        self.tool_number_entry_tool_page.setPalette(palette2)
        font8 = QFont()
        font8.setFamilies([u"Bebas Kai"])
        font8.setPointSize(16)
        font8.setBold(False)
        font8.setItalic(False)
        self.tool_number_entry_tool_page.setFont(font8)
        self.tool_number_entry_tool_page.setFocusPolicy(Qt.ClickFocus)
        self.tool_number_entry_tool_page.setContextMenuPolicy(Qt.NoContextMenu)
        self.tool_number_entry_tool_page.setStyleSheet(u"font: 16pt;")
        self.tool_number_entry_tool_page.setFrame(True)
        self.tool_number_entry_tool_page.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_145.addWidget(self.tool_number_entry_tool_page)

        self.m6_tool_call_button_tool_page = SubCallButton(self.frame_17)
        self.m6_tool_call_button_tool_page.setObjectName(u"m6_tool_call_button_tool_page")
        self.m6_tool_call_button_tool_page.setMinimumSize(QSize(120, 45))
        self.m6_tool_call_button_tool_page.setMaximumSize(QSize(16777215, 45))
        self.m6_tool_call_button_tool_page.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_145.addWidget(self.m6_tool_call_button_tool_page)


        self.verticalLayout_49.addLayout(self.horizontalLayout_145)

        self.frame_18 = QFrame(self.widget_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(320, 298, 250, 150))
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy10)
        self.frame_18.setMinimumSize(QSize(250, 150))
        self.frame_18.setMaximumSize(QSize(250, 150))
        self.frame_18.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(51, 57, 59);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.verticalLayout_53 = QVBoxLayout(self.frame_18)
        self.verticalLayout_53.setSpacing(5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(6, -1, 6, 6)
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 2, 0, 2)
        self.machine_column_header_8 = QLabel(self.frame_18)
        self.machine_column_header_8.setObjectName(u"machine_column_header_8")
        self.machine_column_header_8.setMinimumSize(QSize(0, 45))
        self.machine_column_header_8.setMaximumSize(QSize(16777215, 45))
        self.machine_column_header_8.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_82.addWidget(self.machine_column_header_8)


        self.verticalLayout_53.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(2, 2, 2, 2)
        self.tool_touch_off_button = SubCallButton(self.frame_18)
        self.tool_touch_off_button.setObjectName(u"tool_touch_off_button")
        self.tool_touch_off_button.setMinimumSize(QSize(145, 45))
        self.tool_touch_off_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_100.addWidget(self.tool_touch_off_button)


        self.verticalLayout_53.addLayout(self.horizontalLayout_100)


        self.verticalLayout_73.addWidget(self.widget_10)

        self.mdi_entry_box_4 = MDIEntry(self.tool_tab)
        self.mdi_entry_box_4.setObjectName(u"mdi_entry_box_4")
        sizePolicy1.setHeightForWidth(self.mdi_entry_box_4.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_4.setSizePolicy(sizePolicy1)
        self.mdi_entry_box_4.setMinimumSize(QSize(0, 40))
        self.mdi_entry_box_4.setMaximumSize(QSize(16777215, 40))
        self.mdi_entry_box_4.setFont(font7)
        self.mdi_entry_box_4.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_73.addWidget(self.mdi_entry_box_4)


        self.horizontalLayout_41.addLayout(self.verticalLayout_73)

        self.tabWidget.addTab(self.tool_tab, "")
        self.offsets_tab = QWidget()
        self.offsets_tab.setObjectName(u"offsets_tab")
        self.horizontalLayout_8 = QHBoxLayout(self.offsets_tab)
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 22, 20, 20)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(30)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(0, -1, 0, 1)
        self.frame_37 = QFrame(self.offsets_tab)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy4.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy4)
        self.frame_37.setMinimumSize(QSize(796, 0))
        self.frame_37.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.frame_37)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(16, 12, 16, 0)
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(-1, 0, -1, 0)
        self.offset_table = OffsetTable(self.frame_37)
        self.offset_table.setObjectName(u"offset_table")
        sizePolicy6.setHeightForWidth(self.offset_table.sizePolicy().hasHeightForWidth())
        self.offset_table.setSizePolicy(sizePolicy6)
        self.offset_table.setMinimumSize(QSize(0, 426))
        self.offset_table.setMaximumSize(QSize(16777215, 428))
        self.offset_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.offset_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.offset_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.offset_table.setAutoScroll(False)
        self.offset_table.setAutoScrollMargin(0)
        self.offset_table.setWordWrap(False)
        self.offset_table.setCornerButtonEnabled(False)
        self.offset_table.setProperty(u"currentRowColor", QColor(255, 255, 255))
        self.offset_table.setProperty(u"currentRowBackground", QColor(93, 95, 239))
        self.offset_table.horizontalHeader().setCascadingSectionResizes(False)
        self.offset_table.horizontalHeader().setMinimumSectionSize(118)
        self.offset_table.horizontalHeader().setDefaultSectionSize(118)
        self.offset_table.horizontalHeader().setHighlightSections(False)
        self.offset_table.horizontalHeader().setStretchLastSection(True)
        self.offset_table.verticalHeader().setMinimumSectionSize(43)
        self.offset_table.verticalHeader().setDefaultSectionSize(43)
        self.offset_table.verticalHeader().setHighlightSections(False)
        self.offset_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_47.addWidget(self.offset_table)


        self.verticalLayout_39.addLayout(self.horizontalLayout_47)

        self.widget = QWidget(self.frame_37)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_130 = QHBoxLayout(self.widget)
        self.horizontalLayout_130.setSpacing(10)
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.horizontalLayout_130.setContentsMargins(-1, 1, -1, 1)
        self.offset_table_clear_selected_button = QPushButton(self.widget)
        self.offset_table_clear_selected_button.setObjectName(u"offset_table_clear_selected_button")
        sizePolicy.setHeightForWidth(self.offset_table_clear_selected_button.sizePolicy().hasHeightForWidth())
        self.offset_table_clear_selected_button.setSizePolicy(sizePolicy)
        self.offset_table_clear_selected_button.setMinimumSize(QSize(100, 33))
        self.offset_table_clear_selected_button.setMaximumSize(QSize(150, 33))
        self.offset_table_clear_selected_button.setFocusPolicy(Qt.NoFocus)
        self.offset_table_clear_selected_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_130.addWidget(self.offset_table_clear_selected_button)

        self.offset_table_clear_all_button = QPushButton(self.widget)
        self.offset_table_clear_all_button.setObjectName(u"offset_table_clear_all_button")
        sizePolicy.setHeightForWidth(self.offset_table_clear_all_button.sizePolicy().hasHeightForWidth())
        self.offset_table_clear_all_button.setSizePolicy(sizePolicy)
        self.offset_table_clear_all_button.setMinimumSize(QSize(100, 33))
        self.offset_table_clear_all_button.setMaximumSize(QSize(150, 33))
        self.offset_table_clear_all_button.setFocusPolicy(Qt.NoFocus)
        self.offset_table_clear_all_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_130.addWidget(self.offset_table_clear_all_button)

        self.offset_table_save_button = QPushButton(self.widget)
        self.offset_table_save_button.setObjectName(u"offset_table_save_button")
        sizePolicy.setHeightForWidth(self.offset_table_save_button.sizePolicy().hasHeightForWidth())
        self.offset_table_save_button.setSizePolicy(sizePolicy)
        self.offset_table_save_button.setMinimumSize(QSize(100, 33))
        self.offset_table_save_button.setMaximumSize(QSize(150, 33))
        self.offset_table_save_button.setFocusPolicy(Qt.NoFocus)
        self.offset_table_save_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_130.addWidget(self.offset_table_save_button)

        self.offset_table_reload_button = QPushButton(self.widget)
        self.offset_table_reload_button.setObjectName(u"offset_table_reload_button")
        sizePolicy.setHeightForWidth(self.offset_table_reload_button.sizePolicy().hasHeightForWidth())
        self.offset_table_reload_button.setSizePolicy(sizePolicy)
        self.offset_table_reload_button.setMinimumSize(QSize(100, 33))
        self.offset_table_reload_button.setMaximumSize(QSize(150, 33))
        self.offset_table_reload_button.setFocusPolicy(Qt.NoFocus)
        self.offset_table_reload_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_130.addWidget(self.offset_table_reload_button)


        self.verticalLayout_39.addWidget(self.widget)


        self.verticalLayout_11.addWidget(self.frame_37)

        self.mdi_entry_box_6 = MDIEntry(self.offsets_tab)
        self.mdi_entry_box_6.setObjectName(u"mdi_entry_box_6")
        sizePolicy2.setHeightForWidth(self.mdi_entry_box_6.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_6.setSizePolicy(sizePolicy2)
        self.mdi_entry_box_6.setMinimumSize(QSize(0, 40))
        self.mdi_entry_box_6.setMaximumSize(QSize(16777215, 40))
        self.mdi_entry_box_6.setFont(font7)
        self.mdi_entry_box_6.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_11.addWidget(self.mdi_entry_box_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_11)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.offsets_tab)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(800, 16777215))
        self.frame_15.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setSpacing(15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(12, 12, 12, 12)
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_12.setHorizontalSpacing(50)
        self.gridLayout_12.setVerticalSpacing(12)
        self.gridLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.machine_column_header_4 = QLabel(self.frame_15)
        self.machine_column_header_4.setObjectName(u"machine_column_header_4")
        sizePolicy6.setHeightForWidth(self.machine_column_header_4.sizePolicy().hasHeightForWidth())
        self.machine_column_header_4.setSizePolicy(sizePolicy6)
        self.machine_column_header_4.setMinimumSize(QSize(0, 55))
        self.machine_column_header_4.setMaximumSize(QSize(16777215, 55))
        self.machine_column_header_4.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(90, 90, 90);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.machine_column_header_4, 0, 0, 1, 5)

        self.actionbutton_g54_2 = ActionButton(self.frame_15)
        self.actionbutton_g54_2.setObjectName(u"actionbutton_g54_2")
        self.actionbutton_g54_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g54_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g54_2.setSizePolicy(sizePolicy)
        self.actionbutton_g54_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g54_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g54_2.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g54_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g54_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g54_2, 1, 0, 1, 1)

        self.actionbutton_g55_2 = ActionButton(self.frame_15)
        self.actionbutton_g55_2.setObjectName(u"actionbutton_g55_2")
        self.actionbutton_g55_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g55_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g55_2.setSizePolicy(sizePolicy)
        self.actionbutton_g55_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g55_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g55_2.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g55_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g55_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g55_2, 1, 1, 1, 1)

        self.actionbutton_g56_2 = ActionButton(self.frame_15)
        self.actionbutton_g56_2.setObjectName(u"actionbutton_g56_2")
        self.actionbutton_g56_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g56_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g56_2.setSizePolicy(sizePolicy)
        self.actionbutton_g56_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g56_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g56_2.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g56_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g56_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g56_2, 1, 2, 1, 1)

        self.actionbutton_g57_2 = ActionButton(self.frame_15)
        self.actionbutton_g57_2.setObjectName(u"actionbutton_g57_2")
        self.actionbutton_g57_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g57_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g57_2.setSizePolicy(sizePolicy)
        self.actionbutton_g57_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g57_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g57_2.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g57_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g57_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g57_2, 1, 3, 1, 1)

        self.actionbutton_g58_2 = ActionButton(self.frame_15)
        self.actionbutton_g58_2.setObjectName(u"actionbutton_g58_2")
        self.actionbutton_g58_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g58_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g58_2.setSizePolicy(sizePolicy)
        self.actionbutton_g58_2.setMinimumSize(QSize(110, 38))
        self.actionbutton_g58_2.setMaximumSize(QSize(110, 38))
        self.actionbutton_g58_2.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g58_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g58_2.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g58_2, 1, 4, 1, 1)

        self.actionbutton_g59_4 = ActionButton(self.frame_15)
        self.actionbutton_g59_4.setObjectName(u"actionbutton_g59_4")
        self.actionbutton_g59_4.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_4.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_4.setSizePolicy(sizePolicy)
        self.actionbutton_g59_4.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_4.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_4.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_4.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_4.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_4, 2, 1, 1, 1)

        self.actionbutton_g59_5 = ActionButton(self.frame_15)
        self.actionbutton_g59_5.setObjectName(u"actionbutton_g59_5")
        self.actionbutton_g59_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_5.setSizePolicy(sizePolicy)
        self.actionbutton_g59_5.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_5.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_5.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_5.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_5.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_5, 2, 2, 1, 1)

        self.actionbutton_g59_6 = ActionButton(self.frame_15)
        self.actionbutton_g59_6.setObjectName(u"actionbutton_g59_6")
        self.actionbutton_g59_6.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_6.setSizePolicy(sizePolicy)
        self.actionbutton_g59_6.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_6.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_6.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_6.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_6.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_6, 2, 3, 1, 1)

        self.actionbutton_g59_7 = ActionButton(self.frame_15)
        self.actionbutton_g59_7.setObjectName(u"actionbutton_g59_7")
        self.actionbutton_g59_7.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_7.setSizePolicy(sizePolicy)
        self.actionbutton_g59_7.setMinimumSize(QSize(110, 38))
        self.actionbutton_g59_7.setMaximumSize(QSize(110, 38))
        self.actionbutton_g59_7.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_7.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_7.setAutoExclusive(True)

        self.gridLayout_12.addWidget(self.actionbutton_g59_7, 2, 4, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_12)

        self.widget_68 = QWidget(self.frame_15)
        self.widget_68.setObjectName(u"widget_68")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(1)
        sizePolicy11.setHeightForWidth(self.widget_68.sizePolicy().hasHeightForWidth())
        self.widget_68.setSizePolicy(sizePolicy11)
        self.widget_68.setMinimumSize(QSize(0, 10))

        self.verticalLayout_33.addWidget(self.widget_68)

        self.frame_32 = QFrame(self.frame_15)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy6.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy6)
        self.frame_32.setMaximumSize(QSize(16777215, 70))
        self.frame_32.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_32)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, -1, 11, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.axis_column_header_9 = QLabel(self.frame_32)
        self.axis_column_header_9.setObjectName(u"axis_column_header_9")
        sizePolicy1.setHeightForWidth(self.axis_column_header_9.sizePolicy().hasHeightForWidth())
        self.axis_column_header_9.setSizePolicy(sizePolicy1)
        self.axis_column_header_9.setMinimumSize(QSize(55, 50))
        self.axis_column_header_9.setMaximumSize(QSize(55, 50))
        self.axis_column_header_9.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_9.setAlignment(Qt.AlignCenter)
        self.axis_column_header_9.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.axis_column_header_9)

        self.axis_column_header_10 = QLabel(self.frame_32)
        self.axis_column_header_10.setObjectName(u"axis_column_header_10")
        sizePolicy1.setHeightForWidth(self.axis_column_header_10.sizePolicy().hasHeightForWidth())
        self.axis_column_header_10.setSizePolicy(sizePolicy1)
        self.axis_column_header_10.setMinimumSize(QSize(45, 50))
        self.axis_column_header_10.setMaximumSize(QSize(45, 50))
        self.axis_column_header_10.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_10.setAlignment(Qt.AlignCenter)
        self.axis_column_header_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.axis_column_header_10)

        self.machine_column_header_10 = QLabel(self.frame_32)
        self.machine_column_header_10.setObjectName(u"machine_column_header_10")
        sizePolicy1.setHeightForWidth(self.machine_column_header_10.sizePolicy().hasHeightForWidth())
        self.machine_column_header_10.setSizePolicy(sizePolicy1)
        self.machine_column_header_10.setMinimumSize(QSize(88, 50))
        self.machine_column_header_10.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_10.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_10.setAlignment(Qt.AlignCenter)
        self.machine_column_header_10.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_10)

        self.machine_column_header_11 = QLabel(self.frame_32)
        self.machine_column_header_11.setObjectName(u"machine_column_header_11")
        sizePolicy1.setHeightForWidth(self.machine_column_header_11.sizePolicy().hasHeightForWidth())
        self.machine_column_header_11.setSizePolicy(sizePolicy1)
        self.machine_column_header_11.setMinimumSize(QSize(85, 50))
        self.machine_column_header_11.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_11.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_11.setAlignment(Qt.AlignCenter)
        self.machine_column_header_11.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_11)

        self.machine_column_header_12 = QLabel(self.frame_32)
        self.machine_column_header_12.setObjectName(u"machine_column_header_12")
        sizePolicy1.setHeightForWidth(self.machine_column_header_12.sizePolicy().hasHeightForWidth())
        self.machine_column_header_12.setSizePolicy(sizePolicy1)
        self.machine_column_header_12.setMinimumSize(QSize(60, 50))
        self.machine_column_header_12.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_12.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_12.setAlignment(Qt.AlignCenter)
        self.machine_column_header_12.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_12)

        self.ref_coilumn_header_4 = QLabel(self.frame_32)
        self.ref_coilumn_header_4.setObjectName(u"ref_coilumn_header_4")
        sizePolicy6.setHeightForWidth(self.ref_coilumn_header_4.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_4.setSizePolicy(sizePolicy6)
        self.ref_coilumn_header_4.setMinimumSize(QSize(65, 50))
        self.ref_coilumn_header_4.setMaximumSize(QSize(16777215, 50))
        self.ref_coilumn_header_4.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_4.setAlignment(Qt.AlignCenter)
        self.ref_coilumn_header_4.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.ref_coilumn_header_4)

        self.machine_column_header_13 = QLabel(self.frame_32)
        self.machine_column_header_13.setObjectName(u"machine_column_header_13")
        sizePolicy1.setHeightForWidth(self.machine_column_header_13.sizePolicy().hasHeightForWidth())
        self.machine_column_header_13.setSizePolicy(sizePolicy1)
        self.machine_column_header_13.setMinimumSize(QSize(65, 50))
        self.machine_column_header_13.setMaximumSize(QSize(16777215, 50))
        self.machine_column_header_13.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_13.setAlignment(Qt.AlignCenter)
        self.machine_column_header_13.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.machine_column_header_13)


        self.verticalLayout_34.addLayout(self.horizontalLayout_7)


        self.verticalLayout_33.addWidget(self.frame_32)

        self.offset_dro_layout = QVBoxLayout()
        self.offset_dro_layout.setObjectName(u"offset_dro_layout")
        self.offset_dro_layout.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_33.addLayout(self.offset_dro_layout)


        self.horizontalLayout_51.addWidget(self.frame_15)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_51)

        self.tabWidget.addTab(self.offsets_tab, "")
        self.probe_tab = QWidget()
        self.probe_tab.setObjectName(u"probe_tab")
        self.horizontalLayout_43 = QHBoxLayout(self.probe_tab)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.tabWidget_2 = QTabWidget(self.probe_tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(300, 0))
        self.tabWidget_2.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab{\n"
"    margin-top: 0px;\n"
"    margin-right: 6px;\n"
"    margin-bottom:0px;\n"
"    min-width: 35px;\n"
"    min-height: 220px;\n"
"    font: 16pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-top: 50px;\n"
"    border-left-width: 2px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 2px;\n"
"    border-top-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.tabWidget_2.setTabPosition(QTabWidget.East)
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_22 = QHBoxLayout(self.tab)
        self.horizontalLayout_22.setSpacing(9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.tab)
        self.widget_44.setObjectName(u"widget_44")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(1)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.widget_44.sizePolicy().hasHeightForWidth())
        self.widget_44.setSizePolicy(sizePolicy12)
        self.widget_44.setMinimumSize(QSize(530, 0))
        self.widget_44.setMaximumSize(QSize(530, 16777215))
        self.widget_44.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.widget_44)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 6, 6, 10)
        self.label_81 = QLabel(self.widget_44)
        self.label_81.setObjectName(u"label_81")
        sizePolicy6.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy6)
        self.label_81.setMinimumSize(QSize(0, 30))
        self.label_81.setMaximumSize(QSize(16777215, 30))
        self.label_81.setFont(font2)
        self.label_81.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_81.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_81.setIndent(10)

        self.verticalLayout_41.addWidget(self.label_81)

        self.widget_15 = QWidget(self.widget_44)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(112, 90))
        self.widget_15.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_16 = QVBoxLayout(self.widget_15)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 0, 9, 0)
        self.horizontalWidget = QWidget(self.widget_15)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.horizontalWidget.setMinimumSize(QSize(440, 0))
        self.horizontalLayout_45 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_45.setSpacing(9)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(1, 1, 1, 1)
        self.actionbutton_19 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup = QButtonGroup(Form)
        self.probepagewcsbtnGroup.setObjectName(u"probepagewcsbtnGroup")
        self.probepagewcsbtnGroup.addButton(self.actionbutton_19)
        self.actionbutton_19.setObjectName(u"actionbutton_19")
        sizePolicy.setHeightForWidth(self.actionbutton_19.sizePolicy().hasHeightForWidth())
        self.actionbutton_19.setSizePolicy(sizePolicy)
        self.actionbutton_19.setMinimumSize(QSize(75, 38))
        self.actionbutton_19.setMaximumSize(QSize(70, 38))
        self.actionbutton_19.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_19.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_19.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_19)

        self.actionbutton_20 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_20)
        self.actionbutton_20.setObjectName(u"actionbutton_20")
        sizePolicy.setHeightForWidth(self.actionbutton_20.sizePolicy().hasHeightForWidth())
        self.actionbutton_20.setSizePolicy(sizePolicy)
        self.actionbutton_20.setMinimumSize(QSize(75, 38))
        self.actionbutton_20.setMaximumSize(QSize(70, 38))
        self.actionbutton_20.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_20.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_20.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_20)

        self.actionbutton_21 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_21)
        self.actionbutton_21.setObjectName(u"actionbutton_21")
        sizePolicy.setHeightForWidth(self.actionbutton_21.sizePolicy().hasHeightForWidth())
        self.actionbutton_21.setSizePolicy(sizePolicy)
        self.actionbutton_21.setMinimumSize(QSize(75, 38))
        self.actionbutton_21.setMaximumSize(QSize(70, 38))
        self.actionbutton_21.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_21.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_21.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_21)

        self.actionbutton_26 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_26)
        self.actionbutton_26.setObjectName(u"actionbutton_26")
        sizePolicy.setHeightForWidth(self.actionbutton_26.sizePolicy().hasHeightForWidth())
        self.actionbutton_26.setSizePolicy(sizePolicy)
        self.actionbutton_26.setMinimumSize(QSize(75, 38))
        self.actionbutton_26.setMaximumSize(QSize(70, 38))
        self.actionbutton_26.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_26.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_26.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_26)

        self.actionbutton_24 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_24)
        self.actionbutton_24.setObjectName(u"actionbutton_24")
        sizePolicy.setHeightForWidth(self.actionbutton_24.sizePolicy().hasHeightForWidth())
        self.actionbutton_24.setSizePolicy(sizePolicy)
        self.actionbutton_24.setMinimumSize(QSize(75, 38))
        self.actionbutton_24.setMaximumSize(QSize(70, 38))
        self.actionbutton_24.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_24.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_24.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_24)

        self.actionbutton_22 = ActionButton(self.horizontalWidget)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_22)
        self.actionbutton_22.setObjectName(u"actionbutton_22")
        sizePolicy.setHeightForWidth(self.actionbutton_22.sizePolicy().hasHeightForWidth())
        self.actionbutton_22.setSizePolicy(sizePolicy)
        self.actionbutton_22.setMinimumSize(QSize(75, 38))
        self.actionbutton_22.setMaximumSize(QSize(70, 38))
        self.actionbutton_22.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_22.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_22.setAutoExclusive(True)

        self.horizontalLayout_45.addWidget(self.actionbutton_22)


        self.verticalLayout_16.addWidget(self.horizontalWidget)

        self.horizontalWidget_2 = QWidget(self.widget_15)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        sizePolicy1.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy1)
        self.horizontalWidget_2.setMinimumSize(QSize(440, 0))
        self.horizontalLayout_46 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_46.setSpacing(9)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(1, 1, 1, 1)
        self.actionbutton_27 = ActionButton(self.horizontalWidget_2)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_27)
        self.actionbutton_27.setObjectName(u"actionbutton_27")
        sizePolicy.setHeightForWidth(self.actionbutton_27.sizePolicy().hasHeightForWidth())
        self.actionbutton_27.setSizePolicy(sizePolicy)
        self.actionbutton_27.setMinimumSize(QSize(75, 38))
        self.actionbutton_27.setMaximumSize(QSize(70, 38))
        self.actionbutton_27.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_27.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_27.setAutoExclusive(True)

        self.horizontalLayout_46.addWidget(self.actionbutton_27)

        self.actionbutton_25 = ActionButton(self.horizontalWidget_2)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_25)
        self.actionbutton_25.setObjectName(u"actionbutton_25")
        sizePolicy.setHeightForWidth(self.actionbutton_25.sizePolicy().hasHeightForWidth())
        self.actionbutton_25.setSizePolicy(sizePolicy)
        self.actionbutton_25.setMinimumSize(QSize(75, 38))
        self.actionbutton_25.setMaximumSize(QSize(70, 38))
        self.actionbutton_25.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_25.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_25.setAutoExclusive(True)

        self.horizontalLayout_46.addWidget(self.actionbutton_25)

        self.actionbutton_23 = ActionButton(self.horizontalWidget_2)
        self.probepagewcsbtnGroup.addButton(self.actionbutton_23)
        self.actionbutton_23.setObjectName(u"actionbutton_23")
        sizePolicy.setHeightForWidth(self.actionbutton_23.sizePolicy().hasHeightForWidth())
        self.actionbutton_23.setSizePolicy(sizePolicy)
        self.actionbutton_23.setMinimumSize(QSize(75, 38))
        self.actionbutton_23.setMaximumSize(QSize(70, 38))
        self.actionbutton_23.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_23.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_23.setAutoExclusive(True)

        self.horizontalLayout_46.addWidget(self.actionbutton_23)

        self.probe_posn_only_Btn = VCPSettingsPushButton(self.horizontalWidget_2)
        self.probe_posn_only_Btn.setObjectName(u"probe_posn_only_Btn")
        self.probe_posn_only_Btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.probe_posn_only_Btn.sizePolicy().hasHeightForWidth())
        self.probe_posn_only_Btn.setSizePolicy(sizePolicy)
        self.probe_posn_only_Btn.setMinimumSize(QSize(243, 38))
        self.probe_posn_only_Btn.setMaximumSize(QSize(243, 38))
        self.probe_posn_only_Btn.setStyleSheet(u"font: 15pt \"Bebas Kai\";")

        self.horizontalLayout_46.addWidget(self.probe_posn_only_Btn)


        self.verticalLayout_16.addWidget(self.horizontalWidget_2)


        self.verticalLayout_41.addWidget(self.widget_15)

        self.widget_76 = QWidget(self.widget_44)
        self.widget_76.setObjectName(u"widget_76")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_64.setSpacing(1)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.widget_76)
        self.label_82.setObjectName(u"label_82")
        sizePolicy6.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy6)
        self.label_82.setMinimumSize(QSize(0, 27))
        self.label_82.setMaximumSize(QSize(16777215, 27))
        self.label_82.setFont(font2)
        self.label_82.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_82.setIndent(10)

        self.horizontalLayout_64.addWidget(self.label_82)


        self.verticalLayout_41.addWidget(self.widget_76)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, 9, -1)
        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.horizontalLayout_154.setContentsMargins(-1, 1, -1, 1)
        self.ref_coilumn_header_19 = QLabel(self.widget_44)
        self.ref_coilumn_header_19.setObjectName(u"ref_coilumn_header_19")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_19.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_19.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_19.setStyleSheet(u"")
        self.ref_coilumn_header_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_154.addWidget(self.ref_coilumn_header_19)

        self.label_83 = QLabel(self.widget_44)
        self.label_83.setObjectName(u"label_83")
        sizePolicy.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy)
        self.label_83.setMinimumSize(QSize(140, 31))
        self.label_83.setMaximumSize(QSize(150, 31))
        self.label_83.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_83.setLineWidth(0)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_83.setIndent(0)

        self.horizontalLayout_154.addWidget(self.label_83)

        self.probe_tool_number_3014 = VCPSettingsLineEdit(self.widget_44)
        self.probe_tool_number_3014.setObjectName(u"probe_tool_number_3014")
        sizePolicy.setHeightForWidth(self.probe_tool_number_3014.sizePolicy().hasHeightForWidth())
        self.probe_tool_number_3014.setSizePolicy(sizePolicy)
        self.probe_tool_number_3014.setMinimumSize(QSize(100, 31))
        self.probe_tool_number_3014.setMaximumSize(QSize(100, 31))
        self.probe_tool_number_3014.setFocusPolicy(Qt.ClickFocus)
        self.probe_tool_number_3014.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_154.addWidget(self.probe_tool_number_3014)

        self.label_86 = QLabel(self.widget_44)
        self.label_86.setObjectName(u"label_86")
        sizePolicy.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy)
        self.label_86.setMinimumSize(QSize(140, 31))
        self.label_86.setMaximumSize(QSize(140, 31))
        self.label_86.setBaseSize(QSize(140, 30))
        self.label_86.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_86.setLineWidth(0)
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_86.setIndent(0)

        self.horizontalLayout_154.addWidget(self.label_86)

        self.probe_slow_fr_3015 = VCPSettingsLineEdit(self.widget_44)
        self.probe_slow_fr_3015.setObjectName(u"probe_slow_fr_3015")
        sizePolicy.setHeightForWidth(self.probe_slow_fr_3015.sizePolicy().hasHeightForWidth())
        self.probe_slow_fr_3015.setSizePolicy(sizePolicy)
        self.probe_slow_fr_3015.setMinimumSize(QSize(100, 31))
        self.probe_slow_fr_3015.setMaximumSize(QSize(100, 31))
        self.probe_slow_fr_3015.setFocusPolicy(Qt.ClickFocus)
        self.probe_slow_fr_3015.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_154.addWidget(self.probe_slow_fr_3015)


        self.verticalLayout_22.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(-1, 1, -1, 1)
        self.ref_coilumn_header_20 = QLabel(self.widget_44)
        self.ref_coilumn_header_20.setObjectName(u"ref_coilumn_header_20")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_20.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_20.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_20.setStyleSheet(u"")
        self.ref_coilumn_header_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_155.addWidget(self.ref_coilumn_header_20)

        self.label_94 = QLabel(self.widget_44)
        self.label_94.setObjectName(u"label_94")
        sizePolicy.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy)
        self.label_94.setMinimumSize(QSize(140, 31))
        self.label_94.setMaximumSize(QSize(140, 31))
        self.label_94.setBaseSize(QSize(140, 30))
        self.label_94.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_94.setLineWidth(0)
        self.label_94.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_94.setIndent(0)

        self.horizontalLayout_155.addWidget(self.label_94)

        self.probe_traverse_fr_3017 = VCPSettingsLineEdit(self.widget_44)
        self.probe_traverse_fr_3017.setObjectName(u"probe_traverse_fr_3017")
        sizePolicy.setHeightForWidth(self.probe_traverse_fr_3017.sizePolicy().hasHeightForWidth())
        self.probe_traverse_fr_3017.setSizePolicy(sizePolicy)
        self.probe_traverse_fr_3017.setMinimumSize(QSize(100, 31))
        self.probe_traverse_fr_3017.setMaximumSize(QSize(100, 31))
        self.probe_traverse_fr_3017.setFocusPolicy(Qt.ClickFocus)
        self.probe_traverse_fr_3017.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_155.addWidget(self.probe_traverse_fr_3017)

        self.label_85 = QLabel(self.widget_44)
        self.label_85.setObjectName(u"label_85")
        sizePolicy.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy)
        self.label_85.setMinimumSize(QSize(140, 31))
        self.label_85.setMaximumSize(QSize(150, 31))
        self.label_85.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_85.setLineWidth(0)
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_85.setIndent(0)

        self.horizontalLayout_155.addWidget(self.label_85)

        self.probe_fast_fr_3016 = VCPSettingsLineEdit(self.widget_44)
        self.probe_fast_fr_3016.setObjectName(u"probe_fast_fr_3016")
        sizePolicy.setHeightForWidth(self.probe_fast_fr_3016.sizePolicy().hasHeightForWidth())
        self.probe_fast_fr_3016.setSizePolicy(sizePolicy)
        self.probe_fast_fr_3016.setMinimumSize(QSize(100, 31))
        self.probe_fast_fr_3016.setMaximumSize(QSize(100, 31))
        self.probe_fast_fr_3016.setFocusPolicy(Qt.ClickFocus)
        self.probe_fast_fr_3016.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_155.addWidget(self.probe_fast_fr_3016)


        self.verticalLayout_22.addLayout(self.horizontalLayout_155)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(-1, 1, -1, 1)
        self.ref_coilumn_header_21 = QLabel(self.widget_44)
        self.ref_coilumn_header_21.setObjectName(u"ref_coilumn_header_21")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_21.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_21.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_21.setStyleSheet(u"")
        self.ref_coilumn_header_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_156.addWidget(self.ref_coilumn_header_21)

        self.label_87 = QLabel(self.widget_44)
        self.label_87.setObjectName(u"label_87")
        sizePolicy.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy)
        self.label_87.setMinimumSize(QSize(140, 31))
        self.label_87.setMaximumSize(QSize(150, 31))
        self.label_87.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_87.setLineWidth(0)
        self.label_87.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_87.setIndent(0)

        self.horizontalLayout_156.addWidget(self.label_87)

        self.max_xy_distance_3018 = VCPSettingsLineEdit(self.widget_44)
        self.max_xy_distance_3018.setObjectName(u"max_xy_distance_3018")
        sizePolicy.setHeightForWidth(self.max_xy_distance_3018.sizePolicy().hasHeightForWidth())
        self.max_xy_distance_3018.setSizePolicy(sizePolicy)
        self.max_xy_distance_3018.setMinimumSize(QSize(100, 31))
        self.max_xy_distance_3018.setMaximumSize(QSize(100, 31))
        self.max_xy_distance_3018.setFocusPolicy(Qt.ClickFocus)
        self.max_xy_distance_3018.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.max_xy_distance_3018)

        self.label_88 = QLabel(self.widget_44)
        self.label_88.setObjectName(u"label_88")
        sizePolicy.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy)
        self.label_88.setMinimumSize(QSize(140, 31))
        self.label_88.setMaximumSize(QSize(140, 31))
        self.label_88.setBaseSize(QSize(140, 30))
        self.label_88.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_88.setLineWidth(0)
        self.label_88.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_88.setIndent(0)

        self.horizontalLayout_156.addWidget(self.label_88)

        self.xy_clearance_3019 = VCPSettingsLineEdit(self.widget_44)
        self.xy_clearance_3019.setObjectName(u"xy_clearance_3019")
        sizePolicy.setHeightForWidth(self.xy_clearance_3019.sizePolicy().hasHeightForWidth())
        self.xy_clearance_3019.setSizePolicy(sizePolicy)
        self.xy_clearance_3019.setMinimumSize(QSize(100, 31))
        self.xy_clearance_3019.setMaximumSize(QSize(100, 31))
        self.xy_clearance_3019.setFocusPolicy(Qt.ClickFocus)
        self.xy_clearance_3019.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_156.addWidget(self.xy_clearance_3019)


        self.verticalLayout_22.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(-1, 1, -1, 1)
        self.ref_coilumn_header_22 = QLabel(self.widget_44)
        self.ref_coilumn_header_22.setObjectName(u"ref_coilumn_header_22")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_22.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_22.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_22.setStyleSheet(u"")
        self.ref_coilumn_header_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_157.addWidget(self.ref_coilumn_header_22)

        self.label_90 = QLabel(self.widget_44)
        self.label_90.setObjectName(u"label_90")
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        self.label_90.setMinimumSize(QSize(140, 31))
        self.label_90.setMaximumSize(QSize(150, 31))
        self.label_90.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_90.setLineWidth(0)
        self.label_90.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_90.setIndent(0)

        self.horizontalLayout_157.addWidget(self.label_90)

        self.max_z_distance_3020 = VCPSettingsLineEdit(self.widget_44)
        self.max_z_distance_3020.setObjectName(u"max_z_distance_3020")
        sizePolicy.setHeightForWidth(self.max_z_distance_3020.sizePolicy().hasHeightForWidth())
        self.max_z_distance_3020.setSizePolicy(sizePolicy)
        self.max_z_distance_3020.setMinimumSize(QSize(100, 31))
        self.max_z_distance_3020.setMaximumSize(QSize(100, 31))
        self.max_z_distance_3020.setFocusPolicy(Qt.ClickFocus)
        self.max_z_distance_3020.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_157.addWidget(self.max_z_distance_3020)

        self.label_91 = QLabel(self.widget_44)
        self.label_91.setObjectName(u"label_91")
        sizePolicy.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy)
        self.label_91.setMinimumSize(QSize(140, 31))
        self.label_91.setMaximumSize(QSize(140, 31))
        self.label_91.setBaseSize(QSize(140, 30))
        self.label_91.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_91.setLineWidth(0)
        self.label_91.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_91.setIndent(0)

        self.horizontalLayout_157.addWidget(self.label_91)

        self.z_clearance_3021 = VCPSettingsLineEdit(self.widget_44)
        self.z_clearance_3021.setObjectName(u"z_clearance_3021")
        sizePolicy.setHeightForWidth(self.z_clearance_3021.sizePolicy().hasHeightForWidth())
        self.z_clearance_3021.setSizePolicy(sizePolicy)
        self.z_clearance_3021.setMinimumSize(QSize(100, 31))
        self.z_clearance_3021.setMaximumSize(QSize(100, 31))
        self.z_clearance_3021.setFocusPolicy(Qt.ClickFocus)
        self.z_clearance_3021.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_157.addWidget(self.z_clearance_3021)


        self.verticalLayout_22.addLayout(self.horizontalLayout_157)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.horizontalLayout_158.setContentsMargins(1, 1, 1, 1)
        self.ref_coilumn_header_23 = QLabel(self.widget_44)
        self.ref_coilumn_header_23.setObjectName(u"ref_coilumn_header_23")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_23.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_23.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_23.setStyleSheet(u"")
        self.ref_coilumn_header_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_158.addWidget(self.ref_coilumn_header_23)

        self.label_92 = QLabel(self.widget_44)
        self.label_92.setObjectName(u"label_92")
        sizePolicy.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy)
        self.label_92.setMinimumSize(QSize(140, 31))
        self.label_92.setMaximumSize(QSize(150, 31))
        self.label_92.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_92.setLineWidth(0)
        self.label_92.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_92.setIndent(0)

        self.horizontalLayout_158.addWidget(self.label_92)

        self.extra_probe_depth_3022 = VCPSettingsLineEdit(self.widget_44)
        self.extra_probe_depth_3022.setObjectName(u"extra_probe_depth_3022")
        sizePolicy.setHeightForWidth(self.extra_probe_depth_3022.sizePolicy().hasHeightForWidth())
        self.extra_probe_depth_3022.setSizePolicy(sizePolicy)
        self.extra_probe_depth_3022.setMinimumSize(QSize(100, 31))
        self.extra_probe_depth_3022.setMaximumSize(QSize(100, 31))
        self.extra_probe_depth_3022.setFocusPolicy(Qt.ClickFocus)
        self.extra_probe_depth_3022.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_158.addWidget(self.extra_probe_depth_3022)

        self.label_84 = QLabel(self.widget_44)
        self.label_84.setObjectName(u"label_84")
        sizePolicy.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy)
        self.label_84.setMinimumSize(QSize(140, 31))
        self.label_84.setMaximumSize(QSize(140, 31))
        self.label_84.setBaseSize(QSize(140, 30))
        self.label_84.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_84.setLineWidth(0)
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_84.setIndent(0)

        self.horizontalLayout_158.addWidget(self.label_84)

        self.step_off_width_3023 = VCPSettingsLineEdit(self.widget_44)
        self.step_off_width_3023.setObjectName(u"step_off_width_3023")
        sizePolicy.setHeightForWidth(self.step_off_width_3023.sizePolicy().hasHeightForWidth())
        self.step_off_width_3023.setSizePolicy(sizePolicy)
        self.step_off_width_3023.setMinimumSize(QSize(100, 31))
        self.step_off_width_3023.setMaximumSize(QSize(100, 31))
        self.step_off_width_3023.setFocusPolicy(Qt.ClickFocus)
        self.step_off_width_3023.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_158.addWidget(self.step_off_width_3023)


        self.verticalLayout_22.addLayout(self.horizontalLayout_158)


        self.verticalLayout_41.addLayout(self.verticalLayout_22)

        self.widget_19 = QWidget(self.widget_44)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy6.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy6)
        self.widget_19.setMinimumSize(QSize(0, 33))
        self.widget_19.setMaximumSize(QSize(16777215, 33))
        self.horizontalLayout_57 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_57.setSpacing(1)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.update_probe_parameters_btn = SubCallButton(self.widget_19)
        self.update_probe_parameters_btn.setObjectName(u"update_probe_parameters_btn")
        sizePolicy6.setHeightForWidth(self.update_probe_parameters_btn.sizePolicy().hasHeightForWidth())
        self.update_probe_parameters_btn.setSizePolicy(sizePolicy6)
        self.update_probe_parameters_btn.setMinimumSize(QSize(150, 27))
        self.update_probe_parameters_btn.setMaximumSize(QSize(16777215, 27))
        self.update_probe_parameters_btn.setFocusPolicy(Qt.NoFocus)
        self.update_probe_parameters_btn.setStyleSheet(u"SubCallButton{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"	font: 14pt \"Bebas Kai\";\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 13"
                        "5, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_57.addWidget(self.update_probe_parameters_btn)

        self.reset_all_data = SubCallButton(self.widget_19)
        self.reset_all_data.setObjectName(u"reset_all_data")
        sizePolicy.setHeightForWidth(self.reset_all_data.sizePolicy().hasHeightForWidth())
        self.reset_all_data.setSizePolicy(sizePolicy)
        self.reset_all_data.setMinimumSize(QSize(120, 27))
        self.reset_all_data.setMaximumSize(QSize(120, 27))
        self.reset_all_data.setFocusPolicy(Qt.NoFocus)
        self.reset_all_data.setStyleSheet(u".SubCallButton{\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"	font: 14pt \"Bebas Kai\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:"
                        "pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_57.addWidget(self.reset_all_data)

        self.x_data_reset1 = SubCallButton(self.widget_19)
        self.x_data_reset1.setObjectName(u"x_data_reset1")
        sizePolicy.setHeightForWidth(self.x_data_reset1.sizePolicy().hasHeightForWidth())
        self.x_data_reset1.setSizePolicy(sizePolicy)
        self.x_data_reset1.setMinimumSize(QSize(110, 27))
        self.x_data_reset1.setMaximumSize(QSize(110, 27))
        self.x_data_reset1.setFocusPolicy(Qt.NoFocus)
        self.x_data_reset1.setStyleSheet(u".SubCallButton{\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"	font: 14pt \"Bebas Kai\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:"
                        "pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_57.addWidget(self.x_data_reset1)

        self.y_data_reset1 = SubCallButton(self.widget_19)
        self.y_data_reset1.setObjectName(u"y_data_reset1")
        sizePolicy.setHeightForWidth(self.y_data_reset1.sizePolicy().hasHeightForWidth())
        self.y_data_reset1.setSizePolicy(sizePolicy)
        self.y_data_reset1.setMinimumSize(QSize(110, 27))
        self.y_data_reset1.setMaximumSize(QSize(110, 27))
        self.y_data_reset1.setFocusPolicy(Qt.NoFocus)
        self.y_data_reset1.setStyleSheet(u"SubCallButton{\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"	font: 14pt \"Bebas Kai\";\n"
"  	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pa"
                        "d, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_57.addWidget(self.y_data_reset1)


        self.verticalLayout_41.addWidget(self.widget_19)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 0, 9, 3)
        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.horizontalLayout_160.setContentsMargins(1, 1, 1, 1)
        self.label_108 = QLabel(self.widget_44)
        self.label_108.setObjectName(u"label_108")
        sizePolicy6.setHeightForWidth(self.label_108.sizePolicy().hasHeightForWidth())
        self.label_108.setSizePolicy(sizePolicy6)
        self.label_108.setMinimumSize(QSize(0, 31))
        self.label_108.setMaximumSize(QSize(16777215, 31))
        self.label_108.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_108.setFrameShape(QFrame.NoFrame)
        self.label_108.setLineWidth(0)
        self.label_108.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_108.setIndent(0)

        self.horizontalLayout_160.addWidget(self.label_108)

        self.x_minus_probed_position = StatusLabel(self.widget_44)
        self.x_minus_probed_position.setObjectName(u"x_minus_probed_position")
        sizePolicy.setHeightForWidth(self.x_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.x_minus_probed_position.setSizePolicy(sizePolicy)
        self.x_minus_probed_position.setMinimumSize(QSize(80, 31))
        self.x_minus_probed_position.setMaximumSize(QSize(80, 31))
        self.x_minus_probed_position.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_minus_probed_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_160.addWidget(self.x_minus_probed_position)

        self.label_98 = QLabel(self.widget_44)
        self.label_98.setObjectName(u"label_98")
        sizePolicy.setHeightForWidth(self.label_98.sizePolicy().hasHeightForWidth())
        self.label_98.setSizePolicy(sizePolicy)
        self.label_98.setMinimumSize(QSize(80, 31))
        self.label_98.setMaximumSize(QSize(80, 31))
        self.label_98.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_98.setFrameShape(QFrame.NoFrame)
        self.label_98.setLineWidth(0)
        self.label_98.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_98.setIndent(0)

        self.horizontalLayout_160.addWidget(self.label_98)

        self.x_plus_probed_position = StatusLabel(self.widget_44)
        self.x_plus_probed_position.setObjectName(u"x_plus_probed_position")
        sizePolicy.setHeightForWidth(self.x_plus_probed_position.sizePolicy().hasHeightForWidth())
        self.x_plus_probed_position.setSizePolicy(sizePolicy)
        self.x_plus_probed_position.setMinimumSize(QSize(80, 31))
        self.x_plus_probed_position.setMaximumSize(QSize(80, 31))
        self.x_plus_probed_position.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_plus_probed_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_160.addWidget(self.x_plus_probed_position)

        self.label_97 = QLabel(self.widget_44)
        self.label_97.setObjectName(u"label_97")
        sizePolicy.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy)
        self.label_97.setMinimumSize(QSize(80, 31))
        self.label_97.setMaximumSize(QSize(80, 31))
        self.label_97.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_97.setLineWidth(0)
        self.label_97.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_97.setIndent(0)

        self.horizontalLayout_160.addWidget(self.label_97)

        self.x_probed_width = StatusLabel(self.widget_44)
        self.x_probed_width.setObjectName(u"x_probed_width")
        sizePolicy.setHeightForWidth(self.x_probed_width.sizePolicy().hasHeightForWidth())
        self.x_probed_width.setSizePolicy(sizePolicy)
        self.x_probed_width.setMinimumSize(QSize(80, 31))
        self.x_probed_width.setMaximumSize(QSize(80, 31))
        self.x_probed_width.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_probed_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_160.addWidget(self.x_probed_width)


        self.verticalLayout_42.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(1, 1, 1, 1)
        self.label_109 = QLabel(self.widget_44)
        self.label_109.setObjectName(u"label_109")
        sizePolicy6.setHeightForWidth(self.label_109.sizePolicy().hasHeightForWidth())
        self.label_109.setSizePolicy(sizePolicy6)
        self.label_109.setMinimumSize(QSize(0, 31))
        self.label_109.setMaximumSize(QSize(16777215, 31))
        self.label_109.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_109.setLineWidth(0)
        self.label_109.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_109.setIndent(0)

        self.horizontalLayout_29.addWidget(self.label_109)

        self.y_minus_probed_position = StatusLabel(self.widget_44)
        self.y_minus_probed_position.setObjectName(u"y_minus_probed_position")
        sizePolicy.setHeightForWidth(self.y_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.y_minus_probed_position.setSizePolicy(sizePolicy)
        self.y_minus_probed_position.setMinimumSize(QSize(80, 31))
        self.y_minus_probed_position.setMaximumSize(QSize(80, 31))
        self.y_minus_probed_position.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.y_minus_probed_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.y_minus_probed_position)

        self.label_101 = QLabel(self.widget_44)
        self.label_101.setObjectName(u"label_101")
        sizePolicy.setHeightForWidth(self.label_101.sizePolicy().hasHeightForWidth())
        self.label_101.setSizePolicy(sizePolicy)
        self.label_101.setMinimumSize(QSize(80, 31))
        self.label_101.setMaximumSize(QSize(80, 31))
        self.label_101.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_101.setLineWidth(0)
        self.label_101.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_101.setIndent(0)

        self.horizontalLayout_29.addWidget(self.label_101)

        self.y_plus_probed_position = StatusLabel(self.widget_44)
        self.y_plus_probed_position.setObjectName(u"y_plus_probed_position")
        sizePolicy.setHeightForWidth(self.y_plus_probed_position.sizePolicy().hasHeightForWidth())
        self.y_plus_probed_position.setSizePolicy(sizePolicy)
        self.y_plus_probed_position.setMinimumSize(QSize(80, 31))
        self.y_plus_probed_position.setMaximumSize(QSize(80, 31))
        self.y_plus_probed_position.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.y_plus_probed_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.y_plus_probed_position)

        self.label_100 = QLabel(self.widget_44)
        self.label_100.setObjectName(u"label_100")
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setMinimumSize(QSize(80, 31))
        self.label_100.setMaximumSize(QSize(80, 31))
        self.label_100.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_100.setLineWidth(0)
        self.label_100.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_100.setIndent(0)

        self.horizontalLayout_29.addWidget(self.label_100)

        self.y_probed_width = StatusLabel(self.widget_44)
        self.y_probed_width.setObjectName(u"y_probed_width")
        sizePolicy.setHeightForWidth(self.y_probed_width.sizePolicy().hasHeightForWidth())
        self.y_probed_width.setSizePolicy(sizePolicy)
        self.y_probed_width.setMinimumSize(QSize(80, 31))
        self.y_probed_width.setMaximumSize(QSize(80, 31))
        self.y_probed_width.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.y_probed_width.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.y_probed_width)


        self.verticalLayout_42.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.horizontalLayout_161.setContentsMargins(1, 1, 1, 1)
        self.label_110 = QLabel(self.widget_44)
        self.label_110.setObjectName(u"label_110")
        sizePolicy6.setHeightForWidth(self.label_110.sizePolicy().hasHeightForWidth())
        self.label_110.setSizePolicy(sizePolicy6)
        self.label_110.setMinimumSize(QSize(0, 31))
        self.label_110.setMaximumSize(QSize(16777215, 31))
        self.label_110.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_110.setLineWidth(0)
        self.label_110.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_110.setIndent(0)

        self.horizontalLayout_161.addWidget(self.label_110)

        self.z_minus_probed_position = StatusLabel(self.widget_44)
        self.z_minus_probed_position.setObjectName(u"z_minus_probed_position")
        sizePolicy.setHeightForWidth(self.z_minus_probed_position.sizePolicy().hasHeightForWidth())
        self.z_minus_probed_position.setSizePolicy(sizePolicy)
        self.z_minus_probed_position.setMinimumSize(QSize(80, 31))
        self.z_minus_probed_position.setMaximumSize(QSize(80, 31))
        self.z_minus_probed_position.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.z_minus_probed_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.z_minus_probed_position.setMargin(2)

        self.horizontalLayout_161.addWidget(self.z_minus_probed_position)

        self.label_102 = QLabel(self.widget_44)
        self.label_102.setObjectName(u"label_102")
        sizePolicy.setHeightForWidth(self.label_102.sizePolicy().hasHeightForWidth())
        self.label_102.setSizePolicy(sizePolicy)
        self.label_102.setMinimumSize(QSize(80, 31))
        self.label_102.setMaximumSize(QSize(80, 31))
        self.label_102.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_102.setLineWidth(0)
        self.label_102.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_102.setIndent(0)

        self.horizontalLayout_161.addWidget(self.label_102)

        self.averaged_diam = StatusLabel(self.widget_44)
        self.averaged_diam.setObjectName(u"averaged_diam")
        sizePolicy.setHeightForWidth(self.averaged_diam.sizePolicy().hasHeightForWidth())
        self.averaged_diam.setSizePolicy(sizePolicy)
        self.averaged_diam.setMinimumSize(QSize(80, 31))
        self.averaged_diam.setMaximumSize(QSize(80, 31))
        self.averaged_diam.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.averaged_diam.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_161.addWidget(self.averaged_diam)

        self.label_113 = QLabel(self.widget_44)
        self.label_113.setObjectName(u"label_113")
        sizePolicy.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy)
        self.label_113.setMinimumSize(QSize(80, 31))
        self.label_113.setMaximumSize(QSize(80, 31))
        self.label_113.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_113.setLineWidth(0)
        self.label_113.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_113.setIndent(0)

        self.horizontalLayout_161.addWidget(self.label_113)

        self.x_center_probed = StatusLabel(self.widget_44)
        self.x_center_probed.setObjectName(u"x_center_probed")
        sizePolicy.setHeightForWidth(self.x_center_probed.sizePolicy().hasHeightForWidth())
        self.x_center_probed.setSizePolicy(sizePolicy)
        self.x_center_probed.setMinimumSize(QSize(80, 31))
        self.x_center_probed.setMaximumSize(QSize(80, 31))
        self.x_center_probed.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_center_probed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.x_center_probed.setMargin(2)

        self.horizontalLayout_161.addWidget(self.x_center_probed)


        self.verticalLayout_42.addLayout(self.horizontalLayout_161)

        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.horizontalLayout_162.setContentsMargins(1, 1, 1, 1)
        self.label_99 = QLabel(self.widget_44)
        self.label_99.setObjectName(u"label_99")
        sizePolicy6.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy6)
        self.label_99.setMinimumSize(QSize(0, 31))
        self.label_99.setMaximumSize(QSize(16777215, 31))
        self.label_99.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_99.setLineWidth(0)
        self.label_99.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_99.setIndent(0)

        self.horizontalLayout_162.addWidget(self.label_99)

        self.edge_delta = StatusLabel(self.widget_44)
        self.edge_delta.setObjectName(u"edge_delta")
        sizePolicy.setHeightForWidth(self.edge_delta.sizePolicy().hasHeightForWidth())
        self.edge_delta.setSizePolicy(sizePolicy)
        self.edge_delta.setMinimumSize(QSize(80, 31))
        self.edge_delta.setMaximumSize(QSize(80, 31))
        self.edge_delta.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.edge_delta.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_162.addWidget(self.edge_delta)

        self.label_96 = QLabel(self.widget_44)
        self.label_96.setObjectName(u"label_96")
        sizePolicy.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy)
        self.label_96.setMinimumSize(QSize(80, 31))
        self.label_96.setMaximumSize(QSize(80, 31))
        self.label_96.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_96.setLineWidth(0)
        self.label_96.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_96.setIndent(0)

        self.horizontalLayout_162.addWidget(self.label_96)

        self.edge_angle = StatusLabel(self.widget_44)
        self.edge_angle.setObjectName(u"edge_angle")
        sizePolicy.setHeightForWidth(self.edge_angle.sizePolicy().hasHeightForWidth())
        self.edge_angle.setSizePolicy(sizePolicy)
        self.edge_angle.setMinimumSize(QSize(80, 31))
        self.edge_angle.setMaximumSize(QSize(80, 31))
        self.edge_angle.setMouseTracking(True)
        self.edge_angle.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.edge_angle.setTextFormat(Qt.RichText)
        self.edge_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_162.addWidget(self.edge_angle)

        self.label_114 = QLabel(self.widget_44)
        self.label_114.setObjectName(u"label_114")
        sizePolicy.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy)
        self.label_114.setMinimumSize(QSize(80, 31))
        self.label_114.setMaximumSize(QSize(80, 31))
        self.label_114.setStyleSheet(u"QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_114.setLineWidth(0)
        self.label_114.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_114.setIndent(0)

        self.horizontalLayout_162.addWidget(self.label_114)

        self.y_center_probed = StatusLabel(self.widget_44)
        self.y_center_probed.setObjectName(u"y_center_probed")
        sizePolicy.setHeightForWidth(self.y_center_probed.sizePolicy().hasHeightForWidth())
        self.y_center_probed.setSizePolicy(sizePolicy)
        self.y_center_probed.setMinimumSize(QSize(80, 31))
        self.y_center_probed.setMaximumSize(QSize(80, 31))
        self.y_center_probed.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(134, 136, 138);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.y_center_probed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.y_center_probed.setMargin(2)

        self.horizontalLayout_162.addWidget(self.y_center_probed)


        self.verticalLayout_42.addLayout(self.horizontalLayout_162)


        self.verticalLayout_41.addLayout(self.verticalLayout_42)

        self.mdi_entry_box_5 = MDIEntry(self.widget_44)
        self.mdi_entry_box_5.setObjectName(u"mdi_entry_box_5")
        self.mdi_entry_box_5.setMinimumSize(QSize(0, 40))
        self.mdi_entry_box_5.setMaximumSize(QSize(16777215, 40))
        self.mdi_entry_box_5.setFont(font7)
        self.mdi_entry_box_5.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_41.addWidget(self.mdi_entry_box_5)


        self.horizontalLayout_22.addWidget(self.widget_44)

        self.widget_13 = QWidget(self.tab)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_45 = QVBoxLayout(self.widget_13)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.probe_group_select = QWidget(self.widget_13)
        self.probe_group_select.setObjectName(u"probe_group_select")
        self.probe_group_select.setStyleSheet(u"QWidget {\n"
"    font: 13pt \"bebas kai\";\n"
"}")
        self.horizontalLayout_30 = QHBoxLayout(self.probe_group_select)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(20, 3, 20, 6)
        self.outside_corners = QPushButton(self.probe_group_select)
        self.probetabGroup = QButtonGroup(Form)
        self.probetabGroup.setObjectName(u"probetabGroup")
        self.probetabGroup.addButton(self.outside_corners)
        self.outside_corners.setObjectName(u"outside_corners")
        self.outside_corners.setFocusPolicy(Qt.NoFocus)
        self.outside_corners.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 2px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.outside_corners.setCheckable(True)
        self.outside_corners.setChecked(True)
        self.outside_corners.setAutoExclusive(True)
        self.outside_corners.setProperty(u"page", 0)

        self.horizontalLayout_30.addWidget(self.outside_corners)

        self.inside_corners = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.inside_corners)
        self.inside_corners.setObjectName(u"inside_corners")
        self.inside_corners.setFocusPolicy(Qt.NoFocus)
        self.inside_corners.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.inside_corners.setCheckable(True)
        self.inside_corners.setAutoExclusive(True)
        self.inside_corners.setProperty(u"page", 1)

        self.horizontalLayout_30.addWidget(self.inside_corners)

        self.boss_and_pocket = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.boss_and_pocket)
        self.boss_and_pocket.setObjectName(u"boss_and_pocket")
        self.boss_and_pocket.setFocusPolicy(Qt.NoFocus)
        self.boss_and_pocket.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.boss_and_pocket.setCheckable(True)
        self.boss_and_pocket.setAutoExclusive(True)
        self.boss_and_pocket.setProperty(u"page", 2)

        self.horizontalLayout_30.addWidget(self.boss_and_pocket)

        self.ridge_and_valley = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.ridge_and_valley)
        self.ridge_and_valley.setObjectName(u"ridge_and_valley")
        self.ridge_and_valley.setFocusPolicy(Qt.NoFocus)
        self.ridge_and_valley.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.ridge_and_valley.setCheckable(True)
        self.ridge_and_valley.setAutoExclusive(True)
        self.ridge_and_valley.setProperty(u"page", 3)

        self.horizontalLayout_30.addWidget(self.ridge_and_valley)

        self.rotation_angle = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.rotation_angle)
        self.rotation_angle.setObjectName(u"rotation_angle")
        self.rotation_angle.setFocusPolicy(Qt.NoFocus)
        self.rotation_angle.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.rotation_angle.setCheckable(True)
        self.rotation_angle.setAutoExclusive(True)
        self.rotation_angle.setProperty(u"page", 4)

        self.horizontalLayout_30.addWidget(self.rotation_angle)

        self.rotary_axis_2 = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.rotary_axis_2)
        self.rotary_axis_2.setObjectName(u"rotary_axis_2")
        self.rotary_axis_2.setFocusPolicy(Qt.NoFocus)
        self.rotary_axis_2.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.rotary_axis_2.setCheckable(True)
        self.rotary_axis_2.setAutoExclusive(True)
        self.rotary_axis_2.setProperty(u"page", 5)

        self.horizontalLayout_30.addWidget(self.rotary_axis_2)

        self.calibrate = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.calibrate)
        self.calibrate.setObjectName(u"calibrate")
        self.calibrate.setFocusPolicy(Qt.NoFocus)
        self.calibrate.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.calibrate.setCheckable(True)
        self.calibrate.setAutoExclusive(True)
        self.calibrate.setProperty(u"page", 6)

        self.horizontalLayout_30.addWidget(self.calibrate)

        self.probe_help = QPushButton(self.probe_group_select)
        self.probetabGroup.addButton(self.probe_help)
        self.probe_help.setObjectName(u"probe_help")
        self.probe_help.setFocusPolicy(Qt.NoFocus)
        self.probe_help.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 2px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.probe_help.setCheckable(True)
        self.probe_help.setAutoExclusive(True)
        self.probe_help.setProperty(u"page", 7)

        self.horizontalLayout_30.addWidget(self.probe_help)


        self.verticalLayout_45.addWidget(self.probe_group_select)

        self.widget_11 = QWidget(self.widget_13)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.widget_62 = QWidget(self.widget_11)
        self.widget_62.setObjectName(u"widget_62")
        sizePolicy8.setHeightForWidth(self.widget_62.sizePolicy().hasHeightForWidth())
        self.widget_62.setSizePolicy(sizePolicy8)
        self.widget_62.setMinimumSize(QSize(380, 0))
        self.label_19 = QLabel(self.widget_62)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(159, 43, 128, 450))
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setPixmap(QPixmap(u":/images/touch_probe.png"))
        self.label_19.setScaledContents(True)
        self.probe_led = HalLedIndicator(self.widget_62)
        self.probe_led.setObjectName(u"probe_led")
        self.probe_led.setGeometry(QRect(213, 333, 20, 20))
        sizePolicy.setHeightForWidth(self.probe_led.sizePolicy().hasHeightForWidth())
        self.probe_led.setSizePolicy(sizePolicy)
        self.probe_led.setDiameter(20)
        self.probe_led.setColor(QColor(44, 41, 255))
        self.probe_led.setState(False)
        self.halbutton = HalButton(self.widget_62)
        self.halbutton.setObjectName(u"halbutton")
        self.halbutton.setGeometry(QRect(182, 450, 80, 70))
        sizePolicy.setHeightForWidth(self.halbutton.sizePolicy().hasHeightForWidth())
        self.halbutton.setSizePolicy(sizePolicy)
        self.halbutton.setStyleSheet(u".HalButton{\n"
"background: transparent;\n"
"border: none;\n"
"}")
        self.halbutton.setFlat(False)

        self.horizontalLayout_31.addWidget(self.widget_62)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 9)
        self.probe_tab_widget = QStackedWidget(self.widget_11)
        self.probe_tab_widget.setObjectName(u"probe_tab_widget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy13.setHorizontalStretch(3)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.probe_tab_widget.sizePolicy().hasHeightForWidth())
        self.probe_tab_widget.setSizePolicy(sizePolicy13)
        self.probe_tab_widget.setMinimumSize(QSize(550, 0))
        font9 = QFont()
        font9.setFamilies([u"Bebas Kai"])
        font9.setPointSize(13)
        self.probe_tab_widget.setFont(font9)
        self.probe_tab_widget.setStyleSheet(u"SubCallButton {\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #eaeaea, stop: 1.0 #b8b8b8);\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #CFCDCA, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"SubCallButton:checked[option=\"false\"] {\n"
"    background:  qlineargradient(sprea"
                        "d:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.horizontalLayout_132 = QHBoxLayout(self.Page1)
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.widget_40 = QWidget(self.Page1)
        self.widget_40.setObjectName(u"widget_40")
        sizePolicy.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy)
        self.widget_40.setMinimumSize(QSize(465, 465))
        self.widget_40.setMaximumSize(QSize(465, 465))
        self.widget_40.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.widget_40)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.probe_back_left_top_corner = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup = QButtonGroup(Form)
        self.proberoutinebtnGroup.setObjectName(u"proberoutinebtnGroup")
        self.proberoutinebtnGroup.addButton(self.probe_back_left_top_corner)
        self.probe_back_left_top_corner.setObjectName(u"probe_back_left_top_corner")
        sizePolicy.setHeightForWidth(self.probe_back_left_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_back_left_top_corner.setSizePolicy(sizePolicy)
        self.probe_back_left_top_corner.setMinimumSize(QSize(140, 140))
        self.probe_back_left_top_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_back_left_top_corner.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/images/back_left_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_back_left_top_corner.setIcon(icon12)
        self.probe_back_left_top_corner.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_back_left_top_corner, 0, 0, 1, 1)

        self.probe_back_right_top_corner = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_back_right_top_corner)
        self.probe_back_right_top_corner.setObjectName(u"probe_back_right_top_corner")
        sizePolicy.setHeightForWidth(self.probe_back_right_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_back_right_top_corner.setSizePolicy(sizePolicy)
        self.probe_back_right_top_corner.setMinimumSize(QSize(140, 140))
        self.probe_back_right_top_corner.setMaximumSize(QSize(140, 140))
        self.probe_back_right_top_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_back_right_top_corner.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/images/back_right_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_back_right_top_corner.setIcon(icon13)
        self.probe_back_right_top_corner.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_back_right_top_corner, 0, 4, 1, 1)

        self.probe_right_top_side = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_right_top_side)
        self.probe_right_top_side.setObjectName(u"probe_right_top_side")
        sizePolicy.setHeightForWidth(self.probe_right_top_side.sizePolicy().hasHeightForWidth())
        self.probe_right_top_side.setSizePolicy(sizePolicy)
        self.probe_right_top_side.setMinimumSize(QSize(140, 140))
        self.probe_right_top_side.setMaximumSize(QSize(140, 140))
        self.probe_right_top_side.setFocusPolicy(Qt.NoFocus)
        self.probe_right_top_side.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/images/right_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/images/right_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.probe_right_top_side.setIcon(icon14)
        self.probe_right_top_side.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_right_top_side, 1, 4, 1, 1)

        self.probe_z_minus_wco_edge = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_z_minus_wco_edge)
        self.probe_z_minus_wco_edge.setObjectName(u"probe_z_minus_wco_edge")
        sizePolicy.setHeightForWidth(self.probe_z_minus_wco_edge.sizePolicy().hasHeightForWidth())
        self.probe_z_minus_wco_edge.setSizePolicy(sizePolicy)
        self.probe_z_minus_wco_edge.setMinimumSize(QSize(140, 140))
        self.probe_z_minus_wco_edge.setMaximumSize(QSize(140, 140))
        self.probe_z_minus_wco_edge.setFocusPolicy(Qt.NoFocus)
        self.probe_z_minus_wco_edge.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/images/z_top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_z_minus_wco_edge.setIcon(icon15)
        self.probe_z_minus_wco_edge.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_z_minus_wco_edge, 1, 3, 1, 1)

        self.probe_front_top_side = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_front_top_side)
        self.probe_front_top_side.setObjectName(u"probe_front_top_side")
        sizePolicy.setHeightForWidth(self.probe_front_top_side.sizePolicy().hasHeightForWidth())
        self.probe_front_top_side.setSizePolicy(sizePolicy)
        self.probe_front_top_side.setMinimumSize(QSize(140, 140))
        self.probe_front_top_side.setMaximumSize(QSize(140, 140))
        self.probe_front_top_side.setFocusPolicy(Qt.NoFocus)
        self.probe_front_top_side.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u":/images/front_middle_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_top_side.setIcon(icon16)
        self.probe_front_top_side.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_front_top_side, 2, 3, 1, 1)

        self.probe_back_top_side = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_back_top_side)
        self.probe_back_top_side.setObjectName(u"probe_back_top_side")
        sizePolicy.setHeightForWidth(self.probe_back_top_side.sizePolicy().hasHeightForWidth())
        self.probe_back_top_side.setSizePolicy(sizePolicy)
        self.probe_back_top_side.setMinimumSize(QSize(140, 140))
        self.probe_back_top_side.setMaximumSize(QSize(140, 140))
        self.probe_back_top_side.setFocusPolicy(Qt.NoFocus)
        self.probe_back_top_side.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u":/images/back_middle_outside_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_back_top_side.setIcon(icon17)
        self.probe_back_top_side.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_back_top_side, 0, 3, 1, 1)

        self.probe_front_left_top_corner = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_front_left_top_corner)
        self.probe_front_left_top_corner.setObjectName(u"probe_front_left_top_corner")
        sizePolicy.setHeightForWidth(self.probe_front_left_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_left_top_corner.setSizePolicy(sizePolicy)
        self.probe_front_left_top_corner.setMinimumSize(QSize(140, 140))
        self.probe_front_left_top_corner.setMaximumSize(QSize(140, 140))
        self.probe_front_left_top_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_front_left_top_corner.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u":/images/front_left_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_left_top_corner.setIcon(icon18)
        self.probe_front_left_top_corner.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_front_left_top_corner, 2, 0, 1, 1)

        self.probe_front_right_top_corner = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_front_right_top_corner)
        self.probe_front_right_top_corner.setObjectName(u"probe_front_right_top_corner")
        sizePolicy.setHeightForWidth(self.probe_front_right_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_right_top_corner.setSizePolicy(sizePolicy)
        self.probe_front_right_top_corner.setMinimumSize(QSize(140, 140))
        self.probe_front_right_top_corner.setMaximumSize(QSize(140, 140))
        self.probe_front_right_top_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_front_right_top_corner.setStyleSheet(u"")
        icon19 = QIcon()
        icon19.addFile(u":/images/front_right_outside_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_right_top_corner.setIcon(icon19)
        self.probe_front_right_top_corner.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_front_right_top_corner, 2, 4, 1, 1)

        self.probe_left_top_side = SubCallButton(self.widget_40)
        self.proberoutinebtnGroup.addButton(self.probe_left_top_side)
        self.probe_left_top_side.setObjectName(u"probe_left_top_side")
        sizePolicy.setHeightForWidth(self.probe_left_top_side.sizePolicy().hasHeightForWidth())
        self.probe_left_top_side.setSizePolicy(sizePolicy)
        self.probe_left_top_side.setMinimumSize(QSize(140, 140))
        self.probe_left_top_side.setMaximumSize(QSize(140, 140))
        self.probe_left_top_side.setFocusPolicy(Qt.NoFocus)
        self.probe_left_top_side.setStyleSheet(u"")
        icon20 = QIcon()
        icon20.addFile(u":/images/left_side_edge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_left_top_side.setIcon(icon20)
        self.probe_left_top_side.setIconSize(QSize(130, 130))

        self.gridLayout_7.addWidget(self.probe_left_top_side, 1, 0, 1, 1)


        self.horizontalLayout_132.addWidget(self.widget_40)

        self.probe_tab_widget.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.horizontalLayout_135 = QHBoxLayout(self.Page2)
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.widget_41 = QWidget(self.Page2)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy)
        self.widget_41.setMinimumSize(QSize(465, 465))
        self.widget_41.setMaximumSize(QSize(465, 465))
        self.widget_41.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.widget_41)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.probe_front_right_inside_corner = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_front_right_inside_corner)
        self.probe_front_right_inside_corner.setObjectName(u"probe_front_right_inside_corner")
        sizePolicy.setHeightForWidth(self.probe_front_right_inside_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_right_inside_corner.setSizePolicy(sizePolicy)
        self.probe_front_right_inside_corner.setMinimumSize(QSize(140, 140))
        self.probe_front_right_inside_corner.setMaximumSize(QSize(140, 140))
        self.probe_front_right_inside_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_front_right_inside_corner.setStyleSheet(u"")
        icon21 = QIcon()
        icon21.addFile(u":/images/inside_front_right_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_right_inside_corner.setIcon(icon21)
        self.probe_front_right_inside_corner.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_front_right_inside_corner, 3, 4, 1, 1)

        self.probe_y_plus_wco = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_y_plus_wco)
        self.probe_y_plus_wco.setObjectName(u"probe_y_plus_wco")
        sizePolicy.setHeightForWidth(self.probe_y_plus_wco.sizePolicy().hasHeightForWidth())
        self.probe_y_plus_wco.setSizePolicy(sizePolicy)
        self.probe_y_plus_wco.setMinimumSize(QSize(140, 140))
        self.probe_y_plus_wco.setMaximumSize(QSize(140, 140))
        self.probe_y_plus_wco.setFocusPolicy(Qt.NoFocus)
        self.probe_y_plus_wco.setStyleSheet(u"")
        icon22 = QIcon()
        icon22.addFile(u":/images/y_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_y_plus_wco.setIcon(icon22)
        self.probe_y_plus_wco.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_y_plus_wco, 0, 3, 1, 1)

        self.probe_back_right_inside_corner = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_back_right_inside_corner)
        self.probe_back_right_inside_corner.setObjectName(u"probe_back_right_inside_corner")
        sizePolicy.setHeightForWidth(self.probe_back_right_inside_corner.sizePolicy().hasHeightForWidth())
        self.probe_back_right_inside_corner.setSizePolicy(sizePolicy)
        self.probe_back_right_inside_corner.setMinimumSize(QSize(140, 140))
        self.probe_back_right_inside_corner.setMaximumSize(QSize(140, 140))
        self.probe_back_right_inside_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_back_right_inside_corner.setStyleSheet(u"")
        icon23 = QIcon()
        icon23.addFile(u":/images/inside_back_right_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_back_right_inside_corner.setIcon(icon23)
        self.probe_back_right_inside_corner.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_back_right_inside_corner, 0, 4, 1, 1)

        self.probe_front_left_inside_corner = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_front_left_inside_corner)
        self.probe_front_left_inside_corner.setObjectName(u"probe_front_left_inside_corner")
        sizePolicy.setHeightForWidth(self.probe_front_left_inside_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_left_inside_corner.setSizePolicy(sizePolicy)
        self.probe_front_left_inside_corner.setMinimumSize(QSize(140, 140))
        self.probe_front_left_inside_corner.setMaximumSize(QSize(140, 140))
        self.probe_front_left_inside_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_front_left_inside_corner.setStyleSheet(u"")
        icon24 = QIcon()
        icon24.addFile(u":/images/inside_front_left_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_front_left_inside_corner.setIcon(icon24)
        self.probe_front_left_inside_corner.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_front_left_inside_corner, 3, 0, 1, 1)

        self.probe_z_minus_wco_inside = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_z_minus_wco_inside)
        self.probe_z_minus_wco_inside.setObjectName(u"probe_z_minus_wco_inside")
        sizePolicy.setHeightForWidth(self.probe_z_minus_wco_inside.sizePolicy().hasHeightForWidth())
        self.probe_z_minus_wco_inside.setSizePolicy(sizePolicy)
        self.probe_z_minus_wco_inside.setMinimumSize(QSize(140, 140))
        self.probe_z_minus_wco_inside.setMaximumSize(QSize(140, 140))
        self.probe_z_minus_wco_inside.setFocusPolicy(Qt.NoFocus)
        self.probe_z_minus_wco_inside.setStyleSheet(u"")
        self.probe_z_minus_wco_inside.setIcon(icon15)
        self.probe_z_minus_wco_inside.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_z_minus_wco_inside, 1, 3, 1, 1)

        self.probe_back_left_inside_corner = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_back_left_inside_corner)
        self.probe_back_left_inside_corner.setObjectName(u"probe_back_left_inside_corner")
        sizePolicy.setHeightForWidth(self.probe_back_left_inside_corner.sizePolicy().hasHeightForWidth())
        self.probe_back_left_inside_corner.setSizePolicy(sizePolicy)
        self.probe_back_left_inside_corner.setMinimumSize(QSize(140, 140))
        self.probe_back_left_inside_corner.setMaximumSize(QSize(140, 140))
        self.probe_back_left_inside_corner.setFocusPolicy(Qt.NoFocus)
        self.probe_back_left_inside_corner.setStyleSheet(u"")
        icon25 = QIcon()
        icon25.addFile(u":/images/inside_back_left_corner.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_back_left_inside_corner.setIcon(icon25)
        self.probe_back_left_inside_corner.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_back_left_inside_corner, 0, 0, 1, 1)

        self.probe_x_minus_wco = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_x_minus_wco)
        self.probe_x_minus_wco.setObjectName(u"probe_x_minus_wco")
        sizePolicy.setHeightForWidth(self.probe_x_minus_wco.sizePolicy().hasHeightForWidth())
        self.probe_x_minus_wco.setSizePolicy(sizePolicy)
        self.probe_x_minus_wco.setMinimumSize(QSize(140, 140))
        self.probe_x_minus_wco.setMaximumSize(QSize(140, 140))
        self.probe_x_minus_wco.setFocusPolicy(Qt.NoFocus)
        self.probe_x_minus_wco.setStyleSheet(u"")
        icon26 = QIcon()
        icon26.addFile(u":/images/x_minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_x_minus_wco.setIcon(icon26)
        self.probe_x_minus_wco.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_x_minus_wco, 1, 0, 1, 1)

        self.probe_x_plus_wco = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_x_plus_wco)
        self.probe_x_plus_wco.setObjectName(u"probe_x_plus_wco")
        sizePolicy.setHeightForWidth(self.probe_x_plus_wco.sizePolicy().hasHeightForWidth())
        self.probe_x_plus_wco.setSizePolicy(sizePolicy)
        self.probe_x_plus_wco.setMinimumSize(QSize(140, 140))
        self.probe_x_plus_wco.setMaximumSize(QSize(140, 140))
        self.probe_x_plus_wco.setFocusPolicy(Qt.NoFocus)
        self.probe_x_plus_wco.setStyleSheet(u"")
        icon27 = QIcon()
        icon27.addFile(u":/images/x_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_x_plus_wco.setIcon(icon27)
        self.probe_x_plus_wco.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_x_plus_wco, 1, 4, 1, 1)

        self.probe_y_minus_wco = SubCallButton(self.widget_41)
        self.proberoutinebtnGroup.addButton(self.probe_y_minus_wco)
        self.probe_y_minus_wco.setObjectName(u"probe_y_minus_wco")
        sizePolicy.setHeightForWidth(self.probe_y_minus_wco.sizePolicy().hasHeightForWidth())
        self.probe_y_minus_wco.setSizePolicy(sizePolicy)
        self.probe_y_minus_wco.setMinimumSize(QSize(140, 140))
        self.probe_y_minus_wco.setMaximumSize(QSize(140, 140))
        self.probe_y_minus_wco.setFocusPolicy(Qt.NoFocus)
        self.probe_y_minus_wco.setStyleSheet(u"")
        icon28 = QIcon()
        icon28.addFile(u":/images/y_minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_y_minus_wco.setIcon(icon28)
        self.probe_y_minus_wco.setIconSize(QSize(125, 125))

        self.gridLayout_16.addWidget(self.probe_y_minus_wco, 3, 3, 1, 1)


        self.horizontalLayout_135.addWidget(self.widget_41)

        self.probe_tab_widget.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.horizontalLayout_138 = QHBoxLayout(self.Page3)
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.widget_42 = QWidget(self.Page3)
        self.widget_42.setObjectName(u"widget_42")
        sizePolicy.setHeightForWidth(self.widget_42.sizePolicy().hasHeightForWidth())
        self.widget_42.setSizePolicy(sizePolicy)
        self.widget_42.setMinimumSize(QSize(465, 461))
        self.widget_42.setMaximumSize(QSize(465, 461))
        self.widget_42.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.verticalLayout_43 = QVBoxLayout(self.widget_42)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(3, -1, 3, -1)
        self.gridWidget_8 = QWidget(self.widget_42)
        self.gridWidget_8.setObjectName(u"gridWidget_8")
        self.gridLayout_10 = QGridLayout(self.gridWidget_8)
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.probe_round_pocket_center = SubCallButton(self.gridWidget_8)
        self.probe_round_pocket_center.setObjectName(u"probe_round_pocket_center")
        self.probe_round_pocket_center.setMinimumSize(QSize(140, 140))
        self.probe_round_pocket_center.setMaximumSize(QSize(140, 140))
        self.probe_round_pocket_center.setFocusPolicy(Qt.NoFocus)
        self.probe_round_pocket_center.setStyleSheet(u"")
        icon29 = QIcon()
        icon29.addFile(u":/images/round_pocket_center_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_round_pocket_center.setIcon(icon29)
        self.probe_round_pocket_center.setIconSize(QSize(120, 120))

        self.gridLayout_10.addWidget(self.probe_round_pocket_center, 0, 2, 1, 1)

        self.probe_rect_pocket_2 = SubCallButton(self.gridWidget_8)
        self.probe_rect_pocket_2.setObjectName(u"probe_rect_pocket_2")
        self.probe_rect_pocket_2.setMinimumSize(QSize(140, 140))
        self.probe_rect_pocket_2.setMaximumSize(QSize(140, 140))
        self.probe_rect_pocket_2.setFocusPolicy(Qt.NoFocus)
        self.probe_rect_pocket_2.setStyleSheet(u"")
        icon30 = QIcon()
        icon30.addFile(u":/images/rect_pocket_center_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_rect_pocket_2.setIcon(icon30)
        self.probe_rect_pocket_2.setIconSize(QSize(120, 120))

        self.gridLayout_10.addWidget(self.probe_rect_pocket_2, 1, 2, 1, 1)

        self.probe_round_boss = SubCallButton(self.gridWidget_8)
        self.proberoutinebtnGroup.addButton(self.probe_round_boss)
        self.probe_round_boss.setObjectName(u"probe_round_boss")
        self.probe_round_boss.setMinimumSize(QSize(140, 140))
        self.probe_round_boss.setMaximumSize(QSize(140, 140))
        self.probe_round_boss.setFocusPolicy(Qt.NoFocus)
        self.probe_round_boss.setStyleSheet(u"")
        icon31 = QIcon()
        icon31.addFile(u":/images/boss_round.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_round_boss.setIcon(icon31)
        self.probe_round_boss.setIconSize(QSize(140, 140))

        self.gridLayout_10.addWidget(self.probe_round_boss, 0, 1, 1, 1)

        self.probe_round_pocket = SubCallButton(self.gridWidget_8)
        self.proberoutinebtnGroup.addButton(self.probe_round_pocket)
        self.probe_round_pocket.setObjectName(u"probe_round_pocket")
        self.probe_round_pocket.setMinimumSize(QSize(140, 140))
        self.probe_round_pocket.setMaximumSize(QSize(140, 140))
        self.probe_round_pocket.setFocusPolicy(Qt.NoFocus)
        self.probe_round_pocket.setStyleSheet(u"")
        icon32 = QIcon()
        icon32.addFile(u":/images/round_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_round_pocket.setIcon(icon32)
        self.probe_round_pocket.setIconSize(QSize(120, 120))

        self.gridLayout_10.addWidget(self.probe_round_pocket, 0, 0, 1, 1)

        self.probe_rect_boss = SubCallButton(self.gridWidget_8)
        self.proberoutinebtnGroup.addButton(self.probe_rect_boss)
        self.probe_rect_boss.setObjectName(u"probe_rect_boss")
        self.probe_rect_boss.setMinimumSize(QSize(140, 140))
        self.probe_rect_boss.setMaximumSize(QSize(140, 140))
        self.probe_rect_boss.setFocusPolicy(Qt.NoFocus)
        self.probe_rect_boss.setStyleSheet(u"")
        icon33 = QIcon()
        icon33.addFile(u":/images/rect_boss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_rect_boss.setIcon(icon33)
        self.probe_rect_boss.setIconSize(QSize(140, 140))

        self.gridLayout_10.addWidget(self.probe_rect_boss, 1, 1, 1, 1)

        self.probe_rect_pocket = SubCallButton(self.gridWidget_8)
        self.proberoutinebtnGroup.addButton(self.probe_rect_pocket)
        self.probe_rect_pocket.setObjectName(u"probe_rect_pocket")
        self.probe_rect_pocket.setMinimumSize(QSize(140, 140))
        self.probe_rect_pocket.setMaximumSize(QSize(140, 140))
        self.probe_rect_pocket.setFocusPolicy(Qt.NoFocus)
        self.probe_rect_pocket.setStyleSheet(u"")
        icon34 = QIcon()
        icon34.addFile(u":/images/rect_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_rect_pocket.setIcon(icon34)
        self.probe_rect_pocket.setIconSize(QSize(120, 120))

        self.gridLayout_10.addWidget(self.probe_rect_pocket, 1, 0, 1, 1)


        self.verticalLayout_43.addWidget(self.gridWidget_8)

        self.frame_8 = QFrame(self.widget_42)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(460, 65))
        self.frame_8.setMaximumSize(QSize(460, 65))
        self.frame_8.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_48 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.hint_label = QLabel(self.frame_8)
        self.hint_label.setObjectName(u"hint_label")
        self.hint_label.setMinimumSize(QSize(60, 40))
        self.hint_label.setMaximumSize(QSize(60, 40))
        self.hint_label.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.hint_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.hint_label)

        self.label_70 = QLabel(self.frame_8)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(50, 0))
        self.label_70.setMaximumSize(QSize(50, 16777215))
        self.label_70.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_70.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_70.setIndent(0)

        self.horizontalLayout_20.addWidget(self.label_70)

        self.diameter_hint_3025 = VCPSettingsLineEdit(self.frame_8)
        self.diameter_hint_3025.setObjectName(u"diameter_hint_3025")
        sizePolicy.setHeightForWidth(self.diameter_hint_3025.sizePolicy().hasHeightForWidth())
        self.diameter_hint_3025.setSizePolicy(sizePolicy)
        self.diameter_hint_3025.setMinimumSize(QSize(80, 40))
        self.diameter_hint_3025.setMaximumSize(QSize(80, 40))
        self.diameter_hint_3025.setFocusPolicy(Qt.ClickFocus)
        self.diameter_hint_3025.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.diameter_hint_3025)

        self.label_71 = QLabel(self.frame_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(30, 0))
        self.label_71.setMaximumSize(QSize(30, 16777215))
        self.label_71.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_71.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_71.setIndent(0)

        self.horizontalLayout_20.addWidget(self.label_71)

        self.x_hint_boss_pocket_3026 = VCPSettingsLineEdit(self.frame_8)
        self.x_hint_boss_pocket_3026.setObjectName(u"x_hint_boss_pocket_3026")
        sizePolicy.setHeightForWidth(self.x_hint_boss_pocket_3026.sizePolicy().hasHeightForWidth())
        self.x_hint_boss_pocket_3026.setSizePolicy(sizePolicy)
        self.x_hint_boss_pocket_3026.setMinimumSize(QSize(80, 40))
        self.x_hint_boss_pocket_3026.setMaximumSize(QSize(80, 40))
        self.x_hint_boss_pocket_3026.setFocusPolicy(Qt.ClickFocus)
        self.x_hint_boss_pocket_3026.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.x_hint_boss_pocket_3026)

        self.label_72 = QLabel(self.frame_8)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(30, 0))
        self.label_72.setMaximumSize(QSize(30, 16777215))
        self.label_72.setStyleSheet(u"QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_72.setIndent(0)

        self.horizontalLayout_20.addWidget(self.label_72)

        self.y_hint_boss_pocket_3027 = VCPSettingsLineEdit(self.frame_8)
        self.y_hint_boss_pocket_3027.setObjectName(u"y_hint_boss_pocket_3027")
        sizePolicy.setHeightForWidth(self.y_hint_boss_pocket_3027.sizePolicy().hasHeightForWidth())
        self.y_hint_boss_pocket_3027.setSizePolicy(sizePolicy)
        self.y_hint_boss_pocket_3027.setMinimumSize(QSize(80, 40))
        self.y_hint_boss_pocket_3027.setMaximumSize(QSize(80, 40))
        self.y_hint_boss_pocket_3027.setFocusPolicy(Qt.ClickFocus)
        self.y_hint_boss_pocket_3027.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.y_hint_boss_pocket_3027)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_20)


        self.verticalLayout_43.addWidget(self.frame_8)


        self.horizontalLayout_138.addWidget(self.widget_42, 0, Qt.AlignHCenter)

        self.probe_tab_widget.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.horizontalLayout_141 = QHBoxLayout(self.Page4)
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.widget_43 = QWidget(self.Page4)
        self.widget_43.setObjectName(u"widget_43")
        sizePolicy.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy)
        self.widget_43.setMinimumSize(QSize(465, 461))
        self.widget_43.setMaximumSize(QSize(465, 461))
        self.widget_43.setStyleSheet(u"")
        self.verticalLayout_58 = QVBoxLayout(self.widget_43)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(3, -1, 3, -1)
        self.gridWidget_9 = QWidget(self.widget_43)
        self.gridWidget_9.setObjectName(u"gridWidget_9")
        sizePolicy1.setHeightForWidth(self.gridWidget_9.sizePolicy().hasHeightForWidth())
        self.gridWidget_9.setSizePolicy(sizePolicy1)
        self.gridLayout_9 = QGridLayout(self.gridWidget_9)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.probe_valley_x_center_start = SubCallButton(self.gridWidget_9)
        self.probe_valley_x_center_start.setObjectName(u"probe_valley_x_center_start")
        self.probe_valley_x_center_start.setMinimumSize(QSize(140, 140))
        self.probe_valley_x_center_start.setMaximumSize(QSize(140, 140))
        self.probe_valley_x_center_start.setFocusPolicy(Qt.NoFocus)
        self.probe_valley_x_center_start.setStyleSheet(u"")
        icon35 = QIcon()
        icon35.addFile(u":/images/probe_x_valley_center_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_valley_x_center_start.setIcon(icon35)
        self.probe_valley_x_center_start.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_valley_x_center_start, 1, 2, 1, 1)

        self.probe_valley_y_center_start = SubCallButton(self.gridWidget_9)
        self.probe_valley_y_center_start.setObjectName(u"probe_valley_y_center_start")
        self.probe_valley_y_center_start.setMinimumSize(QSize(140, 140))
        self.probe_valley_y_center_start.setMaximumSize(QSize(140, 140))
        self.probe_valley_y_center_start.setFocusPolicy(Qt.NoFocus)
        self.probe_valley_y_center_start.setStyleSheet(u"")
        icon36 = QIcon()
        icon36.addFile(u":/images/probe_y_valley_center_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_valley_y_center_start.setIcon(icon36)
        self.probe_valley_y_center_start.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_valley_y_center_start, 0, 2, 1, 1)

        self.probe_ridge_y = SubCallButton(self.gridWidget_9)
        self.proberoutinebtnGroup.addButton(self.probe_ridge_y)
        self.probe_ridge_y.setObjectName(u"probe_ridge_y")
        self.probe_ridge_y.setMinimumSize(QSize(140, 140))
        self.probe_ridge_y.setMaximumSize(QSize(140, 140))
        self.probe_ridge_y.setFocusPolicy(Qt.NoFocus)
        self.probe_ridge_y.setStyleSheet(u"")
        icon37 = QIcon()
        icon37.addFile(u":/images/probe_y_ridge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_ridge_y.setIcon(icon37)
        self.probe_ridge_y.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_ridge_y, 0, 1, 1, 1)

        self.probe_valley_y = SubCallButton(self.gridWidget_9)
        self.proberoutinebtnGroup.addButton(self.probe_valley_y)
        self.probe_valley_y.setObjectName(u"probe_valley_y")
        self.probe_valley_y.setMinimumSize(QSize(140, 140))
        self.probe_valley_y.setMaximumSize(QSize(140, 140))
        self.probe_valley_y.setFocusPolicy(Qt.NoFocus)
        self.probe_valley_y.setStyleSheet(u"")
        icon38 = QIcon()
        icon38.addFile(u":/images/probe_y_valley.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_valley_y.setIcon(icon38)
        self.probe_valley_y.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_valley_y, 0, 0, 1, 1)

        self.probe_valley_x = SubCallButton(self.gridWidget_9)
        self.proberoutinebtnGroup.addButton(self.probe_valley_x)
        self.probe_valley_x.setObjectName(u"probe_valley_x")
        self.probe_valley_x.setMinimumSize(QSize(140, 140))
        self.probe_valley_x.setMaximumSize(QSize(140, 140))
        self.probe_valley_x.setFocusPolicy(Qt.NoFocus)
        self.probe_valley_x.setStyleSheet(u"")
        icon39 = QIcon()
        icon39.addFile(u":/images/probe_x_valley.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_valley_x.setIcon(icon39)
        self.probe_valley_x.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_valley_x, 1, 0, 1, 1)

        self.probe_ridge_x = SubCallButton(self.gridWidget_9)
        self.proberoutinebtnGroup.addButton(self.probe_ridge_x)
        self.probe_ridge_x.setObjectName(u"probe_ridge_x")
        self.probe_ridge_x.setMinimumSize(QSize(140, 140))
        self.probe_ridge_x.setMaximumSize(QSize(140, 140))
        self.probe_ridge_x.setFocusPolicy(Qt.NoFocus)
        self.probe_ridge_x.setStyleSheet(u"")
        icon40 = QIcon()
        icon40.addFile(u":/images/probe_x_ridge.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_ridge_x.setIcon(icon40)
        self.probe_ridge_x.setIconSize(QSize(120, 120))

        self.gridLayout_9.addWidget(self.probe_ridge_x, 1, 1, 1, 1)


        self.verticalLayout_58.addWidget(self.gridWidget_9)

        self.frame_9 = QFrame(self.widget_43)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(460, 65))
        self.frame_9.setMaximumSize(QSize(460, 65))
        self.frame_9.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"	border-width: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_143 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.hint_label_2 = QLabel(self.frame_9)
        self.hint_label_2.setObjectName(u"hint_label_2")
        self.hint_label_2.setMinimumSize(QSize(115, 40))
        self.hint_label_2.setMaximumSize(QSize(115, 40))
        self.hint_label_2.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.hint_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.hint_label_2)

        self.label_74 = QLabel(self.frame_9)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(50, 0))
        self.label_74.setMaximumSize(QSize(50, 16777215))
        self.label_74.setStyleSheet(u"QLabel{\n"
"    font: 15pt \"Bebas Kai\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-right: 1px;\n"
"    padding-left: 5px;\n"
"}")
        self.label_74.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_74.setIndent(0)

        self.horizontalLayout_28.addWidget(self.label_74)

        self.x_hint_ridge_valley_3028 = VCPSettingsLineEdit(self.frame_9)
        self.x_hint_ridge_valley_3028.setObjectName(u"x_hint_ridge_valley_3028")
        sizePolicy.setHeightForWidth(self.x_hint_ridge_valley_3028.sizePolicy().hasHeightForWidth())
        self.x_hint_ridge_valley_3028.setSizePolicy(sizePolicy)
        self.x_hint_ridge_valley_3028.setMinimumSize(QSize(80, 40))
        self.x_hint_ridge_valley_3028.setMaximumSize(QSize(80, 40))
        self.x_hint_ridge_valley_3028.setFocusPolicy(Qt.ClickFocus)
        self.x_hint_ridge_valley_3028.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.x_hint_ridge_valley_3028)

        self.label_75 = QLabel(self.frame_9)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(50, 0))
        self.label_75.setMaximumSize(QSize(50, 16777215))
        self.label_75.setStyleSheet(u"QLabel{\n"
"    font: 15pt \"Bebas Kai\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding-right: 1px;\n"
"    padding-left: 5px;\n"
"}")
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_75.setIndent(0)

        self.horizontalLayout_28.addWidget(self.label_75)

        self.y_hint_ridge_valley_3029 = VCPSettingsLineEdit(self.frame_9)
        self.y_hint_ridge_valley_3029.setObjectName(u"y_hint_ridge_valley_3029")
        sizePolicy.setHeightForWidth(self.y_hint_ridge_valley_3029.sizePolicy().hasHeightForWidth())
        self.y_hint_ridge_valley_3029.setSizePolicy(sizePolicy)
        self.y_hint_ridge_valley_3029.setMinimumSize(QSize(80, 40))
        self.y_hint_ridge_valley_3029.setMaximumSize(QSize(80, 40))
        self.y_hint_ridge_valley_3029.setFocusPolicy(Qt.ClickFocus)
        self.y_hint_ridge_valley_3029.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_28.addWidget(self.y_hint_ridge_valley_3029)


        self.horizontalLayout_143.addLayout(self.horizontalLayout_28)


        self.verticalLayout_58.addWidget(self.frame_9)


        self.horizontalLayout_141.addWidget(self.widget_43, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.probe_tab_widget.addWidget(self.Page4)
        self.Page5 = QWidget()
        self.Page5.setObjectName(u"Page5")
        self.horizontalLayout_4 = QHBoxLayout(self.Page5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_16 = QWidget(self.Page5)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.verticalLayout_26 = QVBoxLayout(self.widget_16)
        self.verticalLayout_26.setSpacing(9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_45 = QWidget(self.widget_16)
        self.widget_45.setObjectName(u"widget_45")
        sizePolicy.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy)
        self.widget_45.setMinimumSize(QSize(465, 465))
        self.widget_45.setMaximumSize(QSize(465, 465))
        self.widget_45.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.widget_45)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.probe_top_left_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_top_left_edge_angle)
        self.probe_top_left_edge_angle.setObjectName(u"probe_top_left_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_top_left_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_top_left_edge_angle.setSizePolicy(sizePolicy)
        self.probe_top_left_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_top_left_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_top_left_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_top_left_edge_angle.setStyleSheet(u"")
        icon41 = QIcon()
        icon41.addFile(u":/images/probe_top_left_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_top_left_edge_angle.setIcon(icon41)
        self.probe_top_left_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_top_left_edge_angle, 2, 0, 1, 1)

        self.probe_corner_y_plus_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_corner_y_plus_edge_angle)
        self.probe_corner_y_plus_edge_angle.setObjectName(u"probe_corner_y_plus_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_corner_y_plus_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_corner_y_plus_edge_angle.setSizePolicy(sizePolicy)
        self.probe_corner_y_plus_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_corner_y_plus_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_corner_y_plus_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_corner_y_plus_edge_angle.setStyleSheet(u"")
        icon42 = QIcon()
        icon42.addFile(u":/images/probe_corner_y_plus_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_corner_y_plus_edge_angle.setIcon(icon42)
        self.probe_corner_y_plus_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_corner_y_plus_edge_angle, 3, 0, 1, 1)

        self.probe_corner_x_plus_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_corner_x_plus_edge_angle)
        self.probe_corner_x_plus_edge_angle.setObjectName(u"probe_corner_x_plus_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_corner_x_plus_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_corner_x_plus_edge_angle.setSizePolicy(sizePolicy)
        self.probe_corner_x_plus_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_corner_x_plus_edge_angle.setFocusPolicy(Qt.NoFocus)
        icon43 = QIcon()
        icon43.addFile(u":/images/probe_corner_x_plus_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_corner_x_plus_edge_angle.setIcon(icon43)
        self.probe_corner_x_plus_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_corner_x_plus_edge_angle, 1, 0, 1, 1)

        self.probe_corner_y_minus_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_corner_y_minus_edge_angle)
        self.probe_corner_y_minus_edge_angle.setObjectName(u"probe_corner_y_minus_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_corner_y_minus_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_corner_y_minus_edge_angle.setSizePolicy(sizePolicy)
        self.probe_corner_y_minus_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_corner_y_minus_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_corner_y_minus_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_corner_y_minus_edge_angle.setStyleSheet(u"")
        icon44 = QIcon()
        icon44.addFile(u":/images/probe_corner_y_minus_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_corner_y_minus_edge_angle.setIcon(icon44)
        self.probe_corner_y_minus_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_corner_y_minus_edge_angle, 1, 2, 1, 1)

        self.probe_z_minus_edge = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_z_minus_edge)
        self.probe_z_minus_edge.setObjectName(u"probe_z_minus_edge")
        sizePolicy.setHeightForWidth(self.probe_z_minus_edge.sizePolicy().hasHeightForWidth())
        self.probe_z_minus_edge.setSizePolicy(sizePolicy)
        self.probe_z_minus_edge.setMinimumSize(QSize(140, 140))
        self.probe_z_minus_edge.setMaximumSize(QSize(140, 140))
        self.probe_z_minus_edge.setFocusPolicy(Qt.NoFocus)
        self.probe_z_minus_edge.setStyleSheet(u"")
        icon45 = QIcon()
        icon45.addFile(u":/images/z_top_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_z_minus_edge.setIcon(icon45)
        self.probe_z_minus_edge.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_z_minus_edge, 2, 1, 1, 1)

        self.probe_corner_x_minus_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_corner_x_minus_edge_angle)
        self.probe_corner_x_minus_edge_angle.setObjectName(u"probe_corner_x_minus_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_corner_x_minus_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_corner_x_minus_edge_angle.setSizePolicy(sizePolicy)
        self.probe_corner_x_minus_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_corner_x_minus_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_corner_x_minus_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_corner_x_minus_edge_angle.setStyleSheet(u"")
        icon46 = QIcon()
        icon46.addFile(u":/images/probe_corner_x_minus_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_corner_x_minus_edge_angle.setIcon(icon46)
        self.probe_corner_x_minus_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_corner_x_minus_edge_angle, 3, 2, 1, 1)

        self.probe_top_right_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_top_right_edge_angle)
        self.probe_top_right_edge_angle.setObjectName(u"probe_top_right_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_top_right_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_top_right_edge_angle.setSizePolicy(sizePolicy)
        self.probe_top_right_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_top_right_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_top_right_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_top_right_edge_angle.setStyleSheet(u"")
        icon47 = QIcon()
        icon47.addFile(u":/images/probe_top_right_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_top_right_edge_angle.setIcon(icon47)
        self.probe_top_right_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_top_right_edge_angle, 2, 2, 1, 1)

        self.probe_top_back_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_top_back_edge_angle)
        self.probe_top_back_edge_angle.setObjectName(u"probe_top_back_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_top_back_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_top_back_edge_angle.setSizePolicy(sizePolicy)
        self.probe_top_back_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_top_back_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_top_back_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_top_back_edge_angle.setStyleSheet(u"")
        icon48 = QIcon()
        icon48.addFile(u":/images/probe_top_back_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_top_back_edge_angle.setIcon(icon48)
        self.probe_top_back_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_top_back_edge_angle, 1, 1, 1, 1)

        self.probe_top_front_edge_angle = SubCallButton(self.widget_45)
        self.proberoutinebtnGroup.addButton(self.probe_top_front_edge_angle)
        self.probe_top_front_edge_angle.setObjectName(u"probe_top_front_edge_angle")
        sizePolicy.setHeightForWidth(self.probe_top_front_edge_angle.sizePolicy().hasHeightForWidth())
        self.probe_top_front_edge_angle.setSizePolicy(sizePolicy)
        self.probe_top_front_edge_angle.setMinimumSize(QSize(140, 140))
        self.probe_top_front_edge_angle.setMaximumSize(QSize(140, 140))
        self.probe_top_front_edge_angle.setFocusPolicy(Qt.NoFocus)
        self.probe_top_front_edge_angle.setStyleSheet(u"")
        icon49 = QIcon()
        icon49.addFile(u":/images/probe_top_front_edge_angle_r.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_top_front_edge_angle.setIcon(icon49)
        self.probe_top_front_edge_angle.setIconSize(QSize(130, 130))

        self.gridLayout_8.addWidget(self.probe_top_front_edge_angle, 3, 1, 1, 1)


        self.verticalLayout_26.addWidget(self.widget_45)

        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy6.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy6)
        self.widget_17.setMinimumSize(QSize(0, 42))
        self.widget_17.setMaximumSize(QSize(16777215, 42))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_54.setSpacing(9)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 1, 0, 1)
        self.set_wco_offset_Btn = VCPSettingsPushButton(self.widget_17)
        self.set_wco_offset_Btn.setObjectName(u"set_wco_offset_Btn")
        self.set_wco_offset_Btn.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.set_wco_offset_Btn.sizePolicy().hasHeightForWidth())
        self.set_wco_offset_Btn.setSizePolicy(sizePolicy6)
        self.set_wco_offset_Btn.setMinimumSize(QSize(0, 40))
        self.set_wco_offset_Btn.setMaximumSize(QSize(16777215, 40))
        self.set_wco_offset_Btn.setStyleSheet(u"font: 15pt \"Bebas Kai\";")

        self.horizontalLayout_54.addWidget(self.set_wco_offset_Btn)

        self.frame_16 = QFrame(self.widget_17)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy6.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy6)
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"	border-width: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}")
        self.horizontalLayout_163 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_163.setObjectName(u"horizontalLayout_163")
        self.horizontalLayout_163.setContentsMargins(3, 1, 3, 1)
        self.edge_width_label = QLabel(self.frame_16)
        self.edge_width_label.setObjectName(u"edge_width_label")
        self.edge_width_label.setMinimumSize(QSize(90, 31))
        self.edge_width_label.setMaximumSize(QSize(90, 31))
        self.edge_width_label.setLayoutDirection(Qt.LeftToRight)
        self.edge_width_label.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.edge_width_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_163.addWidget(self.edge_width_label)

        self.edge_width_3024 = VCPSettingsLineEdit(self.frame_16)
        self.edge_width_3024.setObjectName(u"edge_width_3024")
        sizePolicy.setHeightForWidth(self.edge_width_3024.sizePolicy().hasHeightForWidth())
        self.edge_width_3024.setSizePolicy(sizePolicy)
        self.edge_width_3024.setMinimumSize(QSize(100, 31))
        self.edge_width_3024.setMaximumSize(QSize(100, 31))
        self.edge_width_3024.setFocusPolicy(Qt.ClickFocus)
        self.edge_width_3024.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_163.addWidget(self.edge_width_3024)


        self.horizontalLayout_54.addWidget(self.frame_16)


        self.verticalLayout_26.addWidget(self.widget_17)


        self.horizontalLayout_4.addWidget(self.widget_16)

        self.probe_tab_widget.addWidget(self.Page5)
        self.Page6 = QWidget()
        self.Page6.setObjectName(u"Page6")
        self.probe_tab_widget.addWidget(self.Page6)
        self.Page7 = QWidget()
        self.Page7.setObjectName(u"Page7")
        self.horizontalLayout_55 = QHBoxLayout(self.Page7)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.frame_47 = QFrame(self.Page7)
        self.frame_47.setObjectName(u"frame_47")
        sizePolicy8.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy8)
        self.frame_47.setMaximumSize(QSize(520, 520))
        self.frame_47.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(206, 209, 202);\n"
"    background-color: rgb(57, 63, 65);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.verticalLayout_46 = QVBoxLayout(self.frame_47)
        self.verticalLayout_46.setSpacing(9)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(9, 12, 9, 18)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(6)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(9, 3, 9, 3)
        self.label_93 = QLabel(self.frame_47)
        self.label_93.setObjectName(u"label_93")
        sizePolicy.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy)
        self.label_93.setMinimumSize(QSize(210, 30))
        self.label_93.setMaximumSize(QSize(210, 30))
        self.label_93.setBaseSize(QSize(140, 30))
        self.label_93.setStyleSheet(u"QLabel{\n"
"font: 17pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_93.setLineWidth(0)
        self.label_93.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_93.setIndent(0)

        self.horizontalLayout_61.addWidget(self.label_93)

        self.calibration_offset_3032 = VCPSettingsLineEdit(self.frame_47)
        self.calibration_offset_3032.setObjectName(u"calibration_offset_3032")
        sizePolicy.setHeightForWidth(self.calibration_offset_3032.sizePolicy().hasHeightForWidth())
        self.calibration_offset_3032.setSizePolicy(sizePolicy)
        self.calibration_offset_3032.setMinimumSize(QSize(100, 35))
        self.calibration_offset_3032.setMaximumSize(QSize(100, 35))
        self.calibration_offset_3032.setFocusPolicy(Qt.ClickFocus)
        self.calibration_offset_3032.setStyleSheet(u"")
        self.calibration_offset_3032.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calibration_offset_3032.setReadOnly(False)
        self.calibration_offset_3032.setClearButtonEnabled(False)

        self.horizontalLayout_61.addWidget(self.calibration_offset_3032)

        self.probe_cal_reset = SubCallButton(self.frame_47)
        self.probe_cal_reset.setObjectName(u"probe_cal_reset")
        sizePolicy.setHeightForWidth(self.probe_cal_reset.sizePolicy().hasHeightForWidth())
        self.probe_cal_reset.setSizePolicy(sizePolicy)
        self.probe_cal_reset.setMinimumSize(QSize(150, 37))
        self.probe_cal_reset.setMaximumSize(QSize(150, 37))
        self.probe_cal_reset.setFocusPolicy(Qt.NoFocus)
        self.probe_cal_reset.setStyleSheet(u"SubCallButton{\n"
"    border-radius: 5px;\n"
"	font: 15pt \"Bebas Kai\";\n"
"  	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: black;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255)"
                        ");\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_61.addWidget(self.probe_cal_reset)


        self.verticalLayout_46.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setSpacing(21)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(9, 3, -1, 3)
        self.probe_cal_round_pocket = SubCallButton(self.frame_47)
        self.proberoutinebtnGroup.addButton(self.probe_cal_round_pocket)
        self.probe_cal_round_pocket.setObjectName(u"probe_cal_round_pocket")
        self.probe_cal_round_pocket.setMinimumSize(QSize(150, 150))
        self.probe_cal_round_pocket.setMaximumSize(QSize(150, 150))
        self.probe_cal_round_pocket.setFocusPolicy(Qt.NoFocus)
        self.probe_cal_round_pocket.setStyleSheet(u"")
        icon50 = QIcon()
        icon50.addFile(u":/images/probe_cal_round_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_cal_round_pocket.setIcon(icon50)
        self.probe_cal_round_pocket.setIconSize(QSize(135, 135))

        self.horizontalLayout_60.addWidget(self.probe_cal_round_pocket)

        self.probe_cal_round_boss = SubCallButton(self.frame_47)
        self.proberoutinebtnGroup.addButton(self.probe_cal_round_boss)
        self.probe_cal_round_boss.setObjectName(u"probe_cal_round_boss")
        self.probe_cal_round_boss.setMinimumSize(QSize(150, 150))
        self.probe_cal_round_boss.setMaximumSize(QSize(150, 150))
        self.probe_cal_round_boss.setFocusPolicy(Qt.NoFocus)
        self.probe_cal_round_boss.setStyleSheet(u"")
        icon51 = QIcon()
        icon51.addFile(u":/images/probe_cal_round_boss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_cal_round_boss.setIcon(icon51)
        self.probe_cal_round_boss.setIconSize(QSize(140, 140))
        self.probe_cal_round_boss.setAutoDefault(False)

        self.horizontalLayout_60.addWidget(self.probe_cal_round_boss)

        self.widget_21 = QWidget(self.frame_47)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy)
        self.widget_21.setMinimumSize(QSize(130, 150))
        self.widget_21.setMaximumSize(QSize(130, 150))
        self.widget_21.setSizeIncrement(QSize(0, 0))
        self.widget_21.setLayoutDirection(Qt.LeftToRight)
        self.formLayout_2 = QFormLayout(self.widget_21)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(1, 0, 1, 9)
        self.hint_label_4 = QLabel(self.widget_21)
        self.hint_label_4.setObjectName(u"hint_label_4")
        sizePolicy.setHeightForWidth(self.hint_label_4.sizePolicy().hasHeightForWidth())
        self.hint_label_4.setSizePolicy(sizePolicy)
        self.hint_label_4.setMinimumSize(QSize(130, 58))
        self.hint_label_4.setMaximumSize(QSize(130, 58))
        self.hint_label_4.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.hint_label_4.setTextFormat(Qt.RichText)
        self.hint_label_4.setAlignment(Qt.AlignCenter)
        self.hint_label_4.setWordWrap(True)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.hint_label_4)

        self.cal_diameter_3033 = VCPSettingsLineEdit(self.widget_21)
        self.cal_diameter_3033.setObjectName(u"cal_diameter_3033")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.cal_diameter_3033.sizePolicy().hasHeightForWidth())
        self.cal_diameter_3033.setSizePolicy(sizePolicy14)
        self.cal_diameter_3033.setMinimumSize(QSize(130, 35))
        self.cal_diameter_3033.setMaximumSize(QSize(130, 35))
        self.cal_diameter_3033.setFocusPolicy(Qt.ClickFocus)
        self.cal_diameter_3033.setStyleSheet(u"margin-right: 14px;\n"
"margin-left: 14px;")
        self.cal_diameter_3033.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cal_diameter_3033)


        self.horizontalLayout_60.addWidget(self.widget_21)


        self.verticalLayout_46.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setSpacing(9)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(3, 3, 3, 3)
        self.cal_avg_error = VCPSettingsPushButton(self.frame_47)
        self.xycalbtnGroup = QButtonGroup(Form)
        self.xycalbtnGroup.setObjectName(u"xycalbtnGroup")
        self.xycalbtnGroup.addButton(self.cal_avg_error)
        self.cal_avg_error.setObjectName(u"cal_avg_error")
        self.cal_avg_error.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cal_avg_error.sizePolicy().hasHeightForWidth())
        self.cal_avg_error.setSizePolicy(sizePolicy)
        self.cal_avg_error.setMinimumSize(QSize(165, 37))
        self.cal_avg_error.setMaximumSize(QSize(165, 37))
        self.cal_avg_error.setStyleSheet(u"font: 15pt \"Bebas Kai\";")
        self.cal_avg_error.setChecked(True)
        self.cal_avg_error.setAutoExclusive(True)

        self.horizontalLayout_56.addWidget(self.cal_avg_error)

        self.cal_x_error = VCPSettingsPushButton(self.frame_47)
        self.xycalbtnGroup.addButton(self.cal_x_error)
        self.cal_x_error.setObjectName(u"cal_x_error")
        self.cal_x_error.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cal_x_error.sizePolicy().hasHeightForWidth())
        self.cal_x_error.setSizePolicy(sizePolicy)
        self.cal_x_error.setMinimumSize(QSize(140, 37))
        self.cal_x_error.setMaximumSize(QSize(140, 37))
        self.cal_x_error.setStyleSheet(u"font: 15pt \"Bebas Kai\";")
        self.cal_x_error.setAutoExclusive(True)

        self.horizontalLayout_56.addWidget(self.cal_x_error)

        self.cal_y_error = VCPSettingsPushButton(self.frame_47)
        self.xycalbtnGroup.addButton(self.cal_y_error)
        self.cal_y_error.setObjectName(u"cal_y_error")
        self.cal_y_error.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cal_y_error.sizePolicy().hasHeightForWidth())
        self.cal_y_error.setSizePolicy(sizePolicy)
        self.cal_y_error.setMinimumSize(QSize(140, 37))
        self.cal_y_error.setMaximumSize(QSize(140, 37))
        self.cal_y_error.setStyleSheet(u"font: 15pt \"Bebas Kai\";")
        self.cal_y_error.setAutoExclusive(True)

        self.horizontalLayout_56.addWidget(self.cal_y_error)


        self.verticalLayout_46.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setSpacing(21)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(9, 3, -1, 6)
        self.probe_cal_square_pocket = SubCallButton(self.frame_47)
        self.proberoutinebtnGroup.addButton(self.probe_cal_square_pocket)
        self.probe_cal_square_pocket.setObjectName(u"probe_cal_square_pocket")
        self.probe_cal_square_pocket.setMinimumSize(QSize(150, 150))
        self.probe_cal_square_pocket.setMaximumSize(QSize(150, 150))
        self.probe_cal_square_pocket.setFocusPolicy(Qt.NoFocus)
        self.probe_cal_square_pocket.setStyleSheet(u"")
        icon52 = QIcon()
        icon52.addFile(u":/images/probe_cal_square_pocket.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_cal_square_pocket.setIcon(icon52)
        self.probe_cal_square_pocket.setIconSize(QSize(135, 135))

        self.horizontalLayout_62.addWidget(self.probe_cal_square_pocket)

        self.probe_cal_square_boss = SubCallButton(self.frame_47)
        self.proberoutinebtnGroup.addButton(self.probe_cal_square_boss)
        self.probe_cal_square_boss.setObjectName(u"probe_cal_square_boss")
        self.probe_cal_square_boss.setMinimumSize(QSize(150, 150))
        self.probe_cal_square_boss.setMaximumSize(QSize(150, 150))
        self.probe_cal_square_boss.setFocusPolicy(Qt.NoFocus)
        self.probe_cal_square_boss.setStyleSheet(u"")
        icon53 = QIcon()
        icon53.addFile(u":/images/probe_cal_square_boss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.probe_cal_square_boss.setIcon(icon53)
        self.probe_cal_square_boss.setIconSize(QSize(140, 140))

        self.horizontalLayout_62.addWidget(self.probe_cal_square_boss)

        self.widget_18 = QWidget(self.frame_47)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy6.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy6)
        self.widget_18.setMinimumSize(QSize(130, 150))
        self.widget_18.setMaximumSize(QSize(130, 150))
        self.formLayout = QFormLayout(self.widget_18)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(1, 0, 1, 9)
        self.hint_label_3 = QLabel(self.widget_18)
        self.hint_label_3.setObjectName(u"hint_label_3")
        sizePolicy.setHeightForWidth(self.hint_label_3.sizePolicy().hasHeightForWidth())
        self.hint_label_3.setSizePolicy(sizePolicy)
        self.hint_label_3.setMinimumSize(QSize(120, 23))
        self.hint_label_3.setMaximumSize(QSize(130, 0))
        self.hint_label_3.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.hint_label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.hint_label_3)

        self.label_103 = QLabel(self.widget_18)
        self.label_103.setObjectName(u"label_103")
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)
        self.label_103.setMinimumSize(QSize(23, 31))
        self.label_103.setMaximumSize(QSize(23, 31))
        self.label_103.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_103.setLineWidth(0)
        self.label_103.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_103.setIndent(0)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_103)

        self.label_107 = QLabel(self.widget_18)
        self.label_107.setObjectName(u"label_107")
        sizePolicy.setHeightForWidth(self.label_107.sizePolicy().hasHeightForWidth())
        self.label_107.setSizePolicy(sizePolicy)
        self.label_107.setMinimumSize(QSize(23, 31))
        self.label_107.setMaximumSize(QSize(23, 31))
        self.label_107.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_107.setLineWidth(0)
        self.label_107.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_107.setIndent(0)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_107)

        self.x_cal_width_3034 = VCPSettingsLineEdit(self.widget_18)
        self.x_cal_width_3034.setObjectName(u"x_cal_width_3034")
        sizePolicy.setHeightForWidth(self.x_cal_width_3034.sizePolicy().hasHeightForWidth())
        self.x_cal_width_3034.setSizePolicy(sizePolicy)
        self.x_cal_width_3034.setMinimumSize(QSize(87, 35))
        self.x_cal_width_3034.setMaximumSize(QSize(87, 35))
        self.x_cal_width_3034.setFocusPolicy(Qt.ClickFocus)
        self.x_cal_width_3034.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.x_cal_width_3034)

        self.y_cal_width_3035 = VCPSettingsLineEdit(self.widget_18)
        self.y_cal_width_3035.setObjectName(u"y_cal_width_3035")
        sizePolicy.setHeightForWidth(self.y_cal_width_3035.sizePolicy().hasHeightForWidth())
        self.y_cal_width_3035.setSizePolicy(sizePolicy)
        self.y_cal_width_3035.setMinimumSize(QSize(87, 35))
        self.y_cal_width_3035.setMaximumSize(QSize(87, 35))
        self.y_cal_width_3035.setFocusPolicy(Qt.ClickFocus)
        self.y_cal_width_3035.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.y_cal_width_3035)


        self.horizontalLayout_62.addWidget(self.widget_18)


        self.verticalLayout_46.addLayout(self.horizontalLayout_62)


        self.horizontalLayout_55.addWidget(self.frame_47)

        self.probe_tab_widget.addWidget(self.Page7)
        self.Page8 = QWidget()
        self.Page8.setObjectName(u"Page8")
        self.horizontalLayout_5 = QHBoxLayout(self.Page8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.Page8)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(520, 480))
        self.frame.setMaximumSize(QSize(520, 480))
        self.frame.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(206, 209, 202);\n"
"    background-color: rgb(51, 57, 59);\n"
"    border-radius: 8px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.frame)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(3, 6, 3, 12)
        self.probe_help_widget = QStackedWidget(self.frame)
        self.probe_help_widget.setObjectName(u"probe_help_widget")
        sizePolicy14.setHeightForWidth(self.probe_help_widget.sizePolicy().hasHeightForWidth())
        self.probe_help_widget.setSizePolicy(sizePolicy14)
        self.probe_help_widget.setMinimumSize(QSize(0, 410))
        self.probe_help_widget.setMaximumSize(QSize(16777215, 410))
        self.probe_help_widget.setFont(font9)
        self.probe_help_widget.setStyleSheet(u"QStackedWidget{\n"
"border: none;\n"
"background: transparent;\n"
"}")
        self.probe_help_widget.setFrameShape(QFrame.NoFrame)
        self.probe_help_widget.setLineWidth(0)
        self.stackedWidget_4Page1 = QWidget()
        self.stackedWidget_4Page1.setObjectName(u"stackedWidget_4Page1")
        self.horizontalLayout_146 = QHBoxLayout(self.stackedWidget_4Page1)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.label_77 = QLabel(self.stackedWidget_4Page1)
        self.label_77.setObjectName(u"label_77")
        sizePolicy6.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy6)
        self.label_77.setMinimumSize(QSize(450, 400))
        self.label_77.setMaximumSize(QSize(450, 400))
        self.label_77.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/step_off_width.png);\n"
"}")
        self.label_77.setScaledContents(True)
        self.label_77.setIndent(0)

        self.horizontalLayout_146.addWidget(self.label_77)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page1)
        self.stackedWidget_4Page2 = QWidget()
        self.stackedWidget_4Page2.setObjectName(u"stackedWidget_4Page2")
        self.horizontalLayout_148 = QHBoxLayout(self.stackedWidget_4Page2)
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.label_78 = QLabel(self.stackedWidget_4Page2)
        self.label_78.setObjectName(u"label_78")
        sizePolicy6.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy6)
        self.label_78.setMinimumSize(QSize(500, 400))
        self.label_78.setMaximumSize(QSize(500, 400))
        self.label_78.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/extra_probe_depth.png);\n"
"}")
        self.label_78.setScaledContents(True)
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_78.setWordWrap(True)
        self.label_78.setIndent(0)

        self.horizontalLayout_148.addWidget(self.label_78)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page2)
        self.stackedWidget_4Page3 = QWidget()
        self.stackedWidget_4Page3.setObjectName(u"stackedWidget_4Page3")
        self.horizontalLayout_39 = QHBoxLayout(self.stackedWidget_4Page3)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_79 = QLabel(self.stackedWidget_4Page3)
        self.label_79.setObjectName(u"label_79")
        sizePolicy6.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy6)
        self.label_79.setMinimumSize(QSize(440, 400))
        self.label_79.setMaximumSize(QSize(440, 400))
        self.label_79.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/max_z_distance.png);\n"
"}")
        self.label_79.setScaledContents(True)
        self.label_79.setAlignment(Qt.AlignCenter)
        self.label_79.setWordWrap(True)
        self.label_79.setIndent(0)

        self.horizontalLayout_39.addWidget(self.label_79)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page3)
        self.stackedWidget_4Page4 = QWidget()
        self.stackedWidget_4Page4.setObjectName(u"stackedWidget_4Page4")
        self.horizontalLayout_34 = QHBoxLayout(self.stackedWidget_4Page4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_105 = QLabel(self.stackedWidget_4Page4)
        self.label_105.setObjectName(u"label_105")
        sizePolicy6.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy6)
        self.label_105.setMinimumSize(QSize(470, 400))
        self.label_105.setMaximumSize(QSize(470, 400))
        self.label_105.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/max_xy_distance.png);\n"
"}")
        self.label_105.setScaledContents(True)
        self.label_105.setAlignment(Qt.AlignCenter)
        self.label_105.setWordWrap(True)
        self.label_105.setIndent(0)

        self.horizontalLayout_34.addWidget(self.label_105)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page4)
        self.stackedWidget_4Page5 = QWidget()
        self.stackedWidget_4Page5.setObjectName(u"stackedWidget_4Page5")
        self.horizontalLayout_42 = QHBoxLayout(self.stackedWidget_4Page5)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_80 = QLabel(self.stackedWidget_4Page5)
        self.label_80.setObjectName(u"label_80")
        sizePolicy6.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy6)
        self.label_80.setMinimumSize(QSize(450, 400))
        self.label_80.setMaximumSize(QSize(450, 400))
        self.label_80.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/z_clearance.png);\n"
"}")
        self.label_80.setScaledContents(True)
        self.label_80.setAlignment(Qt.AlignCenter)
        self.label_80.setWordWrap(True)
        self.label_80.setIndent(0)

        self.horizontalLayout_42.addWidget(self.label_80)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page5)
        self.stackedWidget_4Page6 = QWidget()
        self.stackedWidget_4Page6.setObjectName(u"stackedWidget_4Page6")
        self.horizontalLayout_35 = QHBoxLayout(self.stackedWidget_4Page6)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_106 = QLabel(self.stackedWidget_4Page6)
        self.label_106.setObjectName(u"label_106")
        sizePolicy6.setHeightForWidth(self.label_106.sizePolicy().hasHeightForWidth())
        self.label_106.setSizePolicy(sizePolicy6)
        self.label_106.setMinimumSize(QSize(480, 400))
        self.label_106.setMaximumSize(QSize(480, 400))
        self.label_106.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"	image: url(:/images/xy_clearance.png);\n"
"}")
        self.label_106.setScaledContents(True)
        self.label_106.setAlignment(Qt.AlignCenter)
        self.label_106.setWordWrap(True)
        self.label_106.setIndent(0)

        self.horizontalLayout_35.addWidget(self.label_106)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page6)
        self.stackedWidget_4Page7 = QWidget()
        self.stackedWidget_4Page7.setObjectName(u"stackedWidget_4Page7")
        self.verticalLayout_18 = QVBoxLayout(self.stackedWidget_4Page7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_41 = QLabel(self.stackedWidget_4Page7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(480, 400))
        self.label_41.setMaximumSize(QSize(480, 400))
        self.label_41.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"    padding: 5px;\n"
"	image: url(:/images/probing_hints.png);\n"
"}")
        self.label_41.setScaledContents(True)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_41)

        self.probe_help_widget.addWidget(self.stackedWidget_4Page7)

        self.verticalLayout_21.addWidget(self.probe_help_widget, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.probe_help_Group_select = QWidget(self.frame)
        self.probe_help_Group_select.setObjectName(u"probe_help_Group_select")
        sizePolicy14.setHeightForWidth(self.probe_help_Group_select.sizePolicy().hasHeightForWidth())
        self.probe_help_Group_select.setSizePolicy(sizePolicy14)
        self.probe_help_Group_select.setMinimumSize(QSize(0, 40))
        self.probe_help_Group_select.setMaximumSize(QSize(16777215, 40))
        self.probe_help_Group_select.setStyleSheet(u"")
        self.horizontalLayout_44 = QHBoxLayout(self.probe_help_Group_select)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(70, 1, 70, 1)
        self.probe_help_prev = QPushButton(self.probe_help_Group_select)
        self.probehelpGroup = QButtonGroup(Form)
        self.probehelpGroup.setObjectName(u"probehelpGroup")
        self.probehelpGroup.addButton(self.probe_help_prev)
        self.probe_help_prev.setObjectName(u"probe_help_prev")
        sizePolicy.setHeightForWidth(self.probe_help_prev.sizePolicy().hasHeightForWidth())
        self.probe_help_prev.setSizePolicy(sizePolicy)
        self.probe_help_prev.setMinimumSize(QSize(150, 37))
        self.probe_help_prev.setMaximumSize(QSize(150, 37))
        self.probe_help_prev.setFocusPolicy(Qt.NoFocus)
        self.probe_help_prev.setStyleSheet(u"QPushButton{\n"
"    padding-left: 0px;\n"
"    padding-right: 0px;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.probe_help_prev.setIcon(icon4)
        self.probe_help_prev.setIconSize(QSize(16, 16))
        self.probe_help_prev.setCheckable(False)
        self.probe_help_prev.setChecked(False)
        self.probe_help_prev.setAutoExclusive(True)

        self.horizontalLayout_44.addWidget(self.probe_help_prev)

        self.probe_help_next = QPushButton(self.probe_help_Group_select)
        self.probehelpGroup.addButton(self.probe_help_next)
        self.probe_help_next.setObjectName(u"probe_help_next")
        sizePolicy.setHeightForWidth(self.probe_help_next.sizePolicy().hasHeightForWidth())
        self.probe_help_next.setSizePolicy(sizePolicy)
        self.probe_help_next.setMinimumSize(QSize(150, 37))
        self.probe_help_next.setMaximumSize(QSize(150, 37))
        self.probe_help_next.setFocusPolicy(Qt.NoFocus)
        self.probe_help_next.setLayoutDirection(Qt.RightToLeft)
        self.probe_help_next.setStyleSheet(u"QPushButton{\n"
"    padding-left: 0px;\n"
"    padding-right: 0px;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.probe_help_next.setIcon(icon6)
        self.probe_help_next.setIconSize(QSize(16, 16))
        self.probe_help_next.setCheckable(False)
        self.probe_help_next.setAutoExclusive(True)

        self.horizontalLayout_44.addWidget(self.probe_help_next)


        self.verticalLayout_21.addWidget(self.probe_help_Group_select)


        self.horizontalLayout_5.addWidget(self.frame)

        self.probe_tab_widget.addWidget(self.Page8)

        self.verticalLayout_3.addWidget(self.probe_tab_widget)


        self.horizontalLayout_31.addLayout(self.verticalLayout_3)

        self.widget_61 = QWidget(self.widget_11)
        self.widget_61.setObjectName(u"widget_61")
        sizePolicy4.setHeightForWidth(self.widget_61.sizePolicy().hasHeightForWidth())
        self.widget_61.setSizePolicy(sizePolicy4)

        self.horizontalLayout_31.addWidget(self.widget_61)


        self.verticalLayout_45.addWidget(self.widget_11)


        self.horizontalLayout_22.addWidget(self.widget_13)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_27 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_27.setSpacing(9)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.tab_2)
        self.widget_46.setObjectName(u"widget_46")
        sizePolicy4.setHeightForWidth(self.widget_46.sizePolicy().hasHeightForWidth())
        self.widget_46.setSizePolicy(sizePolicy4)
        self.widget_46.setMinimumSize(QSize(530, 0))
        self.widget_46.setMaximumSize(QSize(530, 16777215))
        self.widget_46.setStyleSheet(u".QWidget {\n"
"    background-color: #929695;;\n"
"}")
        self.verticalLayout_48 = QVBoxLayout(self.widget_46)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(9, 5, 6, 9)
        self.work_column_header_11 = QLabel(self.widget_46)
        self.work_column_header_11.setObjectName(u"work_column_header_11")
        self.work_column_header_11.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.work_column_header_11.sizePolicy().hasHeightForWidth())
        self.work_column_header_11.setSizePolicy(sizePolicy6)
        self.work_column_header_11.setMinimumSize(QSize(0, 30))
        self.work_column_header_11.setMaximumSize(QSize(16777215, 27))
        self.work_column_header_11.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_11.setFrameShape(QFrame.NoFrame)
        self.work_column_header_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.work_column_header_11.setWordWrap(True)
        self.work_column_header_11.setIndent(10)

        self.verticalLayout_48.addWidget(self.work_column_header_11)

        self.widget_52 = QWidget(self.widget_46)
        self.widget_52.setObjectName(u"widget_52")
        sizePolicy1.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy1)
        self.widget_52.setMinimumSize(QSize(500, 0))
        self.widget_52.setMaximumSize(QSize(500, 16777215))
        self.widget_52.setStyleSheet(u".QFrame{\n"
"    background-color: #929695;\n"
"}\n"
"")
        self.verticalLayout_72 = QVBoxLayout(self.widget_52)
        self.verticalLayout_72.setSpacing(3)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setSpacing(12)
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.horizontalLayout_179.setContentsMargins(12, 1, 6, 1)
        self.probe_spindle_nose_subcallbutton = SubCallButton(self.widget_52)
        self.probe_spindle_nose_subcallbutton.setObjectName(u"probe_spindle_nose_subcallbutton")
        sizePolicy.setHeightForWidth(self.probe_spindle_nose_subcallbutton.sizePolicy().hasHeightForWidth())
        self.probe_spindle_nose_subcallbutton.setSizePolicy(sizePolicy)
        self.probe_spindle_nose_subcallbutton.setMinimumSize(QSize(250, 38))
        self.probe_spindle_nose_subcallbutton.setMaximumSize(QSize(250, 38))

        self.horizontalLayout_179.addWidget(self.probe_spindle_nose_subcallbutton)

        self.widget_71 = QWidget(self.widget_52)
        self.widget_71.setObjectName(u"widget_71")

        self.horizontalLayout_179.addWidget(self.widget_71)

        self.label_135 = QLabel(self.widget_52)
        self.label_135.setObjectName(u"label_135")
        sizePolicy.setHeightForWidth(self.label_135.sizePolicy().hasHeightForWidth())
        self.label_135.setSizePolicy(sizePolicy)
        self.label_135.setMinimumSize(QSize(100, 38))
        self.label_135.setMaximumSize(QSize(100, 38))
        self.label_135.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_135.setLineWidth(0)
        self.label_135.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_135.setIndent(0)

        self.horizontalLayout_179.addWidget(self.label_135)

        self.spindle_zero_height_3010 = VCPSettingsLineEdit(self.widget_52)
        self.spindle_zero_height_3010.setObjectName(u"spindle_zero_height_3010")
        self.spindle_zero_height_3010.setEnabled(False)
        sizePolicy.setHeightForWidth(self.spindle_zero_height_3010.sizePolicy().hasHeightForWidth())
        self.spindle_zero_height_3010.setSizePolicy(sizePolicy)
        self.spindle_zero_height_3010.setMinimumSize(QSize(100, 31))
        self.spindle_zero_height_3010.setMaximumSize(QSize(100, 31))
        font10 = QFont()
        font10.setFamilies([u"bebas kai"])
        font10.setPointSize(15)
        font10.setBold(False)
        font10.setItalic(False)
        self.spindle_zero_height_3010.setFont(font10)
        self.spindle_zero_height_3010.setFocusPolicy(Qt.ClickFocus)
        self.spindle_zero_height_3010.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.spindle_zero_height_3010.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_179.addWidget(self.spindle_zero_height_3010)


        self.verticalLayout_72.addLayout(self.horizontalLayout_179)

        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setSpacing(12)
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.horizontalLayout_180.setContentsMargins(12, 1, 6, 1)
        self.label_59 = QLabel(self.widget_52)
        self.label_59.setObjectName(u"label_59")
        sizePolicy.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy)
        self.label_59.setMinimumSize(QSize(23, 33))
        self.label_59.setMaximumSize(QSize(23, 33))
        self.label_59.setStyleSheet(u"QLabel{\n"
"font: 75 16pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_180.addWidget(self.label_59)

        self.widget_72 = QWidget(self.widget_52)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setMinimumSize(QSize(20, 0))
        self.widget_72.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_180.addWidget(self.widget_72)

        self.x_tool_change_position = VCPSettingsLineEdit(self.widget_52)
        self.x_tool_change_position.setObjectName(u"x_tool_change_position")
        sizePolicy.setHeightForWidth(self.x_tool_change_position.sizePolicy().hasHeightForWidth())
        self.x_tool_change_position.setSizePolicy(sizePolicy)
        self.x_tool_change_position.setMinimumSize(QSize(110, 31))
        self.x_tool_change_position.setMaximumSize(QSize(110, 31))
        self.x_tool_change_position.setFocusPolicy(Qt.ClickFocus)
        self.x_tool_change_position.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_tool_change_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.x_tool_change_position.setReadOnly(True)

        self.horizontalLayout_180.addWidget(self.x_tool_change_position)

        self.widget_70 = QWidget(self.widget_52)
        self.widget_70.setObjectName(u"widget_70")

        self.horizontalLayout_180.addWidget(self.widget_70)

        self.label_5 = QLabel(self.widget_52)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 38))
        self.label_5.setMaximumSize(QSize(100, 38))
        self.label_5.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_5.setLineWidth(0)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5.setIndent(0)

        self.horizontalLayout_180.addWidget(self.label_5)

        self.fast_probe_fr_3004 = VCPSettingsLineEdit(self.widget_52)
        self.fast_probe_fr_3004.setObjectName(u"fast_probe_fr_3004")
        sizePolicy.setHeightForWidth(self.fast_probe_fr_3004.sizePolicy().hasHeightForWidth())
        self.fast_probe_fr_3004.setSizePolicy(sizePolicy)
        self.fast_probe_fr_3004.setMinimumSize(QSize(100, 31))
        self.fast_probe_fr_3004.setMaximumSize(QSize(100, 31))
        self.fast_probe_fr_3004.setFont(font10)
        self.fast_probe_fr_3004.setFocusPolicy(Qt.ClickFocus)
        self.fast_probe_fr_3004.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.fast_probe_fr_3004.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_180.addWidget(self.fast_probe_fr_3004)


        self.verticalLayout_72.addLayout(self.horizontalLayout_180)

        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setSpacing(12)
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.horizontalLayout_181.setContentsMargins(12, 1, 6, 1)
        self.label_60 = QLabel(self.widget_52)
        self.label_60.setObjectName(u"label_60")
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QSize(23, 33))
        self.label_60.setMaximumSize(QSize(23, 33))
        self.label_60.setStyleSheet(u"QLabel{\n"
"font: 75 16pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_181.addWidget(self.label_60)

        self.widget_74 = QWidget(self.widget_52)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setMinimumSize(QSize(20, 0))
        self.widget_74.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_181.addWidget(self.widget_74)

        self.y_tool_change_position = VCPSettingsLineEdit(self.widget_52)
        self.y_tool_change_position.setObjectName(u"y_tool_change_position")
        sizePolicy.setHeightForWidth(self.y_tool_change_position.sizePolicy().hasHeightForWidth())
        self.y_tool_change_position.setSizePolicy(sizePolicy)
        self.y_tool_change_position.setMinimumSize(QSize(110, 31))
        self.y_tool_change_position.setMaximumSize(QSize(110, 31))
        self.y_tool_change_position.setFocusPolicy(Qt.ClickFocus)
        self.y_tool_change_position.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.y_tool_change_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.y_tool_change_position.setReadOnly(True)

        self.horizontalLayout_181.addWidget(self.y_tool_change_position)

        self.widget_73 = QWidget(self.widget_52)
        self.widget_73.setObjectName(u"widget_73")

        self.horizontalLayout_181.addWidget(self.widget_73)

        self.label_120 = QLabel(self.widget_52)
        self.label_120.setObjectName(u"label_120")
        sizePolicy.setHeightForWidth(self.label_120.sizePolicy().hasHeightForWidth())
        self.label_120.setSizePolicy(sizePolicy)
        self.label_120.setMinimumSize(QSize(100, 38))
        self.label_120.setMaximumSize(QSize(100, 38))
        self.label_120.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_120.setLineWidth(0)
        self.label_120.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_120.setIndent(0)

        self.horizontalLayout_181.addWidget(self.label_120)

        self.slow_probe_fr_3005 = VCPSettingsLineEdit(self.widget_52)
        self.slow_probe_fr_3005.setObjectName(u"slow_probe_fr_3005")
        sizePolicy.setHeightForWidth(self.slow_probe_fr_3005.sizePolicy().hasHeightForWidth())
        self.slow_probe_fr_3005.setSizePolicy(sizePolicy)
        self.slow_probe_fr_3005.setMinimumSize(QSize(100, 31))
        self.slow_probe_fr_3005.setMaximumSize(QSize(100, 31))
        self.slow_probe_fr_3005.setFont(font10)
        self.slow_probe_fr_3005.setFocusPolicy(Qt.ClickFocus)
        self.slow_probe_fr_3005.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.slow_probe_fr_3005.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_181.addWidget(self.slow_probe_fr_3005)


        self.verticalLayout_72.addLayout(self.horizontalLayout_181)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setSpacing(12)
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_194.setContentsMargins(12, 1, 6, 1)
        self.label_61 = QLabel(self.widget_52)
        self.label_61.setObjectName(u"label_61")
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QSize(23, 33))
        self.label_61.setMaximumSize(QSize(23, 33))
        self.label_61.setStyleSheet(u"QLabel{\n"
"font: 75 16pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_194.addWidget(self.label_61)

        self.widget_75 = QWidget(self.widget_52)
        self.widget_75.setObjectName(u"widget_75")
        self.widget_75.setMinimumSize(QSize(20, 0))
        self.widget_75.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_194.addWidget(self.widget_75)

        self.z_tool_change_position = VCPSettingsLineEdit(self.widget_52)
        self.z_tool_change_position.setObjectName(u"z_tool_change_position")
        sizePolicy.setHeightForWidth(self.z_tool_change_position.sizePolicy().hasHeightForWidth())
        self.z_tool_change_position.setSizePolicy(sizePolicy)
        self.z_tool_change_position.setMinimumSize(QSize(110, 31))
        self.z_tool_change_position.setMaximumSize(QSize(110, 31))
        self.z_tool_change_position.setFocusPolicy(Qt.ClickFocus)
        self.z_tool_change_position.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.z_tool_change_position.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.z_tool_change_position.setReadOnly(True)

        self.horizontalLayout_194.addWidget(self.z_tool_change_position)

        self.widget_67 = QWidget(self.widget_52)
        self.widget_67.setObjectName(u"widget_67")

        self.horizontalLayout_194.addWidget(self.widget_67)

        self.label_134 = QLabel(self.widget_52)
        self.label_134.setObjectName(u"label_134")
        sizePolicy.setHeightForWidth(self.label_134.sizePolicy().hasHeightForWidth())
        self.label_134.setSizePolicy(sizePolicy)
        self.label_134.setMinimumSize(QSize(100, 38))
        self.label_134.setMaximumSize(QSize(100, 38))
        self.label_134.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_134.setLineWidth(0)
        self.label_134.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_134.setIndent(0)

        self.horizontalLayout_194.addWidget(self.label_134)

        self.traverse_fr_3006 = VCPSettingsLineEdit(self.widget_52)
        self.traverse_fr_3006.setObjectName(u"traverse_fr_3006")
        sizePolicy.setHeightForWidth(self.traverse_fr_3006.sizePolicy().hasHeightForWidth())
        self.traverse_fr_3006.setSizePolicy(sizePolicy)
        self.traverse_fr_3006.setMinimumSize(QSize(100, 31))
        self.traverse_fr_3006.setMaximumSize(QSize(100, 31))
        self.traverse_fr_3006.setFont(font10)
        self.traverse_fr_3006.setFocusPolicy(Qt.ClickFocus)
        self.traverse_fr_3006.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.traverse_fr_3006.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_194.addWidget(self.traverse_fr_3006)


        self.verticalLayout_72.addLayout(self.horizontalLayout_194)

        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setSpacing(12)
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.horizontalLayout_183.setContentsMargins(12, 1, 6, 1)
        self.set_g30_1_position = SubCallButton(self.widget_52)
        self.set_g30_1_position.setObjectName(u"set_g30_1_position")
        sizePolicy2.setHeightForWidth(self.set_g30_1_position.sizePolicy().hasHeightForWidth())
        self.set_g30_1_position.setSizePolicy(sizePolicy2)
        self.set_g30_1_position.setMinimumSize(QSize(185, 38))
        self.set_g30_1_position.setMaximumSize(QSize(185, 38))
        self.set_g30_1_position.setFocusPolicy(Qt.NoFocus)
        self.set_g30_1_position.setStyleSheet(u".SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
".SubCallButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 2"
                        "55));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_183.addWidget(self.set_g30_1_position)

        self.widget_66 = QWidget(self.widget_52)
        self.widget_66.setObjectName(u"widget_66")

        self.horizontalLayout_183.addWidget(self.widget_66)

        self.label_129 = QLabel(self.widget_52)
        self.label_129.setObjectName(u"label_129")
        sizePolicy.setHeightForWidth(self.label_129.sizePolicy().hasHeightForWidth())
        self.label_129.setSizePolicy(sizePolicy)
        self.label_129.setMinimumSize(QSize(100, 38))
        self.label_129.setMaximumSize(QSize(100, 38))
        self.label_129.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_129.setLineWidth(0)
        self.label_129.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_129.setIndent(0)

        self.horizontalLayout_183.addWidget(self.label_129)

        self.z_max_travel_3007 = VCPSettingsLineEdit(self.widget_52)
        self.z_max_travel_3007.setObjectName(u"z_max_travel_3007")
        sizePolicy.setHeightForWidth(self.z_max_travel_3007.sizePolicy().hasHeightForWidth())
        self.z_max_travel_3007.setSizePolicy(sizePolicy)
        self.z_max_travel_3007.setMinimumSize(QSize(100, 31))
        self.z_max_travel_3007.setMaximumSize(QSize(100, 31))
        self.z_max_travel_3007.setFont(font10)
        self.z_max_travel_3007.setFocusPolicy(Qt.ClickFocus)
        self.z_max_travel_3007.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.z_max_travel_3007.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_183.addWidget(self.z_max_travel_3007)


        self.verticalLayout_72.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setSpacing(12)
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_182.setContentsMargins(12, 1, 6, 1)
        self.tool_diameter_probe_Btn = VCPSettingsPushButton(self.widget_52)
        self.tool_diameter_probe_Btn.setObjectName(u"tool_diameter_probe_Btn")
        self.tool_diameter_probe_Btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tool_diameter_probe_Btn.sizePolicy().hasHeightForWidth())
        self.tool_diameter_probe_Btn.setSizePolicy(sizePolicy)
        self.tool_diameter_probe_Btn.setMinimumSize(QSize(150, 38))
        self.tool_diameter_probe_Btn.setMaximumSize(QSize(150, 38))
        self.tool_diameter_probe_Btn.setStyleSheet(u"font: 14pt \"Bebas Kai\";")

        self.horizontalLayout_182.addWidget(self.tool_diameter_probe_Btn)

        self.tool_diameter_probe_mode_3011 = VCPLineEdit(self.widget_52)
        self.tool_diameter_probe_mode_3011.setObjectName(u"tool_diameter_probe_mode_3011")
        sizePolicy.setHeightForWidth(self.tool_diameter_probe_mode_3011.sizePolicy().hasHeightForWidth())
        self.tool_diameter_probe_mode_3011.setSizePolicy(sizePolicy)
        self.tool_diameter_probe_mode_3011.setMinimumSize(QSize(70, 31))
        self.tool_diameter_probe_mode_3011.setMaximumSize(QSize(70, 31))
        self.tool_diameter_probe_mode_3011.setAlignment(Qt.AlignCenter)
        self.tool_diameter_probe_mode_3011.setReadOnly(True)

        self.horizontalLayout_182.addWidget(self.tool_diameter_probe_mode_3011)

        self.widget_55 = QWidget(self.widget_52)
        self.widget_55.setObjectName(u"widget_55")

        self.horizontalLayout_182.addWidget(self.widget_55)

        self.label_133 = QLabel(self.widget_52)
        self.label_133.setObjectName(u"label_133")
        sizePolicy.setHeightForWidth(self.label_133.sizePolicy().hasHeightForWidth())
        self.label_133.setSizePolicy(sizePolicy)
        self.label_133.setMinimumSize(QSize(100, 38))
        self.label_133.setMaximumSize(QSize(100, 38))
        self.label_133.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_133.setLineWidth(0)
        self.label_133.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_133.setIndent(0)

        self.horizontalLayout_182.addWidget(self.label_133)

        self.xy_max_travel_3008 = VCPSettingsLineEdit(self.widget_52)
        self.xy_max_travel_3008.setObjectName(u"xy_max_travel_3008")
        sizePolicy.setHeightForWidth(self.xy_max_travel_3008.sizePolicy().hasHeightForWidth())
        self.xy_max_travel_3008.setSizePolicy(sizePolicy)
        self.xy_max_travel_3008.setMinimumSize(QSize(100, 31))
        self.xy_max_travel_3008.setMaximumSize(QSize(100, 31))
        self.xy_max_travel_3008.setFont(font10)
        self.xy_max_travel_3008.setFocusPolicy(Qt.ClickFocus)
        self.xy_max_travel_3008.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.xy_max_travel_3008.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_182.addWidget(self.xy_max_travel_3008)


        self.verticalLayout_72.addLayout(self.horizontalLayout_182)

        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setSpacing(12)
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.horizontalLayout_187.setContentsMargins(12, 1, 6, 1)
        self.tool_diameter_offset_Btn = VCPSettingsPushButton(self.widget_52)
        self.tool_diameter_offset_Btn.setObjectName(u"tool_diameter_offset_Btn")
        sizePolicy.setHeightForWidth(self.tool_diameter_offset_Btn.sizePolicy().hasHeightForWidth())
        self.tool_diameter_offset_Btn.setSizePolicy(sizePolicy)
        self.tool_diameter_offset_Btn.setMinimumSize(QSize(150, 38))
        self.tool_diameter_offset_Btn.setMaximumSize(QSize(150, 38))
        self.tool_diameter_offset_Btn.setStyleSheet(u"font: 14pt \"Bebas Kai\"")

        self.horizontalLayout_187.addWidget(self.tool_diameter_offset_Btn)

        self.tool_diameter_offset_mode_3012 = VCPLineEdit(self.widget_52)
        self.tool_diameter_offset_mode_3012.setObjectName(u"tool_diameter_offset_mode_3012")
        sizePolicy.setHeightForWidth(self.tool_diameter_offset_mode_3012.sizePolicy().hasHeightForWidth())
        self.tool_diameter_offset_mode_3012.setSizePolicy(sizePolicy)
        self.tool_diameter_offset_mode_3012.setMinimumSize(QSize(70, 31))
        self.tool_diameter_offset_mode_3012.setMaximumSize(QSize(70, 31))
        self.tool_diameter_offset_mode_3012.setAlignment(Qt.AlignCenter)
        self.tool_diameter_offset_mode_3012.setReadOnly(True)

        self.horizontalLayout_187.addWidget(self.tool_diameter_offset_mode_3012)

        self.widget_57 = QWidget(self.widget_52)
        self.widget_57.setObjectName(u"widget_57")

        self.horizontalLayout_187.addWidget(self.widget_57)

        self.label_147 = QLabel(self.widget_52)
        self.label_147.setObjectName(u"label_147")
        sizePolicy.setHeightForWidth(self.label_147.sizePolicy().hasHeightForWidth())
        self.label_147.setSizePolicy(sizePolicy)
        self.label_147.setMinimumSize(QSize(100, 38))
        self.label_147.setMaximumSize(QSize(100, 38))
        self.label_147.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_147.setLineWidth(0)
        self.label_147.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_147.setIndent(0)

        self.horizontalLayout_187.addWidget(self.label_147)

        self.retract_distance_3009 = VCPSettingsLineEdit(self.widget_52)
        self.retract_distance_3009.setObjectName(u"retract_distance_3009")
        sizePolicy.setHeightForWidth(self.retract_distance_3009.sizePolicy().hasHeightForWidth())
        self.retract_distance_3009.setSizePolicy(sizePolicy)
        self.retract_distance_3009.setMinimumSize(QSize(100, 31))
        self.retract_distance_3009.setMaximumSize(QSize(100, 31))
        self.retract_distance_3009.setFont(font10)
        self.retract_distance_3009.setFocusPolicy(Qt.ClickFocus)
        self.retract_distance_3009.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.retract_distance_3009.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_187.addWidget(self.retract_distance_3009)


        self.verticalLayout_72.addLayout(self.horizontalLayout_187)

        self.horizontalLayout_196 = QHBoxLayout()
        self.horizontalLayout_196.setSpacing(12)
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.horizontalLayout_196.setContentsMargins(6, 1, 6, 1)
        self.label_153 = QLabel(self.widget_52)
        self.label_153.setObjectName(u"label_153")
        sizePolicy2.setHeightForWidth(self.label_153.sizePolicy().hasHeightForWidth())
        self.label_153.setSizePolicy(sizePolicy2)
        self.label_153.setMinimumSize(QSize(0, 38))
        self.label_153.setMaximumSize(QSize(16777215, 38))
        self.label_153.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"padding-left: 12px;\n"
"}")
        self.label_153.setLineWidth(0)
        self.label_153.setAlignment(Qt.AlignCenter)
        self.label_153.setIndent(0)

        self.horizontalLayout_196.addWidget(self.label_153)

        self.label_150 = QLabel(self.widget_52)
        self.label_150.setObjectName(u"label_150")
        sizePolicy.setHeightForWidth(self.label_150.sizePolicy().hasHeightForWidth())
        self.label_150.setSizePolicy(sizePolicy)
        self.label_150.setMinimumSize(QSize(150, 38))
        self.label_150.setMaximumSize(QSize(100, 38))
        self.label_150.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_150.setLineWidth(0)
        self.label_150.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_150.setIndent(0)

        self.horizontalLayout_196.addWidget(self.label_150)

        self.breakage_tolerance_3037 = VCPSettingsLineEdit(self.widget_52)
        self.breakage_tolerance_3037.setObjectName(u"breakage_tolerance_3037")
        sizePolicy.setHeightForWidth(self.breakage_tolerance_3037.sizePolicy().hasHeightForWidth())
        self.breakage_tolerance_3037.setSizePolicy(sizePolicy)
        self.breakage_tolerance_3037.setMinimumSize(QSize(100, 31))
        self.breakage_tolerance_3037.setMaximumSize(QSize(100, 31))
        self.breakage_tolerance_3037.setFont(font10)
        self.breakage_tolerance_3037.setFocusPolicy(Qt.ClickFocus)
        self.breakage_tolerance_3037.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.breakage_tolerance_3037.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_196.addWidget(self.breakage_tolerance_3037)


        self.verticalLayout_72.addLayout(self.horizontalLayout_196)

        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setSpacing(12)
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.horizontalLayout_189.setContentsMargins(6, 1, 6, 1)
        self.widget_79 = QWidget(self.widget_52)
        self.widget_79.setObjectName(u"widget_79")
        self.widget_79.setEnabled(False)
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy15.setHorizontalStretch(2)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.widget_79.sizePolicy().hasHeightForWidth())
        self.widget_79.setSizePolicy(sizePolicy15)
        self.widget_79.setMinimumSize(QSize(65, 0))

        self.horizontalLayout_189.addWidget(self.widget_79)

        self.tool_setter_offset_left_Btn_2 = VCPSettingsPushButton(self.widget_52)
        self.tooloffsetdirbtnGroup = QButtonGroup(Form)
        self.tooloffsetdirbtnGroup.setObjectName(u"tooloffsetdirbtnGroup")
        self.tooloffsetdirbtnGroup.addButton(self.tool_setter_offset_left_Btn_2)
        self.tool_setter_offset_left_Btn_2.setObjectName(u"tool_setter_offset_left_Btn_2")
        self.tool_setter_offset_left_Btn_2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tool_setter_offset_left_Btn_2.sizePolicy().hasHeightForWidth())
        self.tool_setter_offset_left_Btn_2.setSizePolicy(sizePolicy)
        self.tool_setter_offset_left_Btn_2.setMinimumSize(QSize(73, 38))
        self.tool_setter_offset_left_Btn_2.setMaximumSize(QSize(73, 38))
        self.tool_setter_offset_left_Btn_2.setStyleSheet(u"font: 14pt \"Bebas Kai\"")
        self.tool_setter_offset_left_Btn_2.setIcon(icon1)
        self.tool_setter_offset_left_Btn_2.setIconSize(QSize(16, 16))
        self.tool_setter_offset_left_Btn_2.setChecked(False)
        self.tool_setter_offset_left_Btn_2.setAutoExclusive(False)
        self.tool_setter_offset_left_Btn_2.setProperty(u"page", 0)

        self.horizontalLayout_189.addWidget(self.tool_setter_offset_left_Btn_2)

        self.widget_82 = QWidget(self.widget_52)
        self.widget_82.setObjectName(u"widget_82")
        self.widget_82.setEnabled(False)
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy16.setHorizontalStretch(2)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.widget_82.sizePolicy().hasHeightForWidth())
        self.widget_82.setSizePolicy(sizePolicy16)
        self.widget_82.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_189.addWidget(self.widget_82)

        self.tool_setter_user_1_name = VCPSettingsLineEdit(self.widget_52)
        self.tool_setter_user_1_name.setObjectName(u"tool_setter_user_1_name")
        self.tool_setter_user_1_name.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.tool_setter_user_1_name.sizePolicy().hasHeightForWidth())
        self.tool_setter_user_1_name.setSizePolicy(sizePolicy6)
        self.tool_setter_user_1_name.setMinimumSize(QSize(0, 38))
        self.tool_setter_user_1_name.setMaximumSize(QSize(16777215, 38))
        self.tool_setter_user_1_name.setFocusPolicy(Qt.ClickFocus)
        self.tool_setter_user_1_name.setStyleSheet(u"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"background-color: #929695;")
        self.tool_setter_user_1_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_189.addWidget(self.tool_setter_user_1_name)

        self.user_setter_1_3038 = VCPSettingsLineEdit(self.widget_52)
        self.user_setter_1_3038.setObjectName(u"user_setter_1_3038")
        sizePolicy.setHeightForWidth(self.user_setter_1_3038.sizePolicy().hasHeightForWidth())
        self.user_setter_1_3038.setSizePolicy(sizePolicy)
        self.user_setter_1_3038.setMinimumSize(QSize(100, 31))
        self.user_setter_1_3038.setMaximumSize(QSize(100, 31))
        self.user_setter_1_3038.setFont(font10)
        self.user_setter_1_3038.setFocusPolicy(Qt.ClickFocus)
        self.user_setter_1_3038.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.user_setter_1_3038.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_189.addWidget(self.user_setter_1_3038)


        self.verticalLayout_72.addLayout(self.horizontalLayout_189)

        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setSpacing(12)
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.horizontalLayout_186.setContentsMargins(6, 1, 6, 1)
        self.tool_setter_offset_left_Btn = VCPSettingsPushButton(self.widget_52)
        self.tooloffsetdirbtnGroup.addButton(self.tool_setter_offset_left_Btn)
        self.tool_setter_offset_left_Btn.setObjectName(u"tool_setter_offset_left_Btn")
        self.tool_setter_offset_left_Btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tool_setter_offset_left_Btn.sizePolicy().hasHeightForWidth())
        self.tool_setter_offset_left_Btn.setSizePolicy(sizePolicy)
        self.tool_setter_offset_left_Btn.setMinimumSize(QSize(73, 38))
        self.tool_setter_offset_left_Btn.setMaximumSize(QSize(73, 38))
        self.tool_setter_offset_left_Btn.setStyleSheet(u"font: 14pt \"Bebas Kai\"")
        self.tool_setter_offset_left_Btn.setIcon(icon4)
        self.tool_setter_offset_left_Btn.setIconSize(QSize(16, 16))
        self.tool_setter_offset_left_Btn.setChecked(True)
        self.tool_setter_offset_left_Btn.setAutoExclusive(False)
        self.tool_setter_offset_left_Btn.setProperty(u"page", 0)

        self.horizontalLayout_186.addWidget(self.tool_setter_offset_left_Btn)

        self.tool_setter_offset_direction_3013 = VCPLineEdit(self.widget_52)
        self.tool_setter_offset_direction_3013.setObjectName(u"tool_setter_offset_direction_3013")
        sizePolicy.setHeightForWidth(self.tool_setter_offset_direction_3013.sizePolicy().hasHeightForWidth())
        self.tool_setter_offset_direction_3013.setSizePolicy(sizePolicy)
        self.tool_setter_offset_direction_3013.setMinimumSize(QSize(60, 35))
        self.tool_setter_offset_direction_3013.setMaximumSize(QSize(60, 35))
        self.tool_setter_offset_direction_3013.setLayoutDirection(Qt.LeftToRight)
        self.tool_setter_offset_direction_3013.setCursorPosition(1)
        self.tool_setter_offset_direction_3013.setAlignment(Qt.AlignCenter)
        self.tool_setter_offset_direction_3013.setReadOnly(True)

        self.horizontalLayout_186.addWidget(self.tool_setter_offset_direction_3013)

        self.tool_setter_offset_right_Btn = VCPSettingsPushButton(self.widget_52)
        self.tooloffsetdirbtnGroup.addButton(self.tool_setter_offset_right_Btn)
        self.tool_setter_offset_right_Btn.setObjectName(u"tool_setter_offset_right_Btn")
        self.tool_setter_offset_right_Btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tool_setter_offset_right_Btn.sizePolicy().hasHeightForWidth())
        self.tool_setter_offset_right_Btn.setSizePolicy(sizePolicy)
        self.tool_setter_offset_right_Btn.setMinimumSize(QSize(73, 38))
        self.tool_setter_offset_right_Btn.setMaximumSize(QSize(73, 38))
        self.tool_setter_offset_right_Btn.setLayoutDirection(Qt.RightToLeft)
        self.tool_setter_offset_right_Btn.setStyleSheet(u"font: 14pt \"Bebas Kai\"")
        self.tool_setter_offset_right_Btn.setIcon(icon6)
        self.tool_setter_offset_right_Btn.setIconSize(QSize(16, 16))
        self.tool_setter_offset_right_Btn.setAutoExclusive(False)
        self.tool_setter_offset_right_Btn.setFlat(False)
        self.tool_setter_offset_right_Btn.setProperty(u"page", 1)

        self.horizontalLayout_186.addWidget(self.tool_setter_offset_right_Btn)

        self.widget_83 = QWidget(self.widget_52)
        self.widget_83.setObjectName(u"widget_83")
        sizePolicy4.setHeightForWidth(self.widget_83.sizePolicy().hasHeightForWidth())
        self.widget_83.setSizePolicy(sizePolicy4)

        self.horizontalLayout_186.addWidget(self.widget_83)

        self.tool_setter_user_2_name = VCPSettingsLineEdit(self.widget_52)
        self.tool_setter_user_2_name.setObjectName(u"tool_setter_user_2_name")
        self.tool_setter_user_2_name.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.tool_setter_user_2_name.sizePolicy().hasHeightForWidth())
        self.tool_setter_user_2_name.setSizePolicy(sizePolicy6)
        self.tool_setter_user_2_name.setMinimumSize(QSize(0, 38))
        self.tool_setter_user_2_name.setMaximumSize(QSize(16777215, 38))
        self.tool_setter_user_2_name.setFocusPolicy(Qt.ClickFocus)
        self.tool_setter_user_2_name.setStyleSheet(u"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"background-color: #929695;")
        self.tool_setter_user_2_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_186.addWidget(self.tool_setter_user_2_name)

        self.user_setter_2_3039 = VCPSettingsLineEdit(self.widget_52)
        self.user_setter_2_3039.setObjectName(u"user_setter_2_3039")
        sizePolicy.setHeightForWidth(self.user_setter_2_3039.sizePolicy().hasHeightForWidth())
        self.user_setter_2_3039.setSizePolicy(sizePolicy)
        self.user_setter_2_3039.setMinimumSize(QSize(100, 31))
        self.user_setter_2_3039.setMaximumSize(QSize(100, 31))
        self.user_setter_2_3039.setFont(font10)
        self.user_setter_2_3039.setFocusPolicy(Qt.ClickFocus)
        self.user_setter_2_3039.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.user_setter_2_3039.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_186.addWidget(self.user_setter_2_3039)


        self.verticalLayout_72.addLayout(self.horizontalLayout_186)

        self.horizontalLayout_195 = QHBoxLayout()
        self.horizontalLayout_195.setSpacing(12)
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.horizontalLayout_195.setContentsMargins(6, 1, 6, 1)
        self.widget_80 = QWidget(self.widget_52)
        self.widget_80.setObjectName(u"widget_80")
        self.widget_80.setEnabled(False)
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy17.setHorizontalStretch(1)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.widget_80.sizePolicy().hasHeightForWidth())
        self.widget_80.setSizePolicy(sizePolicy17)
        self.widget_80.setMinimumSize(QSize(65, 0))

        self.horizontalLayout_195.addWidget(self.widget_80)

        self.tool_setter_offset_right_Btn_3 = VCPSettingsPushButton(self.widget_52)
        self.tooloffsetdirbtnGroup.addButton(self.tool_setter_offset_right_Btn_3)
        self.tool_setter_offset_right_Btn_3.setObjectName(u"tool_setter_offset_right_Btn_3")
        self.tool_setter_offset_right_Btn_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tool_setter_offset_right_Btn_3.sizePolicy().hasHeightForWidth())
        self.tool_setter_offset_right_Btn_3.setSizePolicy(sizePolicy)
        self.tool_setter_offset_right_Btn_3.setMinimumSize(QSize(73, 38))
        self.tool_setter_offset_right_Btn_3.setMaximumSize(QSize(73, 38))
        self.tool_setter_offset_right_Btn_3.setLayoutDirection(Qt.LeftToRight)
        self.tool_setter_offset_right_Btn_3.setStyleSheet(u"font: 14pt \"Bebas Kai\"")
        self.tool_setter_offset_right_Btn_3.setIcon(icon2)
        self.tool_setter_offset_right_Btn_3.setIconSize(QSize(16, 16))
        self.tool_setter_offset_right_Btn_3.setAutoExclusive(False)
        self.tool_setter_offset_right_Btn_3.setProperty(u"page", 1)

        self.horizontalLayout_195.addWidget(self.tool_setter_offset_right_Btn_3)

        self.widget_84 = QWidget(self.widget_52)
        self.widget_84.setObjectName(u"widget_84")
        sizePolicy4.setHeightForWidth(self.widget_84.sizePolicy().hasHeightForWidth())
        self.widget_84.setSizePolicy(sizePolicy4)

        self.horizontalLayout_195.addWidget(self.widget_84)

        self.update_tool_setter_params = SubCallButton(self.widget_52)
        self.update_tool_setter_params.setObjectName(u"update_tool_setter_params")
        sizePolicy2.setHeightForWidth(self.update_tool_setter_params.sizePolicy().hasHeightForWidth())
        self.update_tool_setter_params.setSizePolicy(sizePolicy2)
        self.update_tool_setter_params.setMinimumSize(QSize(235, 38))
        self.update_tool_setter_params.setMaximumSize(QSize(16777215, 38))
        self.update_tool_setter_params.setStyleSheet(u"SubCallButton{\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_195.addWidget(self.update_tool_setter_params)


        self.verticalLayout_72.addLayout(self.horizontalLayout_195)


        self.verticalLayout_48.addWidget(self.widget_52)

        self.mdi_entry_box_7 = MDIEntry(self.widget_46)
        self.mdi_entry_box_7.setObjectName(u"mdi_entry_box_7")
        self.mdi_entry_box_7.setMinimumSize(QSize(0, 42))
        self.mdi_entry_box_7.setMaximumSize(QSize(16777215, 42))
        self.mdi_entry_box_7.setFont(font7)
        self.mdi_entry_box_7.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_48.addWidget(self.mdi_entry_box_7)


        self.horizontalLayout_27.addWidget(self.widget_46)

        self.widget_12 = QWidget(self.tab_2)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_78 = QVBoxLayout(self.widget_12)
        self.verticalLayout_78.setSpacing(6)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.probe_group_select_2 = QWidget(self.widget_12)
        self.probe_group_select_2.setObjectName(u"probe_group_select_2")
        self.probe_group_select_2.setStyleSheet(u"QWidget {\n"
"    font: 13pt \"bebas kai\";\n"
"}")
        self.horizontalLayout_201 = QHBoxLayout(self.probe_group_select_2)
        self.horizontalLayout_201.setSpacing(0)
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.horizontalLayout_201.setContentsMargins(20, 3, 20, 6)
        self.setter_fast_fr = QPushButton(self.probe_group_select_2)
        self.settertabGroup = QButtonGroup(Form)
        self.settertabGroup.setObjectName(u"settertabGroup")
        self.settertabGroup.addButton(self.setter_fast_fr)
        self.setter_fast_fr.setObjectName(u"setter_fast_fr")
        self.setter_fast_fr.setMinimumSize(QSize(127, 37))
        self.setter_fast_fr.setFocusPolicy(Qt.NoFocus)
        self.setter_fast_fr.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 2px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_fast_fr.setCheckable(True)
        self.setter_fast_fr.setChecked(True)
        self.setter_fast_fr.setAutoExclusive(True)
        self.setter_fast_fr.setProperty(u"page", 0)

        self.horizontalLayout_201.addWidget(self.setter_fast_fr)

        self.setter_spindle_zero = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.setter_spindle_zero)
        self.setter_spindle_zero.setObjectName(u"setter_spindle_zero")
        self.setter_spindle_zero.setMinimumSize(QSize(174, 37))
        self.setter_spindle_zero.setFocusPolicy(Qt.NoFocus)
        self.setter_spindle_zero.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 14ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_spindle_zero.setCheckable(True)
        self.setter_spindle_zero.setAutoExclusive(True)
        self.setter_spindle_zero.setProperty(u"page", 1)

        self.horizontalLayout_201.addWidget(self.setter_spindle_zero)

        self.setter_slow_fr = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.setter_slow_fr)
        self.setter_slow_fr.setObjectName(u"setter_slow_fr")
        self.setter_slow_fr.setMinimumSize(QSize(174, 37))
        self.setter_slow_fr.setFocusPolicy(Qt.NoFocus)
        self.setter_slow_fr.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 14ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_slow_fr.setCheckable(True)
        self.setter_slow_fr.setAutoExclusive(True)
        self.setter_slow_fr.setProperty(u"page", 2)

        self.horizontalLayout_201.addWidget(self.setter_slow_fr)

        self.xyz_max_travel = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.xyz_max_travel)
        self.xyz_max_travel.setObjectName(u"xyz_max_travel")
        self.xyz_max_travel.setMinimumSize(QSize(126, 37))
        self.xyz_max_travel.setFocusPolicy(Qt.NoFocus)
        self.xyz_max_travel.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.xyz_max_travel.setCheckable(True)
        self.xyz_max_travel.setAutoExclusive(True)
        self.xyz_max_travel.setProperty(u"page", 3)

        self.horizontalLayout_201.addWidget(self.xyz_max_travel)

        self.setter_retract_dist = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.setter_retract_dist)
        self.setter_retract_dist.setObjectName(u"setter_retract_dist")
        self.setter_retract_dist.setMinimumSize(QSize(126, 37))
        self.setter_retract_dist.setFocusPolicy(Qt.NoFocus)
        self.setter_retract_dist.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_retract_dist.setCheckable(True)
        self.setter_retract_dist.setAutoExclusive(True)
        self.setter_retract_dist.setProperty(u"page", 4)

        self.horizontalLayout_201.addWidget(self.setter_retract_dist)

        self.setter_diam_offset = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.setter_diam_offset)
        self.setter_diam_offset.setObjectName(u"setter_diam_offset")
        self.setter_diam_offset.setMinimumSize(QSize(126, 37))
        self.setter_diam_offset.setFocusPolicy(Qt.NoFocus)
        self.setter_diam_offset.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_diam_offset.setCheckable(True)
        self.setter_diam_offset.setAutoExclusive(True)
        self.setter_diam_offset.setProperty(u"page", 5)

        self.horizontalLayout_201.addWidget(self.setter_diam_offset)

        self.setter_touch_position = QPushButton(self.probe_group_select_2)
        self.settertabGroup.addButton(self.setter_touch_position)
        self.setter_touch_position.setObjectName(u"setter_touch_position")
        self.setter_touch_position.setMinimumSize(QSize(127, 37))
        self.setter_touch_position.setFocusPolicy(Qt.NoFocus)
        self.setter_touch_position.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 2px;\n"
"    border-left-width: 1px;\n"
"    min-width: 10ex;\n"
"    min-height: 25;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 25"
                        "5), stop:0.3 rgba(85, 85, 238, 255), stop:0.694737 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.setter_touch_position.setCheckable(True)
        self.setter_touch_position.setAutoExclusive(True)
        self.setter_touch_position.setProperty(u"page", 6)

        self.horizontalLayout_201.addWidget(self.setter_touch_position)


        self.verticalLayout_78.addWidget(self.probe_group_select_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 9)
        self.setter_tab_widget = QStackedWidget(self.widget_12)
        self.setter_tab_widget.setObjectName(u"setter_tab_widget")
        sizePolicy13.setHeightForWidth(self.setter_tab_widget.sizePolicy().hasHeightForWidth())
        self.setter_tab_widget.setSizePolicy(sizePolicy13)
        self.setter_tab_widget.setMinimumSize(QSize(550, 0))
        self.setter_tab_widget.setFont(font9)
        self.setter_tab_widget.setStyleSheet(u"background-color: #929695;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout_19 = QHBoxLayout(self.page_1)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_38 = QWidget(self.page_1)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy)
        self.verticalLayout_74 = QVBoxLayout(self.widget_38)
        self.verticalLayout_74.setSpacing(9)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.widget_38)

        self.widget_48 = QWidget(self.page_1)
        self.widget_48.setObjectName(u"widget_48")
        self.line_4 = QFrame(self.widget_48)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(330, 388, 220, 2))
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setLayoutDirection(Qt.RightToLeft)
        self.line_4.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.label_140 = QLabel(self.widget_48)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(382, 336, 121, 41))
        self.label_140.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_140.setLineWidth(0)
        self.label_140.setAlignment(Qt.AlignCenter)
        self.label_140.setWordWrap(True)
        self.label_140.setIndent(0)
        self.label_50 = QLabel(self.widget_48)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(290, 390, 171, 131))
        self.label_50.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_50.setScaledContents(True)
        self.label_138 = QLabel(self.widget_48)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(412, 43, 111, 50))
        self.label_138.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"background: transparent;\n"
"}")
        self.label_138.setLineWidth(0)
        self.label_138.setAlignment(Qt.AlignCenter)
        self.label_138.setWordWrap(True)
        self.label_138.setIndent(0)
        self.label_52 = QLabel(self.widget_48)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(230, 19, 161, 221))
        self.label_52.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.label_52.setScaledContents(True)
        self.line_3 = QFrame(self.widget_48)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(380, 95, 170, 2))
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setLayoutDirection(Qt.RightToLeft)
        self.line_3.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.label_136 = QLabel(self.widget_48)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(479, 220, 141, 51))
        self.label_136.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_136.setLineWidth(0)
        self.label_136.setAlignment(Qt.AlignCenter)
        self.label_136.setWordWrap(True)
        self.label_136.setIndent(0)
        self.line_5 = QFrame(self.widget_48)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(548, 96, 2, 295))
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.label_7 = QLabel(self.widget_48)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(660, 21, 321, 391))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(10)
        self.label_7.setIndent(10)
        self.line_9 = QFrame(self.widget_48)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(100, 240, 191, 2))
        sizePolicy.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy)
        self.line_9.setLayoutDirection(Qt.RightToLeft)
        self.line_9.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(1)
        self.line_9.setMidLineWidth(0)
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_10 = QFrame(self.widget_48)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(100, 95, 2, 295))
        sizePolicy.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy)
        self.line_10.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(1)
        self.line_10.setMidLineWidth(0)
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.label_148 = QLabel(self.widget_48)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(46, 139, 111, 61))
        self.label_148.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_148.setLineWidth(0)
        self.label_148.setAlignment(Qt.AlignCenter)
        self.label_148.setWordWrap(True)
        self.label_148.setIndent(0)
        self.line_11 = QFrame(self.widget_48)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(100, 95, 138, 2))
        sizePolicy.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy)
        self.line_11.setLayoutDirection(Qt.RightToLeft)
        self.line_11.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(1)
        self.line_11.setMidLineWidth(0)
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_12 = QFrame(self.widget_48)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(100, 388, 185, 2))
        sizePolicy.setHeightForWidth(self.line_12.sizePolicy().hasHeightForWidth())
        self.line_12.setSizePolicy(sizePolicy)
        self.line_12.setLayoutDirection(Qt.RightToLeft)
        self.line_12.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(1)
        self.line_12.setMidLineWidth(0)
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.label_149 = QLabel(self.widget_48)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(21, 264, 161, 101))
        self.label_149.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_149.setLineWidth(0)
        self.label_149.setAlignment(Qt.AlignCenter)
        self.label_149.setWordWrap(True)
        self.label_149.setIndent(0)
        self.line_4.raise_()
        self.label_140.raise_()
        self.label_50.raise_()
        self.label_138.raise_()
        self.label_52.raise_()
        self.line_3.raise_()
        self.line_5.raise_()
        self.label_7.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_12.raise_()
        self.label_136.raise_()
        self.label_148.raise_()
        self.label_149.raise_()

        self.horizontalLayout_19.addWidget(self.widget_48)

        self.setter_tab_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 30, 500, 261))
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(500, 450))
        self.label_12.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_12.setMargin(10)
        self.label_12.setIndent(10)
        self.label_51 = QLabel(self.page_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(750, 391, 171, 131))
        self.label_51.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_51.setScaledContents(True)
        self.label_53 = QLabel(self.page_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(686, 20, 161, 221))
        self.label_53.setStyleSheet(u"image: url(:/images/atc_spindle_tool.png);")
        self.label_53.setScaledContents(True)
        self.line_6 = QFrame(self.page_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(766, 250, 2, 135))
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setMidLineWidth(0)
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.label_139 = QLabel(self.page_2)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(806, 120, 131, 51))
        self.label_139.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"background: transparent;\n"
"}")
        self.label_139.setLineWidth(0)
        self.label_139.setAlignment(Qt.AlignCenter)
        self.label_139.setWordWrap(True)
        self.label_139.setIndent(0)
        self.label_151 = QLabel(self.page_2)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setGeometry(QRect(697, 277, 141, 81))
        self.label_151.setStyleSheet(u"QLabel{\n"
"font: 15pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_151.setLineWidth(0)
        self.label_151.setAlignment(Qt.AlignCenter)
        self.label_151.setWordWrap(True)
        self.label_151.setIndent(0)
        self.setter_tab_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 30, 500, 450))
        self.label_13.setMaximumSize(QSize(500, 450))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_13.setMargin(10)
        self.label_13.setIndent(10)
        self.setter_tab_widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_15 = QLabel(self.page_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(50, 30, 500, 151))
        self.label_15.setMaximumSize(QSize(500, 400))
        self.label_15.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setMargin(10)
        self.label_15.setIndent(10)
        self.setter_tab_widget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 30, 500, 241))
        self.label_16.setMaximumSize(QSize(500, 400))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_16.setWordWrap(True)
        self.label_16.setMargin(10)
        self.label_16.setIndent(10)
        self.setter_tab_widget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_17 = QLabel(self.page_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 30, 500, 341))
        self.label_17.setMaximumSize(QSize(500, 400))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_17.setWordWrap(True)
        self.label_17.setMargin(10)
        self.label_17.setIndent(10)
        self.label_55 = QLabel(self.page_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(750, 320, 171, 131))
        self.label_55.setStyleSheet(u"image: url(:/images/tool_probe.png);")
        self.label_55.setScaledContents(True)
        self.label_152 = QLabel(self.page_6)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(800, 80, 171, 111))
        self.label_152.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"background: transparent;\n"
"}")
        self.label_152.setLineWidth(0)
        self.label_152.setAlignment(Qt.AlignCenter)
        self.label_152.setWordWrap(True)
        self.label_152.setIndent(0)
        self.line_13 = QFrame(self.page_6)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(766, 208, 2, 105))
        sizePolicy.setHeightForWidth(self.line_13.sizePolicy().hasHeightForWidth())
        self.line_13.setSizePolicy(sizePolicy)
        self.line_13.setStyleSheet(u"color: green;\n"
"background-color: white;\n"
"border: none;\n"
"")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(1)
        self.line_13.setMidLineWidth(0)
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(642, 80, 125, 123))
        self.label_6.setPixmap(QPixmap(u":/images/50mm_facemill_gray.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.setter_tab_widget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_18 = QLabel(self.page_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 30, 500, 151))
        self.label_18.setMaximumSize(QSize(500, 400))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"    padding-right: 10px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_18.setWordWrap(True)
        self.label_18.setMargin(10)
        self.label_18.setIndent(10)
        self.setter_tab_widget.addWidget(self.page_7)

        self.horizontalLayout_6.addWidget(self.setter_tab_widget)


        self.verticalLayout_78.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_27.addWidget(self.widget_12)

        self.tabWidget_2.addTab(self.tab_2, "")

        self.horizontalLayout_43.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.probe_tab, "")
        self.conversational_tab = QWidget()
        self.conversational_tab.setObjectName(u"conversational_tab")
        self.horizontalLayout_13 = QHBoxLayout(self.conversational_tab)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.operation = QTabWidget(self.conversational_tab)
        self.operation.setObjectName(u"operation")
        self.operation.setLayoutDirection(Qt.LeftToRight)
        self.operation.setStyleSheet(u"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget QTabBar::tab{\n"
"    margin-top: 0px;\n"
"    margin-right: 0px;\n"
"    margin-bottom:0px;\n"
"    min-width: 35px;\n"
"    min-height: 100px;\n"
"    font: 15pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-top: 45px;\n"
"    border-left-width: 2px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 2px;\n"
"    border-top-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"")
        self.operation.setTabPosition(QTabWidget.West)
        self.operation.setTabShape(QTabWidget.Rounded)
        self.facing_tab = QWidget()
        self.facing_tab.setObjectName(u"facing_tab")
        self.horizontalLayout_49 = QHBoxLayout(self.facing_tab)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.facingwidget = FacingWidget(self.facing_tab)
        self.facingwidget.setObjectName(u"facingwidget")
        self.facingwidget.setMinimumSize(QSize(1420, 500))

        self.horizontalLayout_49.addWidget(self.facingwidget)

        self.operation.addTab(self.facing_tab, "")
        self.holeop_tab = QWidget()
        self.holeop_tab.setObjectName(u"holeop_tab")
        self.horizontalLayout_15 = QHBoxLayout(self.holeop_tab)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tabWidget_3 = QTabWidget(self.holeop_tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tabWidget_3.setFocusPolicy(Qt.TabFocus)
        self.tabWidget_3.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_3.setStyleSheet(u"QTabWidget QTabBar::tab {\n"
"    margin-top: 5px;\n"
"    margin-right: 0px;\n"
"    min-width: 130px;\n"
"    min-height: 23px;\n"
"    font: 14pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-left: 300px;\n"
"    border-left-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-bottom-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.xy_tab = QWidget()
        self.xy_tab.setObjectName(u"xy_tab")
        self.horizontalLayout_71 = QHBoxLayout(self.xy_tab)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.xycoordwidget = XYCoordWidget(self.xy_tab)
        self.xycoordwidget.setObjectName(u"xycoordwidget")
        sizePolicy8.setHeightForWidth(self.xycoordwidget.sizePolicy().hasHeightForWidth())
        self.xycoordwidget.setSizePolicy(sizePolicy8)
        self.xycoordwidget.setMinimumSize(QSize(1420, 500))
        self.xycoordwidget.setMaximumSize(QSize(1420, 580))

        self.horizontalLayout_71.addWidget(self.xycoordwidget)

        self.tabWidget_3.addTab(self.xy_tab, "")
        self.pattern = QWidget()
        self.pattern.setObjectName(u"pattern")
        self.horizontalLayout_149 = QHBoxLayout(self.pattern)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.holecirclewidget = HoleCircleWidget(self.pattern)
        self.holecirclewidget.setObjectName(u"holecirclewidget")
        self.holecirclewidget.setMinimumSize(QSize(1420, 500))

        self.horizontalLayout_149.addWidget(self.holecirclewidget)

        self.tabWidget_3.addTab(self.pattern, "")
        self.thread_mill = QWidget()
        self.thread_mill.setObjectName(u"thread_mill")
        self.tabWidget_3.addTab(self.thread_mill, "")

        self.horizontalLayout_15.addWidget(self.tabWidget_3)

        self.operation.addTab(self.holeop_tab, "")
        self.perimeter_tab = QWidget()
        self.perimeter_tab.setObjectName(u"perimeter_tab")
        self.horizontalLayout_63 = QHBoxLayout(self.perimeter_tab)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.tabWidget_9 = QTabWidget(self.perimeter_tab)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tabWidget_9.setFocusPolicy(Qt.TabFocus)
        self.tabWidget_9.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_9.setStyleSheet(u"QTabWidget QTabBar::tab {\n"
"    margin-top: 5px;\n"
"    margin-right: 0px;\n"
"    min-width: 130px;\n"
"    min-height: 23px;\n"
"    font: 14pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-left: 300px;\n"
"    border-left-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-bottom-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.widget_28 = QWidget()
        self.widget_28.setObjectName(u"widget_28")
        self.tabWidget_9.addTab(self.widget_28, "")
        self.widget_29 = QWidget()
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_70 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.tabWidget_9.addTab(self.widget_29, "")
        self.widget_30 = QWidget()
        self.widget_30.setObjectName(u"widget_30")
        self.tabWidget_9.addTab(self.widget_30, "")
        self.widget_31 = QWidget()
        self.widget_31.setObjectName(u"widget_31")
        self.tabWidget_9.addTab(self.widget_31, "")
        self.widget_32 = QWidget()
        self.widget_32.setObjectName(u"widget_32")
        self.tabWidget_9.addTab(self.widget_32, "")
        self.widget_33 = QWidget()
        self.widget_33.setObjectName(u"widget_33")
        self.tabWidget_9.addTab(self.widget_33, "")
        self.widget_34 = QWidget()
        self.widget_34.setObjectName(u"widget_34")
        self.tabWidget_9.addTab(self.widget_34, "")
        self.widget_35 = QWidget()
        self.widget_35.setObjectName(u"widget_35")
        self.tabWidget_9.addTab(self.widget_35, "")

        self.horizontalLayout_63.addWidget(self.tabWidget_9)

        self.operation.addTab(self.perimeter_tab, "")
        self.pockets_tab = QWidget()
        self.pockets_tab.setObjectName(u"pockets_tab")
        self.horizontalLayout_65 = QHBoxLayout(self.pockets_tab)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.tabWidget_8 = QTabWidget(self.pockets_tab)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tabWidget_8.setFocusPolicy(Qt.TabFocus)
        self.tabWidget_8.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_8.setStyleSheet(u"QTabWidget QTabBar::tab {\n"
"    margin-top: 5px;\n"
"    margin-right: 0px;\n"
"    min-width: 130px;\n"
"    min-height: 23px;\n"
"    font: 14pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-left: 300px;\n"
"    border-left-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-bottom-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.tabWidget_8.addTab(self.widget_2, "")
        self.widget_20 = QWidget()
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_69 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.tabWidget_8.addTab(self.widget_20, "")
        self.widget_22 = QWidget()
        self.widget_22.setObjectName(u"widget_22")
        self.tabWidget_8.addTab(self.widget_22, "")
        self.widget_23 = QWidget()
        self.widget_23.setObjectName(u"widget_23")
        self.tabWidget_8.addTab(self.widget_23, "")
        self.widget_24 = QWidget()
        self.widget_24.setObjectName(u"widget_24")
        self.tabWidget_8.addTab(self.widget_24, "")
        self.widget_25 = QWidget()
        self.widget_25.setObjectName(u"widget_25")
        self.tabWidget_8.addTab(self.widget_25, "")
        self.widget_26 = QWidget()
        self.widget_26.setObjectName(u"widget_26")
        self.tabWidget_8.addTab(self.widget_26, "")
        self.widget_27 = QWidget()
        self.widget_27.setObjectName(u"widget_27")
        self.tabWidget_8.addTab(self.widget_27, "")

        self.horizontalLayout_65.addWidget(self.tabWidget_8)

        self.operation.addTab(self.pockets_tab, "")
        self.misc_tab = QWidget()
        self.misc_tab.setObjectName(u"misc_tab")
        self.horizontalLayout_68 = QHBoxLayout(self.misc_tab)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.tabWidget_7 = QTabWidget(self.misc_tab)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tabWidget_7.setFocusPolicy(Qt.TabFocus)
        self.tabWidget_7.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_7.setStyleSheet(u"QTabWidget QTabBar::tab {\n"
"    margin-top: 5px;\n"
"    margin-right: 0px;\n"
"    min-width: 130px;\n"
"    min-height: 23px;\n"
"    font: 14pt \"bebas kai\";\n"
"}\n"
"\n"
"QTabBar::tab:first {\n"
"    margin-left: 300px;\n"
"    border-left-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-bottom-width: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:last {\n"
"    border-left-width: 1px;\n"
"    border-right-width: 2px;\n"
"    border-top-width: 2px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    border-width: 2px;\n"
"    border-radius: 4px;\n"
"}")
        self.widget1 = QWidget()
        self.widget1.setObjectName(u"widget1")
        self.tabWidget_7.addTab(self.widget1, "")
        self.widget2 = QWidget()
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_67 = QHBoxLayout(self.widget2)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.tabWidget_7.addTab(self.widget2, "")
        self.widget3 = QWidget()
        self.widget3.setObjectName(u"widget3")
        self.tabWidget_7.addTab(self.widget3, "")
        self.widget4 = QWidget()
        self.widget4.setObjectName(u"widget4")
        self.tabWidget_7.addTab(self.widget4, "")
        self.widget5 = QWidget()
        self.widget5.setObjectName(u"widget5")
        self.tabWidget_7.addTab(self.widget5, "")
        self.widget6 = QWidget()
        self.widget6.setObjectName(u"widget6")
        self.tabWidget_7.addTab(self.widget6, "")
        self.widget7 = QWidget()
        self.widget7.setObjectName(u"widget7")
        self.tabWidget_7.addTab(self.widget7, "")
        self.widget8 = QWidget()
        self.widget8.setObjectName(u"widget8")
        self.tabWidget_7.addTab(self.widget8, "")

        self.horizontalLayout_68.addWidget(self.tabWidget_7)

        self.operation.addTab(self.misc_tab, "")

        self.horizontalLayout_13.addWidget(self.operation)

        self.tabWidget.addTab(self.conversational_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.horizontalLayout_21 = QHBoxLayout(self.settings_tab)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 22, 20, 20)
        self.widget_59 = QWidget(self.settings_tab)
        self.widget_59.setObjectName(u"widget_59")
        sizePolicy4.setHeightForWidth(self.widget_59.sizePolicy().hasHeightForWidth())
        self.widget_59.setSizePolicy(sizePolicy4)

        self.horizontalLayout_21.addWidget(self.widget_59)

        self.widget_53 = QWidget(self.settings_tab)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_7 = QVBoxLayout(self.widget_53)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.frame_19 = QFrame(self.widget_53)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet(u"")
        self.verticalLayout_51 = QVBoxLayout(self.frame_19)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.startup_settings_label = QLabel(self.frame_19)
        self.startup_settings_label.setObjectName(u"startup_settings_label")
        self.startup_settings_label.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.startup_settings_label.sizePolicy().hasHeightForWidth())
        self.startup_settings_label.setSizePolicy(sizePolicy6)
        self.startup_settings_label.setMinimumSize(QSize(100, 25))
        self.startup_settings_label.setMaximumSize(QSize(16777215, 25))
        self.startup_settings_label.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.startup_settings_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.startup_settings_label)

        self.widget_3 = QWidget(self.frame_19)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.startup_tab_label = QLabel(self.widget_3)
        self.startup_tab_label.setObjectName(u"startup_tab_label")
        self.startup_tab_label.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.startup_tab_label.sizePolicy().hasHeightForWidth())
        self.startup_tab_label.setSizePolicy(sizePolicy6)
        self.startup_tab_label.setMinimumSize(QSize(100, 25))
        self.startup_tab_label.setMaximumSize(QSize(16777215, 25))
        self.startup_tab_label.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.startup_tab_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.startup_tab_label)

        self.startup_tab_combobox = QComboBox(self.widget_3)
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.addItem("")
        self.startup_tab_combobox.setObjectName(u"startup_tab_combobox")
        sizePolicy.setHeightForWidth(self.startup_tab_combobox.sizePolicy().hasHeightForWidth())
        self.startup_tab_combobox.setSizePolicy(sizePolicy)
        self.startup_tab_combobox.setMinimumSize(QSize(200, 40))
        self.startup_tab_combobox.setMaximumSize(QSize(200, 40))
        self.startup_tab_combobox.setStyleSheet(u"QComboBox::drop-down:button {\n"
"    width: 36px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    font: 16pt \"Bebas Kai\";\n"
"    padding-left: 15px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.startup_tab_combobox)


        self.verticalLayout_51.addWidget(self.widget_3)


        self.verticalLayout_7.addWidget(self.frame_19)

        self.widget_64 = QWidget(self.widget_53)
        self.widget_64.setObjectName(u"widget_64")

        self.verticalLayout_7.addWidget(self.widget_64)


        self.horizontalLayout_21.addWidget(self.widget_53)

        self.widget_51 = QWidget(self.settings_tab)
        self.widget_51.setObjectName(u"widget_51")
        self.verticalLayout_6 = QVBoxLayout(self.widget_51)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.prog_coolant_setting_frame = QFrame(self.widget_51)
        self.prog_coolant_setting_frame.setObjectName(u"prog_coolant_setting_frame")
        sizePolicy1.setHeightForWidth(self.prog_coolant_setting_frame.sizePolicy().hasHeightForWidth())
        self.prog_coolant_setting_frame.setSizePolicy(sizePolicy1)
        self.prog_coolant_setting_frame.setFrameShape(QFrame.StyledPanel)
        self.prog_coolant_setting_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.prog_coolant_setting_frame)
        self.verticalLayout_76.setSpacing(15)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.prog_coolant_header = QLabel(self.prog_coolant_setting_frame)
        self.prog_coolant_header.setObjectName(u"prog_coolant_header")
        self.prog_coolant_header.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.prog_coolant_header.sizePolicy().hasHeightForWidth())
        self.prog_coolant_header.setSizePolicy(sizePolicy6)
        self.prog_coolant_header.setMinimumSize(QSize(100, 25))
        self.prog_coolant_header.setMaximumSize(QSize(16777215, 25))
        self.prog_coolant_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.prog_coolant_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.prog_coolant_header)

        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.horizontalLayout_175.setContentsMargins(-1, 1, -1, 1)
        self.label_141 = QLabel(self.prog_coolant_setting_frame)
        self.label_141.setObjectName(u"label_141")
        sizePolicy6.setHeightForWidth(self.label_141.sizePolicy().hasHeightForWidth())
        self.label_141.setSizePolicy(sizePolicy6)
        self.label_141.setMinimumSize(QSize(140, 31))
        self.label_141.setMaximumSize(QSize(16777215, 31))
        self.label_141.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_141.setLineWidth(0)
        self.label_141.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_141.setIndent(0)

        self.horizontalLayout_175.addWidget(self.label_141)

        self.activate_programmable_coolant_3000 = VCPSettingsLineEdit(self.prog_coolant_setting_frame)
        self.activate_programmable_coolant_3000.setObjectName(u"activate_programmable_coolant_3000")
        sizePolicy.setHeightForWidth(self.activate_programmable_coolant_3000.sizePolicy().hasHeightForWidth())
        self.activate_programmable_coolant_3000.setSizePolicy(sizePolicy)
        self.activate_programmable_coolant_3000.setMinimumSize(QSize(100, 31))
        self.activate_programmable_coolant_3000.setMaximumSize(QSize(100, 31))
        self.activate_programmable_coolant_3000.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_175.addWidget(self.activate_programmable_coolant_3000)


        self.verticalLayout_76.addLayout(self.horizontalLayout_175)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_188.setContentsMargins(-1, 1, -1, 1)
        self.label_142 = QLabel(self.prog_coolant_setting_frame)
        self.label_142.setObjectName(u"label_142")
        sizePolicy6.setHeightForWidth(self.label_142.sizePolicy().hasHeightForWidth())
        self.label_142.setSizePolicy(sizePolicy6)
        self.label_142.setMinimumSize(QSize(140, 31))
        self.label_142.setMaximumSize(QSize(16777215, 31))
        self.label_142.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_142.setLineWidth(0)
        self.label_142.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_142.setIndent(0)

        self.horizontalLayout_188.addWidget(self.label_142)

        self.horizontal_spindle_nozzle_dist_3001 = VCPSettingsLineEdit(self.prog_coolant_setting_frame)
        self.horizontal_spindle_nozzle_dist_3001.setObjectName(u"horizontal_spindle_nozzle_dist_3001")
        sizePolicy.setHeightForWidth(self.horizontal_spindle_nozzle_dist_3001.sizePolicy().hasHeightForWidth())
        self.horizontal_spindle_nozzle_dist_3001.setSizePolicy(sizePolicy)
        self.horizontal_spindle_nozzle_dist_3001.setMinimumSize(QSize(100, 31))
        self.horizontal_spindle_nozzle_dist_3001.setMaximumSize(QSize(100, 31))
        self.horizontal_spindle_nozzle_dist_3001.setFont(font10)
        self.horizontal_spindle_nozzle_dist_3001.setFocusPolicy(Qt.ClickFocus)
        self.horizontal_spindle_nozzle_dist_3001.setStyleSheet(u"VCPSettingsLineEdit {\n"
"    font: 15pt \"bebas kai\"\n"
"}")
        self.horizontal_spindle_nozzle_dist_3001.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_188.addWidget(self.horizontal_spindle_nozzle_dist_3001)


        self.verticalLayout_76.addLayout(self.horizontalLayout_188)

        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.horizontalLayout_190.setContentsMargins(-1, 1, -1, 1)
        self.label_143 = QLabel(self.prog_coolant_setting_frame)
        self.label_143.setObjectName(u"label_143")
        sizePolicy6.setHeightForWidth(self.label_143.sizePolicy().hasHeightForWidth())
        self.label_143.setSizePolicy(sizePolicy6)
        self.label_143.setMinimumSize(QSize(140, 31))
        self.label_143.setMaximumSize(QSize(16777215, 31))
        self.label_143.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_143.setLineWidth(0)
        self.label_143.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_143.setIndent(0)

        self.horizontalLayout_190.addWidget(self.label_143)

        self.vertical_spindle_nozzle_dist_3002 = VCPSettingsLineEdit(self.prog_coolant_setting_frame)
        self.vertical_spindle_nozzle_dist_3002.setObjectName(u"vertical_spindle_nozzle_dist_3002")
        sizePolicy.setHeightForWidth(self.vertical_spindle_nozzle_dist_3002.sizePolicy().hasHeightForWidth())
        self.vertical_spindle_nozzle_dist_3002.setSizePolicy(sizePolicy)
        self.vertical_spindle_nozzle_dist_3002.setMinimumSize(QSize(100, 31))
        self.vertical_spindle_nozzle_dist_3002.setMaximumSize(QSize(100, 31))
        self.vertical_spindle_nozzle_dist_3002.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_190.addWidget(self.vertical_spindle_nozzle_dist_3002)


        self.verticalLayout_76.addLayout(self.horizontalLayout_190)

        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.horizontalLayout_191.setContentsMargins(-1, 1, -1, 1)
        self.label_144 = QLabel(self.prog_coolant_setting_frame)
        self.label_144.setObjectName(u"label_144")
        sizePolicy6.setHeightForWidth(self.label_144.sizePolicy().hasHeightForWidth())
        self.label_144.setSizePolicy(sizePolicy6)
        self.label_144.setMinimumSize(QSize(140, 31))
        self.label_144.setMaximumSize(QSize(16777215, 31))
        self.label_144.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_144.setLineWidth(0)
        self.label_144.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_144.setIndent(0)

        self.horizontalLayout_191.addWidget(self.label_144)

        self.pc_angle_offset_3003 = VCPSettingsLineEdit(self.prog_coolant_setting_frame)
        self.pc_angle_offset_3003.setObjectName(u"pc_angle_offset_3003")
        sizePolicy.setHeightForWidth(self.pc_angle_offset_3003.sizePolicy().hasHeightForWidth())
        self.pc_angle_offset_3003.setSizePolicy(sizePolicy)
        self.pc_angle_offset_3003.setMinimumSize(QSize(100, 31))
        self.pc_angle_offset_3003.setMaximumSize(QSize(100, 31))
        self.pc_angle_offset_3003.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_191.addWidget(self.pc_angle_offset_3003)


        self.verticalLayout_76.addLayout(self.horizontalLayout_191)

        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.horizontalLayout_192.setContentsMargins(-1, 1, -1, 1)
        self.label_145 = QLabel(self.prog_coolant_setting_frame)
        self.label_145.setObjectName(u"label_145")
        sizePolicy6.setHeightForWidth(self.label_145.sizePolicy().hasHeightForWidth())
        self.label_145.setSizePolicy(sizePolicy6)
        self.label_145.setMinimumSize(QSize(140, 31))
        self.label_145.setMaximumSize(QSize(16777215, 31))
        self.label_145.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_145.setLineWidth(0)
        self.label_145.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_145.setIndent(0)

        self.horizontalLayout_192.addWidget(self.label_145)

        self.pc_tool_length = StatusLabel(self.prog_coolant_setting_frame)
        self.pc_tool_length.setObjectName(u"pc_tool_length")
        sizePolicy.setHeightForWidth(self.pc_tool_length.sizePolicy().hasHeightForWidth())
        self.pc_tool_length.setSizePolicy(sizePolicy)
        self.pc_tool_length.setMinimumSize(QSize(100, 33))
        self.pc_tool_length.setMaximumSize(QSize(100, 33))
        self.pc_tool_length.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.pc_tool_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_192.addWidget(self.pc_tool_length)


        self.verticalLayout_76.addLayout(self.horizontalLayout_192)

        self.horizontalLayout_193 = QHBoxLayout()
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.horizontalLayout_193.setContentsMargins(-1, 1, -1, 1)
        self.label_146 = QLabel(self.prog_coolant_setting_frame)
        self.label_146.setObjectName(u"label_146")
        sizePolicy6.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy6)
        self.label_146.setMinimumSize(QSize(140, 31))
        self.label_146.setMaximumSize(QSize(16777215, 31))
        self.label_146.setStyleSheet(u"QLabel{\n"
"font: 14pt \"Bebas Kai\";\n"
"color: white;\n"
"}")
        self.label_146.setLineWidth(0)
        self.label_146.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_146.setIndent(0)

        self.horizontalLayout_193.addWidget(self.label_146)

        self.coolant_final_angle = StatusLabel(self.prog_coolant_setting_frame)
        self.coolant_final_angle.setObjectName(u"coolant_final_angle")
        sizePolicy.setHeightForWidth(self.coolant_final_angle.sizePolicy().hasHeightForWidth())
        self.coolant_final_angle.setSizePolicy(sizePolicy)
        self.coolant_final_angle.setMinimumSize(QSize(100, 33))
        self.coolant_final_angle.setMaximumSize(QSize(100, 33))
        self.coolant_final_angle.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 15pt \"Bebas Kai\";\n"
"}")
        self.coolant_final_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_193.addWidget(self.coolant_final_angle)


        self.verticalLayout_76.addLayout(self.horizontalLayout_193)

        self.update_programmable_coolant_param = SubCallButton(self.prog_coolant_setting_frame)
        self.update_programmable_coolant_param.setObjectName(u"update_programmable_coolant_param")
        self.update_programmable_coolant_param.setMinimumSize(QSize(0, 35))
        self.update_programmable_coolant_param.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_76.addWidget(self.update_programmable_coolant_param)


        self.verticalLayout_6.addWidget(self.prog_coolant_setting_frame)

        self.rpm_type_setting_frame = QFrame(self.widget_51)
        self.rpm_type_setting_frame.setObjectName(u"rpm_type_setting_frame")
        sizePolicy.setHeightForWidth(self.rpm_type_setting_frame.sizePolicy().hasHeightForWidth())
        self.rpm_type_setting_frame.setSizePolicy(sizePolicy)
        self.rpm_type_setting_frame.setMinimumSize(QSize(530, 100))
        self.rpm_type_setting_frame.setMaximumSize(QSize(530, 100))
        self.rpm_type_setting_frame.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.rpm_type_setting_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.work_column_header_10 = QLabel(self.rpm_type_setting_frame)
        self.work_column_header_10.setObjectName(u"work_column_header_10")
        self.work_column_header_10.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.work_column_header_10.sizePolicy().hasHeightForWidth())
        self.work_column_header_10.setSizePolicy(sizePolicy6)
        self.work_column_header_10.setMinimumSize(QSize(100, 25))
        self.work_column_header_10.setMaximumSize(QSize(16777215, 25))
        self.work_column_header_10.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.work_column_header_10)

        self.rpm_type_container = QWidget(self.rpm_type_setting_frame)
        self.rpm_type_container.setObjectName(u"rpm_type_container")
        sizePolicy11.setHeightForWidth(self.rpm_type_container.sizePolicy().hasHeightForWidth())
        self.rpm_type_container.setSizePolicy(sizePolicy11)
        self.horizontalLayout_153 = QHBoxLayout(self.rpm_type_container)
        self.horizontalLayout_153.setSpacing(12)
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.horizontalLayout_153.setContentsMargins(3, 3, 3, 3)
        self.spindle_calculated_rpm_button = VCPSettingsPushButton(self.rpm_type_container)
        self.spindlerpmsourcebtnGroup = QButtonGroup(Form)
        self.spindlerpmsourcebtnGroup.setObjectName(u"spindlerpmsourcebtnGroup")
        self.spindlerpmsourcebtnGroup.addButton(self.spindle_calculated_rpm_button)
        self.spindle_calculated_rpm_button.setObjectName(u"spindle_calculated_rpm_button")
        self.spindle_calculated_rpm_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.spindle_calculated_rpm_button.sizePolicy().hasHeightForWidth())
        self.spindle_calculated_rpm_button.setSizePolicy(sizePolicy1)
        self.spindle_calculated_rpm_button.setMaximumSize(QSize(16777215, 40))
        self.spindle_calculated_rpm_button.setChecked(False)
        self.spindle_calculated_rpm_button.setProperty(u"page", 0)

        self.horizontalLayout_153.addWidget(self.spindle_calculated_rpm_button)

        self.spindle_encoder_rpm_button = VCPSettingsPushButton(self.rpm_type_container)
        self.spindlerpmsourcebtnGroup.addButton(self.spindle_encoder_rpm_button)
        self.spindle_encoder_rpm_button.setObjectName(u"spindle_encoder_rpm_button")
        self.spindle_encoder_rpm_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.spindle_encoder_rpm_button.sizePolicy().hasHeightForWidth())
        self.spindle_encoder_rpm_button.setSizePolicy(sizePolicy1)
        self.spindle_encoder_rpm_button.setMaximumSize(QSize(16777215, 40))
        self.spindle_encoder_rpm_button.setChecked(True)
        self.spindle_encoder_rpm_button.setProperty(u"page", 1)

        self.horizontalLayout_153.addWidget(self.spindle_encoder_rpm_button)


        self.verticalLayout_23.addWidget(self.rpm_type_container)


        self.verticalLayout_6.addWidget(self.rpm_type_setting_frame)

        self.link_jog_settings_frame = QFrame(self.widget_51)
        self.link_jog_settings_frame.setObjectName(u"link_jog_settings_frame")
        sizePolicy6.setHeightForWidth(self.link_jog_settings_frame.sizePolicy().hasHeightForWidth())
        self.link_jog_settings_frame.setSizePolicy(sizePolicy6)
        self.link_jog_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.link_jog_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.link_jog_settings_frame)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_173 = QHBoxLayout()
        self.horizontalLayout_173.setSpacing(12)
        self.horizontalLayout_173.setObjectName(u"horizontalLayout_173")
        self.horizontalLayout_173.setContentsMargins(-1, 1, -1, 1)
        self.ang_jog_slider_link = VCPSettingsPushButton(self.link_jog_settings_frame)
        self.ang_jog_slider_link.setObjectName(u"ang_jog_slider_link")
        self.ang_jog_slider_link.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ang_jog_slider_link.sizePolicy().hasHeightForWidth())
        self.ang_jog_slider_link.setSizePolicy(sizePolicy1)
        self.ang_jog_slider_link.setMaximumSize(QSize(16777215, 40))
        self.ang_jog_slider_link.setCheckable(True)
        self.ang_jog_slider_link.setChecked(True)
        self.ang_jog_slider_link.setProperty(u"page", 1)

        self.horizontalLayout_173.addWidget(self.ang_jog_slider_link)

        self.anglular_jog_slider = VCPSettingsSlider(self.link_jog_settings_frame)
        self.anglular_jog_slider.setObjectName(u"anglular_jog_slider")
        sizePolicy.setHeightForWidth(self.anglular_jog_slider.sizePolicy().hasHeightForWidth())
        self.anglular_jog_slider.setSizePolicy(sizePolicy)
        self.anglular_jog_slider.setMinimumSize(QSize(274, 50))
        self.anglular_jog_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.anglular_jog_slider.setMaximum(100)
        self.anglular_jog_slider.setValue(50)
        self.anglular_jog_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_173.addWidget(self.anglular_jog_slider)

        self.fr_angular_override_dro = StatusLabel(self.link_jog_settings_frame)
        self.fr_angular_override_dro.setObjectName(u"fr_angular_override_dro")
        self.fr_angular_override_dro.setMinimumSize(QSize(48, 38))
        self.fr_angular_override_dro.setMaximumSize(QSize(48, 38))
        self.fr_angular_override_dro.setStyleSheet(u"StatusLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.fr_angular_override_dro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_173.addWidget(self.fr_angular_override_dro)


        self.verticalLayout_62.addLayout(self.horizontalLayout_173)


        self.verticalLayout_6.addWidget(self.link_jog_settings_frame)


        self.horizontalLayout_21.addWidget(self.widget_51)

        self.tabWidget.addTab(self.settings_tab, "")
        self.status_tab = QWidget()
        self.status_tab.setObjectName(u"status_tab")
        self.horizontalLayout_142 = QHBoxLayout(self.status_tab)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(20, 22, 20, 20)
        self.widget_14 = QWidget(self.status_tab)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy4.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy4)
        self.widget_14.setStyleSheet(u"")
        self.horizontalLayout_66 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.widget_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: white;\n"
"border-radius: 6px;\n"
"color: black;\n"
"padding: 20px;")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_66.addWidget(self.label_4)


        self.horizontalLayout_142.addWidget(self.widget_14)

        self.widget_58 = QWidget(self.status_tab)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy8.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy8)
        self.widget_58.setMinimumSize(QSize(450, 0))
        self.verticalLayout_44 = QVBoxLayout(self.widget_58)
        self.verticalLayout_44.setSpacing(12)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.widget_58)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy11.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy11)
        self.frame_38.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.verticalLayout_47 = QVBoxLayout(self.frame_38)
        self.verticalLayout_47.setSpacing(6)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(-1, 0, -1, 3)
        self.notificationwidget = NotificationWidget(self.frame_38)
        self.notificationwidget.setObjectName(u"notificationwidget")
        self.notificationwidget.setStyleSheet(u"QLabel {\n"
"    font-family: \"Bebas Kai\";\n"
"    color: white;\n"
"    font-size: 16pt;\n"
"}\n"
"")

        self.verticalLayout_47.addWidget(self.notificationwidget)


        self.verticalLayout_44.addWidget(self.frame_38)

        self.frame_2 = QFrame(self.widget_58)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u".QFrame{\n"
"    background-color: rgb(51, 57, 59);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_111 = QLabel(self.frame_2)
        self.label_111.setObjectName(u"label_111")
        sizePolicy6.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy6)
        self.label_111.setMinimumSize(QSize(150, 31))
        self.label_111.setMaximumSize(QSize(200, 31))
        self.label_111.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_111.setLineWidth(0)
        self.label_111.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_111.setIndent(0)

        self.horizontalLayout_52.addWidget(self.label_111)

        self.probe_mode_3030 = VCPLineEdit(self.frame_2)
        self.probe_mode_3030.setObjectName(u"probe_mode_3030")
        sizePolicy.setHeightForWidth(self.probe_mode_3030.sizePolicy().hasHeightForWidth())
        self.probe_mode_3030.setSizePolicy(sizePolicy)
        self.probe_mode_3030.setMinimumSize(QSize(60, 31))
        self.probe_mode_3030.setMaximumSize(QSize(60, 31))
        self.probe_mode_3030.setAlignment(Qt.AlignCenter)
        self.probe_mode_3030.setReadOnly(True)

        self.horizontalLayout_52.addWidget(self.probe_mode_3030)


        self.verticalLayout_25.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_112 = QLabel(self.frame_2)
        self.label_112.setObjectName(u"label_112")
        sizePolicy6.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy6)
        self.label_112.setMinimumSize(QSize(150, 31))
        self.label_112.setMaximumSize(QSize(200, 31))
        self.label_112.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_112.setFrameShape(QFrame.NoFrame)
        self.label_112.setLineWidth(0)
        self.label_112.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_112.setIndent(0)

        self.horizontalLayout_53.addWidget(self.label_112)

        self.wco_rotation_3031 = VCPLineEdit(self.frame_2)
        self.wco_rotation_3031.setObjectName(u"wco_rotation_3031")
        sizePolicy.setHeightForWidth(self.wco_rotation_3031.sizePolicy().hasHeightForWidth())
        self.wco_rotation_3031.setSizePolicy(sizePolicy)
        self.wco_rotation_3031.setMinimumSize(QSize(60, 31))
        self.wco_rotation_3031.setMaximumSize(QSize(60, 31))
        self.wco_rotation_3031.setAlignment(Qt.AlignCenter)
        self.wco_rotation_3031.setReadOnly(True)

        self.horizontalLayout_53.addWidget(self.wco_rotation_3031)


        self.verticalLayout_25.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_115 = QLabel(self.frame_2)
        self.label_115.setObjectName(u"label_115")
        sizePolicy6.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy6)
        self.label_115.setMinimumSize(QSize(150, 31))
        self.label_115.setMaximumSize(QSize(200, 31))
        self.label_115.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"	font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_115.setFrameShape(QFrame.NoFrame)
        self.label_115.setLineWidth(0)
        self.label_115.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_115.setIndent(0)

        self.horizontalLayout_59.addWidget(self.label_115)

        self.sq_cal_axis_3036 = VCPLineEdit(self.frame_2)
        self.sq_cal_axis_3036.setObjectName(u"sq_cal_axis_3036")
        sizePolicy.setHeightForWidth(self.sq_cal_axis_3036.sizePolicy().hasHeightForWidth())
        self.sq_cal_axis_3036.setSizePolicy(sizePolicy)
        self.sq_cal_axis_3036.setMinimumSize(QSize(60, 31))
        self.sq_cal_axis_3036.setMaximumSize(QSize(60, 31))
        self.sq_cal_axis_3036.setAlignment(Qt.AlignCenter)
        self.sq_cal_axis_3036.setReadOnly(True)

        self.horizontalLayout_59.addWidget(self.sq_cal_axis_3036)


        self.verticalLayout_25.addLayout(self.horizontalLayout_59)


        self.verticalLayout_44.addWidget(self.frame_2)


        self.horizontalLayout_142.addWidget(self.widget_58)

        self.tabWidget.addTab(self.status_tab, "")

        self.verticalLayout_30.addWidget(self.tabWidget)


        self.horizontalLayout_101.addLayout(self.verticalLayout_30)

        self.side_bar = QWidget(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        sizePolicy8.setHeightForWidth(self.side_bar.sizePolicy().hasHeightForWidth())
        self.side_bar.setSizePolicy(sizePolicy8)
        self.side_bar.setMinimumSize(QSize(253, 0))
        self.side_bar.setMaximumSize(QSize(253, 16777215))
        self.side_bar.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.side_bar)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_60 = QWidget(self.side_bar)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setStyleSheet(u".QWidget {\n"
"    Background: rgb(146, 150, 149);\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_32.setSpacing(3)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 6)
        self.side_bar_2 = QWidget(self.widget_60)
        self.side_bar_2.setObjectName(u"side_bar_2")
        self.verticalLayout = QVBoxLayout(self.side_bar_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 2, 3, 2)
        self.widget_63 = QWidget(self.side_bar_2)
        self.widget_63.setObjectName(u"widget_63")
        self.verticalLayout_9 = QVBoxLayout(self.widget_63)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_178 = QLabel(self.widget_63)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy)
        self.label_178.setMinimumSize(QSize(201, 20))
        self.label_178.setMaximumSize(QSize(201, 20))
        self.label_178.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_178.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_178)

        self.frame_26 = QFrame(self.widget_63)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy18 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(1)
        sizePolicy18.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy18)
        self.frame_26.setMinimumSize(QSize(201, 0))
        self.frame_26.setMaximumSize(QSize(201, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setSpacing(22)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, 6, 9, 12)
        self.sidebar_widget = QStackedWidget(self.frame_26)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setStyleSheet(u".QWidget{\n"
"    background: rgb(46, 52, 54);\n"
"}")
        self.sb_page_1 = QWidget()
        self.sb_page_1.setObjectName(u"sb_page_1")
        self.sb_page_1.setStyleSheet(u"")
        self.verticalLayout_64 = QVBoxLayout(self.sb_page_1)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.jogDisplay = VCPStackedWidget(self.sb_page_1)
        self.jogDisplay.setObjectName(u"jogDisplay")
        self.jog_xyz = QWidget()
        self.jog_xyz.setObjectName(u"jog_xyz")
        self.verticalLayout_69 = QVBoxLayout(self.jog_xyz)
        self.verticalLayout_69.setSpacing(6)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(-1, 30, -1, 40)
        self.horizontalLayout_164 = QHBoxLayout()
        self.horizontalLayout_164.setObjectName(u"horizontalLayout_164")
        self.horizontalLayout_164.setContentsMargins(-1, 15, -1, 15)
        self.z_plus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.z_plus_jogbutton_3.setObjectName(u"z_plus_jogbutton_3")
        self.z_plus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.z_plus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon54 = QIcon()
        icon54.addFile(u":/images/z_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.z_plus_jogbutton_3.setIcon(icon54)
        self.z_plus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_164.addWidget(self.z_plus_jogbutton_3)


        self.verticalLayout_69.addLayout(self.horizontalLayout_164)

        self.horizontalLayout_172 = QHBoxLayout()
        self.horizontalLayout_172.setObjectName(u"horizontalLayout_172")
        self.horizontalLayout_172.setContentsMargins(-1, 15, -1, 15)
        self.z_minus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.z_minus_jogbutton_3.setObjectName(u"z_minus_jogbutton_3")
        self.z_minus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.z_minus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon55 = QIcon()
        icon55.addFile(u":/images/z_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.z_minus_jogbutton_3.setIcon(icon55)
        self.z_minus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_172.addWidget(self.z_minus_jogbutton_3)


        self.verticalLayout_69.addLayout(self.horizontalLayout_172)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setHorizontalSpacing(0)
        self.gridLayout_13.setVerticalSpacing(15)
        self.gridLayout_13.setContentsMargins(-1, 30, -1, -1)
        self.y_plus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.y_plus_jogbutton_3.setObjectName(u"y_plus_jogbutton_3")
        self.y_plus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.y_plus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon56 = QIcon()
        icon56.addFile(u":/images/y_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.y_plus_jogbutton_3.setIcon(icon56)
        self.y_plus_jogbutton_3.setIconSize(QSize(48, 48))

        self.gridLayout_13.addWidget(self.y_plus_jogbutton_3, 0, 1, 1, 1)

        self.x_plus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.x_plus_jogbutton_3.setObjectName(u"x_plus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton_3.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.x_plus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon57 = QIcon()
        icon57.addFile(u":/images/x_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_plus_jogbutton_3.setIcon(icon57)
        self.x_plus_jogbutton_3.setIconSize(QSize(48, 48))

        self.gridLayout_13.addWidget(self.x_plus_jogbutton_3, 1, 2, 1, 1)

        self.y_minus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.y_minus_jogbutton_3.setObjectName(u"y_minus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton_3.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.y_minus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon58 = QIcon()
        icon58.addFile(u":/images/y_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.y_minus_jogbutton_3.setIcon(icon58)
        self.y_minus_jogbutton_3.setIconSize(QSize(48, 48))

        self.gridLayout_13.addWidget(self.y_minus_jogbutton_3, 2, 1, 1, 1)

        self.x_minus_jogbutton_3 = ActionButton(self.jog_xyz)
        self.x_minus_jogbutton_3.setObjectName(u"x_minus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton_3.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.x_minus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        icon59 = QIcon()
        icon59.addFile(u":/images/x_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.x_minus_jogbutton_3.setIcon(icon59)
        self.x_minus_jogbutton_3.setIconSize(QSize(48, 48))

        self.gridLayout_13.addWidget(self.x_minus_jogbutton_3, 1, 0, 1, 1)


        self.verticalLayout_69.addLayout(self.gridLayout_13)

        self.jogDisplay.addWidget(self.jog_xyz)
        self.jog_xyza = QWidget()
        self.jog_xyza.setObjectName(u"jog_xyza")
        self.verticalLayout_68 = QVBoxLayout(self.jog_xyza)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.horizontalLayout_113 = QHBoxLayout()
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.z_plus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.z_plus_jogbutton_2.setObjectName(u"z_plus_jogbutton_2")
        self.z_plus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.z_plus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.z_plus_jogbutton_2.setIcon(icon54)
        self.z_plus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_113.addWidget(self.z_plus_jogbutton_2)


        self.verticalLayout_68.addLayout(self.horizontalLayout_113)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.z_minus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.z_minus_jogbutton_2.setObjectName(u"z_minus_jogbutton_2")
        self.z_minus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.z_minus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.z_minus_jogbutton_2.setIcon(icon55)
        self.z_minus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_114.addWidget(self.z_minus_jogbutton_2)


        self.verticalLayout_68.addLayout(self.horizontalLayout_114)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(15)
        self.x_plus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.x_plus_jogbutton_2.setObjectName(u"x_plus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton_2.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.x_plus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.x_plus_jogbutton_2.setIcon(icon57)
        self.x_plus_jogbutton_2.setIconSize(QSize(48, 48))

        self.gridLayout_11.addWidget(self.x_plus_jogbutton_2, 1, 2, 1, 1)

        self.x_minus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.x_minus_jogbutton_2.setObjectName(u"x_minus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton_2.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.x_minus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.x_minus_jogbutton_2.setIcon(icon59)
        self.x_minus_jogbutton_2.setIconSize(QSize(48, 48))

        self.gridLayout_11.addWidget(self.x_minus_jogbutton_2, 1, 0, 1, 1)

        self.y_minus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.y_minus_jogbutton_2.setObjectName(u"y_minus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton_2.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.y_minus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.y_minus_jogbutton_2.setIcon(icon58)
        self.y_minus_jogbutton_2.setIconSize(QSize(48, 48))

        self.gridLayout_11.addWidget(self.y_minus_jogbutton_2, 2, 1, 1, 1)

        self.y_plus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.y_plus_jogbutton_2.setObjectName(u"y_plus_jogbutton_2")
        self.y_plus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.y_plus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        self.y_plus_jogbutton_2.setIcon(icon56)
        self.y_plus_jogbutton_2.setIconSize(QSize(48, 48))

        self.gridLayout_11.addWidget(self.y_plus_jogbutton_2, 0, 1, 1, 1)


        self.verticalLayout_68.addLayout(self.gridLayout_11)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.a_minus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.a_minus_jogbutton_2.setObjectName(u"a_minus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.a_minus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton_2.setSizePolicy(sizePolicy)
        self.a_minus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.a_minus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.a_minus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        icon60 = QIcon()
        icon60.addFile(u":/images/a_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.a_minus_jogbutton_2.setIcon(icon60)
        self.a_minus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_137.addWidget(self.a_minus_jogbutton_2)

        self.a_plus_jogbutton_2 = ActionButton(self.jog_xyza)
        self.a_plus_jogbutton_2.setObjectName(u"a_plus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.a_plus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton_2.setSizePolicy(sizePolicy)
        self.a_plus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.a_plus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.a_plus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        icon61 = QIcon()
        icon61.addFile(u":/images/a_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.a_plus_jogbutton_2.setIcon(icon61)
        self.a_plus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_137.addWidget(self.a_plus_jogbutton_2)


        self.verticalLayout_68.addLayout(self.horizontalLayout_137)

        self.jogDisplay.addWidget(self.jog_xyza)
        self.jog_xyzab = QWidget()
        self.jog_xyzab.setObjectName(u"jog_xyzab")
        self.verticalLayout_36 = QVBoxLayout(self.jog_xyzab)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.z_plus_jogbutton = ActionButton(self.jog_xyzab)
        self.z_plus_jogbutton.setObjectName(u"z_plus_jogbutton")
        self.z_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton.setMaximumSize(QSize(56, 56))
        self.z_plus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.z_plus_jogbutton.setIcon(icon54)
        self.z_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_106.addWidget(self.z_plus_jogbutton)


        self.verticalLayout_36.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.z_minus_jogbutton = ActionButton(self.jog_xyzab)
        self.z_minus_jogbutton.setObjectName(u"z_minus_jogbutton")
        self.z_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton.setMaximumSize(QSize(56, 56))
        self.z_minus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.z_minus_jogbutton.setIcon(icon55)
        self.z_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_107.addWidget(self.z_minus_jogbutton)


        self.verticalLayout_36.addLayout(self.horizontalLayout_107)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(15)
        self.x_plus_jogbutton = ActionButton(self.jog_xyzab)
        self.x_plus_jogbutton.setObjectName(u"x_plus_jogbutton")
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton.setMaximumSize(QSize(56, 56))
        self.x_plus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.x_plus_jogbutton.setIcon(icon57)
        self.x_plus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.x_plus_jogbutton, 1, 2, 1, 1)

        self.x_minus_jogbutton = ActionButton(self.jog_xyzab)
        self.x_minus_jogbutton.setObjectName(u"x_minus_jogbutton")
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton.setMaximumSize(QSize(56, 56))
        self.x_minus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.x_minus_jogbutton.setIcon(icon59)
        self.x_minus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.x_minus_jogbutton, 1, 0, 1, 1)

        self.y_minus_jogbutton = ActionButton(self.jog_xyzab)
        self.y_minus_jogbutton.setObjectName(u"y_minus_jogbutton")
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton.setMaximumSize(QSize(56, 56))
        self.y_minus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.y_minus_jogbutton.setIcon(icon58)
        self.y_minus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.y_minus_jogbutton, 2, 1, 1, 1)

        self.y_plus_jogbutton = ActionButton(self.jog_xyzab)
        self.y_plus_jogbutton.setObjectName(u"y_plus_jogbutton")
        self.y_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton.setMaximumSize(QSize(56, 56))
        self.y_plus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.y_plus_jogbutton.setIcon(icon56)
        self.y_plus_jogbutton.setIconSize(QSize(48, 48))

        self.gridLayout_6.addWidget(self.y_plus_jogbutton, 0, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_6)

        self.horizontalLayout_112 = QHBoxLayout()
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.a_minus_jogbutton = ActionButton(self.jog_xyzab)
        self.a_minus_jogbutton.setObjectName(u"a_minus_jogbutton")
        sizePolicy.setHeightForWidth(self.a_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton.setSizePolicy(sizePolicy)
        self.a_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.a_minus_jogbutton.setMaximumSize(QSize(56, 56))
        self.a_minus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.a_minus_jogbutton.setIcon(icon60)
        self.a_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_112.addWidget(self.a_minus_jogbutton)

        self.a_plus_jogbutton = ActionButton(self.jog_xyzab)
        self.a_plus_jogbutton.setObjectName(u"a_plus_jogbutton")
        sizePolicy.setHeightForWidth(self.a_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton.setSizePolicy(sizePolicy)
        self.a_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.a_plus_jogbutton.setMaximumSize(QSize(56, 56))
        self.a_plus_jogbutton.setFocusPolicy(Qt.NoFocus)
        self.a_plus_jogbutton.setIcon(icon61)
        self.a_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_112.addWidget(self.a_plus_jogbutton)


        self.verticalLayout_36.addLayout(self.horizontalLayout_112)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.b_minus_jogbutton = ActionButton(self.jog_xyzab)
        self.b_minus_jogbutton.setObjectName(u"b_minus_jogbutton")
        sizePolicy.setHeightForWidth(self.b_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_minus_jogbutton.setSizePolicy(sizePolicy)
        self.b_minus_jogbutton.setMinimumSize(QSize(56, 56))
        self.b_minus_jogbutton.setMaximumSize(QSize(56, 56))
        self.b_minus_jogbutton.setFocusPolicy(Qt.NoFocus)
        icon62 = QIcon()
        icon62.addFile(u":/images/b_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_minus_jogbutton.setIcon(icon62)
        self.b_minus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_111.addWidget(self.b_minus_jogbutton)

        self.b_plus_jogbutton = ActionButton(self.jog_xyzab)
        self.b_plus_jogbutton.setObjectName(u"b_plus_jogbutton")
        sizePolicy.setHeightForWidth(self.b_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_plus_jogbutton.setSizePolicy(sizePolicy)
        self.b_plus_jogbutton.setMinimumSize(QSize(56, 56))
        self.b_plus_jogbutton.setMaximumSize(QSize(56, 56))
        self.b_plus_jogbutton.setFocusPolicy(Qt.NoFocus)
        icon63 = QIcon()
        icon63.addFile(u":/images/b_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b_plus_jogbutton.setIcon(icon63)
        self.b_plus_jogbutton.setIconSize(QSize(48, 48))

        self.horizontalLayout_111.addWidget(self.b_plus_jogbutton)


        self.verticalLayout_36.addLayout(self.horizontalLayout_111)

        self.jogDisplay.addWidget(self.jog_xyzab)
        self.jog_xyzac = QWidget()
        self.jog_xyzac.setObjectName(u"jog_xyzac")
        self.verticalLayout_79 = QVBoxLayout(self.jog_xyzac)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.horizontalLayout_166 = QHBoxLayout()
        self.horizontalLayout_166.setObjectName(u"horizontalLayout_166")
        self.z_plus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.z_plus_jogbutton_4.setObjectName(u"z_plus_jogbutton_4")
        self.z_plus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.z_plus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.z_plus_jogbutton_4.setIcon(icon54)
        self.z_plus_jogbutton_4.setIconSize(QSize(48, 48))

        self.horizontalLayout_166.addWidget(self.z_plus_jogbutton_4)


        self.verticalLayout_79.addLayout(self.horizontalLayout_166)

        self.horizontalLayout_168 = QHBoxLayout()
        self.horizontalLayout_168.setObjectName(u"horizontalLayout_168")
        self.z_minus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.z_minus_jogbutton_4.setObjectName(u"z_minus_jogbutton_4")
        self.z_minus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.z_minus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.z_minus_jogbutton_4.setIcon(icon55)
        self.z_minus_jogbutton_4.setIconSize(QSize(48, 48))

        self.horizontalLayout_168.addWidget(self.z_minus_jogbutton_4)


        self.verticalLayout_79.addLayout(self.horizontalLayout_168)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setVerticalSpacing(15)
        self.x_plus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.x_plus_jogbutton_4.setObjectName(u"x_plus_jogbutton_4")
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton_4.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton_4.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.x_plus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.x_plus_jogbutton_4.setIcon(icon57)
        self.x_plus_jogbutton_4.setIconSize(QSize(48, 48))

        self.gridLayout_14.addWidget(self.x_plus_jogbutton_4, 1, 2, 1, 1)

        self.x_minus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.x_minus_jogbutton_4.setObjectName(u"x_minus_jogbutton_4")
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton_4.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton_4.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.x_minus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.x_minus_jogbutton_4.setIcon(icon59)
        self.x_minus_jogbutton_4.setIconSize(QSize(48, 48))

        self.gridLayout_14.addWidget(self.x_minus_jogbutton_4, 1, 0, 1, 1)

        self.y_minus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.y_minus_jogbutton_4.setObjectName(u"y_minus_jogbutton_4")
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton_4.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton_4.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.y_minus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.y_minus_jogbutton_4.setIcon(icon58)
        self.y_minus_jogbutton_4.setIconSize(QSize(48, 48))

        self.gridLayout_14.addWidget(self.y_minus_jogbutton_4, 2, 1, 1, 1)

        self.y_plus_jogbutton_4 = ActionButton(self.jog_xyzac)
        self.y_plus_jogbutton_4.setObjectName(u"y_plus_jogbutton_4")
        self.y_plus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.y_plus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.y_plus_jogbutton_4.setIcon(icon56)
        self.y_plus_jogbutton_4.setIconSize(QSize(48, 48))

        self.gridLayout_14.addWidget(self.y_plus_jogbutton_4, 0, 1, 1, 1)


        self.verticalLayout_79.addLayout(self.gridLayout_14)

        self.horizontalLayout_167 = QHBoxLayout()
        self.horizontalLayout_167.setObjectName(u"horizontalLayout_167")
        self.a_minus_jogbutton_3 = ActionButton(self.jog_xyzac)
        self.a_minus_jogbutton_3.setObjectName(u"a_minus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.a_minus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton_3.setSizePolicy(sizePolicy)
        self.a_minus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.a_minus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.a_minus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        self.a_minus_jogbutton_3.setIcon(icon60)
        self.a_minus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_167.addWidget(self.a_minus_jogbutton_3)

        self.a_plus_jogbutton_3 = ActionButton(self.jog_xyzac)
        self.a_plus_jogbutton_3.setObjectName(u"a_plus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.a_plus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton_3.setSizePolicy(sizePolicy)
        self.a_plus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.a_plus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.a_plus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        self.a_plus_jogbutton_3.setIcon(icon61)
        self.a_plus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_167.addWidget(self.a_plus_jogbutton_3)


        self.verticalLayout_79.addLayout(self.horizontalLayout_167)

        self.horizontalLayout_165 = QHBoxLayout()
        self.horizontalLayout_165.setObjectName(u"horizontalLayout_165")
        self.c_minus_jogbutton_2 = ActionButton(self.jog_xyzac)
        self.c_minus_jogbutton_2.setObjectName(u"c_minus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.c_minus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.c_minus_jogbutton_2.setSizePolicy(sizePolicy)
        self.c_minus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.c_minus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.c_minus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        icon64 = QIcon()
        icon64.addFile(u":/images/c_minus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.c_minus_jogbutton_2.setIcon(icon64)
        self.c_minus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_165.addWidget(self.c_minus_jogbutton_2)

        self.c_plus_jogbutton_2 = ActionButton(self.jog_xyzac)
        self.c_plus_jogbutton_2.setObjectName(u"c_plus_jogbutton_2")
        sizePolicy.setHeightForWidth(self.c_plus_jogbutton_2.sizePolicy().hasHeightForWidth())
        self.c_plus_jogbutton_2.setSizePolicy(sizePolicy)
        self.c_plus_jogbutton_2.setMinimumSize(QSize(56, 56))
        self.c_plus_jogbutton_2.setMaximumSize(QSize(56, 56))
        self.c_plus_jogbutton_2.setFocusPolicy(Qt.NoFocus)
        icon65 = QIcon()
        icon65.addFile(u":/images/c_plus_jog_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.c_plus_jogbutton_2.setIcon(icon65)
        self.c_plus_jogbutton_2.setIconSize(QSize(48, 48))

        self.horizontalLayout_165.addWidget(self.c_plus_jogbutton_2)


        self.verticalLayout_79.addLayout(self.horizontalLayout_165)

        self.jogDisplay.addWidget(self.jog_xyzac)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_200 = QHBoxLayout()
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.z_plus_jogbutton_9 = ActionButton(self.page)
        self.z_plus_jogbutton_9.setObjectName(u"z_plus_jogbutton_9")
        self.z_plus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.z_plus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.z_plus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.z_plus_jogbutton_9.setIcon(icon54)
        self.z_plus_jogbutton_9.setIconSize(QSize(48, 48))

        self.horizontalLayout_200.addWidget(self.z_plus_jogbutton_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_200)

        self.horizontalLayout_203 = QHBoxLayout()
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.z_minus_jogbutton_9 = ActionButton(self.page)
        self.z_minus_jogbutton_9.setObjectName(u"z_minus_jogbutton_9")
        self.z_minus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.z_minus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.z_minus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.z_minus_jogbutton_9.setIcon(icon55)
        self.z_minus_jogbutton_9.setIconSize(QSize(48, 48))

        self.horizontalLayout_203.addWidget(self.z_minus_jogbutton_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_203)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(0)
        self.gridLayout_20.setVerticalSpacing(15)
        self.x_plus_jogbutton_9 = ActionButton(self.page)
        self.x_plus_jogbutton_9.setObjectName(u"x_plus_jogbutton_9")
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton_9.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton_9.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.x_plus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.x_plus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.x_plus_jogbutton_9.setIcon(icon57)
        self.x_plus_jogbutton_9.setIconSize(QSize(48, 48))

        self.gridLayout_20.addWidget(self.x_plus_jogbutton_9, 1, 2, 1, 1)

        self.x_minus_jogbutton_9 = ActionButton(self.page)
        self.x_minus_jogbutton_9.setObjectName(u"x_minus_jogbutton_9")
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton_9.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton_9.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.x_minus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.x_minus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.x_minus_jogbutton_9.setIcon(icon59)
        self.x_minus_jogbutton_9.setIconSize(QSize(48, 48))

        self.gridLayout_20.addWidget(self.x_minus_jogbutton_9, 1, 0, 1, 1)

        self.y_minus_jogbutton_9 = ActionButton(self.page)
        self.y_minus_jogbutton_9.setObjectName(u"y_minus_jogbutton_9")
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton_9.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton_9.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.y_minus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.y_minus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.y_minus_jogbutton_9.setIcon(icon58)
        self.y_minus_jogbutton_9.setIconSize(QSize(48, 48))

        self.gridLayout_20.addWidget(self.y_minus_jogbutton_9, 2, 1, 1, 1)

        self.y_plus_jogbutton_9 = ActionButton(self.page)
        self.y_plus_jogbutton_9.setObjectName(u"y_plus_jogbutton_9")
        self.y_plus_jogbutton_9.setMinimumSize(QSize(56, 56))
        self.y_plus_jogbutton_9.setMaximumSize(QSize(56, 56))
        self.y_plus_jogbutton_9.setFocusPolicy(Qt.NoFocus)
        self.y_plus_jogbutton_9.setIcon(icon56)
        self.y_plus_jogbutton_9.setIconSize(QSize(48, 48))

        self.gridLayout_20.addWidget(self.y_plus_jogbutton_9, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_20)

        self.horizontalLayout_202 = QHBoxLayout()
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.b_minus_jogbutton_3 = ActionButton(self.page)
        self.b_minus_jogbutton_3.setObjectName(u"b_minus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.b_minus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.b_minus_jogbutton_3.setSizePolicy(sizePolicy)
        self.b_minus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.b_minus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.b_minus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        self.b_minus_jogbutton_3.setIcon(icon62)
        self.b_minus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_202.addWidget(self.b_minus_jogbutton_3)

        self.b_plus_jogbutton_3 = ActionButton(self.page)
        self.b_plus_jogbutton_3.setObjectName(u"b_plus_jogbutton_3")
        sizePolicy.setHeightForWidth(self.b_plus_jogbutton_3.sizePolicy().hasHeightForWidth())
        self.b_plus_jogbutton_3.setSizePolicy(sizePolicy)
        self.b_plus_jogbutton_3.setMinimumSize(QSize(56, 56))
        self.b_plus_jogbutton_3.setMaximumSize(QSize(56, 56))
        self.b_plus_jogbutton_3.setFocusPolicy(Qt.NoFocus)
        self.b_plus_jogbutton_3.setIcon(icon63)
        self.b_plus_jogbutton_3.setIconSize(QSize(48, 48))

        self.horizontalLayout_202.addWidget(self.b_plus_jogbutton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_202)

        self.horizontalLayout_199 = QHBoxLayout()
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.c_minus_jogbutton_4 = ActionButton(self.page)
        self.c_minus_jogbutton_4.setObjectName(u"c_minus_jogbutton_4")
        sizePolicy.setHeightForWidth(self.c_minus_jogbutton_4.sizePolicy().hasHeightForWidth())
        self.c_minus_jogbutton_4.setSizePolicy(sizePolicy)
        self.c_minus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.c_minus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.c_minus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.c_minus_jogbutton_4.setIcon(icon64)
        self.c_minus_jogbutton_4.setIconSize(QSize(48, 48))

        self.horizontalLayout_199.addWidget(self.c_minus_jogbutton_4)

        self.c_plus_jogbutton_4 = ActionButton(self.page)
        self.c_plus_jogbutton_4.setObjectName(u"c_plus_jogbutton_4")
        sizePolicy.setHeightForWidth(self.c_plus_jogbutton_4.sizePolicy().hasHeightForWidth())
        self.c_plus_jogbutton_4.setSizePolicy(sizePolicy)
        self.c_plus_jogbutton_4.setMinimumSize(QSize(56, 56))
        self.c_plus_jogbutton_4.setMaximumSize(QSize(56, 56))
        self.c_plus_jogbutton_4.setFocusPolicy(Qt.NoFocus)
        self.c_plus_jogbutton_4.setIcon(icon65)
        self.c_plus_jogbutton_4.setIconSize(QSize(48, 48))

        self.horizontalLayout_199.addWidget(self.c_plus_jogbutton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_199)

        self.jogDisplay.addWidget(self.page)

        self.verticalLayout_64.addWidget(self.jogDisplay)

        self.sidebar_widget.addWidget(self.sb_page_1)
        self.sb_page_2 = QWidget()
        self.sb_page_2.setObjectName(u"sb_page_2")
        self.sb_page_2.setStyleSheet(u"")
        self.verticalLayout_63 = QVBoxLayout(self.sb_page_2)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(-1, 15, -1, -1)
        self.widget_5 = QWidget(self.sb_page_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QSize(171, 0))
        self.widget_5.setMaximumSize(QSize(171, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setSpacing(15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 15, 6)
        self.actionbutton_g58_3 = ActionButton(self.widget_5)
        self.customwcsbtnGroup = QButtonGroup(Form)
        self.customwcsbtnGroup.setObjectName(u"customwcsbtnGroup")
        self.customwcsbtnGroup.addButton(self.actionbutton_g58_3)
        self.actionbutton_g58_3.setObjectName(u"actionbutton_g58_3")
        self.actionbutton_g58_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g58_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_g58_3.setSizePolicy(sizePolicy)
        self.actionbutton_g58_3.setMinimumSize(QSize(75, 40))
        self.actionbutton_g58_3.setMaximumSize(QSize(75, 40))
        self.actionbutton_g58_3.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g58_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g58_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g58_3, 4, 0, 1, 1)

        self.actionbutton_g59_8 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g59_8)
        self.actionbutton_g59_8.setObjectName(u"actionbutton_g59_8")
        self.actionbutton_g59_8.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_8.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_8.setSizePolicy(sizePolicy)
        self.actionbutton_g59_8.setMinimumSize(QSize(75, 40))
        self.actionbutton_g59_8.setMaximumSize(QSize(75, 40))
        self.actionbutton_g59_8.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_8.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_8.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g59_8, 9, 0, 1, 1)

        self.actionbutton_g54_3 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g54_3)
        self.actionbutton_g54_3.setObjectName(u"actionbutton_g54_3")
        self.actionbutton_g54_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g54_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_g54_3.setSizePolicy(sizePolicy)
        self.actionbutton_g54_3.setMinimumSize(QSize(75, 40))
        self.actionbutton_g54_3.setMaximumSize(QSize(75, 40))
        self.actionbutton_g54_3.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g54_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g54_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g54_3, 0, 0, 1, 1)

        self.actionbutton_g56_3 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g56_3)
        self.actionbutton_g56_3.setObjectName(u"actionbutton_g56_3")
        self.actionbutton_g56_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g56_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_g56_3.setSizePolicy(sizePolicy)
        self.actionbutton_g56_3.setMinimumSize(QSize(75, 40))
        self.actionbutton_g56_3.setMaximumSize(QSize(75, 40))
        self.actionbutton_g56_3.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g56_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g56_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g56_3, 2, 0, 1, 1)

        self.actionbutton_g55_3 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g55_3)
        self.actionbutton_g55_3.setObjectName(u"actionbutton_g55_3")
        self.actionbutton_g55_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g55_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_g55_3.setSizePolicy(sizePolicy)
        self.actionbutton_g55_3.setMinimumSize(QSize(75, 40))
        self.actionbutton_g55_3.setMaximumSize(QSize(75, 40))
        self.actionbutton_g55_3.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g55_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g55_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g55_3, 0, 1, 1, 1)

        self.actionbutton_g57_3 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g57_3)
        self.actionbutton_g57_3.setObjectName(u"actionbutton_g57_3")
        self.actionbutton_g57_3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g57_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_g57_3.setSizePolicy(sizePolicy)
        self.actionbutton_g57_3.setMinimumSize(QSize(75, 40))
        self.actionbutton_g57_3.setMaximumSize(QSize(75, 40))
        self.actionbutton_g57_3.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g57_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g57_3.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g57_3, 2, 1, 1, 1)

        self.actionbutton_g59_10 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g59_10)
        self.actionbutton_g59_10.setObjectName(u"actionbutton_g59_10")
        self.actionbutton_g59_10.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_10.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_10.setSizePolicy(sizePolicy)
        self.actionbutton_g59_10.setMinimumSize(QSize(75, 40))
        self.actionbutton_g59_10.setMaximumSize(QSize(75, 40))
        self.actionbutton_g59_10.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_10.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_10.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g59_10, 4, 1, 1, 1)

        self.actionbutton_g59_11 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g59_11)
        self.actionbutton_g59_11.setObjectName(u"actionbutton_g59_11")
        self.actionbutton_g59_11.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_11.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_11.setSizePolicy(sizePolicy)
        self.actionbutton_g59_11.setMinimumSize(QSize(75, 40))
        self.actionbutton_g59_11.setMaximumSize(QSize(75, 40))
        self.actionbutton_g59_11.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_11.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_11.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g59_11, 7, 1, 1, 1)

        self.actionbutton_g59_9 = ActionButton(self.widget_5)
        self.customwcsbtnGroup.addButton(self.actionbutton_g59_9)
        self.actionbutton_g59_9.setObjectName(u"actionbutton_g59_9")
        self.actionbutton_g59_9.setEnabled(False)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_9.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_9.setSizePolicy(sizePolicy)
        self.actionbutton_g59_9.setMinimumSize(QSize(75, 40))
        self.actionbutton_g59_9.setMaximumSize(QSize(75, 40))
        self.actionbutton_g59_9.setFocusPolicy(Qt.NoFocus)
        self.actionbutton_g59_9.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_9.setAutoExclusive(True)

        self.gridLayout_3.addWidget(self.actionbutton_g59_9, 7, 0, 1, 1)


        self.verticalLayout_63.addWidget(self.widget_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_47 = QWidget(self.sb_page_2)
        self.widget_47.setObjectName(u"widget_47")
        sizePolicy11.setHeightForWidth(self.widget_47.sizePolicy().hasHeightForWidth())
        self.widget_47.setSizePolicy(sizePolicy11)
        self.verticalLayout_50 = QVBoxLayout(self.widget_47)
        self.verticalLayout_50.setSpacing(20)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(15, 12, 15, 12)
        self.ref_all_button_2 = ActionButton(self.widget_47)
        self.ref_all_button_2.setObjectName(u"ref_all_button_2")
        sizePolicy2.setHeightForWidth(self.ref_all_button_2.sizePolicy().hasHeightForWidth())
        self.ref_all_button_2.setSizePolicy(sizePolicy2)
        self.ref_all_button_2.setMinimumSize(QSize(62, 40))
        self.ref_all_button_2.setMaximumSize(QSize(16777215, 40))
        self.ref_all_button_2.setFocusPolicy(Qt.NoFocus)
        self.ref_all_button_2.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.verticalLayout_50.addWidget(self.ref_all_button_2)

        self.axisactionbutton_12 = ActionButton(self.widget_47)
        self.axisactionbutton_12.setObjectName(u"axisactionbutton_12")
        sizePolicy6.setHeightForWidth(self.axisactionbutton_12.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_12.setSizePolicy(sizePolicy6)
        self.axisactionbutton_12.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_12.setMaximumSize(QSize(16777215, 40))
        self.axisactionbutton_12.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.verticalLayout_50.addWidget(self.axisactionbutton_12)

        self.axisactionbutton_15 = ActionButton(self.widget_47)
        self.axisactionbutton_15.setObjectName(u"axisactionbutton_15")
        sizePolicy6.setHeightForWidth(self.axisactionbutton_15.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_15.setSizePolicy(sizePolicy6)
        self.axisactionbutton_15.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_15.setMaximumSize(QSize(16777215, 40))
        self.axisactionbutton_15.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.verticalLayout_50.addWidget(self.axisactionbutton_15)

        self.axisactionbutton_14 = ActionButton(self.widget_47)
        self.axisactionbutton_14.setObjectName(u"axisactionbutton_14")
        sizePolicy6.setHeightForWidth(self.axisactionbutton_14.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_14.setSizePolicy(sizePolicy6)
        self.axisactionbutton_14.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_14.setMaximumSize(QSize(16777215, 40))
        self.axisactionbutton_14.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")

        self.verticalLayout_50.addWidget(self.axisactionbutton_14)

        self.axisactionbutton_16 = ActionButton(self.widget_47)
        self.axisactionbutton_16.setObjectName(u"axisactionbutton_16")
        sizePolicy6.setHeightForWidth(self.axisactionbutton_16.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_16.setSizePolicy(sizePolicy6)
        self.axisactionbutton_16.setMinimumSize(QSize(60, 40))
        self.axisactionbutton_16.setMaximumSize(QSize(16777215, 40))
        self.axisactionbutton_16.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_16.setCheckable(True)

        self.verticalLayout_50.addWidget(self.axisactionbutton_16)


        self.verticalLayout_63.addWidget(self.widget_47)

        self.sidebar_widget.addWidget(self.sb_page_2)
        self.sb_page_3 = QWidget()
        self.sb_page_3.setObjectName(u"sb_page_3")
        self.sb_page_3.setStyleSheet(u"")
        self.verticalLayout_40 = QVBoxLayout(self.sb_page_3)
        self.verticalLayout_40.setSpacing(9)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 10, -1, -1)
        self.program_boundary_button = VCPSettingsPushButton(self.sb_page_3)
        self.program_boundary_button.setObjectName(u"program_boundary_button")
        sizePolicy6.setHeightForWidth(self.program_boundary_button.sizePolicy().hasHeightForWidth())
        self.program_boundary_button.setSizePolicy(sizePolicy6)
        self.program_boundary_button.setMinimumSize(QSize(0, 40))
        self.program_boundary_button.setMaximumSize(QSize(16777215, 30))
        self.program_boundary_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_40.addWidget(self.program_boundary_button)

        self.machine_boundary_button = VCPSettingsPushButton(self.sb_page_3)
        self.machine_boundary_button.setObjectName(u"machine_boundary_button")
        sizePolicy6.setHeightForWidth(self.machine_boundary_button.sizePolicy().hasHeightForWidth())
        self.machine_boundary_button.setSizePolicy(sizePolicy6)
        self.machine_boundary_button.setMinimumSize(QSize(0, 40))
        self.machine_boundary_button.setMaximumSize(QSize(16777215, 30))
        self.machine_boundary_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_40.addWidget(self.machine_boundary_button)

        self.plot_grid_button = VCPSettingsPushButton(self.sb_page_3)
        self.plot_grid_button.setObjectName(u"plot_grid_button")
        sizePolicy6.setHeightForWidth(self.plot_grid_button.sizePolicy().hasHeightForWidth())
        self.plot_grid_button.setSizePolicy(sizePolicy6)
        self.plot_grid_button.setMinimumSize(QSize(0, 40))
        self.plot_grid_button.setMaximumSize(QSize(16777215, 30))
        self.plot_grid_button.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_40.addWidget(self.plot_grid_button)

        self.widget_101 = QWidget(self.sb_page_3)
        self.widget_101.setObjectName(u"widget_101")
        self.widget_101.setAutoFillBackground(False)
        self.widget_101.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.widget_101)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_40.addWidget(self.widget_101)

        self.sidebar_widget.addWidget(self.sb_page_3)
        self.sb_page_4 = QWidget()
        self.sb_page_4.setObjectName(u"sb_page_4")
        self.sidebar_widget.addWidget(self.sb_page_4)

        self.verticalLayout_32.addWidget(self.sidebar_widget)

        self.horizontalWidget1 = QWidget(self.frame_26)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        sizePolicy6.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy6)
        self.horizontalWidget1.setMinimumSize(QSize(0, 42))
        self.horizontalWidget1.setMaximumSize(QSize(16777215, 42))
        self.horizontalWidget1.setStyleSheet(u".QWidget{\n"
"    background: rgb(46, 52, 54);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.manual_mode_button = ActionButton(self.horizontalWidget1)
        self.manual_mode_button.setObjectName(u"manual_mode_button")
        sizePolicy6.setHeightForWidth(self.manual_mode_button.sizePolicy().hasHeightForWidth())
        self.manual_mode_button.setSizePolicy(sizePolicy6)
        self.manual_mode_button.setMinimumSize(QSize(0, 40))
        self.manual_mode_button.setMaximumSize(QSize(16777215, 40))
        self.manual_mode_button.setFocusPolicy(Qt.NoFocus)
        self.manual_mode_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.manual_mode_button.setCheckable(True)
        self.manual_mode_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.manual_mode_button)

        self.auto_mode_button = ActionButton(self.horizontalWidget1)
        self.auto_mode_button.setObjectName(u"auto_mode_button")
        sizePolicy6.setHeightForWidth(self.auto_mode_button.sizePolicy().hasHeightForWidth())
        self.auto_mode_button.setSizePolicy(sizePolicy6)
        self.auto_mode_button.setMinimumSize(QSize(0, 40))
        self.auto_mode_button.setMaximumSize(QSize(16777215, 40))
        self.auto_mode_button.setFocusPolicy(Qt.NoFocus)
        self.auto_mode_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.auto_mode_button.setCheckable(True)
        self.auto_mode_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.auto_mode_button)

        self.mdi_mode_button = ActionButton(self.horizontalWidget1)
        self.mdi_mode_button.setObjectName(u"mdi_mode_button")
        sizePolicy6.setHeightForWidth(self.mdi_mode_button.sizePolicy().hasHeightForWidth())
        self.mdi_mode_button.setSizePolicy(sizePolicy6)
        self.mdi_mode_button.setMinimumSize(QSize(0, 40))
        self.mdi_mode_button.setMaximumSize(QSize(16777215, 40))
        self.mdi_mode_button.setFocusPolicy(Qt.NoFocus)
        self.mdi_mode_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.mdi_mode_button.setCheckable(True)
        self.mdi_mode_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.mdi_mode_button)


        self.verticalLayout_32.addWidget(self.horizontalWidget1)


        self.verticalLayout_9.addWidget(self.frame_26)


        self.verticalLayout.addWidget(self.widget_63)


        self.horizontalLayout_32.addWidget(self.side_bar_2)

        self.widget_4 = QWidget(self.widget_60)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy8.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy8)
        self.widget_4.setMinimumSize(QSize(35, 0))
        self.widget_4.setMaximumSize(QSize(35, 16777215))
        self.verticalLayout_52 = QVBoxLayout(self.widget_4)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_52.setContentsMargins(0, 2, 0, 0)
        self.statuslabel_19 = StatusLabel(self.widget_4)
        self.statuslabel_19.setObjectName(u"statuslabel_19")
        self.statuslabel_19.setEnabled(True)
        sizePolicy18.setHeightForWidth(self.statuslabel_19.sizePolicy().hasHeightForWidth())
        self.statuslabel_19.setSizePolicy(sizePolicy18)
        self.statuslabel_19.setMinimumSize(QSize(35, 0))
        self.statuslabel_19.setMaximumSize(QSize(35, 16777215))
        self.statuslabel_19.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.statuslabel_19.setWordWrap(True)
        self.statuslabel_19.setIndent(0)

        self.verticalLayout_52.addWidget(self.statuslabel_19, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_186 = QLabel(self.widget_4)
        self.label_186.setObjectName(u"label_186")
        sizePolicy10.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy10)
        self.label_186.setMinimumSize(QSize(35, 9))
        self.label_186.setMaximumSize(QSize(35, 9))

        self.verticalLayout_52.addWidget(self.label_186)

        self.statuslabel_26 = StatusLabel(self.widget_4)
        self.statuslabel_26.setObjectName(u"statuslabel_26")
        sizePolicy18.setHeightForWidth(self.statuslabel_26.sizePolicy().hasHeightForWidth())
        self.statuslabel_26.setSizePolicy(sizePolicy18)
        self.statuslabel_26.setMinimumSize(QSize(35, 0))
        self.statuslabel_26.setMaximumSize(QSize(35, 16777215))
        self.statuslabel_26.setStyleSheet(u"QLabel{\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_26.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.statuslabel_26.setWordWrap(True)
        self.statuslabel_26.setIndent(0)

        self.verticalLayout_52.addWidget(self.statuslabel_26, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_185 = QLabel(self.widget_4)
        self.label_185.setObjectName(u"label_185")
        sizePolicy11.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy11)
        self.label_185.setMinimumSize(QSize(35, 0))
        self.label_185.setMaximumSize(QSize(35, 16777215))

        self.verticalLayout_52.addWidget(self.label_185)


        self.horizontalLayout_32.addWidget(self.widget_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.widget_60)

        self.widget_8 = QWidget(self.side_bar)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 1)
        self.jog_tab = QPushButton(self.widget_8)
        self.sidebartabGroup = QButtonGroup(Form)
        self.sidebartabGroup.setObjectName(u"sidebartabGroup")
        self.sidebartabGroup.addButton(self.jog_tab)
        self.jog_tab.setObjectName(u"jog_tab")
        sizePolicy5.setHeightForWidth(self.jog_tab.sizePolicy().hasHeightForWidth())
        self.jog_tab.setSizePolicy(sizePolicy5)
        self.jog_tab.setMinimumSize(QSize(0, 0))
        self.jog_tab.setFocusPolicy(Qt.NoFocus)
        self.jog_tab.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 2px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.jog_tab.setCheckable(True)
        self.jog_tab.setChecked(True)
        self.jog_tab.setAutoExclusive(True)
        self.jog_tab.setProperty(u"page", 0)

        self.horizontalLayout_9.addWidget(self.jog_tab)

        self.wcs_tab = QPushButton(self.widget_8)
        self.sidebartabGroup.addButton(self.wcs_tab)
        self.wcs_tab.setObjectName(u"wcs_tab")
        sizePolicy5.setHeightForWidth(self.wcs_tab.sizePolicy().hasHeightForWidth())
        self.wcs_tab.setSizePolicy(sizePolicy5)
        self.wcs_tab.setMinimumSize(QSize(0, 40))
        self.wcs_tab.setFocusPolicy(Qt.NoFocus)
        self.wcs_tab.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.wcs_tab.setCheckable(True)
        self.wcs_tab.setAutoExclusive(True)
        self.wcs_tab.setProperty(u"page", 1)

        self.horizontalLayout_9.addWidget(self.wcs_tab)

        self.plot_tab = QPushButton(self.widget_8)
        self.sidebartabGroup.addButton(self.plot_tab)
        self.plot_tab.setObjectName(u"plot_tab")
        sizePolicy5.setHeightForWidth(self.plot_tab.sizePolicy().hasHeightForWidth())
        self.plot_tab.setSizePolicy(sizePolicy5)
        self.plot_tab.setMinimumSize(QSize(0, 0))
        self.plot_tab.setFocusPolicy(Qt.NoFocus)
        self.plot_tab.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 1px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.plot_tab.setCheckable(True)
        self.plot_tab.setAutoExclusive(True)
        self.plot_tab.setProperty(u"page", 2)

        self.horizontalLayout_9.addWidget(self.plot_tab)

        self.user_sb_tab = QPushButton(self.widget_8)
        self.sidebartabGroup.addButton(self.user_sb_tab)
        self.user_sb_tab.setObjectName(u"user_sb_tab")
        sizePolicy5.setHeightForWidth(self.user_sb_tab.sizePolicy().hasHeightForWidth())
        self.user_sb_tab.setSizePolicy(sizePolicy5)
        self.user_sb_tab.setMinimumSize(QSize(0, 0))
        self.user_sb_tab.setFocusPolicy(Qt.NoFocus)
        self.user_sb_tab.setStyleSheet(u"QPushButton {\n"
"    margin-top: 2px;\n"
"    margin-bottom: 2px;\n"
"    color: white;\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #4e4e4e, stop: 1.0 #3a3a3a);\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-top-width: 2px;\n"
"    border-bottom-width: 2px;\n"
"    border-right-width: 2px;\n"
"    border-left-width: 1px;\n"
"    padding: 2px;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(112, 112, 238, 255), stop:0.121053 rgba(123, 123, 232, 255), stop:0.3 rgba(85, 85, 238, 255), stop:0.69473"
                        "7 rgba(85, 85, 238, 255), stop:0.915789 rgba(123, 123, 232, 255), stop:1 rgba(112, 112, 238, 255))\n"
"}")
        self.user_sb_tab.setCheckable(True)
        self.user_sb_tab.setAutoExclusive(True)
        self.user_sb_tab.setProperty(u"page", 3)

        self.horizontalLayout_9.addWidget(self.user_sb_tab)


        self.verticalLayout_12.addWidget(self.widget_8)


        self.horizontalLayout_101.addWidget(self.side_bar)


        self.verticalLayout_31.addLayout(self.horizontalLayout_101)

        self.main_control_screen_layout_panel = QHBoxLayout()
        self.main_control_screen_layout_panel.setSpacing(0)
        self.main_control_screen_layout_panel.setObjectName(u"main_control_screen_layout_panel")
        self.main_control_screen_layout_panel.setSizeConstraint(QLayout.SetFixedSize)
        self.main_control_screen_layout_panel.setContentsMargins(12, 0, 12, -1)
        self.main_control_qframe = QFrame(self.centralwidget)
        self.main_control_qframe.setObjectName(u"main_control_qframe")
        sizePolicy6.setHeightForWidth(self.main_control_qframe.sizePolicy().hasHeightForWidth())
        self.main_control_qframe.setSizePolicy(sizePolicy6)
        self.main_control_qframe.setMinimumSize(QSize(340, 340))
        self.main_control_qframe.setMaximumSize(QSize(340, 340))
        self.main_control_qframe.setStyleSheet(u".QFrame{\n"
"    color: rgb(46, 52, 54);\n"
"    background-color: rgb(46, 52, 54);\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    border-right-width:1px;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.main_control_qframe)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, 12, 20, 3)
        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setSpacing(6)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(-1, -1, -1, 3)
        self.cycle_start_button = ActionButton(self.main_control_qframe)
        self.cycle_start_button.setObjectName(u"cycle_start_button")
        sizePolicy6.setHeightForWidth(self.cycle_start_button.sizePolicy().hasHeightForWidth())
        self.cycle_start_button.setSizePolicy(sizePolicy6)
        self.cycle_start_button.setMinimumSize(QSize(140, 50))
        self.cycle_start_button.setMaximumSize(QSize(16777215, 50))
        self.cycle_start_button.setFocusPolicy(Qt.NoFocus)
        self.cycle_start_button.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QPushButton[style='inactive']{\n"
"    border-color: black;\n"
"}\n"
"\n"
"QPushButton[style='active']{\n"
"	border-color: rgb(16, 37, 255);\n"
"}")

        self.horizontalLayout_92.addWidget(self.cycle_start_button)

        self.ref_coilumn_header_25 = QLabel(self.main_control_qframe)
        self.ref_coilumn_header_25.setObjectName(u"ref_coilumn_header_25")
        sizePolicy19 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy19.setHorizontalStretch(1)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.ref_coilumn_header_25.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_25.setSizePolicy(sizePolicy19)
        self.ref_coilumn_header_25.setMinimumSize(QSize(3, 52))
        self.ref_coilumn_header_25.setMaximumSize(QSize(3, 52))
        self.ref_coilumn_header_25.setStyleSheet(u"")
        self.ref_coilumn_header_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_92.addWidget(self.ref_coilumn_header_25)

        self.stop_button = ActionButton(self.main_control_qframe)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy6.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy6)
        self.stop_button.setMinimumSize(QSize(140, 50))
        self.stop_button.setMaximumSize(QSize(16777215, 50))
        self.stop_button.setFocusPolicy(Qt.NoFocus)
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"   	font: 17pt \"Bebas Kai\";\n"
"}")

        self.horizontalLayout_92.addWidget(self.stop_button)


        self.verticalLayout_28.addLayout(self.horizontalLayout_92)

        self.user_buttons_layout = QVBoxLayout()
        self.user_buttons_layout.setSpacing(0)
        self.user_buttons_layout.setObjectName(u"user_buttons_layout")
        self.user_buttons_layout.setContentsMargins(-1, 0, -1, 3)

        self.verticalLayout_28.addLayout(self.user_buttons_layout)

        self.line = QFrame(self.main_control_qframe)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 2))
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_28.addWidget(self.line)

        self.widget9 = QWidget(self.main_control_qframe)
        self.widget9.setObjectName(u"widget9")
        sizePolicy4.setHeightForWidth(self.widget9.sizePolicy().hasHeightForWidth())
        self.widget9.setSizePolicy(sizePolicy4)
        self.widget9.setMinimumSize(QSize(300, 0))
        self.widget9.setMaximumSize(QSize(300, 16777215))
        self.horizontalLayout_89 = QHBoxLayout(self.widget9)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(1, 3, 4, 8)
        self.power_button = ActionButton(self.widget9)
        self.power_button.setObjectName(u"power_button")
        sizePolicy.setHeightForWidth(self.power_button.sizePolicy().hasHeightForWidth())
        self.power_button.setSizePolicy(sizePolicy)
        self.power_button.setMinimumSize(QSize(75, 35))
        self.power_button.setMaximumSize(QSize(75, 35))
        self.power_button.setFocusPolicy(Qt.NoFocus)
        self.power_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.power_button.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.power_button)

        self.ref_coilumn_header_16 = QLabel(self.widget9)
        self.ref_coilumn_header_16.setObjectName(u"ref_coilumn_header_16")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_16.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_16.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_16.setStyleSheet(u"")
        self.ref_coilumn_header_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_16)

        self.widget10 = QWidget(self.widget9)
        self.widget10.setObjectName(u"widget10")
        self.widget10.setMinimumSize(QSize(100, 32))
        self.widget10.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout_40 = QHBoxLayout(self.widget10)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(1, 1, 1, 1)
        self.timerhours = HalLabel(self.widget10)
        self.timerhours.setObjectName(u"timerhours")
        sizePolicy6.setHeightForWidth(self.timerhours.sizePolicy().hasHeightForWidth())
        self.timerhours.setSizePolicy(sizePolicy6)
        self.timerhours.setMinimumSize(QSize(0, 30))
        self.timerhours.setMaximumSize(QSize(16777215, 30))
        self.timerhours.setStyleSheet(u"HalLabel {\n"
"    border-style: solid;\n"
"    border-color: silver;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 0px;\n"
"    border-left-width: 1px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"    padding-left: 5px;\n"
"}")
        self.timerhours.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.timerhours)

        self.label_2 = QLabel(self.widget10)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(4, 30))
        self.label_2.setMaximumSize(QSize(4, 30))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: silver;\n"
"    border-radius: 0px;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 0px;\n"
"    border-left-width: 0px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_2)

        self.timerminutes = HalLabel(self.widget10)
        self.timerminutes.setObjectName(u"timerminutes")
        sizePolicy.setHeightForWidth(self.timerminutes.sizePolicy().hasHeightForWidth())
        self.timerminutes.setSizePolicy(sizePolicy)
        self.timerminutes.setMinimumSize(QSize(24, 30))
        self.timerminutes.setMaximumSize(QSize(24, 30))
        self.timerminutes.setStyleSheet(u"HalLabel {\n"
"    border-style: solid;\n"
"    border-color: silver;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 0px;\n"
"    border-left-width: 0px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.timerminutes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.timerminutes)

        self.label_3 = QLabel(self.widget10)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(4, 30))
        self.label_3.setMaximumSize(QSize(4, 30))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: silver;\n"
"    border-radius: 0px;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 0px;\n"
"    border-left-width: 0px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_3)

        self.timerseconds = HalLabel(self.widget10)
        self.timerseconds.setObjectName(u"timerseconds")
        sizePolicy6.setHeightForWidth(self.timerseconds.sizePolicy().hasHeightForWidth())
        self.timerseconds.setSizePolicy(sizePolicy6)
        self.timerseconds.setMinimumSize(QSize(0, 30))
        self.timerseconds.setMaximumSize(QSize(16777215, 30))
        self.timerseconds.setStyleSheet(u"HalLabel {\n"
"    border-style: solid;\n"
"    border-color: silver;\n"
"    border-width: 1px;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 1px;\n"
"    border-left-width: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 5px;\n"
"}")
        self.timerseconds.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.timerseconds)


        self.horizontalLayout_89.addWidget(self.widget10)

        self.ref_coilumn_header_18 = QLabel(self.widget9)
        self.ref_coilumn_header_18.setObjectName(u"ref_coilumn_header_18")
        sizePolicy1.setHeightForWidth(self.ref_coilumn_header_18.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_18.setSizePolicy(sizePolicy1)
        self.ref_coilumn_header_18.setStyleSheet(u"")
        self.ref_coilumn_header_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_18)

        self.exit_button = ActionButton(self.widget9)
        self.exit_button.setObjectName(u"exit_button")
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMinimumSize(QSize(75, 35))
        self.exit_button.setMaximumSize(QSize(75, 35))
        self.exit_button.setFocusPolicy(Qt.NoFocus)
        self.exit_button.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 64, 64, 255), stop:0.446154 rgba(204, 0, 0, 255), stop:0.764103 rgba(225, 67, 67, 255), stop:1 rgba(249, 142, 142, 255))")
        self.exit_button.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.exit_button)


        self.verticalLayout_28.addWidget(self.widget9)


        self.main_control_screen_layout_panel.addWidget(self.main_control_qframe)

        self.tool_info_qframe = QFrame(self.centralwidget)
        self.tool_info_qframe.setObjectName(u"tool_info_qframe")
        sizePolicy.setHeightForWidth(self.tool_info_qframe.sizePolicy().hasHeightForWidth())
        self.tool_info_qframe.setSizePolicy(sizePolicy)
        self.tool_info_qframe.setMinimumSize(QSize(250, 340))
        self.tool_info_qframe.setMaximumSize(QSize(250, 340))
        self.tool_info_qframe.setFocusPolicy(Qt.NoFocus)
        self.tool_info_qframe.setStyleSheet(u".QFrame{\n"
"border-left-width: 1px;\n"
"border-right-width:1px;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.tool_info_qframe)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(20, 9, 20, 3)
        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setSpacing(9)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.frame_27 = QFrame(self.tool_info_qframe)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy6.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy6)
        self.frame_27.setMinimumSize(QSize(0, 38))
        self.frame_27.setMaximumSize(QSize(16777215, 38))
        self.frame_27.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 1, 0)
        self.ref_coilumn_header_3 = QLabel(self.frame_27)
        self.ref_coilumn_header_3.setObjectName(u"ref_coilumn_header_3")
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_3.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_3.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_3.setMinimumSize(QSize(15, 36))
        self.ref_coilumn_header_3.setMaximumSize(QSize(15, 36))
        self.ref_coilumn_header_3.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_3.setAlignment(Qt.AlignCenter)
        self.ref_coilumn_header_3.setIndent(0)

        self.horizontalLayout_105.addWidget(self.ref_coilumn_header_3)

        self.tool_number_entry_main_panel = VCPLineEdit(self.frame_27)
        self.tool_number_entry_main_panel.setObjectName(u"tool_number_entry_main_panel")
        sizePolicy.setHeightForWidth(self.tool_number_entry_main_panel.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_main_panel.setSizePolicy(sizePolicy)
        self.tool_number_entry_main_panel.setMinimumSize(QSize(55, 0))
        self.tool_number_entry_main_panel.setMaximumSize(QSize(55, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush7)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush10)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush7)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush7)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush11)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush7)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush10)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush7)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush7)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush11)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush7)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush10)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush10)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush7)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush7)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        self.tool_number_entry_main_panel.setPalette(palette3)
        font11 = QFont()
        font11.setFamilies([u"Bebas Kai"])
        font11.setPointSize(17)
        font11.setBold(False)
        font11.setItalic(False)
        self.tool_number_entry_main_panel.setFont(font11)
        self.tool_number_entry_main_panel.setFocusPolicy(Qt.ClickFocus)
        self.tool_number_entry_main_panel.setContextMenuPolicy(Qt.NoContextMenu)
        self.tool_number_entry_main_panel.setStyleSheet(u"font: 17pt;")
        self.tool_number_entry_main_panel.setFrame(True)
        self.tool_number_entry_main_panel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_105.addWidget(self.tool_number_entry_main_panel)


        self.horizontalLayout_96.addWidget(self.frame_27)

        self.m6_tool_call_button_main_panel = SubCallButton(self.tool_info_qframe)
        self.m6_tool_call_button_main_panel.setObjectName(u"m6_tool_call_button_main_panel")
        self.m6_tool_call_button_main_panel.setMinimumSize(QSize(70, 40))
        self.m6_tool_call_button_main_panel.setMaximumSize(QSize(16777215, 40))
        self.m6_tool_call_button_main_panel.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
""
                        "\n"
"QPushButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_96.addWidget(self.m6_tool_call_button_main_panel)


        self.verticalLayout_29.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setSpacing(9)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.G43 = MDIButton(self.tool_info_qframe)
        self.G43.setObjectName(u"G43")
        self.G43.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.G43.sizePolicy().hasHeightForWidth())
        self.G43.setSizePolicy(sizePolicy2)
        self.G43.setMinimumSize(QSize(0, 40))
        self.G43.setMaximumSize(QSize(16777215, 40))
        self.G43.setFocusPolicy(Qt.NoFocus)
        self.G43.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.G43.setCheckable(True)
        self.G43.setAutoExclusive(True)

        self.horizontalLayout_104.addWidget(self.G43)

        self.G49 = MDIButton(self.tool_info_qframe)
        self.G49.setObjectName(u"G49")
        self.G49.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.G49.sizePolicy().hasHeightForWidth())
        self.G49.setSizePolicy(sizePolicy2)
        self.G49.setMinimumSize(QSize(0, 40))
        self.G49.setMaximumSize(QSize(16777215, 40))
        self.G49.setFocusPolicy(Qt.NoFocus)
        self.G49.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"}")
        self.G49.setCheckable(True)
        self.G49.setAutoExclusive(True)

        self.horizontalLayout_104.addWidget(self.G49)


        self.verticalLayout_29.addLayout(self.horizontalLayout_104)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setSpacing(5)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(-1, -1, 0, -1)
        self.work_column_header_4 = QLabel(self.tool_info_qframe)
        self.work_column_header_4.setObjectName(u"work_column_header_4")
        self.work_column_header_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.work_column_header_4.sizePolicy().hasHeightForWidth())
        self.work_column_header_4.setSizePolicy(sizePolicy)
        self.work_column_header_4.setMinimumSize(QSize(60, 33))
        self.work_column_header_4.setMaximumSize(QSize(60, 33))
        self.work_column_header_4.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.work_column_header_4.setAlignment(Qt.AlignCenter)
        self.work_column_header_4.setWordWrap(True)
        self.work_column_header_4.setIndent(0)

        self.horizontalLayout_94.addWidget(self.work_column_header_4)

        self.tool_length = StatusLabel(self.tool_info_qframe)
        self.tool_length.setObjectName(u"tool_length")
        sizePolicy12.setHeightForWidth(self.tool_length.sizePolicy().hasHeightForWidth())
        self.tool_length.setSizePolicy(sizePolicy12)
        self.tool_length.setMinimumSize(QSize(0, 33))
        self.tool_length.setMaximumSize(QSize(16777215, 33))
        self.tool_length.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.tool_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.tool_length)

        self.statuslabel_8 = StatusLabel(self.tool_info_qframe)
        self.statuslabel_8.setObjectName(u"statuslabel_8")
        sizePolicy6.setHeightForWidth(self.statuslabel_8.sizePolicy().hasHeightForWidth())
        self.statuslabel_8.setSizePolicy(sizePolicy6)
        self.statuslabel_8.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_94.addWidget(self.statuslabel_8)


        self.verticalLayout_29.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setSpacing(5)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.work_column_header_5 = QLabel(self.tool_info_qframe)
        self.work_column_header_5.setObjectName(u"work_column_header_5")
        self.work_column_header_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.work_column_header_5.sizePolicy().hasHeightForWidth())
        self.work_column_header_5.setSizePolicy(sizePolicy)
        self.work_column_header_5.setMinimumSize(QSize(60, 33))
        self.work_column_header_5.setMaximumSize(QSize(60, 33))
        self.work_column_header_5.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Bebas Kai\";\n"
"}\n"
"")
        self.work_column_header_5.setAlignment(Qt.AlignCenter)
        self.work_column_header_5.setWordWrap(True)
        self.work_column_header_5.setIndent(0)

        self.horizontalLayout_93.addWidget(self.work_column_header_5)

        self.tool_diameter = StatusLabel(self.tool_info_qframe)
        self.tool_diameter.setObjectName(u"tool_diameter")
        sizePolicy12.setHeightForWidth(self.tool_diameter.sizePolicy().hasHeightForWidth())
        self.tool_diameter.setSizePolicy(sizePolicy12)
        self.tool_diameter.setMinimumSize(QSize(0, 33))
        self.tool_diameter.setMaximumSize(QSize(16777215, 33))
        self.tool_diameter.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.tool_diameter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.tool_diameter)

        self.statuslabel_11 = StatusLabel(self.tool_info_qframe)
        self.statuslabel_11.setObjectName(u"statuslabel_11")
        sizePolicy6.setHeightForWidth(self.statuslabel_11.sizePolicy().hasHeightForWidth())
        self.statuslabel_11.setSizePolicy(sizePolicy6)
        self.statuslabel_11.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.statuslabel_11)


        self.verticalLayout_29.addLayout(self.horizontalLayout_93)

        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setSpacing(9)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.go_to_zero_button_2 = SubCallButton(self.tool_info_qframe)
        self.go_to_zero_button_2.setObjectName(u"go_to_zero_button_2")
        sizePolicy2.setHeightForWidth(self.go_to_zero_button_2.sizePolicy().hasHeightForWidth())
        self.go_to_zero_button_2.setSizePolicy(sizePolicy2)
        self.go_to_zero_button_2.setMinimumSize(QSize(0, 40))
        self.go_to_zero_button_2.setMaximumSize(QSize(16777215, 40))
        self.go_to_zero_button_2.setFocusPolicy(Qt.NoFocus)
        self.go_to_zero_button_2.setStyleSheet(u".SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
".SubCallButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 2"
                        "55));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_95.addWidget(self.go_to_zero_button_2)

        self.go_to_g30_button = SubCallButton(self.tool_info_qframe)
        self.go_to_g30_button.setObjectName(u"go_to_g30_button")
        sizePolicy2.setHeightForWidth(self.go_to_g30_button.sizePolicy().hasHeightForWidth())
        self.go_to_g30_button.setSizePolicy(sizePolicy2)
        self.go_to_g30_button.setMinimumSize(QSize(0, 40))
        self.go_to_g30_button.setMaximumSize(QSize(16777215, 40))
        self.go_to_g30_button.setFocusPolicy(Qt.NoFocus)
        self.go_to_g30_button.setStyleSheet(u".SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
".SubCallButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 2"
                        "55));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_95.addWidget(self.go_to_g30_button)


        self.verticalLayout_29.addLayout(self.horizontalLayout_95)

        self.line_7 = QFrame(self.tool_info_qframe)
        self.line_7.setObjectName(u"line_7")
        sizePolicy6.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy6)
        self.line_7.setMinimumSize(QSize(0, 2))
        self.line_7.setMaximumSize(QSize(16777215, 2))
        self.line_7.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_29.addWidget(self.line_7)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setSpacing(9)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(-1, -1, -1, 0)
        self.go_to_home_button = SubCallButton(self.tool_info_qframe)
        self.go_to_home_button.setObjectName(u"go_to_home_button")
        sizePolicy2.setHeightForWidth(self.go_to_home_button.sizePolicy().hasHeightForWidth())
        self.go_to_home_button.setSizePolicy(sizePolicy2)
        self.go_to_home_button.setMinimumSize(QSize(0, 40))
        self.go_to_home_button.setMaximumSize(QSize(16777215, 40))
        self.go_to_home_button.setFocusPolicy(Qt.NoFocus)
        self.go_to_home_button.setStyleSheet(u".SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"}\n"
"\n"
".SubCallButton {\n"
"    font-family: \"Bebas Kai\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
".SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
".SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
".SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 2"
                        "55));\n"
"}\n"
"\n"
".SubCallButton:checked[option=\"true\"] {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"\n"
".SubCallButton:checked {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}")

        self.horizontalLayout_97.addWidget(self.go_to_home_button)


        self.verticalLayout_29.addLayout(self.horizontalLayout_97)


        self.main_control_screen_layout_panel.addWidget(self.tool_info_qframe)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(486, 340))
        self.frame_4.setMaximumSize(QSize(486, 340))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.dro_display_layout = QHBoxLayout()
        self.dro_display_layout.setSpacing(0)
        self.dro_display_layout.setObjectName(u"dro_display_layout")
        self.dro_display_layout.setContentsMargins(16, 5, 16, 0)

        self.horizontalLayout_58.addLayout(self.dro_display_layout)


        self.main_control_screen_layout_panel.addWidget(self.frame_4)

        self.main_override_tool_qframe = QFrame(self.centralwidget)
        self.main_override_tool_qframe.setObjectName(u"main_override_tool_qframe")
        sizePolicy20 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.main_override_tool_qframe.sizePolicy().hasHeightForWidth())
        self.main_override_tool_qframe.setSizePolicy(sizePolicy20)
        self.main_override_tool_qframe.setMinimumSize(QSize(370, 340))
        self.main_override_tool_qframe.setMaximumSize(QSize(16777215, 340))
        self.main_override_tool_qframe.setFocusPolicy(Qt.NoFocus)
        self.main_override_tool_qframe.setStyleSheet(u".QFrame{\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    border-left-width: 1px;\n"
"    border-right-width:1px;\n"
"}")
        self.gridLayout = QGridLayout(self.main_override_tool_qframe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setContentsMargins(13, 11, 13, 2)
        self.spindel_load_label = QLabel(self.main_override_tool_qframe)
        self.spindel_load_label.setObjectName(u"spindel_load_label")
        self.spindel_load_label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.spindel_load_label.sizePolicy().hasHeightForWidth())
        self.spindel_load_label.setSizePolicy(sizePolicy)
        self.spindel_load_label.setMinimumSize(QSize(65, 40))
        self.spindel_load_label.setMaximumSize(QSize(65, 40))
        self.spindel_load_label.setStyleSheet(u"QLabel{\n"
"color: white;\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"font: 13pt \"Bebas Kai\";\n"
"}")
        self.spindel_load_label.setLineWidth(0)
        self.spindel_load_label.setAlignment(Qt.AlignCenter)
        self.spindel_load_label.setWordWrap(False)
        self.spindel_load_label.setMargin(-6)
        self.spindel_load_label.setIndent(0)

        self.gridLayout.addWidget(self.spindel_load_label, 0, 2, 1, 1)

        self.spindle_override_slider = ActionSlider(self.main_override_tool_qframe)
        self.spindle_override_slider.setObjectName(u"spindle_override_slider")
        self.spindle_override_slider.setMinimumSize(QSize(0, 50))
        self.spindle_override_slider.setFocusPolicy(Qt.NoFocus)
        self.spindle_override_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSli"
                        "der::add-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}")
        self.spindle_override_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.spindle_override_slider, 4, 0, 1, 1)

        self.feed_override_status = StatusLabel(self.main_override_tool_qframe)
        self.feed_override_status.setObjectName(u"feed_override_status")
        sizePolicy.setHeightForWidth(self.feed_override_status.sizePolicy().hasHeightForWidth())
        self.feed_override_status.setSizePolicy(sizePolicy)
        self.feed_override_status.setMinimumSize(QSize(55, 36))
        self.feed_override_status.setMaximumSize(QSize(55, 36))
        self.feed_override_status.setToolTipDuration(-3)
        self.feed_override_status.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.feed_override_status.setLineWidth(0)
        self.feed_override_status.setAlignment(Qt.AlignCenter)
        self.feed_override_status.setMargin(-6)
        self.feed_override_status.setIndent(0)

        self.gridLayout.addWidget(self.feed_override_status, 2, 1, 1, 1)

        self.spindle_override_status = StatusLabel(self.main_override_tool_qframe)
        self.spindle_override_status.setObjectName(u"spindle_override_status")
        sizePolicy.setHeightForWidth(self.spindle_override_status.sizePolicy().hasHeightForWidth())
        self.spindle_override_status.setSizePolicy(sizePolicy)
        self.spindle_override_status.setMinimumSize(QSize(55, 36))
        self.spindle_override_status.setMaximumSize(QSize(55, 36))
        self.spindle_override_status.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.spindle_override_status.setLineWidth(0)
        self.spindle_override_status.setAlignment(Qt.AlignCenter)
        self.spindle_override_status.setMargin(-6)
        self.spindle_override_status.setIndent(0)

        self.gridLayout.addWidget(self.spindle_override_status, 4, 1, 1, 1)

        self.rapid_override_slider = ActionSlider(self.main_override_tool_qframe)
        self.rapid_override_slider.setObjectName(u"rapid_override_slider")
        self.rapid_override_slider.setMinimumSize(QSize(0, 50))
        self.rapid_override_slider.setFocusPolicy(Qt.NoFocus)
        self.rapid_override_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSli"
                        "der::add-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}")
        self.rapid_override_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.rapid_override_slider, 5, 0, 1, 1)

        self.max_velocity_slider = ActionSlider(self.main_override_tool_qframe)
        self.max_velocity_slider.setObjectName(u"max_velocity_slider")
        self.max_velocity_slider.setMinimumSize(QSize(0, 50))
        self.max_velocity_slider.setFocusPolicy(Qt.NoFocus)
        self.max_velocity_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSli"
                        "der::add-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}")
        self.max_velocity_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.max_velocity_slider, 1, 0, 1, 1)

        self.feed_override_to_100_button = ActionButton(self.main_override_tool_qframe)
        self.feed_override_to_100_button.setObjectName(u"feed_override_to_100_button")
        self.feed_override_to_100_button.setMinimumSize(QSize(65, 40))
        self.feed_override_to_100_button.setMaximumSize(QSize(65, 40))
        self.feed_override_to_100_button.setFocusPolicy(Qt.NoFocus)
        self.feed_override_to_100_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.gridLayout.addWidget(self.feed_override_to_100_button, 2, 2, 1, 1)

        self.spindle_override_to_100_button = ActionButton(self.main_override_tool_qframe)
        self.spindle_override_to_100_button.setObjectName(u"spindle_override_to_100_button")
        self.spindle_override_to_100_button.setMinimumSize(QSize(65, 40))
        self.spindle_override_to_100_button.setMaximumSize(QSize(65, 40))
        self.spindle_override_to_100_button.setFocusPolicy(Qt.NoFocus)
        self.spindle_override_to_100_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.gridLayout.addWidget(self.spindle_override_to_100_button, 4, 2, 1, 1)

        self.spindle_load_indicator = HalBarIndicator(self.main_override_tool_qframe)
        self.spindle_load_indicator.setObjectName(u"spindle_load_indicator")
        self.spindle_load_indicator.setMinimumSize(QSize(0, 30))
        self.spindle_load_indicator.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setFamilies([u"Bebas Kai"])
        font12.setPointSize(14)
        self.spindle_load_indicator.setFont(font12)
        self.spindle_load_indicator.setStyleSheet(u"")
        self.spindle_load_indicator.setProperty(u"value", 100.000000000000000)
        self.spindle_load_indicator.setProperty(u"maximum", 150.000000000000000)
        self.spindle_load_indicator.setProperty(u"textColor", QColor(255, 255, 255))

        self.gridLayout.addWidget(self.spindle_load_indicator, 0, 0, 1, 2)

        self.rapid_override_to_100_button = ActionButton(self.main_override_tool_qframe)
        self.rapid_override_to_100_button.setObjectName(u"rapid_override_to_100_button")
        self.rapid_override_to_100_button.setMinimumSize(QSize(65, 40))
        self.rapid_override_to_100_button.setMaximumSize(QSize(65, 40))
        self.rapid_override_to_100_button.setFocusPolicy(Qt.NoFocus)
        self.rapid_override_to_100_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.gridLayout.addWidget(self.rapid_override_to_100_button, 5, 2, 1, 1)

        self.max_vel_slider = StatusLabel(self.main_override_tool_qframe)
        self.max_vel_slider.setObjectName(u"max_vel_slider")
        sizePolicy.setHeightForWidth(self.max_vel_slider.sizePolicy().hasHeightForWidth())
        self.max_vel_slider.setSizePolicy(sizePolicy)
        self.max_vel_slider.setMinimumSize(QSize(55, 36))
        self.max_vel_slider.setMaximumSize(QSize(55, 36))
        self.max_vel_slider.setToolTipDuration(-1)
        self.max_vel_slider.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.max_vel_slider.setLineWidth(0)
        self.max_vel_slider.setAlignment(Qt.AlignCenter)
        self.max_vel_slider.setIndent(0)

        self.gridLayout.addWidget(self.max_vel_slider, 1, 1, 1, 1)

        self.max_velocity_to_100_button = ActionButton(self.main_override_tool_qframe)
        self.max_velocity_to_100_button.setObjectName(u"max_velocity_to_100_button")
        self.max_velocity_to_100_button.setMinimumSize(QSize(65, 40))
        self.max_velocity_to_100_button.setMaximumSize(QSize(65, 40))
        self.max_velocity_to_100_button.setFocusPolicy(Qt.NoFocus)
        self.max_velocity_to_100_button.setStyleSheet(u"QPushButton {\n"
"   	font: 14pt \"Bebas Kai\";\n"
"}")

        self.gridLayout.addWidget(self.max_velocity_to_100_button, 1, 2, 1, 1)

        self.rapid_override_status = StatusLabel(self.main_override_tool_qframe)
        self.rapid_override_status.setObjectName(u"rapid_override_status")
        sizePolicy.setHeightForWidth(self.rapid_override_status.sizePolicy().hasHeightForWidth())
        self.rapid_override_status.setSizePolicy(sizePolicy)
        self.rapid_override_status.setMinimumSize(QSize(55, 36))
        self.rapid_override_status.setMaximumSize(QSize(55, 36))
        self.rapid_override_status.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.rapid_override_status.setLineWidth(0)
        self.rapid_override_status.setAlignment(Qt.AlignCenter)
        self.rapid_override_status.setMargin(-6)
        self.rapid_override_status.setIndent(0)

        self.gridLayout.addWidget(self.rapid_override_status, 5, 1, 1, 1)

        self.feed_override_slider = ActionSlider(self.main_override_tool_qframe)
        self.feed_override_slider.setObjectName(u"feed_override_slider")
        self.feed_override_slider.setMinimumSize(QSize(0, 50))
        self.feed_override_slider.setFocusPolicy(Qt.NoFocus)
        self.feed_override_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSli"
                        "der::add-page:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"border: 2px solid gray;\n"
"}")
        self.feed_override_slider.setMaximum(100)
        self.feed_override_slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.feed_override_slider, 2, 0, 1, 1)


        self.main_control_screen_layout_panel.addWidget(self.main_override_tool_qframe)

        self.jog_and_spindle_qframe = QFrame(self.centralwidget)
        self.jog_and_spindle_qframe.setObjectName(u"jog_and_spindle_qframe")
        sizePolicy.setHeightForWidth(self.jog_and_spindle_qframe.sizePolicy().hasHeightForWidth())
        self.jog_and_spindle_qframe.setSizePolicy(sizePolicy)
        self.jog_and_spindle_qframe.setMinimumSize(QSize(380, 340))
        self.jog_and_spindle_qframe.setMaximumSize(QSize(380, 16777215))
        self.jog_and_spindle_qframe.setFocusPolicy(Qt.NoFocus)
        self.jog_and_spindle_qframe.setStyleSheet(u".QFrame{\n"
"    border-left-width:1px\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.jog_and_spindle_qframe)
        self.verticalLayout_27.setSpacing(12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(19, 10, 19, 3)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(16)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.jogincrement = JogIncrementWidget(self.jog_and_spindle_qframe)
        self.jogincrement.setObjectName(u"jogincrement")
        sizePolicy6.setHeightForWidth(self.jogincrement.sizePolicy().hasHeightForWidth())
        self.jogincrement.setSizePolicy(sizePolicy6)
        self.jogincrement.setMinimumSize(QSize(0, 42))
        self.jogincrement.setMaximumSize(QSize(16777215, 42))
        self.jogincrement.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Bebas Kai\";\n"
"\n"
"}\n"
"\n"
"")
        self.jogincrement.setProperty(u"diameter", 0)

        self.horizontalLayout_83.addWidget(self.jogincrement)


        self.verticalLayout_27.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, -1, 0, -1)
        self.linear_jog_slider = VCPSettingsSlider(self.jog_and_spindle_qframe)
        self.linear_jog_slider.setObjectName(u"linear_jog_slider")
        self.linear_jog_slider.setMinimumSize(QSize(0, 50))
        self.linear_jog_slider.setFocusPolicy(Qt.NoFocus)
        self.linear_jog_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(235, 235, 235);\n"
"border: 1px solid #777;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255,"
                        " 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #777;\n"
"border-color: rgba(40, 40, 40, 255);\n"
"width: 40px;\n"
"margin-top: -13px;\n"
"margin-bottom: -13px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid #444;\n"
"border-color: rgb(241, 239, 237);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
""
                        "}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.linear_jog_slider.setMinimum(0)
        self.linear_jog_slider.setMaximum(100)
        self.linear_jog_slider.setValue(50)
        self.linear_jog_slider.setSliderPosition(50)
        self.linear_jog_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_84.addWidget(self.linear_jog_slider)

        self.fr_override_dro = StatusLabel(self.jog_and_spindle_qframe)
        self.fr_override_dro.setObjectName(u"fr_override_dro")
        self.fr_override_dro.setMinimumSize(QSize(48, 38))
        self.fr_override_dro.setMaximumSize(QSize(48, 38))
        self.fr_override_dro.setStyleSheet(u"StatusLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.fr_override_dro.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.fr_override_dro)


        self.verticalLayout_27.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.current_velocity_status = StatusLabel(self.jog_and_spindle_qframe)
        self.current_velocity_status.setObjectName(u"current_velocity_status")
        sizePolicy.setHeightForWidth(self.current_velocity_status.sizePolicy().hasHeightForWidth())
        self.current_velocity_status.setSizePolicy(sizePolicy)
        self.current_velocity_status.setMinimumSize(QSize(105, 38))
        self.current_velocity_status.setMaximumSize(QSize(105, 38))
        self.current_velocity_status.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"	font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.current_velocity_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.current_velocity_status)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_3)

        self.frame_30 = QFrame(self.jog_and_spindle_qframe)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setMaximumSize(QSize(16777215, 38))
        self.frame_30.setStyleSheet(u"QFrame {\n"
"    border: none;\n"
"}")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Plain)
        self.frame_30.setLineWidth(0)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.feedrate_label_1 = QLabel(self.frame_30)
        self.feedrate_label_1.setObjectName(u"feedrate_label_1")
        sizePolicy21 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.feedrate_label_1.sizePolicy().hasHeightForWidth())
        self.feedrate_label_1.setSizePolicy(sizePolicy21)
        self.feedrate_label_1.setMaximumSize(QSize(16777215, 30))
        self.feedrate_label_1.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.feedrate_label_1.setAlignment(Qt.AlignCenter)
        self.feedrate_label_1.setWordWrap(False)
        self.feedrate_label_1.setIndent(0)

        self.horizontalLayout_110.addWidget(self.feedrate_label_1)

        self.feedrate_label_2 = QLabel(self.frame_30)
        self.feedrate_label_2.setObjectName(u"feedrate_label_2")
        sizePolicy.setHeightForWidth(self.feedrate_label_2.sizePolicy().hasHeightForWidth())
        self.feedrate_label_2.setSizePolicy(sizePolicy)
        self.feedrate_label_2.setMinimumSize(QSize(5, 30))
        self.feedrate_label_2.setMaximumSize(QSize(5, 16777215))
        self.feedrate_label_2.setStyleSheet(u"QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.feedrate_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.feedrate_label_2.setWordWrap(True)
        self.feedrate_label_2.setIndent(0)

        self.horizontalLayout_110.addWidget(self.feedrate_label_2)

        self.feedrate_label_3 = StatusLabel(self.frame_30)
        self.feedrate_label_3.setObjectName(u"feedrate_label_3")
        sizePolicy21.setHeightForWidth(self.feedrate_label_3.sizePolicy().hasHeightForWidth())
        self.feedrate_label_3.setSizePolicy(sizePolicy21)
        self.feedrate_label_3.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.feedrate_label_3.setAlignment(Qt.AlignCenter)
        self.feedrate_label_3.setIndent(0)

        self.horizontalLayout_110.addWidget(self.feedrate_label_3)

        self.feedrate_label_4 = QLabel(self.frame_30)
        self.feedrate_label_4.setObjectName(u"feedrate_label_4")
        self.feedrate_label_4.setEnabled(True)
        sizePolicy21.setHeightForWidth(self.feedrate_label_4.sizePolicy().hasHeightForWidth())
        self.feedrate_label_4.setSizePolicy(sizePolicy21)
        self.feedrate_label_4.setMaximumSize(QSize(16777215, 30))
        self.feedrate_label_4.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.feedrate_label_4.setAlignment(Qt.AlignCenter)
        self.feedrate_label_4.setWordWrap(False)
        self.feedrate_label_4.setIndent(0)

        self.horizontalLayout_110.addWidget(self.feedrate_label_4)


        self.horizontalLayout_85.addWidget(self.frame_30)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_4)

        self.f_word_status = StatusLabel(self.jog_and_spindle_qframe)
        self.f_word_status.setObjectName(u"f_word_status")
        sizePolicy6.setHeightForWidth(self.f_word_status.sizePolicy().hasHeightForWidth())
        self.f_word_status.setSizePolicy(sizePolicy6)
        self.f_word_status.setMinimumSize(QSize(105, 38))
        self.f_word_status.setMaximumSize(QSize(105, 38))
        self.f_word_status.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.f_word_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.f_word_status)


        self.verticalLayout_27.addLayout(self.horizontalLayout_85)

        self.line_2 = QFrame(self.jog_and_spindle_qframe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 2))
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setStyleSheet(u"Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.spindle_rpm_source_widget = QStackedWidget(self.jog_and_spindle_qframe)
        self.spindle_rpm_source_widget.setObjectName(u"spindle_rpm_source_widget")
        sizePolicy.setHeightForWidth(self.spindle_rpm_source_widget.sizePolicy().hasHeightForWidth())
        self.spindle_rpm_source_widget.setSizePolicy(sizePolicy)
        self.spindle_rpm_source_widget.setMinimumSize(QSize(105, 38))
        self.spindle_rpm_source_widget.setMaximumSize(QSize(105, 38))
        self.spindle_status_rpm = QWidget()
        self.spindle_status_rpm.setObjectName(u"spindle_status_rpm")
        sizePolicy8.setHeightForWidth(self.spindle_status_rpm.sizePolicy().hasHeightForWidth())
        self.spindle_status_rpm.setSizePolicy(sizePolicy8)
        self.spindle_status_rpm.setMinimumSize(QSize(105, 38))
        self.spindle_status_rpm.setMaximumSize(QSize(105, 38))
        self.spindle_status_rpm.setStyleSheet(u"background: rgb(46, 52, 54);")
        self.horizontalLayout_139 = QHBoxLayout(self.spindle_status_rpm)
        self.horizontalLayout_139.setSpacing(0)
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.horizontalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.spindle_stat_rpm = StatusLabel(self.spindle_status_rpm)
        self.spindle_stat_rpm.setObjectName(u"spindle_stat_rpm")
        sizePolicy.setHeightForWidth(self.spindle_stat_rpm.sizePolicy().hasHeightForWidth())
        self.spindle_stat_rpm.setSizePolicy(sizePolicy)
        self.spindle_stat_rpm.setMinimumSize(QSize(105, 38))
        self.spindle_stat_rpm.setMaximumSize(QSize(105, 38))
        self.spindle_stat_rpm.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"	font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_stat_rpm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_139.addWidget(self.spindle_stat_rpm)

        self.spindle_rpm_source_widget.addWidget(self.spindle_status_rpm)
        self.spindle_encoder_rpm = QWidget()
        self.spindle_encoder_rpm.setObjectName(u"spindle_encoder_rpm")
        sizePolicy.setHeightForWidth(self.spindle_encoder_rpm.sizePolicy().hasHeightForWidth())
        self.spindle_encoder_rpm.setSizePolicy(sizePolicy)
        self.spindle_encoder_rpm.setMinimumSize(QSize(105, 38))
        self.spindle_encoder_rpm.setMaximumSize(QSize(105, 38))
        self.spindle_encoder_rpm.setStyleSheet(u"background: rgb(46, 52, 54);")
        self.horizontalLayout_151 = QHBoxLayout(self.spindle_encoder_rpm)
        self.horizontalLayout_151.setSpacing(0)
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.spindle_encoder_rpm1 = HalLabel(self.spindle_encoder_rpm)
        self.spindle_encoder_rpm1.setObjectName(u"spindle_encoder_rpm1")
        sizePolicy.setHeightForWidth(self.spindle_encoder_rpm1.sizePolicy().hasHeightForWidth())
        self.spindle_encoder_rpm1.setSizePolicy(sizePolicy)
        self.spindle_encoder_rpm1.setMinimumSize(QSize(105, 38))
        self.spindle_encoder_rpm1.setMaximumSize(QSize(105, 38))
        self.spindle_encoder_rpm1.setStyleSheet(u"QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_encoder_rpm1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_151.addWidget(self.spindle_encoder_rpm1)

        self.spindle_rpm_source_widget.addWidget(self.spindle_encoder_rpm)

        self.horizontalLayout_87.addWidget(self.spindle_rpm_source_widget)

        self.rpm_label = QLabel(self.jog_and_spindle_qframe)
        self.rpm_label.setObjectName(u"rpm_label")
        sizePolicy1.setHeightForWidth(self.rpm_label.sizePolicy().hasHeightForWidth())
        self.rpm_label.setSizePolicy(sizePolicy1)
        self.rpm_label.setMaximumSize(QSize(16777215, 38))
        self.rpm_label.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.rpm_label.setAlignment(Qt.AlignCenter)
        self.rpm_label.setWordWrap(False)
        self.rpm_label.setIndent(0)

        self.horizontalLayout_87.addWidget(self.rpm_label)

        self.s_word_status = StatusLabel(self.jog_and_spindle_qframe)
        self.s_word_status.setObjectName(u"s_word_status")
        sizePolicy.setHeightForWidth(self.s_word_status.sizePolicy().hasHeightForWidth())
        self.s_word_status.setSizePolicy(sizePolicy)
        self.s_word_status.setMinimumSize(QSize(105, 38))
        self.s_word_status.setMaximumSize(QSize(105, 38))
        self.s_word_status.setStyleSheet(u"QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"	font: 17pt \"Bebas Kai\";\n"
"}")
        self.s_word_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.s_word_status)


        self.verticalLayout_27.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(20)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(-1, 5, -1, -1)
        self.spindle_reverse_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_reverse_button.setObjectName(u"spindle_reverse_button")
        self.spindle_reverse_button.setMinimumSize(QSize(100, 42))
        self.spindle_reverse_button.setMaximumSize(QSize(100, 42))
        self.spindle_reverse_button.setLayoutDirection(Qt.LeftToRight)
        self.spindle_reverse_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 24px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        icon66 = QIcon()
        icon66.addFile(u":/images/ccw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.spindle_reverse_button.setIcon(icon66)
        self.spindle_reverse_button.setIconSize(QSize(18, 18))

        self.horizontalLayout_86.addWidget(self.spindle_reverse_button)

        self.spindle_off_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_off_button.setObjectName(u"spindle_off_button")
        self.spindle_off_button.setMinimumSize(QSize(100, 42))
        self.spindle_off_button.setMaximumSize(QSize(100, 42))
        self.spindle_off_button.setLayoutDirection(Qt.LeftToRight)
        self.spindle_off_button.setStyleSheet(u"QPushButton {\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_off_button.setIconSize(QSize(18, 18))

        self.horizontalLayout_86.addWidget(self.spindle_off_button)

        self.spindle_forward_button = ActionButton(self.jog_and_spindle_qframe)
        self.spindle_forward_button.setObjectName(u"spindle_forward_button")
        self.spindle_forward_button.setMinimumSize(QSize(100, 42))
        self.spindle_forward_button.setMaximumSize(QSize(100, 42))
        self.spindle_forward_button.setLayoutDirection(Qt.RightToLeft)
        self.spindle_forward_button.setStyleSheet(u"QPushButton {\n"
"    text-align: right;\n"
"    padding-right: 23px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_forward_button.setIcon(icon9)
        self.spindle_forward_button.setIconSize(QSize(18, 18))

        self.horizontalLayout_86.addWidget(self.spindle_forward_button)


        self.verticalLayout_27.addLayout(self.horizontalLayout_86)


        self.main_control_screen_layout_panel.addWidget(self.jog_and_spindle_qframe)


        self.verticalLayout_31.addLayout(self.main_control_screen_layout_panel)

        Form.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Form)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1931, 26))
        self.menuBar.setMinimumSize(QSize(0, 25))
        self.menuBar.setStyleSheet(u"QMenuBar {\n"
"color: white;\n"
"background: rgb(118, 122, 124);\n"
"font: 11pt bebas kai;\n"
"}")
        self.menuExit = QMenu(self.menuBar)
        self.menuExit.setObjectName(u"menuExit")
        self.menuRecentFiles = QMenu(self.menuExit)
        self.menuRecentFiles.setObjectName(u"menuRecentFiles")
        self.menuMachine = QMenu(self.menuBar)
        self.menuMachine.setObjectName(u"menuMachine")
        self.menuHoming = QMenu(self.menuMachine)
        self.menuHoming.setObjectName(u"menuHoming")
        self.menuCooling = QMenu(self.menuMachine)
        self.menuCooling.setObjectName(u"menuCooling")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        Form.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(Form)
        self.statusBar.setObjectName(u"statusBar")
        Form.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuExit.menuAction())
        self.menuBar.addAction(self.menuMachine.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuExit.addAction(self.actionOpen)
        self.menuExit.addAction(self.menuRecentFiles.menuAction())
        self.menuExit.addAction(self.actionReload)
        self.menuExit.addAction(self.actionClose)
        self.menuExit.addAction(self.actionSave_As)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menuRecentFiles.addAction(self.actionFile1)
        self.menuMachine.addAction(self.action_EmergencyStop_toggle)
        self.menuMachine.addAction(self.action_MachinePower_toggle)
        self.menuMachine.addSeparator()
        self.menuMachine.addAction(self.actionRun_Program)
        self.menuMachine.addAction(self.menuHoming.menuAction())
        self.menuMachine.addAction(self.menuCooling.menuAction())
        self.menuHoming.addAction(self.actionHome_All)
        self.menuHoming.addAction(self.actionHome_X)
        self.menuHoming.addAction(self.actionHome_Y)
        self.menuHoming.addAction(self.actionHome_Z)
        self.menuCooling.addAction(self.action_Mist_toggle)
        self.menuCooling.addAction(self.action_Flood_toggle)
        self.menuView.addAction(self.actionReport_Actual_Position)
        self.menuView.addAction(self.actionTest)

        self.retranslateUi(Form)
        self.tool_number_entry_main_panel.returnPressed.connect(self.m6_tool_call_button_main_panel.click)
        self.tool_setter_offset_right_Btn_3.clicked.connect(self.setter_diam_offset.click)
        self.z_clearance_3021.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.y_view_button.clicked.connect(self.vtk.setViewY)
        self.z_max_travel_3007.textChanged.connect(self.update_tool_setter_params.click)
        self.filesystemtable.transferFileRequest.connect(self.filesystemtable_2.transferFile)
        self.device_folder_up_button.clicked.connect(self.filesystemtable_2.viewParentDirectory)
        self.tool_table_reload_button.clicked.connect(self.tool_table.loadToolTable)
        self.program_zoom_button.clicked.connect(self.vtk.setViewProgram)
        self.machine_zoom_button.clicked.connect(self.vtk.setViewMachine)
        self.traverse_fr_3006.cursorPositionChanged.connect(self.setter_slow_fr.click)
        self.device_eject_usb_button.clicked["bool"].connect(self.removabledevicecombobox.ejectDevice)
        self.linear_jog_slider.sliderMoved.connect(self.anglular_jog_slider.setValue)
        self.tool_setter_offset_right_Btn.clicked.connect(self.setter_diam_offset.click)
        self.fast_probe_fr_3004.cursorPositionChanged.connect(self.setter_slow_fr.click)
        self.edit_gcode_button.toggled.connect(self.gcodetextedit.EditorReadWrite)
        self.clear_button.clicked.connect(self.vtk.clearLivePlot)
        self.filesystemtable.gcodeFileSelected.connect(self.main_load_gcode_button.setEnabled)
        self.vertical_spindle_nozzle_dist_3002.editingFinished.connect(self.update_programmable_coolant_param.click)
        self.btn_del_history_row_mdi.clicked.connect(self.mdihistory.removeSelectedItem)
        self.main_new_folder_button.clicked.connect(self.filesystemtable.newFolder)
        self.removabledevicecombobox.currentDeviceEjectable.connect(self.device_eject_usb_button.setEnabled)
        self.y_cal_width_3035.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.main_folder_up_button.clicked.connect(self.filesystemtable.viewParentDirectory)
        self.filesystemtable.rootChanged.connect(self.facingwidget.setFilePath)
        self.removabledevicecombobox.currentPathChanged.connect(self.filesystemtable_2.setRootPath)
        self.tool_table_delete_button.clicked.connect(self.tool_table.deleteSelectedTool)
        self.extra_probe_depth_3022.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.copy_to_usb_2.clicked.connect(self.filesystemtable.doFileTransfer)
        self.pan_button.clicked["bool"].connect(self.vtk.enable_panning)
        self.main_delete_item_button.clicked.connect(self.filesystemtable.deleteItem)
        self.wco_rotation_3031.textChanged.connect(self.update_probe_parameters_btn.click)
        self.save_as_button.clicked.connect(self.gcodetextedit.saveFileAs)
        self.activate_programmable_coolant_3000.editingFinished.connect(self.update_programmable_coolant_param.click)
        self.zoom_in_button.clicked.connect(self.vtk.zoomIn)
        self.diameter_hint_3025.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.filesystemtable_2.transferFileRequest.connect(self.filesystemtable.transferFile)
        self.z_view_button.clicked.connect(self.vtk.setViewZ)
        self.breakage_tolerance_3037.cursorPositionChanged.connect(self.update_tool_setter_params.click)
        self.btn_copy_to_editor_mdi.clicked.connect(self.mdihistory.copySelectionToGcodeEditor)
        self.spindle_zero_height_3010.cursorPositionChanged.connect(self.setter_fast_fr.click)
        self.tool_setter_offset_left_Btn.clicked.connect(self.setter_diam_offset.click)
        self.traverse_fr_3006.textChanged.connect(self.update_tool_setter_params.click)
        self.main_rename_item_button.clicked.connect(self.filesystemtable.rename)
        self.x_hint_ridge_valley_3028.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.btn_del_all_mdi.clicked.connect(self.mdihistory.removeAll)
        self.tool_diameter_offset_Btn.clicked.connect(self.setter_diam_offset.click)
        self.max_xy_distance_3018.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.path_button.clicked.connect(self.vtk.setViewPath)
        self.tool_number_entry_tool_page.returnPressed.connect(self.m6_tool_call_button_tool_page.click)
        self.load_spindle_tool_number_2.returnPressed.connect(self.load_spindle_button_2.click)
        self.fast_probe_fr_3004.textChanged.connect(self.update_tool_setter_params.click)
        self.max_z_distance_3020.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.z_max_travel_3007.cursorPositionChanged.connect(self.xyz_max_travel.click)
        self.x_cal_width_3034.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.copy_from_usb_2.clicked.connect(self.filesystemtable_2.doFileTransfer)
        self.tool_setter_offset_left_Btn_2.clicked.connect(self.setter_diam_offset.click)
        self.device_delete_item_button.clicked.connect(self.filesystemtable_2.deleteItem)
        self.mdiEntry.returnPressed.connect(self.enter.click)
        self.y_hint_ridge_valley_3029.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.tool_table_save_button.clicked.connect(self.tool_table.saveToolTable)
        self.slow_probe_fr_3005.cursorPositionChanged.connect(self.setter_slow_fr.click)
        self.tool_setter_offset_direction_3013.textChanged.connect(self.update_tool_setter_params.click)
        self.spindle_zero_height_3010.textChanged.connect(self.update_tool_setter_params.click)
        self.pc_angle_offset_3003.editingFinished.connect(self.update_programmable_coolant_param.click)
        self.xy_clearance_3019.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.tool_diameter_offset_mode_3012.textChanged.connect(self.update_tool_setter_params.click)
        self.probe_traverse_fr_3017.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.y_hint_boss_pocket_3027.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.horizontal_spindle_nozzle_dist_3001.editingFinished.connect(self.update_programmable_coolant_param.click)
        self.iso_view_button.clicked.connect(self.vtk.setViewP)
        self.find_replace_button.clicked.connect(self.gcodetextedit.findDialog)
        self.btn_clear_queue_mdi.clicked.connect(self.mdihistory.clearQueue)
        self.probe_slow_fr_3015.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.tool_diameter_probe_mode_3011.textChanged.connect(self.update_tool_setter_params.click)
        self.save_button.clicked.connect(self.gcodetextedit.saveFile)
        self.tool_table_add_tool_button.clicked.connect(self.tool_table.addTool)
        self.sq_cal_axis_3036.textChanged.connect(self.update_probe_parameters_btn.click)
        self.btn_row_up_mdi.clicked.connect(self.mdihistory.moveRowItemUp)
        self.device_rename_item_button.clicked.connect(self.filesystemtable_2.rename)
        self.xy_max_travel_3008.textChanged.connect(self.update_tool_setter_params.click)
        self.perspective_button.clicked.connect(self.vtk.setViewPersp)
        self.enter.clicked.connect(self.mdihistory.submit)
        self.zoom_out_button.clicked.connect(self.vtk.zoomOut)
        self.btn_run_selection_mdi.clicked.connect(self.mdihistory.runSelection)
        self.slow_probe_fr_3005.textChanged.connect(self.update_tool_setter_params.click)
        self.user_setter_2_3039.cursorPositionChanged.connect(self.update_tool_setter_params.click)
        self.main_load_gcode_button.clicked.connect(self.filesystemtable.loadSelectedFile)
        self.retract_distance_3009.cursorPositionChanged.connect(self.setter_retract_dist.click)
        self.probe_tool_number_3014.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.step_off_width_3023.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.edge_width_3024.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.btn_run_from_line_mdi.clicked.connect(self.mdihistory.runFromSelection)
        self.cal_diameter_3033.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.probe_mode_3030.textChanged.connect(self.update_probe_parameters_btn.click)
        self.x_hint_boss_pocket_3026.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.tool_diameter_probe_Btn.clicked.connect(self.setter_touch_position.click)
        self.btn_row_down_mdi.clicked.connect(self.mdihistory.moveRowItemDown)
        self.user_setter_1_3038.cursorPositionChanged.connect(self.update_tool_setter_params.click)
        self.probe_fast_fr_3016.editingFinished.connect(self.update_probe_parameters_btn.click)
        self.filesystemtable_2.atDeviceRoot.connect(self.device_folder_up_button.setDisabled)
        self.removabledevicecombobox.usbPresent.connect(self.device_eject_usb_button.setEnabled)
        self.btn_pause_mdi.toggled.connect(self.mdihistory.toggleQueue)
        self.x_view_button.clicked.connect(self.vtk.setViewX)
        self.main_new_file_button.clicked.connect(self.filesystemtable.newFile)
        self.retract_distance_3009.textChanged.connect(self.update_tool_setter_params.click)
        self.xy_max_travel_3008.cursorPositionChanged.connect(self.xyz_max_travel.click)
        self.ortho_button.clicked.connect(self.vtk.setViewOrtho)
        self.set_g30_1_position.clicked.connect(self.setter_spindle_zero.click)
        self.hide_show_usb_button.toggled.connect(self.usb_file_frame.setHidden)
        self.hide_show_usb_button.toggled.connect(self.copy_to_usb_2.setHidden)
        self.refresh_folder_button.pressed.connect(self.filesystemtable.update)
        self.refresh_folder_button.pressed.connect(self.filesystemtable_2.update)
        self.offset_table_clear_all_button.clicked.connect(self.offset_table.clearOffsetTable)
        self.offset_table_save_button.clicked.connect(self.offset_table.saveOffsetTable)
        self.offset_table_reload_button.clicked.connect(self.offset_table.loadOffsetTable)
        self.offset_table_clear_selected_button.clicked.connect(self.offset_table.deleteSelectedOffset)
        self.tool_table_reload_button.released.connect(self.m6_tool_call_button_main_panel.animateClick)
        self.undo_button.clicked.connect(self.gcodetextedit.undo)

        self.tabWidget.setCurrentIndex(8)
        self.gcode_mdi.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.probe_tab_widget.setCurrentIndex(0)
        self.probe_help_widget.setCurrentIndex(0)
        self.setter_tab_widget.setCurrentIndex(0)
        self.operation.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_9.setCurrentIndex(2)
        self.tabWidget_8.setCurrentIndex(2)
        self.tabWidget_7.setCurrentIndex(0)
        self.sidebar_widget.setCurrentIndex(0)
        self.jogDisplay.setCurrentIndex(3)
        self.spindle_rpm_source_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Probe Basic", None))
        self.actionExit.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.actionOpen.setText(QCoreApplication.translate("Form", u"&Open ...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("Form", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("Form", u"Close", None))
        self.actionReload.setText(QCoreApplication.translate("Form", u"&Reload", None))
#if QT_CONFIG(shortcut)
        self.actionReload.setShortcut(QCoreApplication.translate("Form", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("Form", u"Save As ...", None))
        self.actionHome_X.setText(QCoreApplication.translate("Form", u"Home &X", None))
        self.actionHome_Y.setText(QCoreApplication.translate("Form", u"Home &Y", None))
        self.actionHome_Z.setText(QCoreApplication.translate("Form", u"Home &Z", None))
        self.action_EmergencyStop_toggle.setText(QCoreApplication.translate("Form", u"Toggle E-stop", None))
#if QT_CONFIG(shortcut)
        self.action_EmergencyStop_toggle.setShortcut(QCoreApplication.translate("Form", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.action_MachinePower_toggle.setText(QCoreApplication.translate("Form", u"Machine Power", None))
#if QT_CONFIG(shortcut)
        self.action_MachinePower_toggle.setShortcut(QCoreApplication.translate("Form", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actionHome_All.setText(QCoreApplication.translate("Form", u"Home All", None))
        self.actionRun_Program.setText(QCoreApplication.translate("Form", u"Run Program", None))
#if QT_CONFIG(shortcut)
        self.actionRun_Program.setShortcut(QCoreApplication.translate("Form", u"R", None))
#endif // QT_CONFIG(shortcut)
        self.actionFile1.setText(QCoreApplication.translate("Form", u"File1", None))
        self.actionReport_Actual_Position.setText(QCoreApplication.translate("Form", u"Report Actual Position", None))
        self.actionTest.setText(QCoreApplication.translate("Form", u"Test", None))
        self.action_Mist_toggle.setText(QCoreApplication.translate("Form", u"Mist On", None))
#if QT_CONFIG(shortcut)
        self.action_Mist_toggle.setShortcut(QCoreApplication.translate("Form", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.action_Flood_toggle.setText(QCoreApplication.translate("Form", u"Flood On", None))
#if QT_CONFIG(shortcut)
        self.action_Flood_toggle.setShortcut(QCoreApplication.translate("Form", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.recentfilecombobox.setProperty(u"resource", "")
        self.find_m6_button.setText(QCoreApplication.translate("Form", u"FIND M6", None))
#if QT_CONFIG(tooltip)
        self.run_from_line_Num.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#ff0000;\">IMPORTANT WARNING!!!</span></p><p><span style=\" font-weight:600; color:#ff0000;\">RUN FROM LINE </span><span style=\" color:#000000;\">does </span><span style=\" font-weight:600; color:#ff0000;\">NOT </span><span style=\" color:#000000;\">account for any</span></p><p><span style=\" color:#000000;\">preceding commands such as but not limited </span></p><p><span style=\" color:#000000;\">too the following:</span></p><p><span style=\" color:#000000;\">- XYZ positioning move Commands</span></p><p><span style=\" color:#000000;\">- Feedrate Commands</span></p><p><span style=\" color:#000000;\">- G5x Work Offset Commands</span></p><p><span style=\" color:#000000;\">- Tool Change Commands</span></p><p><span style=\" color:#000000;\">- Tool length offsets that need to be active</span></p><p><span style=\" color:#000000;\">- Spindle or Coolant ON Commands</span></p><p><span style=\" color:#000000;\">- A"
                        "NY Commands not on the current line</span></p><p><span style=\" font-weight:600; color:#ff0000;\">It is recommended to be run from a previous</span></p><p><span style=\" font-weight:600; color:#ff0000;\">tool change line that reissues all of those </span></p><p><span style=\" font-weight:600; color:#ff0000;\">commands to avoid unexpected behavior!</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.run_from_line_Num.setText("")
        self.run_from_line_Num.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.run_from_line_Btn.setText(QCoreApplication.translate("Form", u"SET QUE", None))
        self.mdihistory.setProperty(u"mdiEntrylineName", QCoreApplication.translate("Form", u"mdiEntry", None))
        self.btn_del_history_row_mdi.setText(QCoreApplication.translate("Form", u"DEL SEL", None))
        self.btn_del_all_mdi.setText(QCoreApplication.translate("Form", u"DEL ALL", None))
        self.btn_clear_queue_mdi.setText(QCoreApplication.translate("Form", u"CLR QUE", None))
        self.btn_pause_mdi.setText(QCoreApplication.translate("Form", u"PAUSE", None))
        self.btn_run_from_line_mdi.setText(QCoreApplication.translate("Form", u"RUN FROM", None))
        self.btn_run_selection_mdi.setText(QCoreApplication.translate("Form", u"RUN SEL", None))
        self.btn_copy_to_editor_mdi.setText(QCoreApplication.translate("Form", u"GCODE", None))
        self.R.setText(QCoreApplication.translate("Form", u"R", None))
        self.I.setText(QCoreApplication.translate("Form", u"I", None))
        self.NP6.setText(QCoreApplication.translate("Form", u"6", None))
        self.A.setText(QCoreApplication.translate("Form", u"A", None))
        self.S.setText(QCoreApplication.translate("Form", u"S", None))
        self.F.setText(QCoreApplication.translate("Form", u"F", None))
        self.J.setText(QCoreApplication.translate("Form", u"J", None))
        self.NP3.setText(QCoreApplication.translate("Form", u"3", None))
        self.NP7.setText(QCoreApplication.translate("Form", u"7", None))
        self.M.setText(QCoreApplication.translate("Form", u"M", None))
        self.NP5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btnMdiSpace.setText(QCoreApplication.translate("Form", u"SPACE", None))
        self.D.setText(QCoreApplication.translate("Form", u"D", None))
        self.B.setText(QCoreApplication.translate("Form", u"B", None))
        self.Q.setText(QCoreApplication.translate("Form", u"Q", None))
        self.O.setText(QCoreApplication.translate("Form", u"O", None))
        self.Z.setText(QCoreApplication.translate("Form", u"Z", None))
        self.NP1.setText(QCoreApplication.translate("Form", u"1", None))
        self.P.setText(QCoreApplication.translate("Form", u"P", None))
        self.NP4.setText(QCoreApplication.translate("Form", u"4", None))
        self.NP8.setText(QCoreApplication.translate("Form", u"8", None))
        self.decimal.setText(QCoreApplication.translate("Form", u".", None))
        self.NP9.setText(QCoreApplication.translate("Form", u"9", None))
        self.L.setText(QCoreApplication.translate("Form", u"L", None))
        self.X.setText(QCoreApplication.translate("Form", u"X", None))
        self.H.setText(QCoreApplication.translate("Form", u"H", None))
        self.btnMdiLeft_arrow.setText("")
        self.enter.setText(QCoreApplication.translate("Form", u"ENTER", None))
        self.T.setText(QCoreApplication.translate("Form", u"T", None))
        self.btnMdiBksp.setText("")
        self.btnMdiRight_arrow.setText("")
        self.NP0.setText(QCoreApplication.translate("Form", u"0", None))
        self.G.setText(QCoreApplication.translate("Form", u"G", None))
        self.subtract.setText(QCoreApplication.translate("Form", u"-", None))
        self.K.setText(QCoreApplication.translate("Form", u"K", None))
        self.Y.setText(QCoreApplication.translate("Form", u"Y", None))
        self.NP2.setText(QCoreApplication.translate("Form", u"2", None))
        self.mdiEntry.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.mdiEntry.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.gcode_page.setText(QCoreApplication.translate("Form", u"GCODE", None))
        self.mdi_page.setText(QCoreApplication.translate("Form", u"MDI", None))
        self.iso_view_button.setText(QCoreApplication.translate("Form", u"ISO VIEW", None))
        self.x_view_button.setText(QCoreApplication.translate("Form", u"X View", None))
        self.y_view_button.setText(QCoreApplication.translate("Form", u"Y View", None))
        self.z_view_button.setText(QCoreApplication.translate("Form", u"Z View", None))
        self.pan_button.setText(QCoreApplication.translate("Form", u"PAN", None))
        self.zoom_in_button.setText(QCoreApplication.translate("Form", u"ZOOM +", None))
        self.zoom_out_button.setText(QCoreApplication.translate("Form", u"ZOOM -", None))
        self.program_zoom_button.setText(QCoreApplication.translate("Form", u"PGM EXT", None))
        self.machine_zoom_button.setText(QCoreApplication.translate("Form", u"MCH EXT", None))
        self.path_button.setStyleSheet("")
        self.path_button.setText(QCoreApplication.translate("Form", u"PATH", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.ortho_button.setText(QCoreApplication.translate("Form", u"ORTHO", None))
        self.perspective_button.setText(QCoreApplication.translate("Form", u"PSPECT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("Form", u"MAIN", None))
        self.device_folder_up_button.setText(QCoreApplication.translate("Form", u"  FOLDER UP", None))
        self.device_eject_usb_button.setText(QCoreApplication.translate("Form", u"EJECT USB", None))
        self.filesystemtable_2.setProperty(u"hiddenColumns", QCoreApplication.translate("Form", u"2, 4,1", None))
        self.device_delete_item_button.setText(QCoreApplication.translate("Form", u" DELETE", None))
        self.device_rename_item_button.setText(QCoreApplication.translate("Form", u"RENAME", None))
        self.copy_from_usb_2.setText(QCoreApplication.translate("Form", u"TO PC  ", None))
        self.main_folder_up_button.setText(QCoreApplication.translate("Form", u"  FOLDER UP", None))
        self.main_load_gcode_button.setText(QCoreApplication.translate("Form", u"LOAD G-CODE", None))
        self.filesystemtable.setProperty(u"hiddenColumns", QCoreApplication.translate("Form", u"1, 2", None))
        self.hide_show_usb_button.setText(QCoreApplication.translate("Form", u"HIDE USB", None))
        self.hide_show_usb_button.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"hide_show_usb\", \"property\": \"Text\", \"expression\": \"'SHOW USB' if ch[0] else 'HIDE USB'\", \"channels\": [{\"url\": \"settings:startup-settings.usb-hide-show\", \"trigger\": true}]}]", None))
        self.hide_show_usb_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"startup-settings.usb-hide-show", None))
        self.copy_to_usb_2.setText(QCoreApplication.translate("Form", u" TO USB", None))
        self.main_delete_item_button.setText(QCoreApplication.translate("Form", u" DELETE", None))
        self.main_new_file_button.setText(QCoreApplication.translate("Form", u" NEW FILE", None))
        self.main_new_folder_button.setText(QCoreApplication.translate("Form", u" NEW FOLDER", None))
        self.main_rename_item_button.setText(QCoreApplication.translate("Form", u"RENAME", None))
        self.gcodeeditor_label.setText(QCoreApplication.translate("Form", u"G-CODE FILE EDITOR", None))
        self.edit_gcode_button.setText(QCoreApplication.translate("Form", u"EDIT G-CODE", None))
        self.find_replace_button.setText(QCoreApplication.translate("Form", u"FIND/REPLACE", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.save_as_button.setText(QCoreApplication.translate("Form", u"SAVE AS", None))
        self.undo_button.setText(QCoreApplication.translate("Form", u"UNDO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file_tab), QCoreApplication.translate("Form", u"FILE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.atc_tab), QCoreApplication.translate("Form", u"ATC", None))
        self.tool_table.setProperty(u"displayColumns", QCoreApplication.translate("Form", u"TXYZDR", None))
        self.tool_table_delete_button.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.tool_table_add_tool_button.setText(QCoreApplication.translate("Form", u"ADD TOOL", None))
        self.tool_table_save_button.setText(QCoreApplication.translate("Form", u"SAVE TABLE", None))
        self.tool_table_reload_button.setText(QCoreApplication.translate("Form", u"RELOAD TABLE", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"COMMENT", None))
        self.tool_length_7.setText(QCoreApplication.translate("Form", u"No Tool Loaded", None))
        self.tool_length_7.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?Remark\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Tool Comment\"}]", None))
        self.tool_length_7.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.label_43.setText("")
        self.label_48.setText(QCoreApplication.translate("Form", u"TOOL LENGTH", None))
        self.tool_length_5.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length_5.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length_5.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"DIAM", None))
        self.tool_diameter_2.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_diameter_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]", None))
        self.tool_diameter_2.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length_6.setText(QCoreApplication.translate("Form", u"T0", None))
        self.tool_length_6.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'T' + ch[0]\", \"name\": \"current tool\"}]", None))
        self.tool_length_6.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.machine_column_header_7.setText(QCoreApplication.translate("Form", u"TOOL CHANGE PANEL", None))
        self.load_spindle_tool_number_2.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.load_spindle_tool_number_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(0)\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.load_spindle_button_2.setText(QCoreApplication.translate("Form", u"LOAD SPINDLE", None))
        self.load_spindle_button_2.setProperty(u"filename", QCoreApplication.translate("Form", u"load_spindle_safety_2.ngc", None))
        self.remove_tool_2.setText(QCoreApplication.translate("Form", u"UNLOAD SPINDLE", None))
        self.remove_tool_2.setProperty(u"filename", QCoreApplication.translate("Form", u"unload_spindle.ngc", None))
        self.tool_number_entry_tool_page.setText(QCoreApplication.translate("Form", u"0", None))
        self.tool_number_entry_tool_page.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
        self.m6_tool_call_button_tool_page.setText(QCoreApplication.translate("Form", u"M6 G43", None))
        self.m6_tool_call_button_tool_page.setProperty(u"filename", QCoreApplication.translate("Form", u"m6_tool_call_tool_page.ngc", None))
        self.machine_column_header_8.setText(QCoreApplication.translate("Form", u"ELECTRONIC TOOL SETTER", None))
        self.tool_touch_off_button.setText(QCoreApplication.translate("Form", u"TOUCH OFF CURRENT TOOL", None))
        self.tool_touch_off_button.setProperty(u"filename", QCoreApplication.translate("Form", u"tool_touch_off.ngc", None))
        self.mdi_entry_box_4.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tool_tab), QCoreApplication.translate("Form", u"TOOL", None))
        self.offset_table.setProperty(u"displayColumns", QCoreApplication.translate("Form", u"XYZABCR", None))
        self.offset_table_clear_selected_button.setText(QCoreApplication.translate("Form", u"CLEAR SELECTED", None))
        self.offset_table_clear_all_button.setText(QCoreApplication.translate("Form", u"CLEAR ALL", None))
#if QT_CONFIG(tooltip)
        self.offset_table_save_button.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><img src=\":/images/floppy_disc.png\"/></p><p>Saves the Offset Table</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.offset_table_save_button.setText(QCoreApplication.translate("Form", u"SAVE TABLE", None))
        self.offset_table_reload_button.setText(QCoreApplication.translate("Form", u"RELOAD TABLE", None))
        self.mdi_entry_box_6.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.machine_column_header_4.setText(QCoreApplication.translate("Form", u"WORK COORDINATE OFFSETS", None))
        self.actionbutton_g54_2.setText(QCoreApplication.translate("Form", u"G54", None))
        self.actionbutton_g54_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G54", None))
        self.actionbutton_g55_2.setText(QCoreApplication.translate("Form", u"G55", None))
        self.actionbutton_g55_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G55", None))
        self.actionbutton_g56_2.setText(QCoreApplication.translate("Form", u"G56", None))
        self.actionbutton_g56_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G56", None))
        self.actionbutton_g57_2.setText(QCoreApplication.translate("Form", u"G57", None))
        self.actionbutton_g57_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G57", None))
        self.actionbutton_g58_2.setText(QCoreApplication.translate("Form", u"G58", None))
        self.actionbutton_g58_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G58", None))
        self.actionbutton_g59_4.setText(QCoreApplication.translate("Form", u"G59", None))
        self.actionbutton_g59_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59", None))
        self.actionbutton_g59_5.setText(QCoreApplication.translate("Form", u"G59.1", None))
        self.actionbutton_g59_5.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.1", None))
        self.actionbutton_g59_6.setText(QCoreApplication.translate("Form", u"G59.2", None))
        self.actionbutton_g59_6.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.2", None))
        self.actionbutton_g59_7.setText(QCoreApplication.translate("Form", u"G59.3", None))
        self.actionbutton_g59_7.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.3", None))
        self.axis_column_header_9.setText(QCoreApplication.translate("Form", u"SET TO ZERO", None))
        self.axis_column_header_10.setText(QCoreApplication.translate("Form", u"AXIS", None))
        self.machine_column_header_10.setText(QCoreApplication.translate("Form", u"WC CURRENT POSITION", None))
        self.machine_column_header_11.setText(QCoreApplication.translate("Form", u"MACHINE\n"
"COORDS", None))
        self.machine_column_header_12.setText(QCoreApplication.translate("Form", u"WC\n"
"OFFSET", None))
        self.ref_coilumn_header_4.setText(QCoreApplication.translate("Form", u"G52/G92\n"
"OFFSET", None))
        self.machine_column_header_13.setText(QCoreApplication.translate("Form", u"TOOL\n"
"OFFSET", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.offsets_tab), QCoreApplication.translate("Form", u"OFFSETS", None))
        self.label_81.setText(QCoreApplication.translate("Form", u"WORK OFFSETS", None))
        self.actionbutton_19.setText(QCoreApplication.translate("Form", u"G54", None))
        self.actionbutton_19.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G54", None))
        self.actionbutton_20.setText(QCoreApplication.translate("Form", u"G55", None))
        self.actionbutton_20.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G55", None))
        self.actionbutton_21.setText(QCoreApplication.translate("Form", u"G56", None))
        self.actionbutton_21.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G56", None))
        self.actionbutton_26.setText(QCoreApplication.translate("Form", u"G57", None))
        self.actionbutton_26.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G57", None))
        self.actionbutton_24.setText(QCoreApplication.translate("Form", u"G58", None))
        self.actionbutton_24.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G58", None))
        self.actionbutton_22.setText(QCoreApplication.translate("Form", u"G59", None))
        self.actionbutton_22.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59", None))
        self.actionbutton_27.setText(QCoreApplication.translate("Form", u"G59.1", None))
        self.actionbutton_27.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.1", None))
        self.actionbutton_25.setText(QCoreApplication.translate("Form", u"G59.2", None))
        self.actionbutton_25.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.2", None))
        self.actionbutton_23.setText(QCoreApplication.translate("Form", u"G59.3", None))
        self.actionbutton_23.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.3", None))
        self.probe_posn_only_Btn.setText(QCoreApplication.translate("Form", u"PROBE POSITION ONLY", None))
        self.probe_posn_only_Btn.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_posn_only_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.probe-posn-btn", None))
        self.label_82.setText(QCoreApplication.translate("Form", u"Probing Parameters", None))
        self.ref_coilumn_header_19.setText("")
        self.label_83.setText(QCoreApplication.translate("Form", u"Probe Tool #  ", None))
        self.probe_tool_number_3014.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.probe_tool_number_3014.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_tool_number_3014.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.probe-tool-number", None))
        self.probe_tool_number_3014.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.0f}", None))
        self.label_86.setText(QCoreApplication.translate("Form", u"PROBE SLOW FDRATE  ", None))
        self.probe_slow_fr_3015.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.probe_slow_fr_3015.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_slow_fr_3015.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.probe-slow-fr", None))
        self.probe_slow_fr_3015.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.ref_coilumn_header_20.setText("")
        self.label_94.setText(QCoreApplication.translate("Form", u"PROBE TRAVERSE FR  ", None))
        self.probe_traverse_fr_3017.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.probe_traverse_fr_3017.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_traverse_fr_3017.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.probe-traverse-fr", None))
        self.probe_traverse_fr_3017.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.label_85.setText(QCoreApplication.translate("Form", u"PROBE FAST FDRATE  ", None))
        self.probe_fast_fr_3016.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.probe_fast_fr_3016.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_fast_fr_3016.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.probe-fast-fr", None))
        self.probe_fast_fr_3016.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.ref_coilumn_header_21.setText("")
        self.label_87.setText(QCoreApplication.translate("Form", u"Max X/Y Distance  ", None))
        self.max_xy_distance_3018.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.max_xy_distance_3018.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.max_xy_distance_3018.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.max-xy-distance", None))
        self.max_xy_distance_3018.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_88.setText(QCoreApplication.translate("Form", u"X/Y Clearance  ", None))
        self.xy_clearance_3019.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.xy_clearance_3019.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.xy_clearance_3019.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.xy-clearance", None))
        self.xy_clearance_3019.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.ref_coilumn_header_22.setText("")
        self.label_90.setText(QCoreApplication.translate("Form", u"Max Z Distance  ", None))
        self.max_z_distance_3020.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.max_z_distance_3020.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.max_z_distance_3020.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.max-z-distance", None))
        self.max_z_distance_3020.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_91.setText(QCoreApplication.translate("Form", u"Z Clearance  ", None))
        self.z_clearance_3021.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.z_clearance_3021.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.z_clearance_3021.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.z-clearance", None))
        self.z_clearance_3021.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.ref_coilumn_header_23.setText("")
        self.label_92.setText(QCoreApplication.translate("Form", u"Extra Probe Depth  ", None))
        self.extra_probe_depth_3022.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.extra_probe_depth_3022.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.extra_probe_depth_3022.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.extra-probe-depth", None))
        self.extra_probe_depth_3022.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_84.setText(QCoreApplication.translate("Form", u"Step Off Width  ", None))
        self.step_off_width_3023.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.step_off_width_3023.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.step_off_width_3023.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.step-off-width", None))
        self.step_off_width_3023.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.update_probe_parameters_btn.setText(QCoreApplication.translate("Form", u"UPDATE PROBE PARAMS", None))
        self.update_probe_parameters_btn.setProperty(u"filename", QCoreApplication.translate("Form", u"touch_probe_param_update.ngc", None))
        self.reset_all_data.setText(QCoreApplication.translate("Form", u"RESET ALL DATA", None))
        self.reset_all_data.setProperty(u"filename", QCoreApplication.translate("Form", u"reset_all_data.ngc", None))
        self.x_data_reset1.setText(QCoreApplication.translate("Form", u"X DATA RESET", None))
        self.x_data_reset1.setProperty(u"filename", QCoreApplication.translate("Form", u"x_data_reset.ngc", None))
        self.y_data_reset1.setText(QCoreApplication.translate("Form", u"Y DATA RESET", None))
        self.y_data_reset1.setProperty(u"filename", QCoreApplication.translate("Form", u"y_data_reset.ngc", None))
        self.label_108.setText(QCoreApplication.translate("Form", u"X- PROBED ", None))
        self.x_minus_probed_position.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_minus_probed_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.x_minus_probed_position.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_98.setText(QCoreApplication.translate("Form", u"X+ PROBED ", None))
        self.x_plus_probed_position.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_plus_probed_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.x_plus_probed_position.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_97.setText(QCoreApplication.translate("Form", u"X WIDTH ", None))
        self.x_probed_width.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_probed_width.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.x_probed_width.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_109.setText(QCoreApplication.translate("Form", u"Y- PROBED ", None))
        self.y_minus_probed_position.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_minus_probed_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.y_minus_probed_position.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_101.setText(QCoreApplication.translate("Form", u"Y+ PROBED ", None))
        self.y_plus_probed_position.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_plus_probed_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.y_plus_probed_position.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_100.setText(QCoreApplication.translate("Form", u"Y WIDTH ", None))
        self.y_probed_width.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_probed_width.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.y_probed_width.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_110.setText(QCoreApplication.translate("Form", u"Z- PROBED ", None))
        self.z_minus_probed_position.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.z_minus_probed_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.z_minus_probed_position.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_102.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>DIAM <span style=\" font-size:18pt;\">\u2300</span></p></body></html> ", None))
        self.averaged_diam.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.averaged_diam.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.averaged_diam.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_113.setText(QCoreApplication.translate("Form", u"X CENTER ", None))
        self.x_center_probed.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_center_probed.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.x_center_probed.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_99.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>EDGE <span style=\" font-weight:400;\">\u0394</span></p></body></html> ", None))
        self.edge_delta.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.edge_delta.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.edge_delta.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_96.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>EDGE <span style=\" font-weight:400;\">\u2220</span></p></body></html> ", None))
        self.edge_angle.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.edge_angle.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.edge_angle.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.edge_angle.setProperty(u"expression", QCoreApplication.translate("Form", u"val", None))
        self.label_114.setText(QCoreApplication.translate("Form", u"Y CENTER ", None))
        self.y_center_probed.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_center_probed.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.y_center_probed.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.mdi_entry_box_5.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.outside_corners.setText(QCoreApplication.translate("Form", u"OUTSIDE CORNERS", None))
        self.inside_corners.setText(QCoreApplication.translate("Form", u"INSIDE CORNERS", None))
        self.boss_and_pocket.setText(QCoreApplication.translate("Form", u"BOSS AND POCKET", None))
        self.ridge_and_valley.setText(QCoreApplication.translate("Form", u"RIDGE AND VALLEY", None))
        self.rotation_angle.setText(QCoreApplication.translate("Form", u"EDGE ANGLE", None))
        self.rotary_axis_2.setText(QCoreApplication.translate("Form", u"ROTARY AXIS", None))
        self.calibrate.setText(QCoreApplication.translate("Form", u"CALIBRATE", None))
        self.probe_help.setText(QCoreApplication.translate("Form", u"PROBE HELP", None))
        self.label_19.setText("")
        self.probe_led.setProperty(u"pinBaseName", QCoreApplication.translate("Form", u"probe-led", None))
        self.halbutton.setText("")
        self.halbutton.setProperty(u"pinBaseName", QCoreApplication.translate("Form", u"probe-in", None))
        self.probe_back_left_top_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_back_left_top_corner.ngc", None))
        self.probe_back_right_top_corner.setText("")
        self.probe_back_right_top_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_back_right_top_corner.ngc", None))
        self.probe_right_top_side.setText("")
        self.probe_right_top_side.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_right_top_side.ngc", None))
        self.probe_z_minus_wco_edge.setText("")
        self.probe_z_minus_wco_edge.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_z_minus_wco.ngc", None))
        self.probe_front_top_side.setText("")
        self.probe_front_top_side.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_front_top_side.ngc", None))
        self.probe_back_top_side.setText("")
        self.probe_back_top_side.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_back_top_side.ngc", None))
        self.probe_front_left_top_corner.setText("")
        self.probe_front_left_top_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_front_left_top_corner.ngc", None))
        self.probe_front_right_top_corner.setText("")
        self.probe_front_right_top_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_front_right_top_corner.ngc", None))
        self.probe_left_top_side.setText("")
        self.probe_left_top_side.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_left_top_side.ngc", None))
        self.probe_front_right_inside_corner.setText("")
        self.probe_front_right_inside_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_front_right_inside_corner.ngc", None))
        self.probe_y_plus_wco.setText("")
        self.probe_y_plus_wco.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_y_plus_wco.ngc", None))
        self.probe_back_right_inside_corner.setText("")
        self.probe_back_right_inside_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_back_right_inside_corner.ngc", None))
        self.probe_front_left_inside_corner.setText("")
        self.probe_front_left_inside_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_front_left_inside_corner.ngc", None))
        self.probe_z_minus_wco_inside.setText("")
        self.probe_z_minus_wco_inside.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_z_minus_wco.ngc", None))
        self.probe_back_left_inside_corner.setText("")
        self.probe_back_left_inside_corner.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_back_left_inside_corner.ngc", None))
        self.probe_x_minus_wco.setText("")
        self.probe_x_minus_wco.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_x_minus_wco.ngc", None))
        self.probe_x_plus_wco.setText("")
        self.probe_x_plus_wco.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_x_plus_wco.ngc", None))
        self.probe_y_minus_wco.setText("")
        self.probe_y_minus_wco.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_y_minus_wco.ngc", None))
        self.probe_round_pocket_center.setText("")
        self.probe_round_pocket_center.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_round_pocket_center_start.ngc", None))
        self.probe_rect_pocket_2.setText("")
        self.probe_rect_pocket_2.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_rect_pocket_center_start.ngc", None))
        self.probe_round_boss.setText("")
        self.probe_round_boss.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_round_boss.ngc", None))
        self.probe_round_pocket.setText("")
        self.probe_round_pocket.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_round_pocket.ngc", None))
        self.probe_rect_boss.setText("")
        self.probe_rect_boss.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_rect_boss.ngc", None))
        self.probe_rect_pocket.setText("")
        self.probe_rect_pocket.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_rect_pocket.ngc", None))
        self.hint_label.setText(QCoreApplication.translate("Form", u"HINT", None))
        self.label_70.setText(QCoreApplication.translate("Form", u"DIAM:", None))
        self.diameter_hint_3025.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.diameter_hint_3025.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.diameter_hint_3025.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.diameter-hint", None))
        self.diameter_hint_3025.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_71.setText(QCoreApplication.translate("Form", u"X :", None))
        self.x_hint_boss_pocket_3026.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_hint_boss_pocket_3026.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.x_hint_boss_pocket_3026.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.x-hint-boss-pocket", None))
        self.x_hint_boss_pocket_3026.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_72.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.y_hint_boss_pocket_3027.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_hint_boss_pocket_3027.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.y_hint_boss_pocket_3027.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.y-hint-boss-pocket", None))
        self.y_hint_boss_pocket_3027.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.probe_valley_x_center_start.setText("")
        self.probe_valley_x_center_start.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_valley_x_center_start.ngc", None))
        self.probe_valley_y_center_start.setText("")
        self.probe_valley_y_center_start.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_valley_y_center_start.ngc", None))
        self.probe_ridge_y.setText("")
        self.probe_ridge_y.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_ridge_y.ngc", None))
        self.probe_valley_y.setText("")
        self.probe_valley_y.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_valley_y.ngc", None))
        self.probe_valley_x.setText("")
        self.probe_valley_x.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_valley_x.ngc", None))
        self.probe_ridge_x.setText("")
        self.probe_ridge_x.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_ridge_x.ngc", None))
        self.hint_label_2.setText(QCoreApplication.translate("Form", u"HINT", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"X :", None))
        self.x_hint_ridge_valley_3028.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_hint_ridge_valley_3028.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.x_hint_ridge_valley_3028.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.x-hint-ridge-valley", None))
        self.x_hint_ridge_valley_3028.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.y_hint_ridge_valley_3029.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_hint_ridge_valley_3029.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.y_hint_ridge_valley_3029.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.y-hint-ridge-valley", None))
        self.y_hint_ridge_valley_3029.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.probe_top_left_edge_angle.setText("")
        self.probe_top_left_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_top_left_edge_angle.ngc", None))
        self.probe_corner_y_plus_edge_angle.setText("")
        self.probe_corner_y_plus_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_corner_y_plus_edge_angle.ngc", None))
        self.probe_corner_x_plus_edge_angle.setStyleSheet("")
        self.probe_corner_x_plus_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_corner_x_plus_edge_angle.ngc", None))
        self.probe_corner_y_minus_edge_angle.setText("")
        self.probe_corner_y_minus_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_corner_y_minus_edge_angle.ngc", None))
        self.probe_z_minus_edge.setText("")
        self.probe_z_minus_edge.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_z_minus_wco.ngc", None))
        self.probe_corner_x_minus_edge_angle.setText("")
        self.probe_corner_x_minus_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_corner_x_minus_edge_angle.ngc", None))
        self.probe_top_right_edge_angle.setText("")
        self.probe_top_right_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_top_right_edge_angle.ngc", None))
        self.probe_top_back_edge_angle.setText("")
        self.probe_top_back_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_top_back_edge_angle.ngc", None))
        self.probe_top_front_edge_angle.setText("")
        self.probe_top_front_edge_angle.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_top_front_edge_angle.ngc", None))
        self.set_wco_offset_Btn.setText(QCoreApplication.translate("Form", u"SET ROTATION WCO", None))
        self.set_wco_offset_Btn.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.set_wco_offset_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.rotation-wco-btn", None))
        self.edge_width_label.setText(QCoreApplication.translate("Form", u"EDGE WIDTH", None))
        self.edge_width_3024.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.edge_width_3024.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.edge_width_3024.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.edge-width", None))
        self.edge_width_3024.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"PROBE CALIBRATION OFFSET:", None))
        self.calibration_offset_3032.setPlaceholderText(QCoreApplication.translate("Form", u"0.000000", None))
        self.calibration_offset_3032.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.calibration_offset_3032.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.calibration-offset", None))
        self.calibration_offset_3032.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.6f}", None))
        self.probe_cal_reset.setText(QCoreApplication.translate("Form", u"PROBE CAL RESET", None))
        self.probe_cal_reset.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.probe_cal_reset.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_cal_reset.ngc", None))
#if QT_CONFIG(statustip)
        self.probe_cal_round_pocket.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.probe_cal_round_pocket.setText("")
        self.probe_cal_round_pocket.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_cal_round_pocket.ngc", None))
#if QT_CONFIG(statustip)
        self.probe_cal_round_boss.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.probe_cal_round_boss.setText("")
        self.probe_cal_round_boss.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_cal_round_boss.ngc", None))
        self.hint_label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">CALIBRATION</p><p align=\"center\">DIAMETER</p></body></html>", None))
        self.cal_diameter_3033.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.cal_diameter_3033.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.cal_diameter_3033.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.cal-diameter", None))
        self.cal_diameter_3033.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.cal_avg_error.setText(QCoreApplication.translate("Form", u"CAL ON AVG XY ERROR", None))
        self.cal_avg_error.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.cal_avg_error.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.cal-xy-btn", None))
        self.cal_x_error.setText(QCoreApplication.translate("Form", u"CAL ON X ERROR", None))
        self.cal_x_error.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.cal_x_error.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.cal-x-btn", None))
        self.cal_y_error.setText(QCoreApplication.translate("Form", u"CAL ON Y ERROR", None))
        self.cal_y_error.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.cal_y_error.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.cal-y-btn", None))
#if QT_CONFIG(statustip)
        self.probe_cal_square_pocket.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.probe_cal_square_pocket.setText("")
        self.probe_cal_square_pocket.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_cal_square_pocket.ngc", None))
#if QT_CONFIG(statustip)
        self.probe_cal_square_boss.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.probe_cal_square_boss.setText("")
        self.probe_cal_square_boss.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_cal_square_boss.ngc", None))
        self.hint_label_3.setText(QCoreApplication.translate("Form", u"CALIBRATION WIDTH", None))
        self.label_103.setText(QCoreApplication.translate("Form", u"X :", None))
        self.label_107.setText(QCoreApplication.translate("Form", u"Y :", None))
        self.x_cal_width_3034.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_cal_width_3034.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.x_cal_width_3034.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.x-cal-width", None))
        self.x_cal_width_3034.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.y_cal_width_3035.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_cal_width_3035.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.y_cal_width_3035.setProperty(u"settingName", QCoreApplication.translate("Form", u"probe-parameters.y-cal-width", None))
        self.y_cal_width_3035.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_77.setText("")
        self.label_78.setText("")
        self.label_79.setText("")
        self.label_105.setText("")
        self.label_80.setText("")
        self.label_106.setText("")
        self.label_41.setText("")
        self.probe_help_prev.setText(QCoreApplication.translate("Form", u"     PREV PAGE  ", None))
        self.probe_help_next.setText(QCoreApplication.translate("Form", u" NEXT PAGE     ", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("Form", u"      TOUCH  PROBE      ", None))
        self.work_column_header_11.setText(QCoreApplication.translate("Form", u"TOOL SETTER PARAMETERS", None))
        self.probe_spindle_nose_subcallbutton.setText(QCoreApplication.translate("Form", u"PROBE SPINDLE NOSE ZERO", None))
        self.probe_spindle_nose_subcallbutton.setProperty(u"filename", QCoreApplication.translate("Form", u"probe_spindle_nose.ngc", None))
        self.label_135.setText(QCoreApplication.translate("Form", u"SPINDLE ZERO", None))
        self.spindle_zero_height_3010.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.spindle_zero_height_3010.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.spindle_zero_height_3010.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.spindle-nose-height", None))
        self.spindle_zero_height_3010.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"X", None))
        self.x_tool_change_position.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.x_tool_change_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.x_tool_change_position.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-change-position.x-tool-change-position", None))
        self.x_tool_change_position.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"FAST PROBE FR", None))
        self.fast_probe_fr_3004.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.fast_probe_fr_3004.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.fast_probe_fr_3004.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.fast-probe-fr", None))
        self.fast_probe_fr_3004.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Y", None))
        self.y_tool_change_position.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.y_tool_change_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.y_tool_change_position.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-change-position.y-tool-change-position", None))
        self.y_tool_change_position.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_120.setText(QCoreApplication.translate("Form", u"SLOW PROBE FR", None))
        self.slow_probe_fr_3005.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.slow_probe_fr_3005.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.slow_probe_fr_3005.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.slow-probe-fr", None))
        self.slow_probe_fr_3005.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"Z", None))
        self.z_tool_change_position.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.z_tool_change_position.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.z_tool_change_position.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-change-position.z-tool-change-position", None))
        self.z_tool_change_position.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_134.setText(QCoreApplication.translate("Form", u"TRAVERSE FR", None))
        self.traverse_fr_3006.setPlaceholderText(QCoreApplication.translate("Form", u"0.0", None))
        self.traverse_fr_3006.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.traverse_fr_3006.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.traverse-fr", None))
        self.traverse_fr_3006.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.set_g30_1_position.setText(QCoreApplication.translate("Form", u"SET TOOL TOUCH OFF POS", None))
        self.set_g30_1_position.setProperty(u"filename", QCoreApplication.translate("Form", u"set_g30_position.ngc", None))
        self.label_129.setText(QCoreApplication.translate("Form", u"Z MAX TRAVEL", None))
        self.z_max_travel_3007.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.z_max_travel_3007.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.z_max_travel_3007.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.z-max-travel", None))
        self.z_max_travel_3007.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.tool_diameter_probe_Btn.setText(QCoreApplication.translate("Form", u"TOOL DIAM PROBE", None))
        self.tool_diameter_probe_Btn.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.tool_diameter_probe_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.diameter-probe", None))
        self.tool_diameter_probe_mode_3011.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"Tool diameter offset\", \"property\": \"Text\", \"expression\": \"\\\"1\\\" if ch[0] else \\\"0\\\"\", \"channels\": [{\"url\": \"settings:tool-setter-probe.diameter-probe\", \"trigger\": true}]}]", None))
        self.label_133.setText(QCoreApplication.translate("Form", u"XY MAX TRAVEL", None))
        self.xy_max_travel_3008.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.xy_max_travel_3008.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.xy_max_travel_3008.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.xy-max-travel", None))
        self.xy_max_travel_3008.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.tool_diameter_offset_Btn.setText(QCoreApplication.translate("Form", u"TOOL DIAM OFFSET", None))
        self.tool_diameter_offset_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.diameter-offset", None))
        self.tool_diameter_offset_mode_3012.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"Tool diameter offset\", \"property\": \"Text\", \"expression\": \"\\\"1\\\" if ch[0] else \\\"0\\\"\", \"channels\": [{\"url\": \"settings:tool-setter-probe.diameter-offset\", \"trigger\": true}]}]", None))
        self.label_147.setText(QCoreApplication.translate("Form", u"RETRACT DIST", None))
        self.retract_distance_3009.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.retract_distance_3009.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.retract_distance_3009.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.retract-distance", None))
        self.retract_distance_3009.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.label_153.setText(QCoreApplication.translate("Form", u"TOOL OFFSET DIRECTION", None))
        self.label_150.setText(QCoreApplication.translate("Form", u"Breakage Tolerance", None))
        self.breakage_tolerance_3037.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.breakage_tolerance_3037.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.breakage_tolerance_3037.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.breakage-tolerance", None))
        self.breakage_tolerance_3037.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.tool_setter_offset_left_Btn_2.setText(QCoreApplication.translate("Form", u" BACK", None))
        self.tool_setter_offset_left_Btn_2.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.setter-offset-direction-back", None))
        self.tool_setter_user_1_name.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.user-param-name-1", None))
        self.user_setter_1_3038.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.user_setter_1_3038.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.user_setter_1_3038.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.user-setter-1", None))
        self.user_setter_1_3038.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.tool_setter_offset_left_Btn.setText(QCoreApplication.translate("Form", u" Left", None))
        self.tool_setter_offset_left_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.setter-offset-direction-left", None))
        self.tool_setter_offset_direction_3013.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"Tool setter offset direction\", \"property\": \"Text\", \"expression\": \"\\\"1\\\" if ch[0] else \\\"2\\\" if ch[1] else \\\"3\\\" if ch[2] else \\\"0\\\"\", \"channels\": [{\"url\": \"settings:tool-setter-probe.setter-offset-direction-right\", \"trigger\": true}, {\"url\": \"settings:tool-setter-probe.setter-offset-direction-front\", \"trigger\": true}, {\"url\": \"settings:tool-setter-probe.setter-offset-direction-back\", \"trigger\": true}]}]", None))
        self.tool_setter_offset_right_Btn.setText(QCoreApplication.translate("Form", u"RIGHT  ", None))
        self.tool_setter_offset_right_Btn.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.setter-offset-direction-right", None))
        self.tool_setter_user_2_name.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.user-param-name-2", None))
        self.user_setter_2_3039.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.user_setter_2_3039.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"enable\", \"property\": \"Enable\", \"expression\": \"True if ch[0] else False\", \"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}]}]", None))
        self.user_setter_2_3039.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.user-setter-2", None))
        self.user_setter_2_3039.setProperty(u"textFormat", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.tool_setter_offset_right_Btn_3.setText(QCoreApplication.translate("Form", u" FRONT", None))
        self.tool_setter_offset_right_Btn_3.setProperty(u"settingName", QCoreApplication.translate("Form", u"tool-setter-probe.setter-offset-direction-front", None))
        self.update_tool_setter_params.setText(QCoreApplication.translate("Form", u"UPDATE TOOL SETTER PARAMETERS", None))
        self.update_tool_setter_params.setProperty(u"filename", QCoreApplication.translate("Form", u"tool_setter_param_update.ngc", None))
        self.mdi_entry_box_7.setPlaceholderText(QCoreApplication.translate("Form", u"MDI", None))
        self.setter_fast_fr.setText(QCoreApplication.translate("Form", u"SPINDLE ZERO", None))
        self.setter_spindle_zero.setText(QCoreApplication.translate("Form", u"TOOL TOUCH OFF POSITION", None))
        self.setter_slow_fr.setText(QCoreApplication.translate("Form", u"FAST AND SLOW PROBE FR", None))
        self.xyz_max_travel.setText(QCoreApplication.translate("Form", u"XYZ MAX TRAVEL", None))
        self.setter_retract_dist.setText(QCoreApplication.translate("Form", u"RETRACT DISTANCE", None))
        self.setter_diam_offset.setText(QCoreApplication.translate("Form", u"TOOL DIAM OFFSET", None))
        self.setter_touch_position.setText(QCoreApplication.translate("Form", u"PROBE TOOL DIAM", None))
        self.label_140.setText(QCoreApplication.translate("Form", u"TOOL SETTER TRIGGERED POINT", None))
        self.label_50.setText("")
        self.label_138.setText(QCoreApplication.translate("Form", u"SPINDLE NOSE HOMED POSITION", None))
        self.label_52.setText("")
        self.label_136.setText(QCoreApplication.translate("Form", u"SPINDLE ZERO IN\n"
"ABSOLUTE DISTANCE", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">SPINDLE ZERO:</span></p><p>THE SPINDLE ZERO DISTANCE PARAMETER IS MEASURED FROM THE Z HOMED POSITION FROM THE REPEATABLE SPINDLE NOSE DOWN TO THE TOOL SETTER'S TRIGGERED HEIGHT. </p><p>THE PARAMETER ENTRY MUST BE A POSITIVE (ABSOLUTE) NUMBER. </p><p><span style=\" font-weight:600; text-decoration: underline;\">EXAMPLE:</span></p><p>SPINDLE NOSE HOME = Z 0.0000</p><p>TOOL SETTER TRIGGERed DISTANCE = Z -12.375</p><p>SPINDLE ZERO = 12.375</p></body></html>", None))
        self.label_148.setText(QCoreApplication.translate("Form", u"TOOL LENGTH OFFSET", None))
        self.label_149.setText(QCoreApplication.translate("Form", u"PROBED DISTANCE SUBTRACTED FROM \"SPINDLE ZERO\" TO FIND THE TOOL LENGTH OFFSET", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">SETTING TOOL TOUCH OFF POSITION:</span></p><p>TO SET THE TOOL TOUCH OFF POSITION, JOG THE MILL SO THAT THE SPINDLE CENTERLINE IS CONCENTRIC TO THE TOOL SETTER TOUCH PLATFORM. </p><p>MOVE THE Z AXIS TO THE THE HOMED (ASSUMES Z0.0000 IS THE FULL UP POSITION), AND PRESS THE &quot;SET TOOL TOUCH OFF POSITION&quot; BUTTON. </p><p>THIS RECORDS AND STORES THE CURRENT MACHINE COORDINATES AND DEFINES WHERE THE MACHINE WILL MOVE TO WHEN A TOOL TOUCH OFF CALL IS COMMANDED.</p></body></html>", None))
        self.label_51.setText("")
        self.label_53.setText("")
        self.label_139.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>SPINDLE IN Z AXIS HOMED POSITION</p></body></html>", None))
        self.label_151.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>SPINDLE CENTERED ABOVE TOOL SETTER TOUCH PLATFORM</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">FAST PROBE FEEDRATE:</span></p><p>FAST PROBE FEEDRATE IS THE SPEED AT WHICH THE TOOL INITIALLY SEARCHES FOR THE TOOL SETTER IN THE Z MINUS DIRECTION. THIS PARAMETER ENTRY SHOULD BE SET AT A SPEED THAT IS NOT TOO FAST THAT THE TRIGGER EVENT AND SUBSEQUENT MOTION CAUSES THE TOOL TO OVER SHOOT THE TRIGGER POINT AND CAUSE DAMAGE TO THE TOOL SETTER. START WITH A CONSERVATIVE ENTRY HERE, PERHAPS 10IPM AND WORK YOUR WAY TO A COMFORTABLE SPEED.</p><p><span style=\" text-decoration: underline;\">SLOW PROBE FEEDRATE:</span></p><p>SLOW PROBE FEED IS THE SECONDARY PROBING SPEED. THIS SPEED WILL BE MUCH SLOWER FOR A MORE CONSISTENT TOUCH RESULT. IF THIS PARAMETER IS LEFT SET AT ZERO, THE SUBROUTINE WILL SLIP THE SECONDARY PROBE EVENT AND USE THE FAST PROBE EVENT ONLY.</p><p><span style=\" text-decoration: underline;\">Traverse Feedrate:</span></p><p>Traversing feedrate for non probing event moves.</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">XYZ Max Travel:</span></p><p>Maximum distance the probing subroutine will allow travel before stopping with an error message letting you know the probe move failed to record a probe event.</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">RETRACT DISTANCE:</span></p><p>The retract distance is the amount of travel the tool will move after contacting the tool setter and triggering a probe event. if slow probe feedrate is non zero, a subsequent probe event will take place starting from the &quot;retract distance&quot; above or to the side of the tool setter depending on the active probe modes. the final resting position will be the retract distance above the tool setter contact plate.</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">tool diameter offset probe:</span></p><p>when this feature is active, the probing function will offset the spindle centerline by the currently loaded tool's radius in order to ensure the tools edge contacts the center of the tool setter's contact platform. this is useful for larger tools such as facemills and fly cutters or any other tool too large to correctly touch the tool setter with a centered tool TO TOOL setter alignment. </p><p>tHE DIRECTIONAL OFFSET BUTTONS IN THE PARAMETER PANEL WILL DETERMINE WHICH DIRECTION THE TOOLS CENTERLINE WILL BE OFFSET TOWARDS.  THE GRAPHIC TO THE RIGHT DEPICTS THE OPERATORS VIEW ON A TRADITIONAL MACHINE WHERE THE TOOL DIAMETER OFFSET MODE BUTTON IS ACTIVE AND THE OFFSET DIRECTION SELECTED IS &quot;&lt; LEFT&quot;.</p></body></html>", None))
        self.label_55.setText("")
        self.label_152.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">EXAMPLE REPRESENTATION:</span></p><p>TOOL DIAMETER OFFSET ACTIVE WITH &quot;LEFT&quot; TOOL OFFSET DIRECTION ACTIVE</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" text-decoration: underline;\">probe tool diameter:</span></p><p>this probing function is a place holder and is not yet included in probe basic.  its function will be to probe the tool while spinning to set the tool's diameter in the tool table.</p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("Form", u"      TOOL  SETTER      ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.probe_tab), QCoreApplication.translate("Form", u"PROBING", None))
        self.operation.setTabText(self.operation.indexOf(self.facing_tab), QCoreApplication.translate("Form", u"FACING", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.xy_tab), QCoreApplication.translate("Form", u"XY COORD", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.pattern), QCoreApplication.translate("Form", u"PATTERN", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.thread_mill), QCoreApplication.translate("Form", u"THREAD MILL", None))
        self.operation.setTabText(self.operation.indexOf(self.holeop_tab), QCoreApplication.translate("Form", u"   HOLE OPS   ", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_28), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_29), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_30), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_31), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_32), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_33), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_34), "")
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget_35), "")
        self.operation.setTabText(self.operation.indexOf(self.perimeter_tab), QCoreApplication.translate("Form", u"PERIMETER", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_2), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_20), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_22), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_23), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_24), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_25), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_26), "")
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.widget_27), "")
        self.operation.setTabText(self.operation.indexOf(self.pockets_tab), QCoreApplication.translate("Form", u"POCKETS", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget1), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget2), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget3), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget4), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget5), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget6), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget7), "")
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.widget8), "")
        self.operation.setTabText(self.operation.indexOf(self.misc_tab), QCoreApplication.translate("Form", u"MISC", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.conversational_tab), QCoreApplication.translate("Form", u"CONVERSATIONAL", None))
        self.startup_settings_label.setText(QCoreApplication.translate("Form", u"START UP SETTINGS", None))
        self.startup_tab_label.setText(QCoreApplication.translate("Form", u"START UP TAB", None))
        self.startup_tab_combobox.setItemText(0, QCoreApplication.translate("Form", u"MAIN", None))
        self.startup_tab_combobox.setItemText(1, QCoreApplication.translate("Form", u"FILE", None))
        self.startup_tab_combobox.setItemText(2, QCoreApplication.translate("Form", u"ATC", None))
        self.startup_tab_combobox.setItemText(3, QCoreApplication.translate("Form", u"TOOL", None))
        self.startup_tab_combobox.setItemText(4, QCoreApplication.translate("Form", u"OFFSETS", None))
        self.startup_tab_combobox.setItemText(5, QCoreApplication.translate("Form", u"PROBING", None))
        self.startup_tab_combobox.setItemText(6, QCoreApplication.translate("Form", u"CONVERSATIONAL", None))
        self.startup_tab_combobox.setItemText(7, QCoreApplication.translate("Form", u"SETTINGS", None))
        self.startup_tab_combobox.setItemText(8, QCoreApplication.translate("Form", u"STATUS", None))
        self.startup_tab_combobox.setItemText(9, QCoreApplication.translate("Form", u"USER", None))

        self.startup_tab_combobox.setCurrentText(QCoreApplication.translate("Form", u"MAIN", None))
        self.prog_coolant_header.setText(QCoreApplication.translate("Form", u"PROGRAMMED COOLANT CONSTANTS", None))
        self.label_141.setText(QCoreApplication.translate("Form", u"ACTIVATE PROGRAMMABLE COOLANT = 1", None))
        self.activate_programmable_coolant_3000.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.activate_programmable_coolant_3000.setProperty(u"settingName", QCoreApplication.translate("Form", u"programmable-coolant.activation", None))
        self.activate_programmable_coolant_3000.setProperty(u"textFormat", "")
        self.label_142.setText(QCoreApplication.translate("Form", u"HORIZONTAL CENTERLINE DISTANCE, SPINDLE TO NOZZLE", None))
        self.horizontal_spindle_nozzle_dist_3001.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.horizontal_spindle_nozzle_dist_3001.setProperty(u"settingName", QCoreApplication.translate("Form", u"programmable-coolant.horizontal-distance", None))
        self.horizontal_spindle_nozzle_dist_3001.setProperty(u"textFormat", "")
        self.label_143.setText(QCoreApplication.translate("Form", u"VERTICAL CENTERLINE DISTANCE, SPINDLE TO NOZZLE", None))
        self.vertical_spindle_nozzle_dist_3002.setPlaceholderText(QCoreApplication.translate("Form", u"0.0000", None))
        self.vertical_spindle_nozzle_dist_3002.setProperty(u"settingName", QCoreApplication.translate("Form", u"programmable-coolant.vertical-distance", None))
        self.vertical_spindle_nozzle_dist_3002.setProperty(u"textFormat", "")
        self.label_144.setText(QCoreApplication.translate("Form", u"NOZZLE ANGLE OFFSET", None))
        self.pc_angle_offset_3003.setPlaceholderText(QCoreApplication.translate("Form", u"0.00", None))
        self.pc_angle_offset_3003.setProperty(u"settingName", QCoreApplication.translate("Form", u"programmable-coolant.nozzle-offset", None))
        self.pc_angle_offset_3003.setProperty(u"textFormat", "")
        self.label_145.setText(QCoreApplication.translate("Form", u"TOOL LENGTH OFFSET", None))
        self.pc_tool_length.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.pc_tool_length.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.pc_tool_length.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.pc_tool_length.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.label_146.setText(QCoreApplication.translate("Form", u"CALCULATED NOZZLE ANGLE", None))
        self.coolant_final_angle.setText("")
        self.coolant_final_angle.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.coolant_final_angle.setProperty(u"format", QCoreApplication.translate("Form", u"{:.4f}", None))
        self.update_programmable_coolant_param.setText(QCoreApplication.translate("Form", u"UPDATE PARAMETER SETTINGS", None))
        self.update_programmable_coolant_param.setProperty(u"filename", QCoreApplication.translate("Form", u"update_programmable_coolant_params.ngc", None))
        self.work_column_header_10.setText(QCoreApplication.translate("Form", u"Spindle speed display rpm source", None))
        self.spindle_calculated_rpm_button.setText(QCoreApplication.translate("Form", u"Calculated Spindle RPM", None))
        self.spindle_calculated_rpm_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"spindle-rpm-display.calculated-rpm", None))
        self.spindle_encoder_rpm_button.setText(QCoreApplication.translate("Form", u"encoder spindle rpm", None))
        self.spindle_encoder_rpm_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"spindle-rpm-display.encoder-feedback-rpm", None))
        self.ang_jog_slider_link.setText(QCoreApplication.translate("Form", u"LINK ANGULAR JOG", None))
        self.anglular_jog_slider.setProperty(u"settingName", QCoreApplication.translate("Form", u"machine.jog.angular-speed-percentage", None))
        self.fr_angular_override_dro.setText(QCoreApplication.translate("Form", u"30%", None))
        self.fr_angular_override_dro.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"settings:machine.jog.angular-speed-percentage\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{ch[0]}%\\\"\", \"name\": \"angular_jog_slider_dro\"}]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("Form", u"SETTINGS", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><a href=\"https://kcjengr.github.io/probe_basic/update_notes.html\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#0000ff;\">Probe Basic Update Release Notes and Instructions</span></a><span style=\" font-size:14pt; font-weight:600;\"><br/></span></p></body></html>", None))
        self.label_111.setText(QCoreApplication.translate("Form", u"PROBE POS/WCO MODE", None))
        self.probe_mode_3030.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"probe_mode\", \"property\": \"Text\", \"expression\": \"\\\"1\\\" if ch[0] else \\\"0\\\"\", \"channels\": [{\"url\": \"settings:probe-parameters.probe-posn-btn\", \"trigger\": true}]}]", None))
        self.label_112.setText(QCoreApplication.translate("Form", u"WCO ROTATION MODE", None))
        self.wco_rotation_3031.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"wco_rotation_mode\", \"property\": \"Text\", \"expression\": \"\\\"1\\\" if ch[0] else \\\"0\\\"\", \"channels\": [{\"url\": \"settings:probe-parameters.rotation-wco-btn\", \"trigger\": true}]}]", None))
        self.label_115.setText(QCoreApplication.translate("Form", u"X and Y CAL AXIS SELECTION", None))
        self.sq_cal_axis_3036.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"calibration_mode\", \"property\": \"Text\", \"expression\": \"\\\"0\\\" if ch[0] else (\\\"1\\\" if ch[1] else \\\"2\\\")\", \"channels\": [{\"url\": \"settings:probe-parameters.cal-xy-btn\", \"trigger\": true}, {\"url\": \"settings:probe-parameters.cal-x-btn\", \"trigger\": true}]}]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status_tab), QCoreApplication.translate("Form", u"STATUS", None))
        self.label_178.setText(QCoreApplication.translate("Form", u"MACHINE STATUS:", None))
        self.jogDisplay.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"axis_display_rule\", \"property\": \"currentIndex\", \"expression\": \"0 if ch[0] == 'XYZ' else (1 if ch[0] == 'XYZA' else (2 if ch[0] == 'XYZAB' else (3 if ch[0] == 'XYZAC' else (4 if ch[0] == 'XYZBC' else -1))))\", \"channels\": [{\"url\": \"status:axis_mask?string\", \"trigger\": true}]}]", None))
        self.jogDisplay.setProperty(u"settingName", QCoreApplication.translate("Form", u"jog-display.currentIndex", None))
        self.z_plus_jogbutton_3.setText("")
        self.z_plus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_plus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton_3.setText("")
        self.z_minus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_minus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.y_plus_jogbutton_3.setText("")
        self.y_plus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_plus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.x_plus_jogbutton_3.setText("")
        self.x_plus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_plus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.y_minus_jogbutton_3.setText("")
        self.y_minus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_minus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.x_minus_jogbutton_3.setText("")
        self.x_minus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enabled\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_minus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.z_plus_jogbutton_2.setText("")
        self.z_plus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_plus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton_2.setText("")
        self.z_minus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_minus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.x_plus_jogbutton_2.setText("")
        self.x_plus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_plus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.x_minus_jogbutton_2.setText("")
        self.x_minus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_minus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.y_minus_jogbutton_2.setText("")
        self.y_minus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_minus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.y_plus_jogbutton_2.setText("")
        self.y_plus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_plus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.a_minus_jogbutton_2.setText("")
        self.a_minus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_minus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,neg", None))
        self.a_plus_jogbutton_2.setText("")
        self.a_plus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"task_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_plus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,pos", None))
        self.z_plus_jogbutton.setText("")
        self.z_plus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton.setText("")
        self.z_minus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.x_plus_jogbutton.setText("")
        self.x_plus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.x_minus_jogbutton.setText("")
        self.x_minus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.y_minus_jogbutton.setText("")
        self.y_minus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.y_plus_jogbutton.setText("")
        self.y_plus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.a_minus_jogbutton.setText("")
        self.a_minus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,neg", None))
        self.a_plus_jogbutton.setText("")
        self.a_plus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,pos", None))
        self.b_minus_jogbutton.setText("")
        self.b_minus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.b_minus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,neg", None))
        self.b_plus_jogbutton.setText("")
        self.b_plus_jogbutton.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.b_plus_jogbutton.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,pos", None))
        self.z_plus_jogbutton_4.setText("")
        self.z_plus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_plus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton_4.setText("")
        self.z_minus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_minus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.x_plus_jogbutton_4.setText("")
        self.x_plus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_plus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.x_minus_jogbutton_4.setText("")
        self.x_minus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_minus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.y_minus_jogbutton_4.setText("")
        self.y_minus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_minus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.y_plus_jogbutton_4.setText("")
        self.y_plus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_plus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.a_minus_jogbutton_3.setText("")
        self.a_minus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_minus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,neg", None))
        self.a_plus_jogbutton_3.setText("")
        self.a_plus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.a_plus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:a,pos", None))
        self.c_minus_jogbutton_2.setText("")
        self.c_minus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.c_minus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:c,neg", None))
        self.c_plus_jogbutton_2.setText("")
        self.c_plus_jogbutton_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.c_plus_jogbutton_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:c,pos", None))
        self.z_plus_jogbutton_9.setText("")
        self.z_plus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_plus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,pos", None))
        self.z_minus_jogbutton_9.setText("")
        self.z_minus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.z_minus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:z,neg", None))
        self.x_plus_jogbutton_9.setText("")
        self.x_plus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_plus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,pos", None))
        self.x_minus_jogbutton_9.setText("")
        self.x_minus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.x_minus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:x,neg", None))
        self.y_minus_jogbutton_9.setText("")
        self.y_minus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_minus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,neg", None))
        self.y_plus_jogbutton_9.setText("")
        self.y_plus_jogbutton_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.y_plus_jogbutton_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:y,pos", None))
        self.b_minus_jogbutton_3.setText("")
        self.b_minus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.b_minus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,neg", None))
        self.b_plus_jogbutton_3.setText("")
        self.b_plus_jogbutton_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.b_plus_jogbutton_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:b,pos", None))
        self.c_minus_jogbutton_4.setText("")
        self.c_minus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.c_minus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:c,neg", None))
        self.c_plus_jogbutton_4.setText("")
        self.c_plus_jogbutton_4.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"taske_mode_enable\", \"property\": \"Enable\", \"expression\": \"False if ch[0] != 1 else True\", \"channels\": [{\"url\": \"status:task_mode\", \"trigger\": true}]}]", None))
        self.c_plus_jogbutton_4.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.jog.axis:c,pos", None))
        self.actionbutton_g58_3.setText(QCoreApplication.translate("Form", u"G58", None))
        self.actionbutton_g58_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 5\", \"name\": \"g58_offset_status\"}]", None))
        self.actionbutton_g58_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G58", None))
        self.actionbutton_g59_8.setText(QCoreApplication.translate("Form", u"G59.3", None))
        self.actionbutton_g59_8.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 9\", \"name\": \"g59_3_offset_status\"}]", None))
        self.actionbutton_g59_8.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.3", None))
        self.actionbutton_g54_3.setText(QCoreApplication.translate("Form", u"G54", None))
        self.actionbutton_g54_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 1\", \"name\": \"g54_offset_status\"}]", None))
        self.actionbutton_g54_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G54", None))
        self.actionbutton_g56_3.setText(QCoreApplication.translate("Form", u"G56", None))
        self.actionbutton_g56_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 3\", \"name\": \"g56_offset_status\"}]", None))
        self.actionbutton_g56_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G56", None))
        self.actionbutton_g55_3.setText(QCoreApplication.translate("Form", u"G55", None))
        self.actionbutton_g55_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 2\", \"name\": \"g55_offset_status\"}]", None))
        self.actionbutton_g55_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G55", None))
        self.actionbutton_g57_3.setText(QCoreApplication.translate("Form", u"G57", None))
        self.actionbutton_g57_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 4\", \"name\": \"g57_offset_status\"}]", None))
        self.actionbutton_g57_3.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G57", None))
        self.actionbutton_g59_10.setText(QCoreApplication.translate("Form", u"G59", None))
        self.actionbutton_g59_10.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 6\", \"name\": \"g59_offset_status\"}]", None))
        self.actionbutton_g59_10.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59", None))
        self.actionbutton_g59_11.setText(QCoreApplication.translate("Form", u"G59.2", None))
        self.actionbutton_g59_11.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 8\", \"name\": \"g59_2_offset_status\"}]", None))
        self.actionbutton_g59_11.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.2", None))
        self.actionbutton_g59_9.setText(QCoreApplication.translate("Form", u"G59.1", None))
        self.actionbutton_g59_9.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:g5x_index\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 7\", \"name\": \"g59_1_offset_status\"}]", None))
        self.actionbutton_g59_9.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.set-work-coord:G59.1", None))
        self.ref_all_button_2.setText(QCoreApplication.translate("Form", u"UN REF ALL", None))
        self.ref_all_button_2.setProperty(u"rules", QCoreApplication.translate("Form", u"[]", None))
        self.ref_all_button_2.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.unhome.all", None))
        self.axisactionbutton_12.setText(QCoreApplication.translate("Form", u"UN REF X", None))
        self.axisactionbutton_12.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.unhome.axis:x", None))
        self.axisactionbutton_15.setText(QCoreApplication.translate("Form", u"UN REF Y", None))
        self.axisactionbutton_15.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.unhome.axis:y", None))
        self.axisactionbutton_14.setText(QCoreApplication.translate("Form", u"UN REF Z", None))
        self.axisactionbutton_14.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.unhome.axis:z", None))
        self.axisactionbutton_16.setText(QCoreApplication.translate("Form", u"LIMITS OVERRIDE", None))
        self.axisactionbutton_16.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.override_limits", None))
        self.program_boundary_button.setText(QCoreApplication.translate("Form", u"PGM BDRY", None))
        self.program_boundary_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"backplot.show-program-bounds", None))
        self.machine_boundary_button.setText(QCoreApplication.translate("Form", u"MCH BDRY", None))
        self.machine_boundary_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"backplot.show-machine-bounds", None))
        self.plot_grid_button.setText(QCoreApplication.translate("Form", u"PLOT GRID", None))
        self.plot_grid_button.setProperty(u"settingName", QCoreApplication.translate("Form", u"backplot.show-grid", None))
        self.manual_mode_button.setText(QCoreApplication.translate("Form", u"MAN", None))
        self.manual_mode_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.mode.manual", None))
        self.auto_mode_button.setText(QCoreApplication.translate("Form", u"AUTO", None))
        self.auto_mode_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.mode.auto", None))
        self.mdi_mode_button.setText(QCoreApplication.translate("Form", u"MDI", None))
        self.mdi_mode_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.mode.mdi", None))
        self.statuslabel_19.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"active_g_codes\"}]", None))
        self.statuslabel_19.setProperty(u"statusItem", "")
        self.label_186.setText("")
        self.statuslabel_26.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:mcodes?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"active_m_codes\"}]", None))
        self.statuslabel_26.setProperty(u"statusItem", "")
        self.label_185.setText("")
        self.jog_tab.setText(QCoreApplication.translate("Form", u"JOG", None))
        self.wcs_tab.setText(QCoreApplication.translate("Form", u"WCS", None))
        self.plot_tab.setText(QCoreApplication.translate("Form", u"PLOT", None))
        self.user_sb_tab.setText(QCoreApplication.translate("Form", u"USER", None))
        self.cycle_start_button.setText(QCoreApplication.translate("Form", u"CYCLE START", None))
        self.cycle_start_button.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"probe_safety_lockout\", \"property\": \"Enable\", \"expression\": \"False if ch[0]['T'] == 99 else True\", \"channels\": [{\"url\": \"tooltable:current_tool\", \"trigger\": true}]}, {\"name\": \"resume_program\", \"property\": \"Text\", \"expression\": \"'RESUME FEED' if ch[0] else 'CYCLE START'\", \"channels\": [{\"url\": \"status:paused\", \"trigger\": true}]}, {\"name\": \"resume_program_style\", \"property\": \"Style Class\", \"expression\": \"\\\"active\\\" if ch[0] else \\\"inactive\\\"\", \"channels\": [{\"url\": \"status:paused\", \"trigger\": true}]}]", None))
        self.cycle_start_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.run", None))
        self.ref_coilumn_header_25.setText("")
        self.stop_button.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.stop_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"program.abort", None))
        self.power_button.setText(QCoreApplication.translate("Form", u"POWER", None))
        self.power_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.power.toggle", None))
        self.ref_coilumn_header_16.setText("")
        self.timerhours.setText(QCoreApplication.translate("Form", u"00", None))
        self.timerhours.setProperty(u"textFormat", QCoreApplication.translate("Form", u"02d", None))
        self.timerhours.setProperty(u"pinType", QCoreApplication.translate("Form", u"u32", None))
        self.label_2.setText(QCoreApplication.translate("Form", u":", None))
        self.timerminutes.setText(QCoreApplication.translate("Form", u"00", None))
        self.timerminutes.setProperty(u"textFormat", QCoreApplication.translate("Form", u"02d", None))
        self.timerminutes.setProperty(u"pinType", QCoreApplication.translate("Form", u"u32", None))
        self.label_3.setText(QCoreApplication.translate("Form", u":", None))
        self.timerseconds.setText(QCoreApplication.translate("Form", u"00", None))
        self.timerseconds.setProperty(u"textFormat", QCoreApplication.translate("Form", u"02d", None))
        self.timerseconds.setProperty(u"pinType", QCoreApplication.translate("Form", u"u32", None))
        self.ref_coilumn_header_18.setText("")
        self.exit_button.setText(QCoreApplication.translate("Form", u"E-STOP", None))
        self.exit_button.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"estop_button_color\", \"property\": \"Style Sheet\", \"expression\": \"\\\"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255))\\\" if ch[0] else \\\"background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 64, 64, 255), stop:0.446154 rgba(204, 0, 0, 255), stop:0.764103 rgba(225, 67, 67, 255), stop:1 rgba(249, 142, 142, 255))\\\"\", \"channels\": [{\"url\": \"status:estop\", \"trigger\": true}]}]", None))
        self.exit_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.estop.toggle", None))
        self.ref_coilumn_header_3.setText(QCoreApplication.translate("Form", u"  T", None))
        self.tool_number_entry_main_panel.setText(QCoreApplication.translate("Form", u"0", None))
        self.tool_number_entry_main_panel.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?tool_number\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str(ch[0])\", \"name\": \"update tool num\"}, {\"channels\": [{\"url\": \"status:task_state?text\", \"trigger\": true}, {\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] == 'On' and ch[1] == 'Idle'\", \"name\": \"enable/disable\"}]", None))
#if QT_CONFIG(tooltip)
        self.m6_tool_call_button_main_panel.setToolTip(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/probe_cal_round_boss.png\" /><br /><span style=\" font-size:16pt; font-weight:600;\"><br />Probing Button for Boss</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.m6_tool_call_button_main_panel.setText(QCoreApplication.translate("Form", u"M6 G43", None))
        self.m6_tool_call_button_main_panel.setProperty(u"filename", QCoreApplication.translate("Form", u"m6_tool_call_main_panel.ngc", None))
        self.G43.setText(QCoreApplication.translate("Form", u"G43", None))
        self.G43.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"'G43' in ch[0]\", \"name\": \"G43\"}, {\"channels\": [{\"url\": \"status:tool_in_spindle\", \"trigger\": false}, {\"url\": \"status:interp_state\", \"trigger\": true}, {\"url\": \"status:homed\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] != 0\", \"name\": \"disable if no tool loaded\"}]", None))
        self.G43.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G43", None))
        self.G49.setText(QCoreApplication.translate("Form", u"G49", None))
        self.G49.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"'G49' in ch[0]\", \"name\": \"G49\"}]", None))
        self.G49.setProperty(u"MDICommand", QCoreApplication.translate("Form", u"G49", None))
        self.work_column_header_4.setText(QCoreApplication.translate("Form", u"LENGTH", None))
        self.tool_length.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_length.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]", None))
        self.tool_length.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_length.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.statuslabel_8.setProperty(u"rules", QCoreApplication.translate("Form", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:linear_units?text\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"str\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"ch[0]\",\n"
"        \"name\": \"Units\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]", None))
        self.work_column_header_5.setText(QCoreApplication.translate("Form", u"DIAM", None))
        self.tool_diameter.setText(QCoreApplication.translate("Form", u"0.0000", None))
        self.tool_diameter.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == 'in' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]", None))
        self.tool_diameter.setProperty(u"format", QCoreApplication.translate("Form", u"{:.3f}", None))
        self.tool_diameter.setProperty(u"statusItem", QCoreApplication.translate("Form", u"tool_offset.3", None))
        self.statuslabel_11.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:linear_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Units\"}]", None))
        self.go_to_zero_button_2.setText(QCoreApplication.translate("Form", u"GO TO ZERO", None))
        self.go_to_zero_button_2.setProperty(u"filename", QCoreApplication.translate("Form", u"go_to_zero.ngc", None))
        self.go_to_g30_button.setText(QCoreApplication.translate("Form", u"GO TO G30", None))
        self.go_to_g30_button.setProperty(u"filename", QCoreApplication.translate("Form", u"go_to_g30.ngc", None))
        self.go_to_home_button.setText(QCoreApplication.translate("Form", u"GO TO HOME", None))
        self.go_to_home_button.setProperty(u"filename", QCoreApplication.translate("Form", u"go_to_home.ngc", None))
        self.spindel_load_label.setText(QCoreApplication.translate("Form", u"SPINDLE\n"
"LOAD", None))
        self.spindle_override_slider.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.override", None))
        self.feed_override_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:feedrate\", \"trigger\": true}], \"expression\": \"f\\\"{(ch[0]):.0%}\\\"\", \"name\": \"New Rule\", \"property\": \"Text\"}]", None))
        self.spindle_override_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:spindle.0.override\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{(ch[0]):.0%}\\\"\", \"name\": \"New Rule\"}]", None))
        self.rapid_override_slider.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.rapid-override.set", None))
        self.max_velocity_slider.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.max-velocity.set", None))
        self.feed_override_to_100_button.setText(QCoreApplication.translate("Form", u"F 100%", None))
        self.feed_override_to_100_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.feed-override.reset", None))
        self.spindle_override_to_100_button.setText(QCoreApplication.translate("Form", u"S 100%", None))
        self.spindle_override_to_100_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.override.reset", None))
        self.spindle_load_indicator.setProperty(u"sufix", QCoreApplication.translate("Form", u"%", None))
        self.spindle_load_indicator.setProperty(u"format", QCoreApplication.translate("Form", u".0f", None))
        self.spindle_load_indicator.setProperty(u"barGradient", [
            QCoreApplication.translate("Form", u"0.0, 170, 170, 236", None),
            QCoreApplication.translate("Form", u"0.63, 85, 85, 238", None),
            QCoreApplication.translate("Form", u"0.65, 171, 171, 158", None),
            QCoreApplication.translate("Form", u"0.79, 227, 237, 106", None),
            QCoreApplication.translate("Form", u"0.84, 219, 124, 55", None),
            QCoreApplication.translate("Form", u"1.0, 209, 0, 0", None)])
        self.rapid_override_to_100_button.setText(QCoreApplication.translate("Form", u"R 100%", None))
        self.rapid_override_to_100_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.rapid-override.reset", None))
        self.max_vel_slider.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:max_velocity\", \"trigger\": true}], \"expression\": \"f\\\"{(ch[0] * 60):.0f}\\\"\", \"name\": \"New Rule\", \"property\": \"Text\"}]", None))
        self.max_velocity_to_100_button.setText(QCoreApplication.translate("Form", u"V 100%", None))
        self.max_velocity_to_100_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.max-velocity.reset", None))
        self.rapid_override_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:rapidrate\", \"trigger\": true}], \"expression\": \"f\\\"{(ch[0]):.0%}\\\"\", \"name\": \"New Rule\", \"property\": \"Text\"}]", None))
        self.feed_override_slider.setProperty(u"actionName", QCoreApplication.translate("Form", u"machine.feed-override.set", None))
        self.linear_jog_slider.setProperty(u"settingName", QCoreApplication.translate("Form", u"machine.jog.linear-speed-percentage", None))
        self.fr_override_dro.setText(QCoreApplication.translate("Form", u"30%", None))
        self.fr_override_dro.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"settings:machine.jog.linear-speed-percentage\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{ch[0]}%\\\"\", \"name\": \"linear_jog_slider_dro\"}]", None))
        self.current_velocity_status.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.current_velocity_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:current_vel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{(ch[0] * 60):.1f}\\\"\", \"name\": \"cur vel\"}]", None))
        self.current_velocity_status.setProperty(u"format", QCoreApplication.translate("Form", u"{:.1f}", None))
        self.feedrate_label_1.setText(QCoreApplication.translate("Form", u"FEEDRATE", None))
        self.feedrate_label_2.setText("")
        self.feedrate_label_3.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:program_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Linear Units\"}]", None))
        self.feedrate_label_3.setProperty(u"fromat", "")
        self.feedrate_label_4.setText(QCoreApplication.translate("Form", u"/M", None))
        self.f_word_status.setText(QCoreApplication.translate("Form", u"0.0", None))
        self.f_word_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:settings\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{ch[0][1]:.1f}\\\"\", \"name\": \"F Word\"}]", None))
        self.f_word_status.setProperty(u"format", QCoreApplication.translate("Form", u"{:1f}", None))
        self.spindle_stat_rpm.setText(QCoreApplication.translate("Form", u"0", None))
        self.spindle_stat_rpm.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:spindle.0.speed\", \"trigger\": true}, {\"url\": \"status:spindle.0.override\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{(ch[0] * ch[1]):.0f}\\\"\", \"name\": \"Speed\"}]", None))
        self.spindle_encoder_rpm1.setText(QCoreApplication.translate("Form", u"0", None))
        self.spindle_encoder_rpm1.setProperty(u"pinBaseName", QCoreApplication.translate("Form", u"spindle-encoder-rpm", None))
        self.spindle_encoder_rpm1.setProperty(u"textFormat", QCoreApplication.translate("Form", u".0f", None))
        self.spindle_encoder_rpm1.setProperty(u"pinType", QCoreApplication.translate("Form", u"float", None))
        self.rpm_label.setText(QCoreApplication.translate("Form", u"SPINDLE RPM", None))
        self.s_word_status.setText(QCoreApplication.translate("Form", u"0", None))
        self.s_word_status.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"channels\": [{\"url\": \"status:settings?speed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"f\\\"{ch[0]:.0f}\\\"\", \"name\": \"S Word\"}]", None))
        self.s_word_status.setProperty(u"format", QCoreApplication.translate("Form", u".0f", None))
        self.spindle_reverse_button.setText(QCoreApplication.translate("Form", u"REV", None))
        self.spindle_reverse_button.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"spindle_probe_safety\", \"property\": \"Enable\", \"expression\": \"False if ch[0]==99 else True\", \"channels\": [{\"url\": \"tooltable:current_tool?T\", \"trigger\": true}]}]", None))
        self.spindle_reverse_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.reverse", None))
        self.spindle_off_button.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.spindle_off_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.off", None))
        self.spindle_forward_button.setText(QCoreApplication.translate("Form", u"FWD", None))
        self.spindle_forward_button.setProperty(u"rules", QCoreApplication.translate("Form", u"[{\"name\": \"Spindle_probe_safety\", \"property\": \"Enable\", \"expression\": \"False if ch[0]==99 else True\", \"channels\": [{\"url\": \"tooltable:current_tool?T\", \"trigger\": true}]}]", None))
        self.spindle_forward_button.setProperty(u"actionName", QCoreApplication.translate("Form", u"spindle.forward", None))
        self.menuExit.setTitle(QCoreApplication.translate("Form", u"File", None))
        self.menuRecentFiles.setTitle(QCoreApplication.translate("Form", u"Recent &Files", None))
        self.menuMachine.setTitle(QCoreApplication.translate("Form", u"Machine", None))
        self.menuHoming.setTitle(QCoreApplication.translate("Form", u"Homing", None))
        self.menuCooling.setTitle(QCoreApplication.translate("Form", u"Cooling", None))
        self.menuView.setTitle(QCoreApplication.translate("Form", u"View", None))
    # retranslateUi

