# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/turboss/Proyectos/qtpyvcp/examples/probe_basic/probe_basic_vertical.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1924, 1083)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(11)
        Form.setFont(font)
        Form.setToolTipDuration(-1)
        Form.setStyleSheet("Form {\n"
"bottom-margin: 0px;\n"
"}")
        Form.setDocumentMode(False)
        Form.setProperty("promptAtExit", False)
        Form.setProperty("promot_on_exit", False)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_101.setContentsMargins(-1, -1, 0, 3)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 133, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 141, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_24 = QtWidgets.QFrame(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QtCore.QSize(1, 0))
        self.frame_24.setMaximumSize(QtCore.QSize(1, 16777215))
        self.frame_24.setStyleSheet("QFrame{\n"
"border: none;\n"
"background-color: transparent;\n"
"}")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout.addWidget(self.frame_24)
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setFocusPolicy(QtCore.Qt.NoFocus)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recentfilecombobox = RecentFileComboBox(self.verticalLayoutWidget)
        self.recentfilecombobox.setMinimumSize(QtCore.QSize(148, 30))
        self.recentfilecombobox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.recentfilecombobox.setStyleSheet("QComboBox {\n"
"    border: 1px solid black;\n"
"    border-radius: 3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    padding: 1px 23px 1px 3px;\n"
"    min-width: 6em;\n"
"    color: #ffffff;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"     border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"QComboBox::down-arrow {\n"
"     image: url(:/images/combobox-arrow.png);\n"
"}\n"
" \n"
"QComboBox QAbstractItemView{\n"
"    background-color: #4f4f4f;\n"
"    color: #999999;\n"
"     selection-background-color: #999999;\n"
"    selection-color: #4f4f4f;\n"
"}")
        self.recentfilecombobox.setProperty("resource", "")
        self.recentfilecombobox.setObjectName("recentfilecombobox")
        self.verticalLayout_2.addWidget(self.recentfilecombobox)
        self.gcodeeditor = GcodeEditor(self.verticalLayoutWidget)
        self.gcodeeditor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gcodeeditor.setObjectName("gcodeeditor")
        self.verticalLayout_2.addWidget(self.gcodeeditor)
        self.mdi_entry_box = MDIEntry(self.verticalLayoutWidget)
        self.mdi_entry_box.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.mdi_entry_box.setFont(font)
        self.mdi_entry_box.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mdi_entry_box.setObjectName("mdi_entry_box")
        self.verticalLayout_2.addWidget(self.mdi_entry_box)
        self.gcodebackplot = GcodeBackplot(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gcodebackplot.sizePolicy().hasHeightForWidth())
        self.gcodebackplot.setSizePolicy(sizePolicy)
        self.gcodebackplot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gcodebackplot.setProperty("renderProgramAlpha", True)
        self.gcodebackplot.setBackgroundColor(QtGui.QColor(0, 0, 0))
        self.gcodebackplot.setObjectName("gcodebackplot")
        self.horizontalLayout.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_15)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_120 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_120.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_120.setContentsMargins(15, 20, 15, 20)
        self.horizontalLayout_120.setSpacing(15)
        self.horizontalLayout_120.setObjectName("horizontalLayout_120")
        self.frame_35 = QtWidgets.QFrame(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_35.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_35.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.horizontalLayout_124 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_124.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_124.setObjectName("horizontalLayout_124")
        self.x_axis_button_30 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_30.sizePolicy().hasHeightForWidth())
        self.x_axis_button_30.setSizePolicy(sizePolicy)
        self.x_axis_button_30.setMinimumSize(QtCore.QSize(110, 30))
        self.x_axis_button_30.setMaximumSize(QtCore.QSize(110, 30))
        self.x_axis_button_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_30.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/folder_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_axis_button_30.setIcon(icon)
        self.x_axis_button_30.setIconSize(QtCore.QSize(30, 17))
        self.x_axis_button_30.setObjectName("x_axis_button_30")
        self.horizontalLayout_124.addWidget(self.x_axis_button_30)
        self.removabledevicecombobox = RemovableDeviceComboBox(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removabledevicecombobox.sizePolicy().hasHeightForWidth())
        self.removabledevicecombobox.setSizePolicy(sizePolicy)
        self.removabledevicecombobox.setMinimumSize(QtCore.QSize(0, 30))
        self.removabledevicecombobox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.removabledevicecombobox.setObjectName("removabledevicecombobox")
        self.horizontalLayout_124.addWidget(self.removabledevicecombobox)
        self.x_axis_button_32 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_32.sizePolicy().hasHeightForWidth())
        self.x_axis_button_32.setSizePolicy(sizePolicy)
        self.x_axis_button_32.setMinimumSize(QtCore.QSize(100, 30))
        self.x_axis_button_32.setMaximumSize(QtCore.QSize(100, 30))
        self.x_axis_button_32.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_32.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_32.setObjectName("x_axis_button_32")
        self.horizontalLayout_124.addWidget(self.x_axis_button_32)
        self.verticalLayout_37.addLayout(self.horizontalLayout_124)
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.filesystemtable_2 = FileSystemTable(self.frame_35)
        self.filesystemtable_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filesystemtable_2.setStyleSheet("FileSystemTable {\n"
"    color: black;\n"
"       border: 4px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius:none;\n"
"    border-style: none;\n"
"    font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filesystemtable_2.setShowGrid(False)
        self.filesystemtable_2.setObjectName("filesystemtable_2")
        self.horizontalLayout_125.addWidget(self.filesystemtable_2)
        self.verticalLayout_37.addLayout(self.horizontalLayout_125)
        self.horizontalLayout_126 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_126.setObjectName("horizontalLayout_126")
        self.x_axis_button_33 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_33.sizePolicy().hasHeightForWidth())
        self.x_axis_button_33.setSizePolicy(sizePolicy)
        self.x_axis_button_33.setMinimumSize(QtCore.QSize(90, 30))
        self.x_axis_button_33.setMaximumSize(QtCore.QSize(90, 30))
        self.x_axis_button_33.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_33.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_axis_button_33.setIcon(icon1)
        self.x_axis_button_33.setIconSize(QtCore.QSize(14, 14))
        self.x_axis_button_33.setObjectName("x_axis_button_33")
        self.horizontalLayout_126.addWidget(self.x_axis_button_33)
        self.x_axis_button_37 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_37.sizePolicy().hasHeightForWidth())
        self.x_axis_button_37.setSizePolicy(sizePolicy)
        self.x_axis_button_37.setMinimumSize(QtCore.QSize(100, 30))
        self.x_axis_button_37.setMaximumSize(QtCore.QSize(100, 30))
        self.x_axis_button_37.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_37.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/new_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_axis_button_37.setIcon(icon2)
        self.x_axis_button_37.setIconSize(QtCore.QSize(12, 16))
        self.x_axis_button_37.setObjectName("x_axis_button_37")
        self.horizontalLayout_126.addWidget(self.x_axis_button_37)
        self.x_axis_button_35 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_35.sizePolicy().hasHeightForWidth())
        self.x_axis_button_35.setSizePolicy(sizePolicy)
        self.x_axis_button_35.setMinimumSize(QtCore.QSize(125, 30))
        self.x_axis_button_35.setMaximumSize(QtCore.QSize(125, 30))
        self.x_axis_button_35.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_35.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/new_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_axis_button_35.setIcon(icon3)
        self.x_axis_button_35.setIconSize(QtCore.QSize(28, 15))
        self.x_axis_button_35.setObjectName("x_axis_button_35")
        self.horizontalLayout_126.addWidget(self.x_axis_button_35)
        self.x_axis_button_34 = QtWidgets.QPushButton(self.frame_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_34.sizePolicy().hasHeightForWidth())
        self.x_axis_button_34.setSizePolicy(sizePolicy)
        self.x_axis_button_34.setMinimumSize(QtCore.QSize(90, 30))
        self.x_axis_button_34.setMaximumSize(QtCore.QSize(90, 30))
        self.x_axis_button_34.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_34.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_34.setObjectName("x_axis_button_34")
        self.horizontalLayout_126.addWidget(self.x_axis_button_34)
        self.verticalLayout_37.addLayout(self.horizontalLayout_126)
        self.horizontalLayout_120.addWidget(self.frame_35)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_36.setContentsMargins(0, 110, 0, 100)
        self.verticalLayout_36.setSpacing(15)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.copy_from_usb_2 = QtWidgets.QPushButton(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_from_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_from_usb_2.setSizePolicy(sizePolicy)
        self.copy_from_usb_2.setMinimumSize(QtCore.QSize(60, 90))
        self.copy_from_usb_2.setMaximumSize(QtCore.QSize(60, 90))
        self.copy_from_usb_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.copy_from_usb_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.copy_from_usb_2.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"    padding-right: 4px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/tall_right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_from_usb_2.setIcon(icon4)
        self.copy_from_usb_2.setIconSize(QtCore.QSize(18, 60))
        self.copy_from_usb_2.setObjectName("copy_from_usb_2")
        self.verticalLayout_36.addWidget(self.copy_from_usb_2)
        self.copy_to_usb_2 = QtWidgets.QPushButton(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_to_usb_2.sizePolicy().hasHeightForWidth())
        self.copy_to_usb_2.setSizePolicy(sizePolicy)
        self.copy_to_usb_2.setMinimumSize(QtCore.QSize(60, 90))
        self.copy_to_usb_2.setMaximumSize(QtCore.QSize(60, 90))
        self.copy_to_usb_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.copy_to_usb_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.copy_to_usb_2.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"    padding-right: 8px;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/tall_left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_to_usb_2.setIcon(icon5)
        self.copy_to_usb_2.setIconSize(QtCore.QSize(28, 60))
        self.copy_to_usb_2.setObjectName("copy_to_usb_2")
        self.verticalLayout_36.addWidget(self.copy_to_usb_2)
        self.horizontalLayout_120.addLayout(self.verticalLayout_36)
        self.frame_34 = QtWidgets.QFrame(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_34.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_34.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.horizontalLayout_121 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_121.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_121.setObjectName("horizontalLayout_121")
        self.x_axis_button_23 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_23.sizePolicy().hasHeightForWidth())
        self.x_axis_button_23.setSizePolicy(sizePolicy)
        self.x_axis_button_23.setMinimumSize(QtCore.QSize(110, 30))
        self.x_axis_button_23.setMaximumSize(QtCore.QSize(110, 30))
        self.x_axis_button_23.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_23.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_23.setIcon(icon)
        self.x_axis_button_23.setIconSize(QtCore.QSize(30, 17))
        self.x_axis_button_23.setObjectName("x_axis_button_23")
        self.horizontalLayout_121.addWidget(self.x_axis_button_23)
        self.recentfilecombobox_2 = RecentFileComboBox(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentfilecombobox_2.sizePolicy().hasHeightForWidth())
        self.recentfilecombobox_2.setSizePolicy(sizePolicy)
        self.recentfilecombobox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.recentfilecombobox_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.recentfilecombobox_2.setObjectName("recentfilecombobox_2")
        self.horizontalLayout_121.addWidget(self.recentfilecombobox_2)
        self.x_axis_button_26 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_26.sizePolicy().hasHeightForWidth())
        self.x_axis_button_26.setSizePolicy(sizePolicy)
        self.x_axis_button_26.setMinimumSize(QtCore.QSize(100, 30))
        self.x_axis_button_26.setMaximumSize(QtCore.QSize(100, 30))
        self.x_axis_button_26.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_26.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_26.setObjectName("x_axis_button_26")
        self.horizontalLayout_121.addWidget(self.x_axis_button_26)
        self.verticalLayout_35.addLayout(self.horizontalLayout_121)
        self.horizontalLayout_122 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_122.setObjectName("horizontalLayout_122")
        self.filesystemtable = FileSystemTable(self.frame_34)
        self.filesystemtable.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.filesystemtable.setStyleSheet("FileSystemTable {\n"
"    color: black;\n"
"       border: 4px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius:none;\n"
"    border-style: none;\n"
"    font: 13pt \"Bebas Kai\";\n"
"}")
        self.filesystemtable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filesystemtable.setShowGrid(False)
        self.filesystemtable.setObjectName("filesystemtable")
        self.horizontalLayout_122.addWidget(self.filesystemtable)
        self.verticalLayout_35.addLayout(self.horizontalLayout_122)
        self.horizontalLayout_123 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_123.setObjectName("horizontalLayout_123")
        self.x_axis_button_27 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_27.sizePolicy().hasHeightForWidth())
        self.x_axis_button_27.setSizePolicy(sizePolicy)
        self.x_axis_button_27.setMinimumSize(QtCore.QSize(90, 30))
        self.x_axis_button_27.setMaximumSize(QtCore.QSize(90, 30))
        self.x_axis_button_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_27.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_27.setIcon(icon1)
        self.x_axis_button_27.setIconSize(QtCore.QSize(14, 14))
        self.x_axis_button_27.setObjectName("x_axis_button_27")
        self.horizontalLayout_123.addWidget(self.x_axis_button_27)
        self.x_axis_button_31 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_31.sizePolicy().hasHeightForWidth())
        self.x_axis_button_31.setSizePolicy(sizePolicy)
        self.x_axis_button_31.setMinimumSize(QtCore.QSize(100, 30))
        self.x_axis_button_31.setMaximumSize(QtCore.QSize(100, 30))
        self.x_axis_button_31.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_31.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_31.setIcon(icon2)
        self.x_axis_button_31.setIconSize(QtCore.QSize(12, 16))
        self.x_axis_button_31.setObjectName("x_axis_button_31")
        self.horizontalLayout_123.addWidget(self.x_axis_button_31)
        self.x_axis_button_29 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_29.sizePolicy().hasHeightForWidth())
        self.x_axis_button_29.setSizePolicy(sizePolicy)
        self.x_axis_button_29.setMinimumSize(QtCore.QSize(125, 30))
        self.x_axis_button_29.setMaximumSize(QtCore.QSize(125, 30))
        self.x_axis_button_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_29.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_29.setIcon(icon3)
        self.x_axis_button_29.setIconSize(QtCore.QSize(28, 15))
        self.x_axis_button_29.setObjectName("x_axis_button_29")
        self.horizontalLayout_123.addWidget(self.x_axis_button_29)
        self.x_axis_button_28 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_28.sizePolicy().hasHeightForWidth())
        self.x_axis_button_28.setSizePolicy(sizePolicy)
        self.x_axis_button_28.setMinimumSize(QtCore.QSize(90, 30))
        self.x_axis_button_28.setMaximumSize(QtCore.QSize(90, 30))
        self.x_axis_button_28.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_28.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_28.setObjectName("x_axis_button_28")
        self.horizontalLayout_123.addWidget(self.x_axis_button_28)
        self.verticalLayout_35.addLayout(self.horizontalLayout_123)
        self.horizontalLayout_120.addWidget(self.frame_34)
        self.frame_36 = QtWidgets.QFrame(self.tab_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.horizontalLayout_127 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_127.setObjectName("horizontalLayout_127")
        self.work_column_header_8 = QtWidgets.QLabel(self.frame_36)
        self.work_column_header_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_8.sizePolicy().hasHeightForWidth())
        self.work_column_header_8.setSizePolicy(sizePolicy)
        self.work_column_header_8.setMinimumSize(QtCore.QSize(200, 30))
        self.work_column_header_8.setMaximumSize(QtCore.QSize(200, 30))
        self.work_column_header_8.setStyleSheet("QLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(238, 238, 236);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_8.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_8.setObjectName("work_column_header_8")
        self.horizontalLayout_127.addWidget(self.work_column_header_8)
        self.verticalLayout_38.addLayout(self.horizontalLayout_127)
        self.horizontalLayout_128 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_128.setObjectName("horizontalLayout_128")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_36)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    color: black;\n"
"       border: 4px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(238, 238, 236);\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_128.addWidget(self.plainTextEdit)
        self.verticalLayout_38.addLayout(self.horizontalLayout_128)
        self.horizontalLayout_129 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.x_axis_button_36 = QtWidgets.QPushButton(self.frame_36)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_36.sizePolicy().hasHeightForWidth())
        self.x_axis_button_36.setSizePolicy(sizePolicy)
        self.x_axis_button_36.setMinimumSize(QtCore.QSize(150, 30))
        self.x_axis_button_36.setMaximumSize(QtCore.QSize(150, 30))
        self.x_axis_button_36.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_36.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_36.setObjectName("x_axis_button_36")
        self.horizontalLayout_129.addWidget(self.x_axis_button_36)
        self.verticalLayout_38.addLayout(self.horizontalLayout_129)
        self.horizontalLayout_120.addWidget(self.frame_36)
        self.verticalLayout_5.addLayout(self.horizontalLayout_120)
        self.tabWidget.addTab(self.tab_15, "")
        self.status_tab = QtWidgets.QWidget()
        self.status_tab.setObjectName("status_tab")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.status_tab)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(12, -1, -1, -1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_33 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setMinimumSize(QtCore.QSize(360, 550))
        self.frame_33.setMaximumSize(QtCore.QSize(360, 550))
        self.frame_33.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_113 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_113.setSpacing(0)
        self.horizontalLayout_113.setObjectName("horizontalLayout_113")
        self.machine_column_header_9 = QtWidgets.QLabel(self.frame_33)
        self.machine_column_header_9.setMinimumSize(QtCore.QSize(0, 50))
        self.machine_column_header_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_9.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_9.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_9.setObjectName("machine_column_header_9")
        self.horizontalLayout_113.addWidget(self.machine_column_header_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_113)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_33)
        self.lineEdit_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(130, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_11.addWidget(self.lineEdit_3)
        self.m01_break_button_4 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_4.sizePolicy().hasHeightForWidth())
        self.m01_break_button_4.setSizePolicy(sizePolicy)
        self.m01_break_button_4.setMinimumSize(QtCore.QSize(130, 45))
        self.m01_break_button_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_4.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_4.setObjectName("m01_break_button_4")
        self.horizontalLayout_11.addWidget(self.m01_break_button_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_114 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_114.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_114.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_114.setSpacing(15)
        self.horizontalLayout_114.setObjectName("horizontalLayout_114")
        self.m01_break_button_8 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_8.sizePolicy().hasHeightForWidth())
        self.m01_break_button_8.setSizePolicy(sizePolicy)
        self.m01_break_button_8.setMinimumSize(QtCore.QSize(130, 45))
        self.m01_break_button_8.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_8.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_8.setObjectName("m01_break_button_8")
        self.horizontalLayout_114.addWidget(self.m01_break_button_8)
        self.m01_break_button_9 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_9.sizePolicy().hasHeightForWidth())
        self.m01_break_button_9.setSizePolicy(sizePolicy)
        self.m01_break_button_9.setMinimumSize(QtCore.QSize(130, 45))
        self.m01_break_button_9.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_9.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_9.setObjectName("m01_break_button_9")
        self.horizontalLayout_114.addWidget(self.m01_break_button_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_114)
        self.horizontalLayout_115 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_115.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_115.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_115.setSpacing(15)
        self.horizontalLayout_115.setObjectName("horizontalLayout_115")
        self.subcallbutton_9 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_9.sizePolicy().hasHeightForWidth())
        self.subcallbutton_9.setSizePolicy(sizePolicy)
        self.subcallbutton_9.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_9.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_9.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/ccw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subcallbutton_9.setIcon(icon6)
        self.subcallbutton_9.setIconSize(QtCore.QSize(20, 20))
        self.subcallbutton_9.setObjectName("subcallbutton_9")
        self.horizontalLayout_115.addWidget(self.subcallbutton_9)
        self.subcallbutton_3 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_3.sizePolicy().hasHeightForWidth())
        self.subcallbutton_3.setSizePolicy(sizePolicy)
        self.subcallbutton_3.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_3.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.subcallbutton_3.setStyleSheet("SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 28px;\n"
"       font: 16pt \"Bebas Kai\";\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/cw_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subcallbutton_3.setIcon(icon7)
        self.subcallbutton_3.setIconSize(QtCore.QSize(20, 20))
        self.subcallbutton_3.setObjectName("subcallbutton_3")
        self.horizontalLayout_115.addWidget(self.subcallbutton_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_115)
        self.horizontalLayout_116 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_116.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_116.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_116.setSpacing(15)
        self.horizontalLayout_116.setObjectName("horizontalLayout_116")
        self.subcallbutton_10 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_10.sizePolicy().hasHeightForWidth())
        self.subcallbutton_10.setSizePolicy(sizePolicy)
        self.subcallbutton_10.setMinimumSize(QtCore.QSize(10, 45))
        self.subcallbutton_10.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_10.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subcallbutton_10.setIcon(icon8)
        self.subcallbutton_10.setObjectName("subcallbutton_10")
        self.horizontalLayout_116.addWidget(self.subcallbutton_10)
        self.subcallbutton_11 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_11.sizePolicy().hasHeightForWidth())
        self.subcallbutton_11.setSizePolicy(sizePolicy)
        self.subcallbutton_11.setMinimumSize(QtCore.QSize(10, 45))
        self.subcallbutton_11.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.subcallbutton_11.setStyleSheet("SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 22px;\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subcallbutton_11.setIcon(icon9)
        self.subcallbutton_11.setObjectName("subcallbutton_11")
        self.horizontalLayout_116.addWidget(self.subcallbutton_11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_116)
        self.horizontalLayout_117 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_117.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_117.setSpacing(15)
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.subcallbutton_12 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_12.sizePolicy().hasHeightForWidth())
        self.subcallbutton_12.setSizePolicy(sizePolicy)
        self.subcallbutton_12.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_12.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_12.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.subcallbutton_12.setObjectName("subcallbutton_12")
        self.horizontalLayout_117.addWidget(self.subcallbutton_12)
        self.subcallbutton_13 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_13.sizePolicy().hasHeightForWidth())
        self.subcallbutton_13.setSizePolicy(sizePolicy)
        self.subcallbutton_13.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_13.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_13.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.subcallbutton_13.setObjectName("subcallbutton_13")
        self.horizontalLayout_117.addWidget(self.subcallbutton_13)
        self.verticalLayout_7.addLayout(self.horizontalLayout_117)
        self.horizontalLayout_118 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_118.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_118.setSpacing(15)
        self.horizontalLayout_118.setObjectName("horizontalLayout_118")
        self.m01_break_button_10 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_10.sizePolicy().hasHeightForWidth())
        self.m01_break_button_10.setSizePolicy(sizePolicy)
        self.m01_break_button_10.setMinimumSize(QtCore.QSize(130, 45))
        self.m01_break_button_10.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_10.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_10.setObjectName("m01_break_button_10")
        self.horizontalLayout_118.addWidget(self.m01_break_button_10)
        self.m01_break_button_27 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_27.sizePolicy().hasHeightForWidth())
        self.m01_break_button_27.setSizePolicy(sizePolicy)
        self.m01_break_button_27.setMinimumSize(QtCore.QSize(130, 45))
        self.m01_break_button_27.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_27.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_27.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_27.setObjectName("m01_break_button_27")
        self.horizontalLayout_118.addWidget(self.m01_break_button_27)
        self.verticalLayout_7.addLayout(self.horizontalLayout_118)
        self.horizontalLayout_119 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_119.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_119.setSpacing(15)
        self.horizontalLayout_119.setObjectName("horizontalLayout_119")
        self.subcallbutton_14 = SubCallButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_14.sizePolicy().hasHeightForWidth())
        self.subcallbutton_14.setSizePolicy(sizePolicy)
        self.subcallbutton_14.setMinimumSize(QtCore.QSize(135, 45))
        self.subcallbutton_14.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_14.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.subcallbutton_14.setObjectName("subcallbutton_14")
        self.horizontalLayout_119.addWidget(self.subcallbutton_14)
        self.m01_break_button_14 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_14.sizePolicy().hasHeightForWidth())
        self.m01_break_button_14.setSizePolicy(sizePolicy)
        self.m01_break_button_14.setMinimumSize(QtCore.QSize(60, 45))
        self.m01_break_button_14.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_14.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_14.setObjectName("m01_break_button_14")
        self.horizontalLayout_119.addWidget(self.m01_break_button_14)
        self.m01_break_button_15 = ActionButton(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_15.sizePolicy().hasHeightForWidth())
        self.m01_break_button_15.setSizePolicy(sizePolicy)
        self.m01_break_button_15.setMinimumSize(QtCore.QSize(60, 45))
        self.m01_break_button_15.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_15.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_15.setStyleSheet("QPushButton {\n"
"       font: 20pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_15.setObjectName("m01_break_button_15")
        self.horizontalLayout_119.addWidget(self.m01_break_button_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout_119)
        self.verticalLayout_18.addWidget(self.frame_33)
        self.mdi_entry_box_3 = MDIEntry(self.status_tab)
        self.mdi_entry_box_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.mdi_entry_box_3.setFont(font)
        self.mdi_entry_box_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mdi_entry_box_3.setObjectName("mdi_entry_box_3")
        self.verticalLayout_18.addWidget(self.mdi_entry_box_3)
        self.horizontalLayout_36.addLayout(self.verticalLayout_18)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.frame_22 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_49.addWidget(self.frame_22)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_49)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_4 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(863, 521))
        self.frame_4.setMaximumSize(QtCore.QSize(883, 521))
        self.frame_4.setStyleSheet("QFrame{\n"
"border: none;\n"
"border-color: Transparent;\n"
"background-color:transparent;\n"
"border-width: 2px;\n"
"border-radius: 8px;\n"
"}")
        self.frame_4.setObjectName("frame_4")
        self.widget_3 = QtWidgets.QWidget(self.frame_4)
        self.widget_3.setGeometry(QtCore.QRect(10, 9, 500, 500))
        self.widget_3.setObjectName("widget_3")
        self.label_53 = QtWidgets.QLabel(self.widget_3)
        self.label_53.setGeometry(QtCore.QRect(3, 3, 500, 500))
        self.label_53.setStyleSheet("image: url(:/images/carousel_12.png);")
        self.label_53.setText("")
        self.label_53.setScaledContents(True)
        self.label_53.setIndent(0)
        self.label_53.setObjectName("label_53")
        self.label_60 = QtWidgets.QLabel(self.widget_3)
        self.label_60.setGeometry(QtCore.QRect(158, 353, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QtCore.QSize(0, 0))
        self.label_60.setMaximumSize(QtCore.QSize(100, 100))
        self.label_60.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setIndent(0)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.widget_3)
        self.label_61.setGeometry(QtCore.QRect(112, 34, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QtCore.QSize(0, 0))
        self.label_61.setMaximumSize(QtCore.QSize(100, 100))
        self.label_61.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setIndent(0)
        self.label_61.setObjectName("label_61")
        self.label_67 = QtWidgets.QLabel(self.widget_3)
        self.label_67.setGeometry(QtCore.QRect(403, 112, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setMinimumSize(QtCore.QSize(0, 0))
        self.label_67.setMaximumSize(QtCore.QSize(100, 100))
        self.label_67.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setIndent(0)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.widget_3)
        self.label_68.setGeometry(QtCore.QRect(33, 324, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy)
        self.label_68.setMinimumSize(QtCore.QSize(0, 0))
        self.label_68.setMaximumSize(QtCore.QSize(100, 100))
        self.label_68.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setIndent(0)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.widget_3)
        self.label_69.setGeometry(QtCore.QRect(353, 158, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        self.label_69.setMinimumSize(QtCore.QSize(0, 0))
        self.label_69.setMaximumSize(QtCore.QSize(100, 100))
        self.label_69.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setIndent(0)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.widget_3)
        self.label_70.setGeometry(QtCore.QRect(302, 108, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMinimumSize(QtCore.QSize(0, 0))
        self.label_70.setMaximumSize(QtCore.QSize(100, 100))
        self.label_70.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setIndent(0)
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.widget_3)
        self.label_71.setGeometry(QtCore.QRect(218, 429, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy)
        self.label_71.setMinimumSize(QtCore.QSize(0, 0))
        self.label_71.setMaximumSize(QtCore.QSize(100, 100))
        self.label_71.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setIndent(0)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.widget_3)
        self.label_72.setGeometry(QtCore.QRect(304, 353, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QtCore.QSize(0, 0))
        self.label_72.setMaximumSize(QtCore.QSize(100, 100))
        self.label_72.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setIndent(0)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.widget_3)
        self.label_73.setGeometry(QtCore.QRect(218, 6, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(0, 0))
        self.label_73.setMaximumSize(QtCore.QSize(100, 100))
        self.label_73.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setIndent(0)
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.widget_3)
        self.label_74.setGeometry(QtCore.QRect(162, 107, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setMinimumSize(QtCore.QSize(0, 0))
        self.label_74.setMaximumSize(QtCore.QSize(100, 100))
        self.label_74.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setIndent(0)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.widget_3)
        self.label_75.setGeometry(QtCore.QRect(373, 229, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setMinimumSize(QtCore.QSize(0, 0))
        self.label_75.setMaximumSize(QtCore.QSize(100, 100))
        self.label_75.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setIndent(0)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.widget_3)
        self.label_76.setGeometry(QtCore.QRect(109, 158, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setMinimumSize(QtCore.QSize(0, 0))
        self.label_76.setMaximumSize(QtCore.QSize(100, 100))
        self.label_76.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setIndent(0)
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.widget_3)
        self.label_77.setGeometry(QtCore.QRect(324, 35, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setMinimumSize(QtCore.QSize(0, 0))
        self.label_77.setMaximumSize(QtCore.QSize(100, 100))
        self.label_77.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setIndent(0)
        self.label_77.setObjectName("label_77")
        self.label_78 = QtWidgets.QLabel(self.widget_3)
        self.label_78.setGeometry(QtCore.QRect(430, 217, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setMinimumSize(QtCore.QSize(0, 0))
        self.label_78.setMaximumSize(QtCore.QSize(100, 100))
        self.label_78.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setIndent(0)
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.widget_3)
        self.label_79.setGeometry(QtCore.QRect(34, 112, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setMinimumSize(QtCore.QSize(0, 0))
        self.label_79.setMaximumSize(QtCore.QSize(100, 100))
        self.label_79.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setIndent(0)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.widget_3)
        self.label_80.setGeometry(QtCore.QRect(231, 89, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy)
        self.label_80.setMinimumSize(QtCore.QSize(0, 0))
        self.label_80.setMaximumSize(QtCore.QSize(100, 100))
        self.label_80.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setIndent(0)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.widget_3)
        self.label_81.setGeometry(QtCore.QRect(112, 401, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy)
        self.label_81.setMinimumSize(QtCore.QSize(0, 0))
        self.label_81.setMaximumSize(QtCore.QSize(100, 100))
        self.label_81.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setIndent(0)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.widget_3)
        self.label_82.setGeometry(QtCore.QRect(108, 301, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy)
        self.label_82.setMinimumSize(QtCore.QSize(0, 0))
        self.label_82.setMaximumSize(QtCore.QSize(100, 100))
        self.label_82.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setIndent(0)
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.widget_3)
        self.label_83.setGeometry(QtCore.QRect(324, 402, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy)
        self.label_83.setMinimumSize(QtCore.QSize(0, 0))
        self.label_83.setMaximumSize(QtCore.QSize(100, 100))
        self.label_83.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setIndent(0)
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.widget_3)
        self.label_84.setGeometry(QtCore.QRect(90, 231, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy)
        self.label_84.setMinimumSize(QtCore.QSize(0, 0))
        self.label_84.setMaximumSize(QtCore.QSize(100, 100))
        self.label_84.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setIndent(0)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.widget_3)
        self.label_85.setGeometry(QtCore.QRect(402, 323, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy)
        self.label_85.setMinimumSize(QtCore.QSize(0, 0))
        self.label_85.setMaximumSize(QtCore.QSize(100, 100))
        self.label_85.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setIndent(0)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.widget_3)
        self.label_86.setGeometry(QtCore.QRect(232, 373, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy)
        self.label_86.setMinimumSize(QtCore.QSize(0, 0))
        self.label_86.setMaximumSize(QtCore.QSize(100, 100))
        self.label_86.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setIndent(0)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.widget_3)
        self.label_87.setGeometry(QtCore.QRect(355, 301, 44, 44))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_87.sizePolicy().hasHeightForWidth())
        self.label_87.setSizePolicy(sizePolicy)
        self.label_87.setMinimumSize(QtCore.QSize(0, 0))
        self.label_87.setMaximumSize(QtCore.QSize(100, 100))
        self.label_87.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(74, 74, 75);\n"
"    border-width: 1px;\n"
"    border-radius: 22px;\n"
"    color: white;\n"
"    background: rgb(122, 129, 131);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_87.setAlignment(QtCore.Qt.AlignCenter)
        self.label_87.setIndent(0)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.widget_3)
        self.label_88.setGeometry(QtCore.QRect(5, 218, 70, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy)
        self.label_88.setMinimumSize(QtCore.QSize(0, 0))
        self.label_88.setMaximumSize(QtCore.QSize(100, 100))
        self.label_88.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(217, 217, 217);\n"
"    border-width: 2px;\n"
"    border-radius: 35px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.label_88.setAlignment(QtCore.Qt.AlignCenter)
        self.label_88.setIndent(0)
        self.label_88.setObjectName("label_88")
        self.widget_4 = QtWidgets.QWidget(self.frame_4)
        self.widget_4.setGeometry(QtCore.QRect(534, 4, 176, 291))
        self.widget_4.setObjectName("widget_4")
        self.label_89 = QtWidgets.QLabel(self.widget_4)
        self.label_89.setGeometry(QtCore.QRect(4, 3, 169, 300))
        self.label_89.setStyleSheet("image: url(:/images/atc_spindle_tool.png);")
        self.label_89.setText("")
        self.label_89.setScaledContents(True)
        self.label_89.setIndent(0)
        self.label_89.setObjectName("label_89")
        self.tool_length_8 = StatusLabel(self.widget_4)
        self.tool_length_8.setGeometry(QtCore.QRect(64, 139, 50, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_8.sizePolicy().hasHeightForWidth())
        self.tool_length_8.setSizePolicy(sizePolicy)
        self.tool_length_8.setMinimumSize(QtCore.QSize(50, 33))
        self.tool_length_8.setMaximumSize(QtCore.QSize(50, 33))
        self.tool_length_8.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 16pt \"Bebas Kai\";\n"
"}")
        self.tool_length_8.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_length_8.setObjectName("tool_length_8")
        self.label_38 = QtWidgets.QLabel(self.frame_4)
        self.label_38.setGeometry(QtCore.QRect(610, 317, 240, 200))
        self.label_38.setStyleSheet("image: url(:/images/tool_probe.png);")
        self.label_38.setText("")
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.widget_4.raise_()
        self.label_38.raise_()
        self.widget_3.raise_()
        self.verticalLayout_19.addWidget(self.frame_4)
        self.horizontalLayout_36.addLayout(self.verticalLayout_19)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.frame_21 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_50.addWidget(self.frame_21)
        self.horizontalLayout_36.addLayout(self.horizontalLayout_50)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(-1, -1, 16, 20)
        self.verticalLayout_17.setSpacing(35)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_6 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(340, 320))
        self.frame_6.setMaximumSize(QtCore.QSize(340, 320))
        self.frame_6.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.machine_column_header_3 = QtWidgets.QLabel(self.frame_6)
        self.machine_column_header_3.setMinimumSize(QtCore.QSize(0, 50))
        self.machine_column_header_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_3.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_3.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_3.setObjectName("machine_column_header_3")
        self.horizontalLayout_25.addWidget(self.machine_column_header_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_26.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.load_spindle_tool_number = QtWidgets.QLineEdit(self.frame_6)
        self.load_spindle_tool_number.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_spindle_tool_number.sizePolicy().hasHeightForWidth())
        self.load_spindle_tool_number.setSizePolicy(sizePolicy)
        self.load_spindle_tool_number.setMinimumSize(QtCore.QSize(130, 40))
        self.load_spindle_tool_number.setMaximumSize(QtCore.QSize(16777215, 40))
        self.load_spindle_tool_number.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.load_spindle_tool_number.setAlignment(QtCore.Qt.AlignCenter)
        self.load_spindle_tool_number.setObjectName("load_spindle_tool_number")
        self.horizontalLayout_26.addWidget(self.load_spindle_tool_number)
        self.load_current_tool = MDIButton(self.frame_6)
        self.load_current_tool.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_current_tool.sizePolicy().hasHeightForWidth())
        self.load_current_tool.setSizePolicy(sizePolicy)
        self.load_current_tool.setMinimumSize(QtCore.QSize(130, 45))
        self.load_current_tool.setMaximumSize(QtCore.QSize(16777215, 45))
        self.load_current_tool.setStyleSheet("MDIButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.load_current_tool.setCheckable(False)
        self.load_current_tool.setAutoExclusive(True)
        self.load_current_tool.setObjectName("load_current_tool")
        self.horizontalLayout_26.addWidget(self.load_current_tool)
        self.verticalLayout_10.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.remove_current_tool = MDIButton(self.frame_6)
        self.remove_current_tool.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_current_tool.sizePolicy().hasHeightForWidth())
        self.remove_current_tool.setSizePolicy(sizePolicy)
        self.remove_current_tool.setMinimumSize(QtCore.QSize(130, 45))
        self.remove_current_tool.setMaximumSize(QtCore.QSize(16777215, 45))
        self.remove_current_tool.setStyleSheet("MDIButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.remove_current_tool.setCheckable(False)
        self.remove_current_tool.setAutoExclusive(True)
        self.remove_current_tool.setObjectName("remove_current_tool")
        self.horizontalLayout_14.addWidget(self.remove_current_tool)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.subcallbutton_15 = SubCallButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_15.sizePolicy().hasHeightForWidth())
        self.subcallbutton_15.setSizePolicy(sizePolicy)
        self.subcallbutton_15.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_15.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_15.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.subcallbutton_15.setIcon(icon6)
        self.subcallbutton_15.setIconSize(QtCore.QSize(20, 20))
        self.subcallbutton_15.setObjectName("subcallbutton_15")
        self.horizontalLayout_16.addWidget(self.subcallbutton_15)
        self.subcallbutton_4 = SubCallButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subcallbutton_4.sizePolicy().hasHeightForWidth())
        self.subcallbutton_4.setSizePolicy(sizePolicy)
        self.subcallbutton_4.setMinimumSize(QtCore.QSize(130, 45))
        self.subcallbutton_4.setMaximumSize(QtCore.QSize(16777215, 45))
        self.subcallbutton_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.subcallbutton_4.setStyleSheet("SubCallButton {\n"
"    text-align: right;\n"
"    padding-right: 28px;\n"
"       font: 16pt \"Bebas Kai\";\n"
"}\n"
"")
        self.subcallbutton_4.setIcon(icon7)
        self.subcallbutton_4.setIconSize(QtCore.QSize(20, 20))
        self.subcallbutton_4.setObjectName("subcallbutton_4")
        self.horizontalLayout_16.addWidget(self.subcallbutton_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_21.setSpacing(2)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.store_current_tool = MDIButton(self.frame_6)
        self.store_current_tool.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.store_current_tool.sizePolicy().hasHeightForWidth())
        self.store_current_tool.setSizePolicy(sizePolicy)
        self.store_current_tool.setMinimumSize(QtCore.QSize(130, 45))
        self.store_current_tool.setMaximumSize(QtCore.QSize(16777215, 45))
        self.store_current_tool.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.store_current_tool.setCheckable(False)
        self.store_current_tool.setAutoExclusive(True)
        self.store_current_tool.setObjectName("store_current_tool")
        self.horizontalLayout_21.addWidget(self.store_current_tool)
        self.verticalLayout_10.addLayout(self.horizontalLayout_21)
        self.verticalLayout_17.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.status_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(340, 215))
        self.frame_7.setMaximumSize(QtCore.QSize(340, 215))
        self.frame_7.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"border-radius: 6px;\n"
"padding-top: 0px;\n"
"padding-bottom: 0px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.machine_column_header_2 = QtWidgets.QLabel(self.frame_7)
        self.machine_column_header_2.setMinimumSize(QtCore.QSize(0, 50))
        self.machine_column_header_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_2.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_2.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_2.setObjectName("machine_column_header_2")
        self.horizontalLayout_24.addWidget(self.machine_column_header_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.m01_break_button_24 = ActionButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_24.sizePolicy().hasHeightForWidth())
        self.m01_break_button_24.setSizePolicy(sizePolicy)
        self.m01_break_button_24.setMinimumSize(QtCore.QSize(250, 45))
        self.m01_break_button_24.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_24.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_24.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_24.setObjectName("m01_break_button_24")
        self.horizontalLayout_19.addWidget(self.m01_break_button_24)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(2, 5, 2, 5)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.m01_break_button_25 = ActionButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m01_break_button_25.sizePolicy().hasHeightForWidth())
        self.m01_break_button_25.setSizePolicy(sizePolicy)
        self.m01_break_button_25.setMinimumSize(QtCore.QSize(250, 45))
        self.m01_break_button_25.setMaximumSize(QtCore.QSize(16777215, 45))
        self.m01_break_button_25.setFocusPolicy(QtCore.Qt.NoFocus)
        self.m01_break_button_25.setStyleSheet("QPushButton {\n"
"       font: 16pt \"Bebas Kai\";\n"
"}")
        self.m01_break_button_25.setObjectName("m01_break_button_25")
        self.horizontalLayout_23.addWidget(self.m01_break_button_25)
        self.verticalLayout_6.addLayout(self.horizontalLayout_23)
        self.verticalLayout_17.addWidget(self.frame_7)
        self.horizontalLayout_36.addLayout(self.verticalLayout_17)
        self.tabWidget.addTab(self.status_tab, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_16)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(0, 18, 5, 18)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_37 = QtWidgets.QFrame(self.tab_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setMinimumSize(QtCore.QSize(560, 500))
        self.frame_37.setMaximumSize(QtCore.QSize(520, 500))
        self.frame_37.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_39.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_37)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tableWidget_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("QTableView {\n"
"    color: rgb(235, 235, 237);\n"
"       border-top: 8px rgb(120, 120, 120);\n"
"    border-left: 4px  rgb(120, 120, 120);\n"
"    border-bottom: 1px rgb(120, 120, 120);\n"
"    border-right: 4px rgb(120, 120, 120);\n"
"    border-radius: 5px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(120, 120, 120);\n"
"    gridline-color: rgb(203, 203, 203);\n"
"    alternate-background-color: rgb(90, 90, 90);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}\n"
"\n"
"QHeaderView {\n"
"    font: 16pt \"Bebas Kai\";\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"}")
        self.tableWidget_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_3.setLineWidth(6)
        self.tableWidget_3.setMidLineWidth(4)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(16)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(7, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget_3.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        item.setFont(font)
        self.tableWidget_3.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget_3.setItem(8, 5, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(86)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(87)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(42)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(42)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_47.addWidget(self.tableWidget_3)
        self.verticalLayout_39.addLayout(self.horizontalLayout_47)
        self.horizontalLayout_130 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_130.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_130.setObjectName("horizontalLayout_130")
        self.x_axis_button_10 = QtWidgets.QPushButton(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_10.sizePolicy().hasHeightForWidth())
        self.x_axis_button_10.setSizePolicy(sizePolicy)
        self.x_axis_button_10.setMinimumSize(QtCore.QSize(108, 33))
        self.x_axis_button_10.setMaximumSize(QtCore.QSize(108, 33))
        self.x_axis_button_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_10.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_10.setCheckable(True)
        self.x_axis_button_10.setObjectName("x_axis_button_10")
        self.horizontalLayout_130.addWidget(self.x_axis_button_10)
        self.x_axis_button_12 = QtWidgets.QPushButton(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_12.sizePolicy().hasHeightForWidth())
        self.x_axis_button_12.setSizePolicy(sizePolicy)
        self.x_axis_button_12.setMinimumSize(QtCore.QSize(108, 33))
        self.x_axis_button_12.setMaximumSize(QtCore.QSize(108, 33))
        self.x_axis_button_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_12.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_12.setCheckable(True)
        self.x_axis_button_12.setObjectName("x_axis_button_12")
        self.horizontalLayout_130.addWidget(self.x_axis_button_12)
        self.x_axis_button_13 = QtWidgets.QPushButton(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_13.sizePolicy().hasHeightForWidth())
        self.x_axis_button_13.setSizePolicy(sizePolicy)
        self.x_axis_button_13.setMinimumSize(QtCore.QSize(108, 33))
        self.x_axis_button_13.setMaximumSize(QtCore.QSize(108, 33))
        self.x_axis_button_13.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_13.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_13.setCheckable(True)
        self.x_axis_button_13.setObjectName("x_axis_button_13")
        self.horizontalLayout_130.addWidget(self.x_axis_button_13)
        self.x_axis_button_14 = QtWidgets.QPushButton(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_axis_button_14.sizePolicy().hasHeightForWidth())
        self.x_axis_button_14.setSizePolicy(sizePolicy)
        self.x_axis_button_14.setMinimumSize(QtCore.QSize(130, 33))
        self.x_axis_button_14.setMaximumSize(QtCore.QSize(130, 33))
        self.x_axis_button_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.x_axis_button_14.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.x_axis_button_14.setCheckable(True)
        self.x_axis_button_14.setObjectName("x_axis_button_14")
        self.horizontalLayout_130.addWidget(self.x_axis_button_14)
        self.verticalLayout_39.addLayout(self.horizontalLayout_130)
        self.verticalLayout_11.addWidget(self.frame_37)
        self.mdi_entry_box_6 = MDIEntry(self.tab_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdi_entry_box_6.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_6.setSizePolicy(sizePolicy)
        self.mdi_entry_box_6.setMinimumSize(QtCore.QSize(560, 40))
        self.mdi_entry_box_6.setMaximumSize(QtCore.QSize(560, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.mdi_entry_box_6.setFont(font)
        self.mdi_entry_box_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mdi_entry_box_6.setObjectName("mdi_entry_box_6")
        self.verticalLayout_11.addWidget(self.mdi_entry_box_6)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.frame_15 = QtWidgets.QFrame(self.tab_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QtCore.QSize(700, 560))
        self.frame_15.setMaximumSize(QtCore.QSize(650, 560))
        self.frame_15.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setContentsMargins(-1, 5, -1, 9)
        self.verticalLayout_33.setSpacing(15)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.gridLayout_12.setHorizontalSpacing(31)
        self.gridLayout_12.setVerticalSpacing(12)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.machine_column_header_4 = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header_4.sizePolicy().hasHeightForWidth())
        self.machine_column_header_4.setSizePolicy(sizePolicy)
        self.machine_column_header_4.setMinimumSize(QtCore.QSize(675, 55))
        self.machine_column_header_4.setMaximumSize(QtCore.QSize(16777215, 55))
        self.machine_column_header_4.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(90, 90, 90);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_4.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_4.setObjectName("machine_column_header_4")
        self.gridLayout_12.addWidget(self.machine_column_header_4, 0, 0, 1, 5)
        self.actionbutton_g54_2 = ActionButton(self.frame_15)
        self.actionbutton_g54_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g54_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g54_2.setSizePolicy(sizePolicy)
        self.actionbutton_g54_2.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g54_2.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g54_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g54_2.setAutoExclusive(True)
        self.actionbutton_g54_2.setObjectName("actionbutton_g54_2")
        self.gridLayout_12.addWidget(self.actionbutton_g54_2, 1, 0, 1, 1)
        self.actionbutton_g55_2 = ActionButton(self.frame_15)
        self.actionbutton_g55_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g55_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g55_2.setSizePolicy(sizePolicy)
        self.actionbutton_g55_2.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g55_2.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g55_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g55_2.setAutoExclusive(True)
        self.actionbutton_g55_2.setObjectName("actionbutton_g55_2")
        self.gridLayout_12.addWidget(self.actionbutton_g55_2, 1, 1, 1, 1)
        self.actionbutton_g56_2 = ActionButton(self.frame_15)
        self.actionbutton_g56_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g56_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g56_2.setSizePolicy(sizePolicy)
        self.actionbutton_g56_2.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g56_2.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g56_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g56_2.setAutoExclusive(True)
        self.actionbutton_g56_2.setObjectName("actionbutton_g56_2")
        self.gridLayout_12.addWidget(self.actionbutton_g56_2, 1, 2, 1, 1)
        self.actionbutton_g57_2 = ActionButton(self.frame_15)
        self.actionbutton_g57_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g57_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g57_2.setSizePolicy(sizePolicy)
        self.actionbutton_g57_2.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g57_2.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g57_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g57_2.setAutoExclusive(True)
        self.actionbutton_g57_2.setObjectName("actionbutton_g57_2")
        self.gridLayout_12.addWidget(self.actionbutton_g57_2, 1, 3, 1, 1)
        self.actionbutton_g58_2 = ActionButton(self.frame_15)
        self.actionbutton_g58_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g58_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_g58_2.setSizePolicy(sizePolicy)
        self.actionbutton_g58_2.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g58_2.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g58_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g58_2.setAutoExclusive(True)
        self.actionbutton_g58_2.setObjectName("actionbutton_g58_2")
        self.gridLayout_12.addWidget(self.actionbutton_g58_2, 1, 4, 1, 1)
        self.actionbutton_g59_4 = ActionButton(self.frame_15)
        self.actionbutton_g59_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_4.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_4.setSizePolicy(sizePolicy)
        self.actionbutton_g59_4.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_4.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_4.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_4.setAutoExclusive(True)
        self.actionbutton_g59_4.setObjectName("actionbutton_g59_4")
        self.gridLayout_12.addWidget(self.actionbutton_g59_4, 2, 1, 1, 1)
        self.actionbutton_g59_5 = ActionButton(self.frame_15)
        self.actionbutton_g59_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_5.setSizePolicy(sizePolicy)
        self.actionbutton_g59_5.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_5.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_5.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_5.setAutoExclusive(True)
        self.actionbutton_g59_5.setObjectName("actionbutton_g59_5")
        self.gridLayout_12.addWidget(self.actionbutton_g59_5, 2, 2, 1, 1)
        self.actionbutton_g59_6 = ActionButton(self.frame_15)
        self.actionbutton_g59_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_6.setSizePolicy(sizePolicy)
        self.actionbutton_g59_6.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_6.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_6.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_6.setAutoExclusive(True)
        self.actionbutton_g59_6.setObjectName("actionbutton_g59_6")
        self.gridLayout_12.addWidget(self.actionbutton_g59_6, 2, 3, 1, 1)
        self.actionbutton_g59_7 = ActionButton(self.frame_15)
        self.actionbutton_g59_7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_g59_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_g59_7.setSizePolicy(sizePolicy)
        self.actionbutton_g59_7.setMinimumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_7.setMaximumSize(QtCore.QSize(110, 38))
        self.actionbutton_g59_7.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_g59_7.setAutoExclusive(True)
        self.actionbutton_g59_7.setObjectName("actionbutton_g59_7")
        self.gridLayout_12.addWidget(self.actionbutton_g59_7, 2, 4, 1, 1)
        self.verticalLayout_33.addLayout(self.gridLayout_12)
        self.frame_31 = QtWidgets.QFrame(self.frame_15)
        self.frame_31.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_33.addWidget(self.frame_31)
        self.frame_32 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_32.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_34.setContentsMargins(10, -1, 11, -1)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_7.setSpacing(13)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.axis_column_header_9 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_column_header_9.sizePolicy().hasHeightForWidth())
        self.axis_column_header_9.setSizePolicy(sizePolicy)
        self.axis_column_header_9.setMinimumSize(QtCore.QSize(55, 50))
        self.axis_column_header_9.setMaximumSize(QtCore.QSize(55, 50))
        self.axis_column_header_9.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_9.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_9.setWordWrap(True)
        self.axis_column_header_9.setObjectName("axis_column_header_9")
        self.horizontalLayout_7.addWidget(self.axis_column_header_9)
        self.axis_column_header_10 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_column_header_10.sizePolicy().hasHeightForWidth())
        self.axis_column_header_10.setSizePolicy(sizePolicy)
        self.axis_column_header_10.setMinimumSize(QtCore.QSize(45, 50))
        self.axis_column_header_10.setMaximumSize(QtCore.QSize(45, 50))
        self.axis_column_header_10.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_10.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_10.setWordWrap(True)
        self.axis_column_header_10.setObjectName("axis_column_header_10")
        self.horizontalLayout_7.addWidget(self.axis_column_header_10)
        self.machine_column_header_10 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header_10.sizePolicy().hasHeightForWidth())
        self.machine_column_header_10.setSizePolicy(sizePolicy)
        self.machine_column_header_10.setMinimumSize(QtCore.QSize(88, 50))
        self.machine_column_header_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_10.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_10.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_10.setWordWrap(True)
        self.machine_column_header_10.setObjectName("machine_column_header_10")
        self.horizontalLayout_7.addWidget(self.machine_column_header_10)
        self.machine_column_header_11 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header_11.sizePolicy().hasHeightForWidth())
        self.machine_column_header_11.setSizePolicy(sizePolicy)
        self.machine_column_header_11.setMinimumSize(QtCore.QSize(85, 50))
        self.machine_column_header_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_11.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_11.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_11.setWordWrap(True)
        self.machine_column_header_11.setObjectName("machine_column_header_11")
        self.horizontalLayout_7.addWidget(self.machine_column_header_11)
        self.machine_column_header_12 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header_12.sizePolicy().hasHeightForWidth())
        self.machine_column_header_12.setSizePolicy(sizePolicy)
        self.machine_column_header_12.setMinimumSize(QtCore.QSize(60, 50))
        self.machine_column_header_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_12.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_12.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_12.setWordWrap(True)
        self.machine_column_header_12.setObjectName("machine_column_header_12")
        self.horizontalLayout_7.addWidget(self.machine_column_header_12)
        self.ref_coilumn_header_4 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_4.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_4.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_4.setMinimumSize(QtCore.QSize(65, 50))
        self.ref_coilumn_header_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ref_coilumn_header_4.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_4.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_4.setWordWrap(True)
        self.ref_coilumn_header_4.setObjectName("ref_coilumn_header_4")
        self.horizontalLayout_7.addWidget(self.ref_coilumn_header_4)
        self.machine_column_header_13 = QtWidgets.QLabel(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_column_header_13.sizePolicy().hasHeightForWidth())
        self.machine_column_header_13.setSizePolicy(sizePolicy)
        self.machine_column_header_13.setMinimumSize(QtCore.QSize(65, 50))
        self.machine_column_header_13.setMaximumSize(QtCore.QSize(16777215, 50))
        self.machine_column_header_13.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: none;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.machine_column_header_13.setAlignment(QtCore.Qt.AlignCenter)
        self.machine_column_header_13.setWordWrap(True)
        self.machine_column_header_13.setObjectName("machine_column_header_13")
        self.horizontalLayout_7.addWidget(self.machine_column_header_13)
        self.verticalLayout_34.addLayout(self.horizontalLayout_7)
        self.verticalLayout_33.addWidget(self.frame_32)
        self.dro_qvboxlayout_3 = QtWidgets.QVBoxLayout()
        self.dro_qvboxlayout_3.setContentsMargins(6, 0, 6, 5)
        self.dro_qvboxlayout_3.setSpacing(15)
        self.dro_qvboxlayout_3.setObjectName("dro_qvboxlayout_3")
        self.x_axis_dro_layout_3 = QtWidgets.QHBoxLayout()
        self.x_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.x_axis_dro_layout_3.setSpacing(12)
        self.x_axis_dro_layout_3.setObjectName("x_axis_dro_layout_3")
        self.zero_x_button_2 = MDIButton(self.frame_15)
        self.zero_x_button_2.setEnabled(False)
        self.zero_x_button_2.setMinimumSize(QtCore.QSize(55, 38))
        self.zero_x_button_2.setMaximumSize(QtCore.QSize(55, 38))
        self.zero_x_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_x_button_2.setObjectName("zero_x_button_2")
        self.x_axis_dro_layout_3.addWidget(self.zero_x_button_2)
        self.axis_column_header_11 = QtWidgets.QLabel(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_column_header_11.sizePolicy().hasHeightForWidth())
        self.axis_column_header_11.setSizePolicy(sizePolicy)
        self.axis_column_header_11.setMinimumSize(QtCore.QSize(45, 35))
        self.axis_column_header_11.setMaximumSize(QtCore.QSize(45, 35))
        self.axis_column_header_11.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_11.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_11.setObjectName("axis_column_header_11")
        self.x_axis_dro_layout_3.addWidget(self.axis_column_header_11)
        self.statuslabel_50 = StatusLabel(self.frame_15)
        self.statuslabel_50.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_50.setObjectName("statuslabel_50")
        self.x_axis_dro_layout_3.addWidget(self.statuslabel_50)
        self.statuslabel_51 = StatusLabel(self.frame_15)
        self.statuslabel_51.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_51.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_51.setObjectName("statuslabel_51")
        self.x_axis_dro_layout_3.addWidget(self.statuslabel_51)
        self.statuslabel_52 = StatusLabel(self.frame_15)
        self.statuslabel_52.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_52.setObjectName("statuslabel_52")
        self.x_axis_dro_layout_3.addWidget(self.statuslabel_52)
        self.statuslabel_53 = StatusLabel(self.frame_15)
        self.statuslabel_53.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_53.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_53.setObjectName("statuslabel_53")
        self.x_axis_dro_layout_3.addWidget(self.statuslabel_53)
        self.statuslabel_54 = StatusLabel(self.frame_15)
        self.statuslabel_54.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_54.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_54.setObjectName("statuslabel_54")
        self.x_axis_dro_layout_3.addWidget(self.statuslabel_54)
        self.dro_qvboxlayout_3.addLayout(self.x_axis_dro_layout_3)
        self.y_axis_dro_layout_3 = QtWidgets.QHBoxLayout()
        self.y_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.y_axis_dro_layout_3.setSpacing(12)
        self.y_axis_dro_layout_3.setObjectName("y_axis_dro_layout_3")
        self.zero_y_button_2 = MDIButton(self.frame_15)
        self.zero_y_button_2.setEnabled(False)
        self.zero_y_button_2.setMinimumSize(QtCore.QSize(55, 38))
        self.zero_y_button_2.setMaximumSize(QtCore.QSize(55, 38))
        self.zero_y_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_y_button_2.setObjectName("zero_y_button_2")
        self.y_axis_dro_layout_3.addWidget(self.zero_y_button_2)
        self.axis_column_header_12 = QtWidgets.QLabel(self.frame_15)
        self.axis_column_header_12.setMinimumSize(QtCore.QSize(45, 35))
        self.axis_column_header_12.setMaximumSize(QtCore.QSize(45, 35))
        self.axis_column_header_12.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_12.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_12.setObjectName("axis_column_header_12")
        self.y_axis_dro_layout_3.addWidget(self.axis_column_header_12)
        self.statuslabel_55 = StatusLabel(self.frame_15)
        self.statuslabel_55.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_55.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_55.setObjectName("statuslabel_55")
        self.y_axis_dro_layout_3.addWidget(self.statuslabel_55)
        self.statuslabel_56 = StatusLabel(self.frame_15)
        self.statuslabel_56.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_56.setObjectName("statuslabel_56")
        self.y_axis_dro_layout_3.addWidget(self.statuslabel_56)
        self.statuslabel_57 = StatusLabel(self.frame_15)
        self.statuslabel_57.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_57.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_57.setObjectName("statuslabel_57")
        self.y_axis_dro_layout_3.addWidget(self.statuslabel_57)
        self.statuslabel_58 = StatusLabel(self.frame_15)
        self.statuslabel_58.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_58.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_58.setObjectName("statuslabel_58")
        self.y_axis_dro_layout_3.addWidget(self.statuslabel_58)
        self.statuslabel_59 = StatusLabel(self.frame_15)
        self.statuslabel_59.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_59.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_59.setObjectName("statuslabel_59")
        self.y_axis_dro_layout_3.addWidget(self.statuslabel_59)
        self.dro_qvboxlayout_3.addLayout(self.y_axis_dro_layout_3)
        self.z_axis_dro_layout_3 = QtWidgets.QHBoxLayout()
        self.z_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.z_axis_dro_layout_3.setSpacing(12)
        self.z_axis_dro_layout_3.setObjectName("z_axis_dro_layout_3")
        self.zero_z_button_2 = MDIButton(self.frame_15)
        self.zero_z_button_2.setEnabled(False)
        self.zero_z_button_2.setMinimumSize(QtCore.QSize(55, 38))
        self.zero_z_button_2.setMaximumSize(QtCore.QSize(55, 38))
        self.zero_z_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_z_button_2.setObjectName("zero_z_button_2")
        self.z_axis_dro_layout_3.addWidget(self.zero_z_button_2)
        self.axis_column_header_13 = QtWidgets.QLabel(self.frame_15)
        self.axis_column_header_13.setMinimumSize(QtCore.QSize(45, 35))
        self.axis_column_header_13.setMaximumSize(QtCore.QSize(45, 35))
        self.axis_column_header_13.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_13.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_13.setObjectName("axis_column_header_13")
        self.z_axis_dro_layout_3.addWidget(self.axis_column_header_13)
        self.statuslabel_60 = StatusLabel(self.frame_15)
        self.statuslabel_60.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_60.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_60.setObjectName("statuslabel_60")
        self.z_axis_dro_layout_3.addWidget(self.statuslabel_60)
        self.statuslabel_61 = StatusLabel(self.frame_15)
        self.statuslabel_61.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_61.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_61.setObjectName("statuslabel_61")
        self.z_axis_dro_layout_3.addWidget(self.statuslabel_61)
        self.statuslabel_62 = StatusLabel(self.frame_15)
        self.statuslabel_62.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_62.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_62.setObjectName("statuslabel_62")
        self.z_axis_dro_layout_3.addWidget(self.statuslabel_62)
        self.statuslabel_63 = StatusLabel(self.frame_15)
        self.statuslabel_63.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_63.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_63.setObjectName("statuslabel_63")
        self.z_axis_dro_layout_3.addWidget(self.statuslabel_63)
        self.statuslabel_64 = StatusLabel(self.frame_15)
        self.statuslabel_64.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_64.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_64.setObjectName("statuslabel_64")
        self.z_axis_dro_layout_3.addWidget(self.statuslabel_64)
        self.dro_qvboxlayout_3.addLayout(self.z_axis_dro_layout_3)
        self.a_axis_dro_layout_3 = QtWidgets.QHBoxLayout()
        self.a_axis_dro_layout_3.setContentsMargins(-1, 1, -1, 1)
        self.a_axis_dro_layout_3.setSpacing(12)
        self.a_axis_dro_layout_3.setObjectName("a_axis_dro_layout_3")
        self.zero_a_button_2 = MDIButton(self.frame_15)
        self.zero_a_button_2.setEnabled(False)
        self.zero_a_button_2.setMinimumSize(QtCore.QSize(55, 38))
        self.zero_a_button_2.setMaximumSize(QtCore.QSize(55, 38))
        self.zero_a_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_a_button_2.setObjectName("zero_a_button_2")
        self.a_axis_dro_layout_3.addWidget(self.zero_a_button_2)
        self.axis_column_header_14 = QtWidgets.QLabel(self.frame_15)
        self.axis_column_header_14.setMinimumSize(QtCore.QSize(45, 35))
        self.axis_column_header_14.setMaximumSize(QtCore.QSize(45, 35))
        self.axis_column_header_14.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_14.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_14.setObjectName("axis_column_header_14")
        self.a_axis_dro_layout_3.addWidget(self.axis_column_header_14)
        self.statuslabel_65 = StatusLabel(self.frame_15)
        self.statuslabel_65.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_65.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_65.setObjectName("statuslabel_65")
        self.a_axis_dro_layout_3.addWidget(self.statuslabel_65)
        self.statuslabel_66 = StatusLabel(self.frame_15)
        self.statuslabel_66.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_66.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_66.setObjectName("statuslabel_66")
        self.a_axis_dro_layout_3.addWidget(self.statuslabel_66)
        self.statuslabel_67 = StatusLabel(self.frame_15)
        self.statuslabel_67.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_67.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_67.setObjectName("statuslabel_67")
        self.a_axis_dro_layout_3.addWidget(self.statuslabel_67)
        self.statuslabel_68 = StatusLabel(self.frame_15)
        self.statuslabel_68.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_68.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_68.setObjectName("statuslabel_68")
        self.a_axis_dro_layout_3.addWidget(self.statuslabel_68)
        self.statuslabel_69 = StatusLabel(self.frame_15)
        self.statuslabel_69.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_69.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_69.setObjectName("statuslabel_69")
        self.a_axis_dro_layout_3.addWidget(self.statuslabel_69)
        self.dro_qvboxlayout_3.addLayout(self.a_axis_dro_layout_3)
        self.b_axis_dro_layout_4 = QtWidgets.QHBoxLayout()
        self.b_axis_dro_layout_4.setContentsMargins(-1, 1, -1, 1)
        self.b_axis_dro_layout_4.setSpacing(12)
        self.b_axis_dro_layout_4.setObjectName("b_axis_dro_layout_4")
        self.zero_b_button_2 = MDIButton(self.frame_15)
        self.zero_b_button_2.setEnabled(False)
        self.zero_b_button_2.setMinimumSize(QtCore.QSize(55, 38))
        self.zero_b_button_2.setMaximumSize(QtCore.QSize(55, 38))
        self.zero_b_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.zero_b_button_2.setObjectName("zero_b_button_2")
        self.b_axis_dro_layout_4.addWidget(self.zero_b_button_2)
        self.axis_column_header_15 = QtWidgets.QLabel(self.frame_15)
        self.axis_column_header_15.setMinimumSize(QtCore.QSize(45, 35))
        self.axis_column_header_15.setMaximumSize(QtCore.QSize(45, 35))
        self.axis_column_header_15.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header_15.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header_15.setObjectName("axis_column_header_15")
        self.b_axis_dro_layout_4.addWidget(self.axis_column_header_15)
        self.statuslabel_70 = StatusLabel(self.frame_15)
        self.statuslabel_70.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_70.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_70.setObjectName("statuslabel_70")
        self.b_axis_dro_layout_4.addWidget(self.statuslabel_70)
        self.statuslabel_71 = StatusLabel(self.frame_15)
        self.statuslabel_71.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_71.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_71.setObjectName("statuslabel_71")
        self.b_axis_dro_layout_4.addWidget(self.statuslabel_71)
        self.statuslabel_72 = StatusLabel(self.frame_15)
        self.statuslabel_72.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_72.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_72.setObjectName("statuslabel_72")
        self.b_axis_dro_layout_4.addWidget(self.statuslabel_72)
        self.statuslabel_73 = StatusLabel(self.frame_15)
        self.statuslabel_73.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_73.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_73.setObjectName("statuslabel_73")
        self.b_axis_dro_layout_4.addWidget(self.statuslabel_73)
        self.statuslabel_74 = StatusLabel(self.frame_15)
        self.statuslabel_74.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_74.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_74.setObjectName("statuslabel_74")
        self.b_axis_dro_layout_4.addWidget(self.statuslabel_74)
        self.dro_qvboxlayout_3.addLayout(self.b_axis_dro_layout_4)
        self.verticalLayout_33.addLayout(self.dro_qvboxlayout_3)
        self.horizontalLayout_51.addWidget(self.frame_15)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_51)
        self.horizontalLayout_131 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_131.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_131.setObjectName("horizontalLayout_131")
        self.frame_38 = QtWidgets.QFrame(self.tab_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setMinimumSize(QtCore.QSize(345, 560))
        self.frame_38.setMaximumSize(QtCore.QSize(345, 560))
        self.frame_38.setStyleSheet("QFrame{\n"
"border-style: none;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_38.setObjectName("frame_38")
        self.label_47 = QtWidgets.QLabel(self.frame_38)
        self.label_47.setGeometry(QtCore.QRect(120, 250, 200, 167))
        self.label_47.setStyleSheet("image: url(:/images/tool_probe.png);")
        self.label_47.setText("")
        self.label_47.setScaledContents(True)
        self.label_47.setObjectName("label_47")
        self.label_51 = QtWidgets.QLabel(self.frame_38)
        self.label_51.setGeometry(QtCore.QRect(61, 0, 140, 231))
        self.label_51.setStyleSheet("image: url(:/images/atc_spindle_tool.png);")
        self.label_51.setText("")
        self.label_51.setScaledContents(True)
        self.label_51.setObjectName("label_51")
        self.frame_39 = QtWidgets.QFrame(self.frame_38)
        self.frame_39.setGeometry(QtCore.QRect(2, 440, 340, 120))
        self.frame_39.setMinimumSize(QtCore.QSize(340, 120))
        self.frame_39.setMaximumSize(QtCore.QSize(330, 120))
        self.frame_39.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_39.setObjectName("frame_39")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.frame_39)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(3, 10, 334, 93))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.set_tool_touch_off_position_button_2 = MDIButton(self.verticalLayoutWidget_6)
        self.set_tool_touch_off_position_button_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_tool_touch_off_position_button_2.sizePolicy().hasHeightForWidth())
        self.set_tool_touch_off_position_button_2.setSizePolicy(sizePolicy)
        self.set_tool_touch_off_position_button_2.setMinimumSize(QtCore.QSize(280, 40))
        self.set_tool_touch_off_position_button_2.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.set_tool_touch_off_position_button_2.setObjectName("set_tool_touch_off_position_button_2")
        self.horizontalLayout_22.addWidget(self.set_tool_touch_off_position_button_2)
        self.verticalLayout_13.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setSpacing(2)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_55 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy)
        self.label_55.setMinimumSize(QtCore.QSize(23, 33))
        self.label_55.setMaximumSize(QtCore.QSize(23, 33))
        self.label_55.setStyleSheet("QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_27.addWidget(self.label_55)
        self.tool_length_2 = StatusLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_2.sizePolicy().hasHeightForWidth())
        self.tool_length_2.setSizePolicy(sizePolicy)
        self.tool_length_2.setMinimumSize(QtCore.QSize(75, 33))
        self.tool_length_2.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_length_2.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.tool_length_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length_2.setObjectName("tool_length_2")
        self.horizontalLayout_27.addWidget(self.tool_length_2)
        self.label_57 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        self.label_57.setMinimumSize(QtCore.QSize(23, 33))
        self.label_57.setMaximumSize(QtCore.QSize(23, 33))
        self.label_57.setStyleSheet("QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_27.addWidget(self.label_57)
        self.tool_length_4 = StatusLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_4.sizePolicy().hasHeightForWidth())
        self.tool_length_4.setSizePolicy(sizePolicy)
        self.tool_length_4.setMinimumSize(QtCore.QSize(75, 33))
        self.tool_length_4.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_length_4.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.tool_length_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length_4.setObjectName("tool_length_4")
        self.horizontalLayout_27.addWidget(self.tool_length_4)
        self.label_58 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        self.label_58.setMinimumSize(QtCore.QSize(23, 33))
        self.label_58.setMaximumSize(QtCore.QSize(23, 33))
        self.label_58.setStyleSheet("QLabel{\n"
"border: none;\n"
"background: transparent;\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"}")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_27.addWidget(self.label_58)
        self.tool_length_3 = StatusLabel(self.verticalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_3.sizePolicy().hasHeightForWidth())
        self.tool_length_3.setSizePolicy(sizePolicy)
        self.tool_length_3.setMinimumSize(QtCore.QSize(75, 33))
        self.tool_length_3.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_length_3.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.tool_length_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length_3.setObjectName("tool_length_3")
        self.horizontalLayout_27.addWidget(self.tool_length_3)
        self.verticalLayout_13.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_131.addWidget(self.frame_38)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_131)
        self.tabWidget.addTab(self.tab_16, "")
        self.tooling_tab = QtWidgets.QWidget()
        self.tooling_tab.setObjectName("tooling_tab")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.tooling_tab)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setContentsMargins(15, 25, -1, 25)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.frame_13 = QtWidgets.QFrame(self.tooling_tab)
        self.frame_13.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"font: 15pt \"Bebas Kai\";\n"
"}")
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setContentsMargins(5, 5, 5, -1)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.tableWidget_2 = ToolTable(self.frame_13)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tableWidget_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("TootTable,\n"
"QHeaderView {\n"
"    font: 14pt \"Bebas Kai\";\n"
"    background-color: rgb(220, 220, 220);\n"
"    color: black;\n"
"    border: none;\n"
"}\n"
"\n"
"ToolTable {\n"
"       border-top: 8px rgb(120, 120, 120);\n"
"    border-left: 4px  rgb(120, 120, 120);\n"
"    border-bottom: 5px rgb(120, 120, 120);\n"
"    border-right: 4px rgb(120, 120, 120);\n"
"    border-radius: 5px;\n"
"    border-color: rgb(120, 120, 120);\n"
"    border-style: solid;\n"
"    background-color: rgb(120, 120, 120);\n"
"    gridline-color: rgb(203, 203, 203);\n"
"    alternate-background-color: rgb(90, 90, 90);\n"
"}")
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setLineWidth(3)
        self.tableWidget_2.setMidLineWidth(3)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(90)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(30)
        self.horizontalLayout_38.addWidget(self.tableWidget_2)
        self.verticalLayout_20.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.tool_table_delete_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_delete_button.sizePolicy().hasHeightForWidth())
        self.tool_table_delete_button.setSizePolicy(sizePolicy)
        self.tool_table_delete_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_delete_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_delete_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_delete_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_delete_button.setObjectName("tool_table_delete_button")
        self.horizontalLayout_37.addWidget(self.tool_table_delete_button)
        self.tool_table_add_tool_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_add_tool_button.sizePolicy().hasHeightForWidth())
        self.tool_table_add_tool_button.setSizePolicy(sizePolicy)
        self.tool_table_add_tool_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_add_tool_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_add_tool_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_add_tool_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_add_tool_button.setObjectName("tool_table_add_tool_button")
        self.horizontalLayout_37.addWidget(self.tool_table_add_tool_button)
        self.tool_table_reread_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_reread_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reread_button.setSizePolicy(sizePolicy)
        self.tool_table_reread_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_reread_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_reread_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_reread_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_reread_button.setObjectName("tool_table_reread_button")
        self.horizontalLayout_37.addWidget(self.tool_table_reread_button)
        self.tool_table_save_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_save_button.sizePolicy().hasHeightForWidth())
        self.tool_table_save_button.setSizePolicy(sizePolicy)
        self.tool_table_save_button.setMinimumSize(QtCore.QSize(120, 33))
        self.tool_table_save_button.setMaximumSize(QtCore.QSize(120, 33))
        self.tool_table_save_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_save_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_save_button.setObjectName("tool_table_save_button")
        self.horizontalLayout_37.addWidget(self.tool_table_save_button)
        self.tool_table_reload_button = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_table_reload_button.sizePolicy().hasHeightForWidth())
        self.tool_table_reload_button.setSizePolicy(sizePolicy)
        self.tool_table_reload_button.setMinimumSize(QtCore.QSize(140, 33))
        self.tool_table_reload_button.setMaximumSize(QtCore.QSize(140, 33))
        self.tool_table_reload_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_table_reload_button.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.tool_table_reload_button.setObjectName("tool_table_reload_button")
        self.horizontalLayout_37.addWidget(self.tool_table_reload_button)
        self.verticalLayout_20.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_40.addWidget(self.frame_13)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.tooling_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(580, 590))
        self.frame_10.setMaximumSize(QtCore.QSize(580, 590))
        self.frame_10.setStyleSheet("QFrame{\n"
"border-style: none;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_10.setObjectName("frame_10")
        self.label_43 = QtWidgets.QLabel(self.frame_10)
        self.label_43.setGeometry(QtCore.QRect(195, 78, 250, 403))
        self.label_43.setStyleSheet("image: url(:/images/atc_spindle_tool_dimensioned.png);")
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/images/atc_spindle_tool_dimensioned.png"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(122, 267, 145, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(100, 60))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 58))
        self.frame_11.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_98 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_98.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_98.setObjectName("horizontalLayout_98")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_48 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QtCore.QSize(48, 33))
        self.label_48.setMaximumSize(QtCore.QSize(48, 33))
        self.label_48.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.horizontalLayout_17.addWidget(self.label_48)
        self.tool_length_5 = StatusLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_5.sizePolicy().hasHeightForWidth())
        self.tool_length_5.setSizePolicy(sizePolicy)
        self.tool_length_5.setMinimumSize(QtCore.QSize(70, 33))
        self.tool_length_5.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_length_5.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_length_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length_5.setObjectName("tool_length_5")
        self.horizontalLayout_17.addWidget(self.tool_length_5)
        self.horizontalLayout_98.addLayout(self.horizontalLayout_17)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setGeometry(QtCore.QRect(180, 446, 132, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(100, 60))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_99 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_99.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_49 = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setMinimumSize(QtCore.QSize(35, 33))
        self.label_49.setMaximumSize(QtCore.QSize(35, 33))
        self.label_49.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setWordWrap(True)
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_18.addWidget(self.label_49)
        self.tool_diameter_2 = StatusLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_diameter_2.sizePolicy().hasHeightForWidth())
        self.tool_diameter_2.setSizePolicy(sizePolicy)
        self.tool_diameter_2.setMinimumSize(QtCore.QSize(70, 33))
        self.tool_diameter_2.setMaximumSize(QtCore.QSize(70, 33))
        self.tool_diameter_2.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_diameter_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_diameter_2.setObjectName("tool_diameter_2")
        self.horizontalLayout_18.addWidget(self.tool_diameter_2)
        self.horizontalLayout_99.addLayout(self.horizontalLayout_18)
        self.frame_28 = QtWidgets.QFrame(self.frame_10)
        self.frame_28.setGeometry(QtCore.QRect(4, 0, 570, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QtCore.QSize(570, 60))
        self.frame_28.setMaximumSize(QtCore.QSize(570, 58))
        self.frame_28.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_108 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_108.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_108.setObjectName("horizontalLayout_108")
        self.horizontalLayout_109 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_109.setSpacing(3)
        self.horizontalLayout_109.setObjectName("horizontalLayout_109")
        self.label_56 = QtWidgets.QLabel(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QtCore.QSize(60, 33))
        self.label_56.setMaximumSize(QtCore.QSize(60, 33))
        self.label_56.setStyleSheet("QLabel{\n"
"font: 75 13pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 0px;\n"
"padding-left: 0px;\n"
"border-style: none;\n"
"}")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setWordWrap(True)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_109.addWidget(self.label_56)
        self.tool_length_7 = StatusLabel(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_7.sizePolicy().hasHeightForWidth())
        self.tool_length_7.setSizePolicy(sizePolicy)
        self.tool_length_7.setMinimumSize(QtCore.QSize(70, 33))
        self.tool_length_7.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.tool_length_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tool_length_7.setIndent(4)
        self.tool_length_7.setObjectName("tool_length_7")
        self.horizontalLayout_109.addWidget(self.tool_length_7)
        self.horizontalLayout_108.addLayout(self.horizontalLayout_109)
        self.mdi_entry_box_4 = MDIEntry(self.frame_10)
        self.mdi_entry_box_4.setGeometry(QtCore.QRect(4, 550, 570, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdi_entry_box_4.sizePolicy().hasHeightForWidth())
        self.mdi_entry_box_4.setSizePolicy(sizePolicy)
        self.mdi_entry_box_4.setMinimumSize(QtCore.QSize(570, 40))
        self.mdi_entry_box_4.setMaximumSize(QtCore.QSize(570, 40))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.mdi_entry_box_4.setFont(font)
        self.mdi_entry_box_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mdi_entry_box_4.setObjectName("mdi_entry_box_4")
        self.tool_length_6 = StatusLabel(self.frame_10)
        self.tool_length_6.setGeometry(QtCore.QRect(330, 227, 50, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length_6.sizePolicy().hasHeightForWidth())
        self.tool_length_6.setSizePolicy(sizePolicy)
        self.tool_length_6.setMinimumSize(QtCore.QSize(50, 33))
        self.tool_length_6.setMaximumSize(QtCore.QSize(50, 33))
        self.tool_length_6.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 16pt \"Bebas Kai\";\n"
"}")
        self.tool_length_6.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_length_6.setObjectName("tool_length_6")
        self.horizontalLayout_6.addWidget(self.frame_10)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tooling_tab, "")
        self.probing_tab = QtWidgets.QWidget()
        self.probing_tab.setObjectName("probing_tab")
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout(self.probing_tab)
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.frame_20 = QtWidgets.QFrame(self.probing_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QtCore.QSize(530, 0))
        self.frame_20.setMaximumSize(QtCore.QSize(530, 16777215))
        self.frame_20.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_20.setLineWidth(0)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_26.setContentsMargins(-1, 0, 5, 5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_24 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QtCore.QSize(0, 27))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_26.addWidget(self.label_24)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_8.setVerticalSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.actionbutton_11 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_11.sizePolicy().hasHeightForWidth())
        self.actionbutton_11.setSizePolicy(sizePolicy)
        self.actionbutton_11.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_11.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_11.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_11.setAutoExclusive(True)
        self.actionbutton_11.setObjectName("actionbutton_11")
        self.gridLayout_8.addWidget(self.actionbutton_11, 0, 0, 1, 1)
        self.actionbutton_14 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_14.sizePolicy().hasHeightForWidth())
        self.actionbutton_14.setSizePolicy(sizePolicy)
        self.actionbutton_14.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_14.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_14.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_14.setAutoExclusive(True)
        self.actionbutton_14.setObjectName("actionbutton_14")
        self.gridLayout_8.addWidget(self.actionbutton_14, 0, 1, 1, 1)
        self.actionbutton_15 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_15.sizePolicy().hasHeightForWidth())
        self.actionbutton_15.setSizePolicy(sizePolicy)
        self.actionbutton_15.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_15.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_15.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_15.setAutoExclusive(True)
        self.actionbutton_15.setObjectName("actionbutton_15")
        self.gridLayout_8.addWidget(self.actionbutton_15, 0, 2, 1, 1)
        self.actionbutton_17 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_17.sizePolicy().hasHeightForWidth())
        self.actionbutton_17.setSizePolicy(sizePolicy)
        self.actionbutton_17.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_17.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_17.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_17.setAutoExclusive(True)
        self.actionbutton_17.setObjectName("actionbutton_17")
        self.gridLayout_8.addWidget(self.actionbutton_17, 1, 2, 1, 1)
        self.actionbutton_16 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_16.sizePolicy().hasHeightForWidth())
        self.actionbutton_16.setSizePolicy(sizePolicy)
        self.actionbutton_16.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_16.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_16.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_16.setAutoExclusive(True)
        self.actionbutton_16.setObjectName("actionbutton_16")
        self.gridLayout_8.addWidget(self.actionbutton_16, 2, 2, 1, 1)
        self.actionbutton_12 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_12.sizePolicy().hasHeightForWidth())
        self.actionbutton_12.setSizePolicy(sizePolicy)
        self.actionbutton_12.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_12.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_12.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_12.setAutoExclusive(True)
        self.actionbutton_12.setObjectName("actionbutton_12")
        self.gridLayout_8.addWidget(self.actionbutton_12, 1, 1, 1, 1)
        self.actionbutton_13 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_13.sizePolicy().hasHeightForWidth())
        self.actionbutton_13.setSizePolicy(sizePolicy)
        self.actionbutton_13.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_13.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_13.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_13.setAutoExclusive(True)
        self.actionbutton_13.setObjectName("actionbutton_13")
        self.gridLayout_8.addWidget(self.actionbutton_13, 2, 1, 1, 1)
        self.actionbutton_4 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_4.sizePolicy().hasHeightForWidth())
        self.actionbutton_4.setSizePolicy(sizePolicy)
        self.actionbutton_4.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_4.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_4.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_4.setAutoExclusive(True)
        self.actionbutton_4.setObjectName("actionbutton_4")
        self.gridLayout_8.addWidget(self.actionbutton_4, 1, 0, 1, 1)
        self.actionbutton_18 = ActionButton(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_18.sizePolicy().hasHeightForWidth())
        self.actionbutton_18.setSizePolicy(sizePolicy)
        self.actionbutton_18.setMinimumSize(QtCore.QSize(120, 32))
        self.actionbutton_18.setMaximumSize(QtCore.QSize(120, 38))
        self.actionbutton_18.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_18.setAutoExclusive(True)
        self.actionbutton_18.setObjectName("actionbutton_18")
        self.gridLayout_8.addWidget(self.actionbutton_18, 2, 0, 1, 1)
        self.verticalLayout_26.addLayout(self.gridLayout_8)
        self.label_23 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QtCore.QSize(0, 27))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_26.addWidget(self.label_23)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, 5, -1)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.ref_coilumn_header_12 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_12.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_12.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_12.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_12.setText("")
        self.ref_coilumn_header_12.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_12.setObjectName("ref_coilumn_header_12")
        self.horizontalLayout_82.addWidget(self.ref_coilumn_header_12)
        self.label_22 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(150, 30))
        self.label_22.setMaximumSize(QtCore.QSize(150, 30))
        self.label_22.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_22.setLineWidth(0)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setIndent(0)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_82.addWidget(self.label_22)
        self.probe_tool_number = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_tool_number.sizePolicy().hasHeightForWidth())
        self.probe_tool_number.setSizePolicy(sizePolicy)
        self.probe_tool_number.setMinimumSize(QtCore.QSize(100, 30))
        self.probe_tool_number.setMaximumSize(QtCore.QSize(100, 30))
        self.probe_tool_number.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.probe_tool_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probe_tool_number.setObjectName("probe_tool_number")
        self.horizontalLayout_82.addWidget(self.probe_tool_number)
        self.label_5 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(130, 30))
        self.label_5.setMaximumSize(QtCore.QSize(130, 30))
        self.label_5.setBaseSize(QtCore.QSize(140, 30))
        self.label_5.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_5.setLineWidth(0)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_82.addWidget(self.label_5)
        self.step_off_width = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_off_width.sizePolicy().hasHeightForWidth())
        self.step_off_width.setSizePolicy(sizePolicy)
        self.step_off_width.setMinimumSize(QtCore.QSize(100, 30))
        self.step_off_width.setMaximumSize(QtCore.QSize(100, 30))
        self.step_off_width.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.step_off_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.step_off_width.setObjectName("step_off_width")
        self.horizontalLayout_82.addWidget(self.step_off_width)
        self.verticalLayout_16.addLayout(self.horizontalLayout_82)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.ref_coilumn_header_11 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_11.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_11.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_11.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_11.setText("")
        self.ref_coilumn_header_11.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_11.setObjectName("ref_coilumn_header_11")
        self.horizontalLayout_80.addWidget(self.ref_coilumn_header_11)
        self.label_6 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(150, 30))
        self.label_6.setMaximumSize(QtCore.QSize(150, 30))
        self.label_6.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_6.setLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setIndent(0)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_80.addWidget(self.label_6)
        self.probe_fast_fr = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_fast_fr.sizePolicy().hasHeightForWidth())
        self.probe_fast_fr.setSizePolicy(sizePolicy)
        self.probe_fast_fr.setMinimumSize(QtCore.QSize(100, 30))
        self.probe_fast_fr.setMaximumSize(QtCore.QSize(100, 30))
        self.probe_fast_fr.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.probe_fast_fr.setInputMask("")
        self.probe_fast_fr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probe_fast_fr.setObjectName("probe_fast_fr")
        self.horizontalLayout_80.addWidget(self.probe_fast_fr)
        self.label_7 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(130, 30))
        self.label_7.setMaximumSize(QtCore.QSize(130, 30))
        self.label_7.setBaseSize(QtCore.QSize(140, 30))
        self.label_7.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_7.setLineWidth(0)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_80.addWidget(self.label_7)
        self.probe_slow_fr = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_slow_fr.sizePolicy().hasHeightForWidth())
        self.probe_slow_fr.setSizePolicy(sizePolicy)
        self.probe_slow_fr.setMinimumSize(QtCore.QSize(100, 30))
        self.probe_slow_fr.setMaximumSize(QtCore.QSize(100, 30))
        self.probe_slow_fr.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.probe_slow_fr.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probe_slow_fr.setObjectName("probe_slow_fr")
        self.horizontalLayout_80.addWidget(self.probe_slow_fr)
        self.verticalLayout_16.addLayout(self.horizontalLayout_80)
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.ref_coilumn_header_10 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_10.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_10.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_10.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_10.setText("")
        self.ref_coilumn_header_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_10.setObjectName("ref_coilumn_header_10")
        self.horizontalLayout_81.addWidget(self.ref_coilumn_header_10)
        self.label_11 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(150, 30))
        self.label_11.setMaximumSize(QtCore.QSize(150, 30))
        self.label_11.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_11.setLineWidth(0)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_81.addWidget(self.label_11)
        self.max_xy_distance = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_xy_distance.sizePolicy().hasHeightForWidth())
        self.max_xy_distance.setSizePolicy(sizePolicy)
        self.max_xy_distance.setMinimumSize(QtCore.QSize(100, 30))
        self.max_xy_distance.setMaximumSize(QtCore.QSize(100, 30))
        self.max_xy_distance.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.max_xy_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_xy_distance.setObjectName("max_xy_distance")
        self.horizontalLayout_81.addWidget(self.max_xy_distance)
        self.label_8 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(130, 30))
        self.label_8.setMaximumSize(QtCore.QSize(130, 30))
        self.label_8.setBaseSize(QtCore.QSize(140, 30))
        self.label_8.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_8.setLineWidth(0)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_81.addWidget(self.label_8)
        self.xy_clearance = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_clearance.sizePolicy().hasHeightForWidth())
        self.xy_clearance.setSizePolicy(sizePolicy)
        self.xy_clearance.setMinimumSize(QtCore.QSize(100, 30))
        self.xy_clearance.setMaximumSize(QtCore.QSize(100, 30))
        self.xy_clearance.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.xy_clearance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xy_clearance.setObjectName("xy_clearance")
        self.horizontalLayout_81.addWidget(self.xy_clearance)
        self.verticalLayout_16.addLayout(self.horizontalLayout_81)
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.ref_coilumn_header_9 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_9.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_9.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_9.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_9.setText("")
        self.ref_coilumn_header_9.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_9.setObjectName("ref_coilumn_header_9")
        self.horizontalLayout_79.addWidget(self.ref_coilumn_header_9)
        self.label_10 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(150, 30))
        self.label_10.setMaximumSize(QtCore.QSize(150, 30))
        self.label_10.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_10.setLineWidth(0)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setIndent(0)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_79.addWidget(self.label_10)
        self.max_z_distance = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_z_distance.sizePolicy().hasHeightForWidth())
        self.max_z_distance.setSizePolicy(sizePolicy)
        self.max_z_distance.setMinimumSize(QtCore.QSize(100, 30))
        self.max_z_distance.setMaximumSize(QtCore.QSize(100, 30))
        self.max_z_distance.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.max_z_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.max_z_distance.setObjectName("max_z_distance")
        self.horizontalLayout_79.addWidget(self.max_z_distance)
        self.label_9 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(130, 30))
        self.label_9.setMaximumSize(QtCore.QSize(130, 30))
        self.label_9.setBaseSize(QtCore.QSize(140, 30))
        self.label_9.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_9.setLineWidth(0)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_79.addWidget(self.label_9)
        self.z_clearance = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_clearance.sizePolicy().hasHeightForWidth())
        self.z_clearance.setSizePolicy(sizePolicy)
        self.z_clearance.setMinimumSize(QtCore.QSize(100, 30))
        self.z_clearance.setMaximumSize(QtCore.QSize(100, 30))
        self.z_clearance.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.z_clearance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.z_clearance.setObjectName("z_clearance")
        self.horizontalLayout_79.addWidget(self.z_clearance)
        self.verticalLayout_16.addLayout(self.horizontalLayout_79)
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.ref_coilumn_header_8 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_8.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_8.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_8.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_8.setText("")
        self.ref_coilumn_header_8.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_8.setObjectName("ref_coilumn_header_8")
        self.horizontalLayout_78.addWidget(self.ref_coilumn_header_8)
        self.label_12 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(150, 30))
        self.label_12.setMaximumSize(QtCore.QSize(150, 30))
        self.label_12.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_12.setLineWidth(0)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setIndent(0)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_78.addWidget(self.label_12)
        self.extra_probe_depth = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extra_probe_depth.sizePolicy().hasHeightForWidth())
        self.extra_probe_depth.setSizePolicy(sizePolicy)
        self.extra_probe_depth.setMinimumSize(QtCore.QSize(100, 30))
        self.extra_probe_depth.setMaximumSize(QtCore.QSize(100, 30))
        self.extra_probe_depth.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.extra_probe_depth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.extra_probe_depth.setObjectName("extra_probe_depth")
        self.horizontalLayout_78.addWidget(self.extra_probe_depth)
        self.label_13 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(130, 30))
        self.label_13.setMaximumSize(QtCore.QSize(130, 30))
        self.label_13.setBaseSize(QtCore.QSize(140, 30))
        self.label_13.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_13.setLineWidth(0)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setIndent(0)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_78.addWidget(self.label_13)
        self.calibration_dia = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calibration_dia.sizePolicy().hasHeightForWidth())
        self.calibration_dia.setSizePolicy(sizePolicy)
        self.calibration_dia.setMinimumSize(QtCore.QSize(100, 30))
        self.calibration_dia.setMaximumSize(QtCore.QSize(100, 30))
        self.calibration_dia.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.calibration_dia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.calibration_dia.setObjectName("calibration_dia")
        self.horizontalLayout_78.addWidget(self.calibration_dia)
        self.verticalLayout_16.addLayout(self.horizontalLayout_78)
        self.horizontalLayout_102 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.ref_coilumn_header_7 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_7.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_7.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_7.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_7.setText("")
        self.ref_coilumn_header_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_7.setObjectName("ref_coilumn_header_7")
        self.horizontalLayout_102.addWidget(self.ref_coilumn_header_7)
        self.label_54 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy)
        self.label_54.setMinimumSize(QtCore.QSize(130, 30))
        self.label_54.setMaximumSize(QtCore.QSize(130, 30))
        self.label_54.setBaseSize(QtCore.QSize(140, 30))
        self.label_54.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_54.setLineWidth(0)
        self.label_54.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_54.setIndent(0)
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_102.addWidget(self.label_54)
        self.step_off_width_2 = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_off_width_2.sizePolicy().hasHeightForWidth())
        self.step_off_width_2.setSizePolicy(sizePolicy)
        self.step_off_width_2.setMinimumSize(QtCore.QSize(100, 30))
        self.step_off_width_2.setMaximumSize(QtCore.QSize(100, 30))
        self.step_off_width_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.step_off_width_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.step_off_width_2.setObjectName("step_off_width_2")
        self.horizontalLayout_102.addWidget(self.step_off_width_2)
        self.verticalLayout_16.addLayout(self.horizontalLayout_102)
        self.verticalLayout_26.addLayout(self.verticalLayout_16)
        self.label_25 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(0, 27))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_26.addWidget(self.label_25)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(-1, 0, 5, -1)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.label_52 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(0, 30))
        self.label_52.setMaximumSize(QtCore.QSize(130, 30))
        self.label_52.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_52.setLineWidth(0)
        self.label_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_52.setIndent(0)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_77.addWidget(self.label_52)
        self.probed_diameter_2 = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probed_diameter_2.sizePolicy().hasHeightForWidth())
        self.probed_diameter_2.setSizePolicy(sizePolicy)
        self.probed_diameter_2.setMinimumSize(QtCore.QSize(80, 30))
        self.probed_diameter_2.setMaximumSize(QtCore.QSize(80, 30))
        self.probed_diameter_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.probed_diameter_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probed_diameter_2.setReadOnly(True)
        self.probed_diameter_2.setObjectName("probed_diameter_2")
        self.horizontalLayout_77.addWidget(self.probed_diameter_2)
        self.label_15 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(60, 30))
        self.label_15.setMaximumSize(QtCore.QSize(60, 30))
        self.label_15.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_15.setLineWidth(0)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setIndent(0)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_77.addWidget(self.label_15)
        self.x_probed_width = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_probed_width.sizePolicy().hasHeightForWidth())
        self.x_probed_width.setSizePolicy(sizePolicy)
        self.x_probed_width.setMinimumSize(QtCore.QSize(80, 30))
        self.x_probed_width.setMaximumSize(QtCore.QSize(80, 30))
        self.x_probed_width.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.x_probed_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_probed_width.setReadOnly(True)
        self.x_probed_width.setObjectName("x_probed_width")
        self.horizontalLayout_77.addWidget(self.x_probed_width)
        self.label_14 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(95, 30))
        self.label_14.setMaximumSize(QtCore.QSize(95, 30))
        self.label_14.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setLineWidth(0)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setIndent(0)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_77.addWidget(self.label_14)
        self.x_probed_pos = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_probed_pos.sizePolicy().hasHeightForWidth())
        self.x_probed_pos.setSizePolicy(sizePolicy)
        self.x_probed_pos.setMinimumSize(QtCore.QSize(80, 30))
        self.x_probed_pos.setMaximumSize(QtCore.QSize(80, 30))
        self.x_probed_pos.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.x_probed_pos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_probed_pos.setReadOnly(True)
        self.x_probed_pos.setObjectName("x_probed_pos")
        self.horizontalLayout_77.addWidget(self.x_probed_pos)
        self.verticalLayout_25.addLayout(self.horizontalLayout_77)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_30 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QtCore.QSize(0, 30))
        self.label_30.setMaximumSize(QtCore.QSize(130, 30))
        self.label_30.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_30.setLineWidth(0)
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setIndent(0)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_5.addWidget(self.label_30)
        self.x_probed_width_2 = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_probed_width_2.sizePolicy().hasHeightForWidth())
        self.x_probed_width_2.setSizePolicy(sizePolicy)
        self.x_probed_width_2.setMinimumSize(QtCore.QSize(80, 30))
        self.x_probed_width_2.setMaximumSize(QtCore.QSize(80, 30))
        self.x_probed_width_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.x_probed_width_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_probed_width_2.setReadOnly(True)
        self.x_probed_width_2.setObjectName("x_probed_width_2")
        self.horizontalLayout_5.addWidget(self.x_probed_width_2)
        self.label_17 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QtCore.QSize(60, 30))
        self.label_17.setMaximumSize(QtCore.QSize(60, 30))
        self.label_17.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_17.setLineWidth(0)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setIndent(0)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        self.probed_diameter = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probed_diameter.sizePolicy().hasHeightForWidth())
        self.probed_diameter.setSizePolicy(sizePolicy)
        self.probed_diameter.setMinimumSize(QtCore.QSize(80, 30))
        self.probed_diameter.setMaximumSize(QtCore.QSize(80, 30))
        self.probed_diameter.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.probed_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.probed_diameter.setReadOnly(True)
        self.probed_diameter.setObjectName("probed_diameter")
        self.horizontalLayout_5.addWidget(self.probed_diameter)
        self.label_16 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(95, 30))
        self.label_16.setMaximumSize(QtCore.QSize(95, 30))
        self.label_16.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_16.setLineWidth(0)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setIndent(0)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.z_probed_pos = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_probed_pos.sizePolicy().hasHeightForWidth())
        self.z_probed_pos.setSizePolicy(sizePolicy)
        self.z_probed_pos.setMinimumSize(QtCore.QSize(80, 30))
        self.z_probed_pos.setMaximumSize(QtCore.QSize(80, 30))
        self.z_probed_pos.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.z_probed_pos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.z_probed_pos.setReadOnly(True)
        self.z_probed_pos.setObjectName("z_probed_pos")
        self.horizontalLayout_5.addWidget(self.z_probed_pos)
        self.verticalLayout_25.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.ref_coilumn_header = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header.setSizePolicy(sizePolicy)
        self.ref_coilumn_header.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header.setText("")
        self.ref_coilumn_header.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header.setObjectName("ref_coilumn_header")
        self.horizontalLayout_76.addWidget(self.ref_coilumn_header)
        self.label_50 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QtCore.QSize(60, 30))
        self.label_50.setMaximumSize(QtCore.QSize(60, 30))
        self.label_50.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_50.setLineWidth(0)
        self.label_50.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_50.setIndent(0)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_76.addWidget(self.label_50)
        self.y_probed_width = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_probed_width.sizePolicy().hasHeightForWidth())
        self.y_probed_width.setSizePolicy(sizePolicy)
        self.y_probed_width.setMinimumSize(QtCore.QSize(80, 30))
        self.y_probed_width.setMaximumSize(QtCore.QSize(80, 30))
        self.y_probed_width.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.y_probed_width.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_probed_width.setReadOnly(True)
        self.y_probed_width.setObjectName("y_probed_width")
        self.horizontalLayout_76.addWidget(self.y_probed_width)
        self.label_18 = QtWidgets.QLabel(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(95, 30))
        self.label_18.setMaximumSize(QtCore.QSize(95, 30))
        self.label_18.setStyleSheet("QLabel{\n"
"font: 75 14pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_18.setLineWidth(0)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setIndent(0)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_76.addWidget(self.label_18)
        self.y_probed_pos = QtWidgets.QLineEdit(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_probed_pos.sizePolicy().hasHeightForWidth())
        self.y_probed_pos.setSizePolicy(sizePolicy)
        self.y_probed_pos.setMinimumSize(QtCore.QSize(80, 30))
        self.y_probed_pos.setMaximumSize(QtCore.QSize(80, 30))
        self.y_probed_pos.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.y_probed_pos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_probed_pos.setReadOnly(True)
        self.y_probed_pos.setObjectName("y_probed_pos")
        self.horizontalLayout_76.addWidget(self.y_probed_pos)
        self.verticalLayout_25.addLayout(self.horizontalLayout_76)
        self.verticalLayout_26.addLayout(self.verticalLayout_25)
        self.mdi_entry_box_2 = MDIEntry(self.frame_20)
        self.mdi_entry_box_2.setMinimumSize(QtCore.QSize(0, 35))
        self.mdi_entry_box_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.mdi_entry_box_2.setFont(font)
        self.mdi_entry_box_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.mdi_entry_box_2.setObjectName("mdi_entry_box_2")
        self.verticalLayout_26.addWidget(self.mdi_entry_box_2)
        self.horizontalLayout_70.addWidget(self.frame_20)
        self.horizontalLayout_100 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.frame_23 = QtWidgets.QFrame(self.probing_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_100.addWidget(self.frame_23)
        self.horizontalLayout_70.addLayout(self.horizontalLayout_100)
        self.probe_tab_widget = QtWidgets.QTabWidget(self.probing_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_tab_widget.sizePolicy().hasHeightForWidth())
        self.probe_tab_widget.setSizePolicy(sizePolicy)
        self.probe_tab_widget.setMinimumSize(QtCore.QSize(1079, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(13)
        self.probe_tab_widget.setFont(font)
        self.probe_tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.probe_tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.probe_tab_widget.setIconSize(QtCore.QSize(25, 16))
        self.probe_tab_widget.setObjectName("probe_tab_widget")
        self.outside_corners_tab = QtWidgets.QWidget()
        self.outside_corners_tab.setObjectName("outside_corners_tab")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.outside_corners_tab)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.frame_16 = QtWidgets.QFrame(self.outside_corners_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(465, 465))
        self.frame_16.setMaximumSize(QtCore.QSize(465, 465))
        self.frame_16.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setLineWidth(0)
        self.frame_16.setObjectName("frame_16")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_16)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(2, 2, 461, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_10 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_10.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/front_middle_edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon10)
        self.pushButton_10.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_14 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_14.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/left_side_edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 1, 0, 1, 1)
        self.pushButton_12 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_12.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/front_left_outside_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.pushButton_13 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_13.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/back_right_outside_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon13)
        self.pushButton_13.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 0, 2, 1, 1)
        self.pushButton_11 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_11.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/front_right_outside_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon14)
        self.pushButton_11.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_15 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_15.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/z_top.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon15)
        self.pushButton_15.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.pushButton_17 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_17.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_17.setStyleSheet("")
        self.pushButton_17.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/back_middle_outside_edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon16)
        self.pushButton_17.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 1, 1, 1)
        self.pushButton_18 = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_18.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_18.setStyleSheet("")
        self.pushButton_18.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/right_side_edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon17.addPixmap(QtGui.QPixmap(":/images/right_side_edge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon17)
        self.pushButton_18.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 1, 2, 1, 1)
        self.probe_front_left_top_corner = SubCallButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probe_front_left_top_corner.sizePolicy().hasHeightForWidth())
        self.probe_front_left_top_corner.setSizePolicy(sizePolicy)
        self.probe_front_left_top_corner.setMinimumSize(QtCore.QSize(140, 140))
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/images/back_left_outside_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.probe_front_left_top_corner.setIcon(icon18)
        self.probe_front_left_top_corner.setIconSize(QtCore.QSize(130, 130))
        self.probe_front_left_top_corner.setObjectName("probe_front_left_top_corner")
        self.gridLayout_2.addWidget(self.probe_front_left_top_corner, 0, 0, 1, 1)
        self.horizontalLayout_61.addWidget(self.frame_16)
        self.horizontalLayout_63.addLayout(self.horizontalLayout_61)
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_62.setContentsMargins(0, -1, -1, 170)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.label_36 = QtWidgets.QLabel(self.outside_corners_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QtCore.QSize(441, 311))
        self.label_36.setMaximumSize(QtCore.QSize(441, 311))
        self.label_36.setStyleSheet("image: url(:/images/probe_corner_group_3d_images.png);")
        self.label_36.setText("")
        self.label_36.setScaledContents(True)
        self.label_36.setIndent(0)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_62.addWidget(self.label_36)
        self.horizontalLayout_63.addLayout(self.horizontalLayout_62)
        self.probe_tab_widget.addTab(self.outside_corners_tab, "")
        self.inside_corners_tab = QtWidgets.QWidget()
        self.inside_corners_tab.setObjectName("inside_corners_tab")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.inside_corners_tab)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setContentsMargins(30, -1, -1, -1)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.frame_17 = QtWidgets.QFrame(self.inside_corners_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(465, 465))
        self.frame_17.setMaximumSize(QtCore.QSize(465, 465))
        self.frame_17.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_17)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(7, 7, 451, 451))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_19 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_19.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_19.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_19.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/images/y_minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon19)
        self.pushButton_19.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_3.addWidget(self.pushButton_19, 2, 1, 1, 1)
        self.pushButton_25 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_25.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_25.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_25.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/images/inside_back_left_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon20)
        self.pushButton_25.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_3.addWidget(self.pushButton_25, 0, 0, 1, 1)
        self.pushButton_22 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_22.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_22.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_22.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/images/inside_back_right_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon21)
        self.pushButton_22.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 0, 2, 1, 1)
        self.pushButton_21 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_21.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_21.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_21.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/images/inside_front_left_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon22)
        self.pushButton_21.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 2, 0, 1, 1)
        self.pushButton_20 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_20.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_20.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_20.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/images/inside_front_right_corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon23)
        self.pushButton_20.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_3.addWidget(self.pushButton_20, 2, 2, 1, 1)
        self.pushButton_24 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_24.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_24.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_24.setText("")
        self.pushButton_24.setIcon(icon15)
        self.pushButton_24.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_3.addWidget(self.pushButton_24, 1, 1, 1, 1)
        self.pushButton_23 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_23.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_23.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_23.setText("")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/images/x_minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon24)
        self.pushButton_23.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_3.addWidget(self.pushButton_23, 1, 0, 1, 1)
        self.pushButton_26 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_26.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_26.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_26.setText("")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/images/y_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon25)
        self.pushButton_26.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_3.addWidget(self.pushButton_26, 0, 1, 1, 1)
        self.pushButton_27 = SubCallButton(self.gridLayoutWidget_3)
        self.pushButton_27.setMinimumSize(QtCore.QSize(140, 140))
        self.pushButton_27.setMaximumSize(QtCore.QSize(140, 140))
        self.pushButton_27.setText("")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/images/x_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon26)
        self.pushButton_27.setIconSize(QtCore.QSize(125, 125))
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_3.addWidget(self.pushButton_27, 1, 2, 1, 1)
        self.horizontalLayout_65.addWidget(self.frame_17)
        self.horizontalLayout_66.addLayout(self.horizontalLayout_65)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setContentsMargins(0, -1, -1, 170)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.label_35 = QtWidgets.QLabel(self.inside_corners_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QtCore.QSize(441, 301))
        self.label_35.setMaximumSize(QtCore.QSize(441, 301))
        self.label_35.setStyleSheet("image: url(:/images/inside_corners_3d_image.png);")
        self.label_35.setText("")
        self.label_35.setScaledContents(True)
        self.label_35.setIndent(0)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_64.addWidget(self.label_35)
        self.horizontalLayout_66.addLayout(self.horizontalLayout_64)
        self.probe_tab_widget.addTab(self.inside_corners_tab, "")
        self.boss_and_pocket_tab = QtWidgets.QWidget()
        self.boss_and_pocket_tab.setObjectName("boss_and_pocket_tab")
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout(self.boss_and_pocket_tab)
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.frame_18 = QtWidgets.QFrame(self.boss_and_pocket_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(506, 461))
        self.frame_18.setMaximumSize(QtCore.QSize(506, 461))
        self.frame_18.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.frame_18)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(68, 3, 371, 372))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_35 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_35.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_35.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_35.setStyleSheet("")
        self.pushButton_35.setText("")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/images/round_pocket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon27)
        self.pushButton_35.setIconSize(QtCore.QSize(145, 145))
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_4.addWidget(self.pushButton_35, 0, 1, 1, 1)
        self.pushButton_33 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_33.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_33.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_33.setStyleSheet("")
        self.pushButton_33.setText("")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/images/rect_pocket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon28)
        self.pushButton_33.setIconSize(QtCore.QSize(145, 145))
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_4.addWidget(self.pushButton_33, 1, 1, 1, 1)
        self.pushButton_34 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_34.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_34.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_34.setStyleSheet("")
        self.pushButton_34.setText("")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/images/boss_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon29)
        self.pushButton_34.setIconSize(QtCore.QSize(170, 170))
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_4.addWidget(self.pushButton_34, 0, 0, 1, 1)
        self.pushButton_32 = SubCallButton(self.gridLayoutWidget_4)
        self.pushButton_32.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_32.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_32.setStyleSheet("")
        self.pushButton_32.setText("")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/images/rect_boss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_32.setIcon(icon30)
        self.pushButton_32.setIconSize(QtCore.QSize(170, 170))
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_4.addWidget(self.pushButton_32, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_18)
        self.frame_3.setGeometry(QtCore.QRect(3, 393, 500, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 65))
        self.frame_3.setMaximumSize(QtCore.QSize(500, 65))
        self.frame_3.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.step_increment_label_4 = QtWidgets.QLabel(self.frame_3)
        self.step_increment_label_4.setMinimumSize(QtCore.QSize(60, 40))
        self.step_increment_label_4.setMaximumSize(QtCore.QSize(60, 40))
        self.step_increment_label_4.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.step_increment_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.step_increment_label_4.setObjectName("step_increment_label_4")
        self.horizontalLayout_3.addWidget(self.step_increment_label_4)
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setMinimumSize(QtCore.QSize(80, 0))
        self.label_33.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_33.setStyleSheet("QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setIndent(0)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_3.addWidget(self.label_33)
        self.diameter_hint_2 = QtWidgets.QLineEdit(self.frame_3)
        self.diameter_hint_2.setMinimumSize(QtCore.QSize(80, 40))
        self.diameter_hint_2.setMaximumSize(QtCore.QSize(80, 40))
        self.diameter_hint_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.diameter_hint_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diameter_hint_2.setObjectName("diameter_hint_2")
        self.horizontalLayout_3.addWidget(self.diameter_hint_2)
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setMinimumSize(QtCore.QSize(40, 0))
        self.label_21.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_21.setStyleSheet("QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setIndent(0)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_3.addWidget(self.label_21)
        self.x_hint_2 = QtWidgets.QLineEdit(self.frame_3)
        self.x_hint_2.setMinimumSize(QtCore.QSize(80, 40))
        self.x_hint_2.setMaximumSize(QtCore.QSize(80, 40))
        self.x_hint_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.x_hint_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_hint_2.setObjectName("x_hint_2")
        self.horizontalLayout_3.addWidget(self.x_hint_2)
        self.label_34 = QtWidgets.QLabel(self.frame_3)
        self.label_34.setMinimumSize(QtCore.QSize(40, 0))
        self.label_34.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_34.setStyleSheet("QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setIndent(0)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_3.addWidget(self.label_34)
        self.y_hint_2 = QtWidgets.QLineEdit(self.frame_3)
        self.y_hint_2.setMinimumSize(QtCore.QSize(80, 40))
        self.y_hint_2.setMaximumSize(QtCore.QSize(80, 40))
        self.y_hint_2.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.y_hint_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_hint_2.setObjectName("y_hint_2")
        self.horizontalLayout_3.addWidget(self.y_hint_2)
        self.horizontalLayout_46.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_67.addWidget(self.frame_18)
        self.horizontalLayout_69.addLayout(self.horizontalLayout_67)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setContentsMargins(0, -1, -1, 170)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.label_31 = QtWidgets.QLabel(self.boss_and_pocket_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QtCore.QSize(441, 281))
        self.label_31.setMaximumSize(QtCore.QSize(441, 281))
        self.label_31.setStyleSheet("image: url(:/images/boss_pocket_3d_image.png);")
        self.label_31.setText("")
        self.label_31.setScaledContents(True)
        self.label_31.setIndent(0)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_68.addWidget(self.label_31)
        self.horizontalLayout_69.addLayout(self.horizontalLayout_68)
        self.probe_tab_widget.addTab(self.boss_and_pocket_tab, "")
        self.valley_and_ridge_tab = QtWidgets.QWidget()
        self.valley_and_ridge_tab.setObjectName("valley_and_ridge_tab")
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout(self.valley_and_ridge_tab)
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setContentsMargins(70, -1, -1, -1)
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.frame_19 = QtWidgets.QFrame(self.valley_and_ridge_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QtCore.QSize(405, 465))
        self.frame_19.setMaximumSize(QtCore.QSize(405, 465))
        self.frame_19.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.frame_19)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(19, 3, 371, 372))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_36 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_36.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_36.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_36.setStyleSheet("")
        self.pushButton_36.setText("")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/images/probe_y_valley.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon31)
        self.pushButton_36.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_5.addWidget(self.pushButton_36, 0, 1, 1, 1)
        self.pushButton_39 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_39.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_39.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_39.setStyleSheet("")
        self.pushButton_39.setText("")
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/images/probe_y_ridge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon32)
        self.pushButton_39.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_5.addWidget(self.pushButton_39, 1, 1, 1, 1)
        self.pushButton_37 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_37.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_37.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_37.setStyleSheet("")
        self.pushButton_37.setText("")
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/images/probe_x_valley.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_37.setIcon(icon33)
        self.pushButton_37.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_5.addWidget(self.pushButton_37, 0, 0, 1, 1)
        self.pushButton_38 = SubCallButton(self.gridLayoutWidget_5)
        self.pushButton_38.setMinimumSize(QtCore.QSize(170, 170))
        self.pushButton_38.setMaximumSize(QtCore.QSize(170, 170))
        self.pushButton_38.setStyleSheet("")
        self.pushButton_38.setText("")
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/images/probe_x_ridge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_38.setIcon(icon34)
        self.pushButton_38.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_5.addWidget(self.pushButton_38, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_19)
        self.frame_5.setGeometry(QtCore.QRect(3, 393, 400, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(400, 70))
        self.frame_5.setMaximumSize(QtCore.QSize(400, 70))
        self.frame_5.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.step_increment_label_5 = QtWidgets.QLabel(self.frame_5)
        self.step_increment_label_5.setMinimumSize(QtCore.QSize(115, 40))
        self.step_increment_label_5.setMaximumSize(QtCore.QSize(115, 40))
        self.step_increment_label_5.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(191, 191, 191);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(81, 86, 85), stop:0.489795 rgb(99, 102, 102), stop:0.699799 rgb(85, 88, 94), stop:0.90444 rgb(77, 84, 86), stop:0.160246 rgb(83, 84, 91), stop:1 rgb(109, 115, 118));\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.step_increment_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.step_increment_label_5.setObjectName("step_increment_label_5")
        self.horizontalLayout_4.addWidget(self.step_increment_label_5)
        self.label_39 = QtWidgets.QLabel(self.frame_5)
        self.label_39.setMinimumSize(QtCore.QSize(50, 0))
        self.label_39.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_39.setStyleSheet("QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_39.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_39.setIndent(0)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_4.addWidget(self.label_39)
        self.x_hint_3 = QtWidgets.QLineEdit(self.frame_5)
        self.x_hint_3.setMinimumSize(QtCore.QSize(80, 40))
        self.x_hint_3.setMaximumSize(QtCore.QSize(80, 40))
        self.x_hint_3.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.x_hint_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_hint_3.setObjectName("x_hint_3")
        self.horizontalLayout_4.addWidget(self.x_hint_3)
        self.label_40 = QtWidgets.QLabel(self.frame_5)
        self.label_40.setMinimumSize(QtCore.QSize(50, 0))
        self.label_40.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_40.setStyleSheet("QLabel{\n"
"font: 75 15pt \"Bebas Kai\";\n"
"color: rgb(255, 255, 255);\n"
"padding-right: 1px;\n"
"padding-left: 5px;\n"
"border: transparent;\n"
"Background:transparent;\n"
"}")
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setIndent(0)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_4.addWidget(self.label_40)
        self.y_hint_3 = QtWidgets.QLineEdit(self.frame_5)
        self.y_hint_3.setMinimumSize(QtCore.QSize(80, 40))
        self.y_hint_3.setMaximumSize(QtCore.QSize(80, 40))
        self.y_hint_3.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: white;\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.y_hint_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_hint_3.setObjectName("y_hint_3")
        self.horizontalLayout_4.addWidget(self.y_hint_3)
        self.horizontalLayout_71.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_72.addWidget(self.frame_19)
        self.horizontalLayout_74.addLayout(self.horizontalLayout_72)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setContentsMargins(0, -1, -1, 170)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.label_37 = QtWidgets.QLabel(self.valley_and_ridge_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QtCore.QSize(411, 271))
        self.label_37.setMaximumSize(QtCore.QSize(411, 271))
        self.label_37.setStyleSheet("image: url(:/images/ridge_and_valley_group.png);")
        self.label_37.setText("")
        self.label_37.setScaledContents(True)
        self.label_37.setIndent(0)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_73.addWidget(self.label_37)
        self.horizontalLayout_74.addLayout(self.horizontalLayout_73)
        self.probe_tab_widget.addTab(self.valley_and_ridge_tab, "")
        self.rotary_axis_tab = QtWidgets.QWidget()
        self.rotary_axis_tab.setObjectName("rotary_axis_tab")
        self.probe_tab_widget.addTab(self.rotary_axis_tab, "")
        self.multi_axis_tab = QtWidgets.QWidget()
        self.multi_axis_tab.setObjectName("multi_axis_tab")
        self.probe_tab_widget.addTab(self.multi_axis_tab, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.probe_tab_widget.addTab(self.tab_7, "")
        self.probe_help_tab = QtWidgets.QWidget()
        self.probe_help_tab.setObjectName("probe_help_tab")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.probe_help_tab)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.probe_help_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(13)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setMinimumSize(QtCore.QSize(541, 451))
        self.label.setMaximumSize(QtCore.QSize(541, 451))
        self.label.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"    image: url(:/images/step_off_width.png);\n"
"}")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.horizontalLayout_59.addWidget(self.label)
        self.horizontalLayout_60.addLayout(self.horizontalLayout_59)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setMinimumSize(QtCore.QSize(411, 331))
        self.label_2.setMaximumSize(QtCore.QSize(411, 331))
        self.label_2.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"    image: url(:/images/extra_probe_depth.png);\n"
"}")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_57.addWidget(self.label_2)
        self.horizontalLayout_58.addLayout(self.horizontalLayout_57)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_3 = QtWidgets.QLabel(self.tab_8)
        self.label_3.setMinimumSize(QtCore.QSize(785, 407))
        self.label_3.setMaximumSize(QtCore.QSize(785, 407))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"    image: url(:/images/max_distance.png);\n"
"}")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(0)
        self.label_3.setMidLineWidth(0)
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_55.addWidget(self.label_3)
        self.horizontalLayout_56.addLayout(self.horizontalLayout_55)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setMinimumSize(QtCore.QSize(791, 391))
        self.label_4.setMaximumSize(QtCore.QSize(791, 391))
        self.label_4.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(46, 54, 56);\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    background: rgb(245, 240, 255);\n"
"    image: url(:/images/clearance.png);\n"
"}")
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_53.addWidget(self.label_4)
        self.horizontalLayout_54.addLayout(self.horizontalLayout_53)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.horizontalLayout_52.addLayout(self.verticalLayout_3)
        self.probe_tab_widget.addTab(self.probe_help_tab, "")
        self.horizontalLayout_70.addWidget(self.probe_tab_widget)
        self.tabWidget.addTab(self.probing_tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame = QtWidgets.QFrame(self.tab_4)
        self.frame.setGeometry(QtCore.QRect(120, 250, 1061, 285))
        self.frame.setStyleSheet("QFrame{ \n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(136, 138, 133);\n"
"    border-radius: 4px;\n"
"    background: rgb(46, 52, 54);    \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_40.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_40.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_40.setObjectName("pushButton_40")
        self.horizontalLayout_2.addWidget(self.pushButton_40)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_16.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_16.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_28.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_28.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_2.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_29.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_29.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_2.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_30.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_30.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_2.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_31.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_31.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_2.addWidget(self.pushButton_31)
        self.pushButton_41 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_41.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_41.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_41.setObjectName("pushButton_41")
        self.horizontalLayout_2.addWidget(self.pushButton_41)
        self.pushButton_42 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_42.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_42.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_42.setObjectName("pushButton_42")
        self.horizontalLayout_2.addWidget(self.pushButton_42)
        self.pushButton_43 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_43.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_43.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_43.setObjectName("pushButton_43")
        self.horizontalLayout_2.addWidget(self.pushButton_43)
        self.pushButton_44 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)
        self.pushButton_44.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_44.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_44.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_44.setObjectName("pushButton_44")
        self.horizontalLayout_2.addWidget(self.pushButton_44)
        self.pushButton_45 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)
        self.pushButton_45.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_45.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_45.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_45.setObjectName("pushButton_45")
        self.horizontalLayout_2.addWidget(self.pushButton_45)
        self.pushButton_46 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        self.pushButton_46.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_46.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_46.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_46.setObjectName("pushButton_46")
        self.horizontalLayout_2.addWidget(self.pushButton_46)
        self.pushButton_47 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_47.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_47.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_47.setObjectName("pushButton_47")
        self.horizontalLayout_2.addWidget(self.pushButton_47)
        self.pushButton_48 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        self.pushButton_48.setMinimumSize(QtCore.QSize(101, 45))
        self.pushButton_48.setMaximumSize(QtCore.QSize(101, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_48.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_48.setObjectName("pushButton_48")
        self.horizontalLayout_2.addWidget(self.pushButton_48)
        self.pushButton_85 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_85.sizePolicy().hasHeightForWidth())
        self.pushButton_85.setSizePolicy(sizePolicy)
        self.pushButton_85.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_85.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_85.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")
        self.pushButton_85.setObjectName("pushButton_85")
        self.horizontalLayout_2.addWidget(self.pushButton_85)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_2.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_49 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        self.pushButton_49.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_49.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_49.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Bebas Kai\";\n"
"}")
        self.pushButton_49.setObjectName("pushButton_49")
        self.horizontalLayout_2.addWidget(self.pushButton_49)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)
        self.pushButton_50.setMinimumSize(QtCore.QSize(71, 45))
        self.pushButton_50.setMaximumSize(QtCore.QSize(71, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_50.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_50.setObjectName("pushButton_50")
        self.horizontalLayout_9.addWidget(self.pushButton_50)
        self.pushButton_51 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy)
        self.pushButton_51.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_51.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_51.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_51.setObjectName("pushButton_51")
        self.horizontalLayout_9.addWidget(self.pushButton_51)
        self.pushButton_52 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy)
        self.pushButton_52.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_52.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_52.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_52.setObjectName("pushButton_52")
        self.horizontalLayout_9.addWidget(self.pushButton_52)
        self.pushButton_53 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy)
        self.pushButton_53.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_53.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_53.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_53.setObjectName("pushButton_53")
        self.horizontalLayout_9.addWidget(self.pushButton_53)
        self.pushButton_54 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy)
        self.pushButton_54.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_54.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_54.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_54.setObjectName("pushButton_54")
        self.horizontalLayout_9.addWidget(self.pushButton_54)
        self.pushButton_55 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy)
        self.pushButton_55.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_55.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_55.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_55.setObjectName("pushButton_55")
        self.horizontalLayout_9.addWidget(self.pushButton_55)
        self.pushButton_56 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        self.pushButton_56.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_56.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_56.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_56.setObjectName("pushButton_56")
        self.horizontalLayout_9.addWidget(self.pushButton_56)
        self.pushButton_57 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_57.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_57.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_57.setObjectName("pushButton_57")
        self.horizontalLayout_9.addWidget(self.pushButton_57)
        self.pushButton_58 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        self.pushButton_58.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_58.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_58.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_58.setObjectName("pushButton_58")
        self.horizontalLayout_9.addWidget(self.pushButton_58)
        self.pushButton_59 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        self.pushButton_59.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_59.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_59.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_59.setObjectName("pushButton_59")
        self.horizontalLayout_9.addWidget(self.pushButton_59)
        self.pushButton_60 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy)
        self.pushButton_60.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_60.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_60.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_60.setObjectName("pushButton_60")
        self.horizontalLayout_9.addWidget(self.pushButton_60)
        self.pushButton_61 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_61.sizePolicy().hasHeightForWidth())
        self.pushButton_61.setSizePolicy(sizePolicy)
        self.pushButton_61.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_61.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_61.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_61.setObjectName("pushButton_61")
        self.horizontalLayout_9.addWidget(self.pushButton_61)
        self.pushButton_62 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy)
        self.pushButton_62.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_62.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_62.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_62.setObjectName("pushButton_62")
        self.horizontalLayout_9.addWidget(self.pushButton_62)
        self.pushButton_63 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        self.pushButton_63.setMinimumSize(QtCore.QSize(75, 45))
        self.pushButton_63.setMaximumSize(QtCore.QSize(70, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_63.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_63.setObjectName("pushButton_63")
        self.horizontalLayout_9.addWidget(self.pushButton_63)
        self.pushButton_79 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_79.sizePolicy().hasHeightForWidth())
        self.pushButton_79.setSizePolicy(sizePolicy)
        self.pushButton_79.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_79.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_79.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")
        self.pushButton_79.setObjectName("pushButton_79")
        self.horizontalLayout_9.addWidget(self.pushButton_79)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_4.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_9.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_5.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_9.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_6.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_9.addWidget(self.pushButton_6)
        self.pushButton_64 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy)
        self.pushButton_64.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_64.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_64.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Bebas Kai\";\n"
"}")
        self.pushButton_64.setObjectName("pushButton_64")
        self.horizontalLayout_9.addWidget(self.pushButton_64)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_65 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_65.sizePolicy().hasHeightForWidth())
        self.pushButton_65.setSizePolicy(sizePolicy)
        self.pushButton_65.setMinimumSize(QtCore.QSize(87, 45))
        self.pushButton_65.setMaximumSize(QtCore.QSize(87, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_65.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_65.setObjectName("pushButton_65")
        self.horizontalLayout_10.addWidget(self.pushButton_65)
        self.pushButton_66 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy)
        self.pushButton_66.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_66.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_66.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_66.setObjectName("pushButton_66")
        self.horizontalLayout_10.addWidget(self.pushButton_66)
        self.pushButton_67 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy)
        self.pushButton_67.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_67.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_67.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_67.setObjectName("pushButton_67")
        self.horizontalLayout_10.addWidget(self.pushButton_67)
        self.pushButton_68 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy)
        self.pushButton_68.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_68.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_68.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_68.setObjectName("pushButton_68")
        self.horizontalLayout_10.addWidget(self.pushButton_68)
        self.pushButton_69 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy)
        self.pushButton_69.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_69.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_69.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_69.setObjectName("pushButton_69")
        self.horizontalLayout_10.addWidget(self.pushButton_69)
        self.pushButton_70 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_70.sizePolicy().hasHeightForWidth())
        self.pushButton_70.setSizePolicy(sizePolicy)
        self.pushButton_70.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_70.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_70.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_70.setObjectName("pushButton_70")
        self.horizontalLayout_10.addWidget(self.pushButton_70)
        self.pushButton_71 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy)
        self.pushButton_71.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_71.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_71.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_71.setObjectName("pushButton_71")
        self.horizontalLayout_10.addWidget(self.pushButton_71)
        self.pushButton_72 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        self.pushButton_72.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_72.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_72.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_72.setObjectName("pushButton_72")
        self.horizontalLayout_10.addWidget(self.pushButton_72)
        self.pushButton_73 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_73.sizePolicy().hasHeightForWidth())
        self.pushButton_73.setSizePolicy(sizePolicy)
        self.pushButton_73.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_73.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_73.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_73.setObjectName("pushButton_73")
        self.horizontalLayout_10.addWidget(self.pushButton_73)
        self.pushButton_74 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy)
        self.pushButton_74.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_74.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_74.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_74.setObjectName("pushButton_74")
        self.horizontalLayout_10.addWidget(self.pushButton_74)
        self.pushButton_75 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_75.sizePolicy().hasHeightForWidth())
        self.pushButton_75.setSizePolicy(sizePolicy)
        self.pushButton_75.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_75.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_75.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_75.setObjectName("pushButton_75")
        self.horizontalLayout_10.addWidget(self.pushButton_75)
        self.pushButton_76 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_76.sizePolicy().hasHeightForWidth())
        self.pushButton_76.setSizePolicy(sizePolicy)
        self.pushButton_76.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_76.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_76.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_76.setObjectName("pushButton_76")
        self.horizontalLayout_10.addWidget(self.pushButton_76)
        self.pushButton_77 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_77.sizePolicy().hasHeightForWidth())
        self.pushButton_77.setSizePolicy(sizePolicy)
        self.pushButton_77.setMinimumSize(QtCore.QSize(110, 45))
        self.pushButton_77.setMaximumSize(QtCore.QSize(110, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_77.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_77.setObjectName("pushButton_77")
        self.horizontalLayout_10.addWidget(self.pushButton_77)
        self.pushButton_83 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_83.sizePolicy().hasHeightForWidth())
        self.pushButton_83.setSizePolicy(sizePolicy)
        self.pushButton_83.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_83.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_83.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")
        self.pushButton_83.setObjectName("pushButton_83")
        self.horizontalLayout_10.addWidget(self.pushButton_83)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_7.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_10.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_9.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.pushButton_78 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_78.sizePolicy().hasHeightForWidth())
        self.pushButton_78.setSizePolicy(sizePolicy)
        self.pushButton_78.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_78.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_78.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Bebas Kai\";\n"
"}")
        self.pushButton_78.setObjectName("pushButton_78")
        self.horizontalLayout_10.addWidget(self.pushButton_78)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(7)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_80 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_80.sizePolicy().hasHeightForWidth())
        self.pushButton_80.setSizePolicy(sizePolicy)
        self.pushButton_80.setMinimumSize(QtCore.QSize(115, 45))
        self.pushButton_80.setMaximumSize(QtCore.QSize(115, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_80.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_80.setObjectName("pushButton_80")
        self.horizontalLayout_12.addWidget(self.pushButton_80)
        self.pushButton_81 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_81.sizePolicy().hasHeightForWidth())
        self.pushButton_81.setSizePolicy(sizePolicy)
        self.pushButton_81.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_81.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_81.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_81.setObjectName("pushButton_81")
        self.horizontalLayout_12.addWidget(self.pushButton_81)
        self.pushButton_82 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_82.sizePolicy().hasHeightForWidth())
        self.pushButton_82.setSizePolicy(sizePolicy)
        self.pushButton_82.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_82.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_82.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_82.setObjectName("pushButton_82")
        self.horizontalLayout_12.addWidget(self.pushButton_82)
        self.pushButton_84 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_84.sizePolicy().hasHeightForWidth())
        self.pushButton_84.setSizePolicy(sizePolicy)
        self.pushButton_84.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_84.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_84.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_84.setObjectName("pushButton_84")
        self.horizontalLayout_12.addWidget(self.pushButton_84)
        self.pushButton_86 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy)
        self.pushButton_86.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_86.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_86.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_86.setObjectName("pushButton_86")
        self.horizontalLayout_12.addWidget(self.pushButton_86)
        self.pushButton_87 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_87.sizePolicy().hasHeightForWidth())
        self.pushButton_87.setSizePolicy(sizePolicy)
        self.pushButton_87.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_87.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_87.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_87.setObjectName("pushButton_87")
        self.horizontalLayout_12.addWidget(self.pushButton_87)
        self.pushButton_88 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_88.sizePolicy().hasHeightForWidth())
        self.pushButton_88.setSizePolicy(sizePolicy)
        self.pushButton_88.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_88.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_88.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_88.setObjectName("pushButton_88")
        self.horizontalLayout_12.addWidget(self.pushButton_88)
        self.pushButton_89 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_89.sizePolicy().hasHeightForWidth())
        self.pushButton_89.setSizePolicy(sizePolicy)
        self.pushButton_89.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_89.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_89.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_89.setObjectName("pushButton_89")
        self.horizontalLayout_12.addWidget(self.pushButton_89)
        self.pushButton_90 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_90.sizePolicy().hasHeightForWidth())
        self.pushButton_90.setSizePolicy(sizePolicy)
        self.pushButton_90.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_90.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_90.setFont(font)
        self.pushButton_90.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_90.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_90.setObjectName("pushButton_90")
        self.horizontalLayout_12.addWidget(self.pushButton_90)
        self.pushButton_91 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_91.sizePolicy().hasHeightForWidth())
        self.pushButton_91.setSizePolicy(sizePolicy)
        self.pushButton_91.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_91.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_91.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_91.setObjectName("pushButton_91")
        self.horizontalLayout_12.addWidget(self.pushButton_91)
        self.pushButton_92 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_92.sizePolicy().hasHeightForWidth())
        self.pushButton_92.setSizePolicy(sizePolicy)
        self.pushButton_92.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_92.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_92.setFont(font)
        self.pushButton_92.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_92.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_92.setObjectName("pushButton_92")
        self.horizontalLayout_12.addWidget(self.pushButton_92)
        self.pushButton_93 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_93.sizePolicy().hasHeightForWidth())
        self.pushButton_93.setSizePolicy(sizePolicy)
        self.pushButton_93.setMinimumSize(QtCore.QSize(78, 45))
        self.pushButton_93.setMaximumSize(QtCore.QSize(82, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_93.setFont(font)
        self.pushButton_93.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_93.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_93.setObjectName("pushButton_93")
        self.horizontalLayout_12.addWidget(self.pushButton_93)
        self.pushButton_94 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_94.sizePolicy().hasHeightForWidth())
        self.pushButton_94.setSizePolicy(sizePolicy)
        self.pushButton_94.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_94.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_94.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_94.setText("")
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/images/up_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_94.setIcon(icon35)
        self.pushButton_94.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_94.setObjectName("pushButton_94")
        self.horizontalLayout_12.addWidget(self.pushButton_94)
        self.pushButton_95 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_95.sizePolicy().hasHeightForWidth())
        self.pushButton_95.setSizePolicy(sizePolicy)
        self.pushButton_95.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_95.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_95.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 12pt \"Bebas Kai\";\n"
"}")
        self.pushButton_95.setObjectName("pushButton_95")
        self.horizontalLayout_12.addWidget(self.pushButton_95)
        self.pushButton_96 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_96.sizePolicy().hasHeightForWidth())
        self.pushButton_96.setSizePolicy(sizePolicy)
        self.pushButton_96.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_96.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_96.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_96.setObjectName("pushButton_96")
        self.horizontalLayout_12.addWidget(self.pushButton_96)
        self.pushButton_97 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_97.sizePolicy().hasHeightForWidth())
        self.pushButton_97.setSizePolicy(sizePolicy)
        self.pushButton_97.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_97.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_97.setFont(font)
        self.pushButton_97.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_97.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_97.setObjectName("pushButton_97")
        self.horizontalLayout_12.addWidget(self.pushButton_97)
        self.pushButton_98 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_98.sizePolicy().hasHeightForWidth())
        self.pushButton_98.setSizePolicy(sizePolicy)
        self.pushButton_98.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_98.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_98.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_98.setText("")
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/images/backspace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_98.setIcon(icon36)
        self.pushButton_98.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_98.setObjectName("pushButton_98")
        self.horizontalLayout_12.addWidget(self.pushButton_98)
        self.pushButton_99 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_99.sizePolicy().hasHeightForWidth())
        self.pushButton_99.setSizePolicy(sizePolicy)
        self.pushButton_99.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_99.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_99.setStyleSheet("QPushButton{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"    color: white;\n"
"    font: 20pt \"Bebas Kai\";\n"
"}")
        self.pushButton_99.setObjectName("pushButton_99")
        self.horizontalLayout_12.addWidget(self.pushButton_99)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_100 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_100.sizePolicy().hasHeightForWidth())
        self.pushButton_100.setSizePolicy(sizePolicy)
        self.pushButton_100.setMinimumSize(QtCore.QSize(55, 45))
        self.pushButton_100.setMaximumSize(QtCore.QSize(55, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_100.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_100.setObjectName("pushButton_100")
        self.horizontalLayout_13.addWidget(self.pushButton_100)
        self.pushButton_101 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_101.sizePolicy().hasHeightForWidth())
        self.pushButton_101.setSizePolicy(sizePolicy)
        self.pushButton_101.setMinimumSize(QtCore.QSize(55, 45))
        self.pushButton_101.setMaximumSize(QtCore.QSize(55, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_101.setFont(font)
        self.pushButton_101.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_101.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_101.setObjectName("pushButton_101")
        self.horizontalLayout_13.addWidget(self.pushButton_101)
        self.pushButton_102 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy)
        self.pushButton_102.setMinimumSize(QtCore.QSize(423, 45))
        self.pushButton_102.setMaximumSize(QtCore.QSize(423, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_102.setStyleSheet("QPushButton{ \n"
"    background: rgb(117, 118, 119);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_102.setText("")
        self.pushButton_102.setObjectName("pushButton_102")
        self.horizontalLayout_13.addWidget(self.pushButton_102)
        self.pushButton_103 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy)
        self.pushButton_103.setMinimumSize(QtCore.QSize(55, 45))
        self.pushButton_103.setMaximumSize(QtCore.QSize(55, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_103.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_103.setObjectName("pushButton_103")
        self.horizontalLayout_13.addWidget(self.pushButton_103)
        self.pushButton_104 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy)
        self.pushButton_104.setMinimumSize(QtCore.QSize(55, 45))
        self.pushButton_104.setMaximumSize(QtCore.QSize(55, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_104.setFont(font)
        self.pushButton_104.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_104.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_104.setObjectName("pushButton_104")
        self.horizontalLayout_13.addWidget(self.pushButton_104)
        self.pushButton_105 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_105.sizePolicy().hasHeightForWidth())
        self.pushButton_105.setSizePolicy(sizePolicy)
        self.pushButton_105.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_105.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_105.setFont(font)
        self.pushButton_105.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_105.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_105.setText("")
        self.pushButton_105.setIcon(icon8)
        self.pushButton_105.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_105.setObjectName("pushButton_105")
        self.horizontalLayout_13.addWidget(self.pushButton_105)
        self.pushButton_106 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_106.sizePolicy().hasHeightForWidth())
        self.pushButton_106.setSizePolicy(sizePolicy)
        self.pushButton_106.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_106.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_106.setFont(font)
        self.pushButton_106.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_106.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_106.setText("")
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/images/down_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_106.setIcon(icon37)
        self.pushButton_106.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_106.setObjectName("pushButton_106")
        self.horizontalLayout_13.addWidget(self.pushButton_106)
        self.pushButton_107 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_107.sizePolicy().hasHeightForWidth())
        self.pushButton_107.setSizePolicy(sizePolicy)
        self.pushButton_107.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_107.setMaximumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_107.setFont(font)
        self.pushButton_107.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_107.setStyleSheet("QPushButton{ \n"
"    background: rgb(147, 148, 149);\n"
"    color: white;\n"
"    font: 18pt \"Bebas Kai\";\n"
"}")
        self.pushButton_107.setText("")
        self.pushButton_107.setIcon(icon9)
        self.pushButton_107.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_107.setObjectName("pushButton_107")
        self.horizontalLayout_13.addWidget(self.pushButton_107)
        self.pushButton_108 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_108.sizePolicy().hasHeightForWidth())
        self.pushButton_108.setSizePolicy(sizePolicy)
        self.pushButton_108.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_108.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_108.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_108.setFont(font)
        self.pushButton_108.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_108.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_108.setObjectName("pushButton_108")
        self.horizontalLayout_13.addWidget(self.pushButton_108)
        self.pushButton_109 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_109.sizePolicy().hasHeightForWidth())
        self.pushButton_109.setSizePolicy(sizePolicy)
        self.pushButton_109.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_109.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_109.setFont(font)
        self.pushButton_109.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_109.setObjectName("pushButton_109")
        self.horizontalLayout_13.addWidget(self.pushButton_109)
        self.pushButton_110 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_110.sizePolicy().hasHeightForWidth())
        self.pushButton_110.setSizePolicy(sizePolicy)
        self.pushButton_110.setMinimumSize(QtCore.QSize(50, 45))
        self.pushButton_110.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_110.setFont(font)
        self.pushButton_110.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_110.setStyleSheet("QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}")
        self.pushButton_110.setObjectName("pushButton_110")
        self.horizontalLayout_13.addWidget(self.pushButton_110)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.verticalLayout_30.addWidget(self.tabWidget)
        self.horizontalLayout_101.addLayout(self.verticalLayout_30)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_24 = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_24.sizePolicy().hasHeightForWidth())
        self.tabWidget_24.setSizePolicy(sizePolicy)
        self.tabWidget_24.setMinimumSize(QtCore.QSize(251, 0))
        self.tabWidget_24.setMaximumSize(QtCore.QSize(251, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(15)
        self.tabWidget_24.setFont(font)
        self.tabWidget_24.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_24.setObjectName("tabWidget_24")
        self.tabWidget_24Page1 = QtWidgets.QWidget()
        self.tabWidget_24Page1.setObjectName("tabWidget_24Page1")
        self.frame_26 = QtWidgets.QFrame(self.tabWidget_24Page1)
        self.frame_26.setGeometry(QtCore.QRect(7, 31, 201, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(51, 57, 59);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_32.setSpacing(12)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.horizontalLayout_106 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_106.setObjectName("horizontalLayout_106")
        self.z_plus_jogbutton = ActionButton(self.frame_26)
        self.z_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_plus_jogbutton.setText("")
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(":/images/z_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_plus_jogbutton.setIcon(icon38)
        self.z_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.z_plus_jogbutton.setObjectName("z_plus_jogbutton")
        self.horizontalLayout_106.addWidget(self.z_plus_jogbutton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_106)
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.z_minus_jogbutton = ActionButton(self.frame_26)
        self.z_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.z_minus_jogbutton.setText("")
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap(":/images/z_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.z_minus_jogbutton.setIcon(icon39)
        self.z_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.z_minus_jogbutton.setObjectName("z_minus_jogbutton")
        self.horizontalLayout_107.addWidget(self.z_minus_jogbutton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_107)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.x_plus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_plus_jogbutton.setSizePolicy(sizePolicy)
        self.x_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.x_plus_jogbutton.setText("")
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap(":/images/x_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_plus_jogbutton.setIcon(icon40)
        self.x_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_plus_jogbutton.setObjectName("x_plus_jogbutton")
        self.gridLayout_6.addWidget(self.x_plus_jogbutton, 1, 2, 1, 1)
        self.x_minus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.x_minus_jogbutton.setSizePolicy(sizePolicy)
        self.x_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.x_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.x_minus_jogbutton.setText("")
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap(":/images/x_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x_minus_jogbutton.setIcon(icon41)
        self.x_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.x_minus_jogbutton.setObjectName("x_minus_jogbutton")
        self.gridLayout_6.addWidget(self.x_minus_jogbutton, 1, 0, 1, 1)
        self.y_minus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.y_minus_jogbutton.setSizePolicy(sizePolicy)
        self.y_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.y_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.y_minus_jogbutton.setText("")
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap(":/images/y_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_minus_jogbutton.setIcon(icon42)
        self.y_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_minus_jogbutton.setObjectName("y_minus_jogbutton")
        self.gridLayout_6.addWidget(self.y_minus_jogbutton, 2, 1, 1, 1)
        self.y_plus_jogbutton = ActionButton(self.frame_26)
        self.y_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.y_plus_jogbutton.setText("")
        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap(":/images/y_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.y_plus_jogbutton.setIcon(icon43)
        self.y_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.y_plus_jogbutton.setObjectName("y_plus_jogbutton")
        self.gridLayout_6.addWidget(self.y_plus_jogbutton, 0, 1, 1, 1)
        self.verticalLayout_32.addLayout(self.gridLayout_6)
        self.horizontalLayout_112 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_112.setObjectName("horizontalLayout_112")
        self.a_minus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_minus_jogbutton.setSizePolicy(sizePolicy)
        self.a_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.a_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.a_minus_jogbutton.setText("")
        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap(":/images/a_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_minus_jogbutton.setIcon(icon44)
        self.a_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_minus_jogbutton.setObjectName("a_minus_jogbutton")
        self.horizontalLayout_112.addWidget(self.a_minus_jogbutton)
        self.a_plus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.a_plus_jogbutton.setSizePolicy(sizePolicy)
        self.a_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.a_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.a_plus_jogbutton.setText("")
        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap(":/images/a_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.a_plus_jogbutton.setIcon(icon45)
        self.a_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.a_plus_jogbutton.setObjectName("a_plus_jogbutton")
        self.horizontalLayout_112.addWidget(self.a_plus_jogbutton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_112)
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.b_minus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_minus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_minus_jogbutton.setSizePolicy(sizePolicy)
        self.b_minus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.b_minus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.b_minus_jogbutton.setText("")
        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap(":/images/b_minus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_minus_jogbutton.setIcon(icon46)
        self.b_minus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.b_minus_jogbutton.setObjectName("b_minus_jogbutton")
        self.horizontalLayout_111.addWidget(self.b_minus_jogbutton)
        self.b_plus_jogbutton = ActionButton(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_plus_jogbutton.sizePolicy().hasHeightForWidth())
        self.b_plus_jogbutton.setSizePolicy(sizePolicy)
        self.b_plus_jogbutton.setMinimumSize(QtCore.QSize(56, 56))
        self.b_plus_jogbutton.setMaximumSize(QtCore.QSize(56, 56))
        self.b_plus_jogbutton.setText("")
        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap(":/images/b_plus_jog_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_plus_jogbutton.setIcon(icon47)
        self.b_plus_jogbutton.setIconSize(QtCore.QSize(48, 48))
        self.b_plus_jogbutton.setObjectName("b_plus_jogbutton")
        self.horizontalLayout_111.addWidget(self.b_plus_jogbutton)
        self.verticalLayout_32.addLayout(self.horizontalLayout_111)
        self.label_20 = QtWidgets.QLabel(self.tabWidget_24Page1)
        self.label_20.setGeometry(QtCore.QRect(55, 3, 150, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(150, 20))
        self.label_20.setMaximumSize(QtCore.QSize(150, 20))
        self.label_20.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabWidget_24Page1)
        self.layoutWidget_2.setGeometry(QtCore.QRect(214, 0, 32, 621))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.statuslabel_15 = StatusLabel(self.layoutWidget_2)
        self.statuslabel_15.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_15.sizePolicy().hasHeightForWidth())
        self.statuslabel_15.setSizePolicy(sizePolicy)
        self.statuslabel_15.setMinimumSize(QtCore.QSize(30, 0))
        self.statuslabel_15.setMaximumSize(QtCore.QSize(30, 16777215))
        self.statuslabel_15.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statuslabel_15.setWordWrap(True)
        self.statuslabel_15.setIndent(0)
        self.statuslabel_15.setProperty("statusItem", "")
        self.statuslabel_15.setObjectName("statuslabel_15")
        self.verticalLayout_12.addWidget(self.statuslabel_15)
        self.statuslabel_16 = StatusLabel(self.layoutWidget_2)
        self.statuslabel_16.setMinimumSize(QtCore.QSize(30, 0))
        self.statuslabel_16.setMaximumSize(QtCore.QSize(30, 16777215))
        self.statuslabel_16.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.statuslabel_16.setWordWrap(True)
        self.statuslabel_16.setIndent(0)
        self.statuslabel_16.setProperty("statusItem", "")
        self.statuslabel_16.setObjectName("statuslabel_16")
        self.verticalLayout_12.addWidget(self.statuslabel_16)
        self.tabWidget_24.addTab(self.tabWidget_24Page1, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.layoutWidget = QtWidgets.QWidget(self.tab_17)
        self.layoutWidget.setGeometry(QtCore.QRect(214, 0, 32, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.statuslabel_13 = StatusLabel(self.layoutWidget)
        self.statuslabel_13.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_13.sizePolicy().hasHeightForWidth())
        self.statuslabel_13.setSizePolicy(sizePolicy)
        self.statuslabel_13.setMinimumSize(QtCore.QSize(30, 0))
        self.statuslabel_13.setMaximumSize(QtCore.QSize(30, 16777215))
        self.statuslabel_13.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statuslabel_13.setWordWrap(True)
        self.statuslabel_13.setIndent(0)
        self.statuslabel_13.setProperty("statusItem", "")
        self.statuslabel_13.setObjectName("statuslabel_13")
        self.verticalLayout_9.addWidget(self.statuslabel_13)
        self.statuslabel_14 = StatusLabel(self.layoutWidget)
        self.statuslabel_14.setMinimumSize(QtCore.QSize(30, 0))
        self.statuslabel_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.statuslabel_14.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.statuslabel_14.setWordWrap(True)
        self.statuslabel_14.setIndent(0)
        self.statuslabel_14.setProperty("statusItem", "")
        self.statuslabel_14.setObjectName("statuslabel_14")
        self.verticalLayout_9.addWidget(self.statuslabel_14)
        self.label_19 = QtWidgets.QLabel(self.tab_17)
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QtCore.QRect(-3, 1, 208, 24))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_19.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: none;\n"
"background-color: transparent;\n"
"font: 14pt \"Bebas Kai\";\n"
"}")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.tabWidget_24.addTab(self.tab_17, "")
        self.verticalLayout.addWidget(self.tabWidget_24)
        self.horizontalLayout_101.addLayout(self.verticalLayout)
        self.verticalLayout_31.addLayout(self.horizontalLayout_101)
        self.main_control_screen_layout_panel = QtWidgets.QHBoxLayout()
        self.main_control_screen_layout_panel.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.main_control_screen_layout_panel.setContentsMargins(12, 0, 12, -1)
        self.main_control_screen_layout_panel.setSpacing(9)
        self.main_control_screen_layout_panel.setObjectName("main_control_screen_layout_panel")
        self.main_control_qframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_control_qframe.sizePolicy().hasHeightForWidth())
        self.main_control_qframe.setSizePolicy(sizePolicy)
        self.main_control_qframe.setMinimumSize(QtCore.QSize(350, 340))
        self.main_control_qframe.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.main_control_qframe.setObjectName("main_control_qframe")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.main_control_qframe)
        self.verticalLayout_28.setContentsMargins(18, 9, 18, 4)
        self.verticalLayout_28.setSpacing(6)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.horizontalLayout_92 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_92.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout_92.setObjectName("horizontalLayout_92")
        self.actionbutton_3 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_3.sizePolicy().hasHeightForWidth())
        self.actionbutton_3.setSizePolicy(sizePolicy)
        self.actionbutton_3.setMinimumSize(QtCore.QSize(0, 52))
        self.actionbutton_3.setMaximumSize(QtCore.QSize(16777215, 52))
        self.actionbutton_3.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_3.setObjectName("actionbutton_3")
        self.horizontalLayout_92.addWidget(self.actionbutton_3)
        self.verticalLayout_28.addLayout(self.horizontalLayout_92)
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.actionbutton_7 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_7.sizePolicy().hasHeightForWidth())
        self.actionbutton_7.setSizePolicy(sizePolicy)
        self.actionbutton_7.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_7.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_7.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_7.setObjectName("actionbutton_7")
        self.horizontalLayout_91.addWidget(self.actionbutton_7)
        self.ref_coilumn_header_13 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_13.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_13.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_13.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_13.setText("")
        self.ref_coilumn_header_13.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_13.setObjectName("ref_coilumn_header_13")
        self.horizontalLayout_91.addWidget(self.ref_coilumn_header_13)
        self.actionbutton_10 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_10.sizePolicy().hasHeightForWidth())
        self.actionbutton_10.setSizePolicy(sizePolicy)
        self.actionbutton_10.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_10.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_10.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_10.setCheckable(True)
        self.actionbutton_10.setObjectName("actionbutton_10")
        self.horizontalLayout_91.addWidget(self.actionbutton_10)
        self.verticalLayout_28.addLayout(self.horizontalLayout_91)
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.actionbutton = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton.sizePolicy().hasHeightForWidth())
        self.actionbutton.setSizePolicy(sizePolicy)
        self.actionbutton.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton.setObjectName("actionbutton")
        self.horizontalLayout_90.addWidget(self.actionbutton)
        self.ref_coilumn_header_14 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_14.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_14.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_14.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_14.setText("")
        self.ref_coilumn_header_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_14.setObjectName("ref_coilumn_header_14")
        self.horizontalLayout_90.addWidget(self.ref_coilumn_header_14)
        self.actionbutton_5 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_5.sizePolicy().hasHeightForWidth())
        self.actionbutton_5.setSizePolicy(sizePolicy)
        self.actionbutton_5.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_5.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_5.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_5.setObjectName("actionbutton_5")
        self.horizontalLayout_90.addWidget(self.actionbutton_5)
        self.verticalLayout_28.addLayout(self.horizontalLayout_90)
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.actionbutton_9 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_9.sizePolicy().hasHeightForWidth())
        self.actionbutton_9.setSizePolicy(sizePolicy)
        self.actionbutton_9.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_9.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_9.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_9.setCheckable(True)
        self.actionbutton_9.setObjectName("actionbutton_9")
        self.horizontalLayout_75.addWidget(self.actionbutton_9)
        self.ref_coilumn_header_15 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_15.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_15.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_15.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_15.setText("")
        self.ref_coilumn_header_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_15.setObjectName("ref_coilumn_header_15")
        self.horizontalLayout_75.addWidget(self.ref_coilumn_header_15)
        self.actionbutton_6 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_6.sizePolicy().hasHeightForWidth())
        self.actionbutton_6.setSizePolicy(sizePolicy)
        self.actionbutton_6.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_6.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_6.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_6.setCheckable(True)
        self.actionbutton_6.setObjectName("actionbutton_6")
        self.horizontalLayout_75.addWidget(self.actionbutton_6)
        self.verticalLayout_28.addLayout(self.horizontalLayout_75)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.actionbutton_8 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_8.sizePolicy().hasHeightForWidth())
        self.actionbutton_8.setSizePolicy(sizePolicy)
        self.actionbutton_8.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_8.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_8.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_8.setCheckable(True)
        self.actionbutton_8.setObjectName("actionbutton_8")
        self.horizontalLayout_88.addWidget(self.actionbutton_8)
        self.ref_coilumn_header_17 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_17.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_17.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_17.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_17.setText("")
        self.ref_coilumn_header_17.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_17.setObjectName("ref_coilumn_header_17")
        self.horizontalLayout_88.addWidget(self.ref_coilumn_header_17)
        self.actionbutton_2 = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionbutton_2.sizePolicy().hasHeightForWidth())
        self.actionbutton_2.setSizePolicy(sizePolicy)
        self.actionbutton_2.setMinimumSize(QtCore.QSize(130, 42))
        self.actionbutton_2.setMaximumSize(QtCore.QSize(130, 42))
        self.actionbutton_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_2.setCheckable(True)
        self.actionbutton_2.setObjectName("actionbutton_2")
        self.horizontalLayout_88.addWidget(self.actionbutton_2)
        self.verticalLayout_28.addLayout(self.horizontalLayout_88)
        self.line = QtWidgets.QFrame(self.main_control_qframe)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line.setStyleSheet("Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_28.addWidget(self.line)
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.power_button = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_button.sizePolicy().hasHeightForWidth())
        self.power_button.setSizePolicy(sizePolicy)
        self.power_button.setMinimumSize(QtCore.QSize(65, 35))
        self.power_button.setMaximumSize(QtCore.QSize(65, 35))
        self.power_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.power_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.power_button.setCheckable(True)
        self.power_button.setObjectName("power_button")
        self.horizontalLayout_89.addWidget(self.power_button)
        self.ref_coilumn_header_16 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_16.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_16.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_16.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_16.setText("")
        self.ref_coilumn_header_16.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_16.setObjectName("ref_coilumn_header_16")
        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_16)
        self.feedrate_2 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedrate_2.sizePolicy().hasHeightForWidth())
        self.feedrate_2.setSizePolicy(sizePolicy)
        self.feedrate_2.setMinimumSize(QtCore.QSize(18, 25))
        self.feedrate_2.setMaximumSize(QtCore.QSize(18, 25))
        self.feedrate_2.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.feedrate_2.setObjectName("feedrate_2")
        self.horizontalLayout_89.addWidget(self.feedrate_2)
        self.label_26 = QtWidgets.QLabel(self.main_control_qframe)
        self.label_26.setMinimumSize(QtCore.QSize(80, 33))
        self.label_26.setMaximumSize(QtCore.QSize(80, 33))
        self.label_26.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_89.addWidget(self.label_26)
        self.ref_coilumn_header_18 = QtWidgets.QLabel(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_18.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_18.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_18.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_18.setText("")
        self.ref_coilumn_header_18.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_18.setObjectName("ref_coilumn_header_18")
        self.horizontalLayout_89.addWidget(self.ref_coilumn_header_18)
        self.exit_button = ActionButton(self.main_control_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setMinimumSize(QtCore.QSize(65, 35))
        self.exit_button.setMaximumSize(QtCore.QSize(65, 35))
        self.exit_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.exit_button.setCheckable(True)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_89.addWidget(self.exit_button)
        self.verticalLayout_28.addLayout(self.horizontalLayout_89)
        self.main_control_screen_layout_panel.addWidget(self.main_control_qframe)
        self.tool_info_qframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_info_qframe.sizePolicy().hasHeightForWidth())
        self.tool_info_qframe.setSizePolicy(sizePolicy)
        self.tool_info_qframe.setMinimumSize(QtCore.QSize(210, 340))
        self.tool_info_qframe.setMaximumSize(QtCore.QSize(210, 340))
        self.tool_info_qframe.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tool_info_qframe.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.tool_info_qframe.setObjectName("tool_info_qframe")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.tool_info_qframe)
        self.verticalLayout_29.setContentsMargins(12, 9, 12, 3)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.horizontalLayout_96 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")
        self.frame_27 = QtWidgets.QFrame(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 38))
        self.frame_27.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_105 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_105.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName("horizontalLayout_105")
        self.ref_coilumn_header_3 = QtWidgets.QLabel(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_coilumn_header_3.sizePolicy().hasHeightForWidth())
        self.ref_coilumn_header_3.setSizePolicy(sizePolicy)
        self.ref_coilumn_header_3.setMinimumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_3.setMaximumSize(QtCore.QSize(15, 36))
        self.ref_coilumn_header_3.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.ref_coilumn_header_3.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_coilumn_header_3.setIndent(0)
        self.ref_coilumn_header_3.setObjectName("ref_coilumn_header_3")
        self.horizontalLayout_105.addWidget(self.ref_coilumn_header_3)
        self.tool_number_entry_box = QtWidgets.QLineEdit(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_number_entry_box.sizePolicy().hasHeightForWidth())
        self.tool_number_entry_box.setSizePolicy(sizePolicy)
        self.tool_number_entry_box.setMinimumSize(QtCore.QSize(55, 0))
        self.tool_number_entry_box.setMaximumSize(QtCore.QSize(55, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tool_number_entry_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tool_number_entry_box.setFont(font)
        self.tool_number_entry_box.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tool_number_entry_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tool_number_entry_box.setStyleSheet("QLineEdit {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.tool_number_entry_box.setFrame(True)
        self.tool_number_entry_box.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_number_entry_box.setObjectName("tool_number_entry_box")
        self.horizontalLayout_105.addWidget(self.tool_number_entry_box)
        self.horizontalLayout_96.addWidget(self.frame_27)
        self.m6_button = MDIButton(self.tool_info_qframe)
        self.m6_button.setMinimumSize(QtCore.QSize(70, 40))
        self.m6_button.setMaximumSize(QtCore.QSize(16777215, 40))
        self.m6_button.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.m6_button.setObjectName("m6_button")
        self.horizontalLayout_96.addWidget(self.m6_button)
        self.verticalLayout_29.addLayout(self.horizontalLayout_96)
        self.horizontalLayout_104 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_104.setObjectName("horizontalLayout_104")
        self.G43 = MDIButton(self.tool_info_qframe)
        self.G43.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G43.sizePolicy().hasHeightForWidth())
        self.G43.setSizePolicy(sizePolicy)
        self.G43.setMinimumSize(QtCore.QSize(0, 40))
        self.G43.setMaximumSize(QtCore.QSize(16777215, 40))
        self.G43.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.G43.setCheckable(True)
        self.G43.setAutoExclusive(True)
        self.G43.setObjectName("G43")
        self.horizontalLayout_104.addWidget(self.G43)
        self.G49 = MDIButton(self.tool_info_qframe)
        self.G49.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G49.sizePolicy().hasHeightForWidth())
        self.G49.setSizePolicy(sizePolicy)
        self.G49.setMinimumSize(QtCore.QSize(0, 40))
        self.G49.setMaximumSize(QtCore.QSize(16777215, 40))
        self.G49.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.G49.setCheckable(True)
        self.G49.setAutoExclusive(True)
        self.G49.setObjectName("G49")
        self.horizontalLayout_104.addWidget(self.G49)
        self.verticalLayout_29.addLayout(self.horizontalLayout_104)
        self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        self.go_to_g30_button_2 = ActionButton(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_to_g30_button_2.sizePolicy().hasHeightForWidth())
        self.go_to_g30_button_2.setSizePolicy(sizePolicy)
        self.go_to_g30_button_2.setMinimumSize(QtCore.QSize(0, 40))
        self.go_to_g30_button_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.go_to_g30_button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.go_to_g30_button_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.go_to_g30_button_2.setObjectName("go_to_g30_button_2")
        self.horizontalLayout_95.addWidget(self.go_to_g30_button_2)
        self.go_to_g30 = MDIButton(self.tool_info_qframe)
        self.go_to_g30.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_to_g30.sizePolicy().hasHeightForWidth())
        self.go_to_g30.setSizePolicy(sizePolicy)
        self.go_to_g30.setMinimumSize(QtCore.QSize(0, 40))
        self.go_to_g30.setMaximumSize(QtCore.QSize(16777215, 40))
        self.go_to_g30.setStyleSheet("MDIButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.go_to_g30.setObjectName("go_to_g30")
        self.horizontalLayout_95.addWidget(self.go_to_g30)
        self.verticalLayout_29.addLayout(self.horizontalLayout_95)
        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_94.setSpacing(5)
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        self.work_column_header_4 = QtWidgets.QLabel(self.tool_info_qframe)
        self.work_column_header_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_4.sizePolicy().hasHeightForWidth())
        self.work_column_header_4.setSizePolicy(sizePolicy)
        self.work_column_header_4.setMinimumSize(QtCore.QSize(60, 33))
        self.work_column_header_4.setMaximumSize(QtCore.QSize(60, 33))
        self.work_column_header_4.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.work_column_header_4.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_4.setWordWrap(True)
        self.work_column_header_4.setIndent(0)
        self.work_column_header_4.setObjectName("work_column_header_4")
        self.horizontalLayout_94.addWidget(self.work_column_header_4)
        self.tool_length = StatusLabel(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_length.sizePolicy().hasHeightForWidth())
        self.tool_length.setSizePolicy(sizePolicy)
        self.tool_length.setMinimumSize(QtCore.QSize(0, 33))
        self.tool_length.setMaximumSize(QtCore.QSize(16777215, 33))
        self.tool_length.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.tool_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_length.setObjectName("tool_length")
        self.horizontalLayout_94.addWidget(self.tool_length)
        self.statuslabel_8 = StatusLabel(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_8.sizePolicy().hasHeightForWidth())
        self.statuslabel_8.setSizePolicy(sizePolicy)
        self.statuslabel_8.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_8.setObjectName("statuslabel_8")
        self.horizontalLayout_94.addWidget(self.statuslabel_8)
        self.verticalLayout_29.addLayout(self.horizontalLayout_94)
        self.horizontalLayout_93 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_93.setSpacing(5)
        self.horizontalLayout_93.setObjectName("horizontalLayout_93")
        self.work_column_header_5 = QtWidgets.QLabel(self.tool_info_qframe)
        self.work_column_header_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_5.sizePolicy().hasHeightForWidth())
        self.work_column_header_5.setSizePolicy(sizePolicy)
        self.work_column_header_5.setMinimumSize(QtCore.QSize(60, 33))
        self.work_column_header_5.setMaximumSize(QtCore.QSize(60, 33))
        self.work_column_header_5.setStyleSheet("QLabel{\n"
"    border-style: none;\n"
"    border-color: rgb(46, 52, 54);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"    background: rgb(46, 52, 54);\n"
"    font: 16pt \"Bebas Kai\";\n"
"}\n"
"")
        self.work_column_header_5.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_5.setWordWrap(True)
        self.work_column_header_5.setIndent(0)
        self.work_column_header_5.setObjectName("work_column_header_5")
        self.horizontalLayout_93.addWidget(self.work_column_header_5)
        self.tool_diameter = StatusLabel(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_diameter.sizePolicy().hasHeightForWidth())
        self.tool_diameter.setSizePolicy(sizePolicy)
        self.tool_diameter.setMinimumSize(QtCore.QSize(0, 33))
        self.tool_diameter.setMaximumSize(QtCore.QSize(16777215, 33))
        self.tool_diameter.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"}")
        self.tool_diameter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tool_diameter.setObjectName("tool_diameter")
        self.horizontalLayout_93.addWidget(self.tool_diameter)
        self.statuslabel_11 = StatusLabel(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_11.sizePolicy().hasHeightForWidth())
        self.statuslabel_11.setSizePolicy(sizePolicy)
        self.statuslabel_11.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_11.setObjectName("statuslabel_11")
        self.horizontalLayout_93.addWidget(self.statuslabel_11)
        self.verticalLayout_29.addLayout(self.horizontalLayout_93)
        self.line_7 = QtWidgets.QFrame(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setMinimumSize(QtCore.QSize(0, 2))
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_7.setStyleSheet("Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_29.addWidget(self.line_7)
        self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_97.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.axisactionbutton_5 = ActionButton(self.tool_info_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_5.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_5.setSizePolicy(sizePolicy)
        self.axisactionbutton_5.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.axisactionbutton_5.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_5.setObjectName("axisactionbutton_5")
        self.horizontalLayout_97.addWidget(self.axisactionbutton_5)
        self.verticalLayout_29.addLayout(self.horizontalLayout_97)
        self.main_control_screen_layout_panel.addWidget(self.tool_info_qframe)
        self.main_dro_qframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_dro_qframe.sizePolicy().hasHeightForWidth())
        self.main_dro_qframe.setSizePolicy(sizePolicy)
        self.main_dro_qframe.setMinimumSize(QtCore.QSize(482, 340))
        self.main_dro_qframe.setMaximumSize(QtCore.QSize(482, 340))
        self.main_dro_qframe.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_dro_qframe.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;\n"
"padding-top: -1px;\n"
"padding-bottom:-1px;\n"
"}")
        self.main_dro_qframe.setObjectName("main_dro_qframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_dro_qframe)
        self.verticalLayout_4.setContentsMargins(-1, 15, -1, 11)
        self.verticalLayout_4.setSpacing(13)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_25 = QtWidgets.QFrame(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_25.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_25.setStyleSheet("QFrame{\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"padding: -5px;\n"
"}")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_103 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_103.setContentsMargins(5, -1, 7, -1)
        self.horizontalLayout_103.setSpacing(8)
        self.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.axis_column_header = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_column_header.sizePolicy().hasHeightForWidth())
        self.axis_column_header.setSizePolicy(sizePolicy)
        self.axis_column_header.setMinimumSize(QtCore.QSize(55, 17))
        self.axis_column_header.setMaximumSize(QtCore.QSize(65, 17))
        self.axis_column_header.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.axis_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.axis_column_header.setObjectName("axis_column_header")
        self.horizontalLayout_103.addWidget(self.axis_column_header)
        self.statuslabel_12 = StatusLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_12.sizePolicy().hasHeightForWidth())
        self.statuslabel_12.setSizePolicy(sizePolicy)
        self.statuslabel_12.setMinimumSize(QtCore.QSize(100, 17))
        self.statuslabel_12.setMaximumSize(QtCore.QSize(100, 17))
        self.statuslabel_12.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_12.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_12.setObjectName("statuslabel_12")
        self.horizontalLayout_103.addWidget(self.statuslabel_12)
        self.work_column_header_2 = QtWidgets.QLabel(self.frame_25)
        self.work_column_header_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_2.sizePolicy().hasHeightForWidth())
        self.work_column_header_2.setSizePolicy(sizePolicy)
        self.work_column_header_2.setMinimumSize(QtCore.QSize(100, 17))
        self.work_column_header_2.setMaximumSize(QtCore.QSize(100, 17))
        self.work_column_header_2.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_2.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_2.setObjectName("work_column_header_2")
        self.horizontalLayout_103.addWidget(self.work_column_header_2)
        self.dtg_column_header = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtg_column_header.sizePolicy().hasHeightForWidth())
        self.dtg_column_header.setSizePolicy(sizePolicy)
        self.dtg_column_header.setMinimumSize(QtCore.QSize(100, 17))
        self.dtg_column_header.setMaximumSize(QtCore.QSize(100, 17))
        self.dtg_column_header.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.dtg_column_header.setAlignment(QtCore.Qt.AlignCenter)
        self.dtg_column_header.setObjectName("dtg_column_header")
        self.horizontalLayout_103.addWidget(self.dtg_column_header)
        self.dtg_column_header_3 = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtg_column_header_3.sizePolicy().hasHeightForWidth())
        self.dtg_column_header_3.setSizePolicy(sizePolicy)
        self.dtg_column_header_3.setMinimumSize(QtCore.QSize(60, 17))
        self.dtg_column_header_3.setMaximumSize(QtCore.QSize(60, 17))
        self.dtg_column_header_3.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 16pt \"Bebas Kai\";\n"
"}")
        self.dtg_column_header_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dtg_column_header_3.setObjectName("dtg_column_header_3")
        self.horizontalLayout_103.addWidget(self.dtg_column_header_3)
        self.verticalLayout_4.addWidget(self.frame_25)
        self.x_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.x_axis_dro_layout.setSpacing(8)
        self.x_axis_dro_layout.setObjectName("x_axis_dro_layout")
        self.zero_x_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_x_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_x_button_3.sizePolicy().hasHeightForWidth())
        self.zero_x_button_3.setSizePolicy(sizePolicy)
        self.zero_x_button_3.setMinimumSize(QtCore.QSize(50, 40))
        self.zero_x_button_3.setMaximumSize(QtCore.QSize(58, 40))
        self.zero_x_button_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zero_x_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap(":/images/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zero_x_button_3.setIcon(icon48)
        self.zero_x_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_x_button_3.setObjectName("zero_x_button_3")
        self.x_axis_dro_layout.addWidget(self.zero_x_button_3)
        self.statuslabel_40 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_40.sizePolicy().hasHeightForWidth())
        self.statuslabel_40.setSizePolicy(sizePolicy)
        self.statuslabel_40.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_40.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_40.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_40.setObjectName("statuslabel_40")
        self.x_axis_dro_layout.addWidget(self.statuslabel_40)
        self.statuslabel_45 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_45.sizePolicy().hasHeightForWidth())
        self.statuslabel_45.setSizePolicy(sizePolicy)
        self.statuslabel_45.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_45.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_45.setStyleSheet("StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_45.setObjectName("statuslabel_45")
        self.x_axis_dro_layout.addWidget(self.statuslabel_45)
        self.statuslabel_75 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_75.sizePolicy().hasHeightForWidth())
        self.statuslabel_75.setSizePolicy(sizePolicy)
        self.statuslabel_75.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_75.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_75.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_75.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_75.setObjectName("statuslabel_75")
        self.x_axis_dro_layout.addWidget(self.statuslabel_75)
        self.axisactionbutton_6 = ActionButton(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_6.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_6.setSizePolicy(sizePolicy)
        self.axisactionbutton_6.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_6.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_6.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_6.setObjectName("axisactionbutton_6")
        self.x_axis_dro_layout.addWidget(self.axisactionbutton_6)
        self.verticalLayout_4.addLayout(self.x_axis_dro_layout)
        self.y_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.y_axis_dro_layout.setSpacing(8)
        self.y_axis_dro_layout.setObjectName("y_axis_dro_layout")
        self.zero_y_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_y_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_y_button_3.sizePolicy().hasHeightForWidth())
        self.zero_y_button_3.setSizePolicy(sizePolicy)
        self.zero_y_button_3.setMinimumSize(QtCore.QSize(50, 40))
        self.zero_y_button_3.setMaximumSize(QtCore.QSize(55, 40))
        self.zero_y_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_y_button_3.setIcon(icon48)
        self.zero_y_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_y_button_3.setObjectName("zero_y_button_3")
        self.y_axis_dro_layout.addWidget(self.zero_y_button_3)
        self.statuslabel_41 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_41.sizePolicy().hasHeightForWidth())
        self.statuslabel_41.setSizePolicy(sizePolicy)
        self.statuslabel_41.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_41.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_41.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_41.setObjectName("statuslabel_41")
        self.y_axis_dro_layout.addWidget(self.statuslabel_41)
        self.statuslabel_46 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_46.sizePolicy().hasHeightForWidth())
        self.statuslabel_46.setSizePolicy(sizePolicy)
        self.statuslabel_46.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_46.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_46.setStyleSheet("StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_46.setObjectName("statuslabel_46")
        self.y_axis_dro_layout.addWidget(self.statuslabel_46)
        self.statuslabel_76 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_76.sizePolicy().hasHeightForWidth())
        self.statuslabel_76.setSizePolicy(sizePolicy)
        self.statuslabel_76.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_76.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_76.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_76.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_76.setObjectName("statuslabel_76")
        self.y_axis_dro_layout.addWidget(self.statuslabel_76)
        self.axisactionbutton_3 = ActionButton(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_3.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_3.setSizePolicy(sizePolicy)
        self.axisactionbutton_3.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_3.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_3.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_3.setObjectName("axisactionbutton_3")
        self.y_axis_dro_layout.addWidget(self.axisactionbutton_3)
        self.verticalLayout_4.addLayout(self.y_axis_dro_layout)
        self.z_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.z_axis_dro_layout.setSpacing(8)
        self.z_axis_dro_layout.setObjectName("z_axis_dro_layout")
        self.zero_z_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_z_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_z_button_3.sizePolicy().hasHeightForWidth())
        self.zero_z_button_3.setSizePolicy(sizePolicy)
        self.zero_z_button_3.setMinimumSize(QtCore.QSize(50, 40))
        self.zero_z_button_3.setMaximumSize(QtCore.QSize(55, 40))
        self.zero_z_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_z_button_3.setIcon(icon48)
        self.zero_z_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_z_button_3.setObjectName("zero_z_button_3")
        self.z_axis_dro_layout.addWidget(self.zero_z_button_3)
        self.statuslabel_42 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_42.sizePolicy().hasHeightForWidth())
        self.statuslabel_42.setSizePolicy(sizePolicy)
        self.statuslabel_42.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_42.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_42.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_42.setObjectName("statuslabel_42")
        self.z_axis_dro_layout.addWidget(self.statuslabel_42)
        self.statuslabel_47 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_47.sizePolicy().hasHeightForWidth())
        self.statuslabel_47.setSizePolicy(sizePolicy)
        self.statuslabel_47.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_47.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_47.setStyleSheet("StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_47.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_47.setObjectName("statuslabel_47")
        self.z_axis_dro_layout.addWidget(self.statuslabel_47)
        self.statuslabel_77 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_77.sizePolicy().hasHeightForWidth())
        self.statuslabel_77.setSizePolicy(sizePolicy)
        self.statuslabel_77.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_77.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_77.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_77.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_77.setObjectName("statuslabel_77")
        self.z_axis_dro_layout.addWidget(self.statuslabel_77)
        self.axisactionbutton = ActionButton(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton.sizePolicy().hasHeightForWidth())
        self.axisactionbutton.setSizePolicy(sizePolicy)
        self.axisactionbutton.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton.setObjectName("axisactionbutton")
        self.z_axis_dro_layout.addWidget(self.axisactionbutton)
        self.verticalLayout_4.addLayout(self.z_axis_dro_layout)
        self.a_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.a_axis_dro_layout.setSpacing(8)
        self.a_axis_dro_layout.setObjectName("a_axis_dro_layout")
        self.zero_a_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_a_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_a_button_3.sizePolicy().hasHeightForWidth())
        self.zero_a_button_3.setSizePolicy(sizePolicy)
        self.zero_a_button_3.setMinimumSize(QtCore.QSize(50, 40))
        self.zero_a_button_3.setMaximumSize(QtCore.QSize(55, 40))
        self.zero_a_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_a_button_3.setIcon(icon48)
        self.zero_a_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_a_button_3.setObjectName("zero_a_button_3")
        self.a_axis_dro_layout.addWidget(self.zero_a_button_3)
        self.statuslabel_43 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_43.sizePolicy().hasHeightForWidth())
        self.statuslabel_43.setSizePolicy(sizePolicy)
        self.statuslabel_43.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_43.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_43.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_43.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_43.setObjectName("statuslabel_43")
        self.a_axis_dro_layout.addWidget(self.statuslabel_43)
        self.statuslabel_48 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_48.sizePolicy().hasHeightForWidth())
        self.statuslabel_48.setSizePolicy(sizePolicy)
        self.statuslabel_48.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_48.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_48.setStyleSheet("StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_48.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_48.setObjectName("statuslabel_48")
        self.a_axis_dro_layout.addWidget(self.statuslabel_48)
        self.statuslabel_78 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_78.sizePolicy().hasHeightForWidth())
        self.statuslabel_78.setSizePolicy(sizePolicy)
        self.statuslabel_78.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_78.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_78.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_78.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_78.setObjectName("statuslabel_78")
        self.a_axis_dro_layout.addWidget(self.statuslabel_78)
        self.axisactionbutton_2 = ActionButton(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_2.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_2.setSizePolicy(sizePolicy)
        self.axisactionbutton_2.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_2.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_2.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_2.setObjectName("axisactionbutton_2")
        self.a_axis_dro_layout.addWidget(self.axisactionbutton_2)
        self.verticalLayout_4.addLayout(self.a_axis_dro_layout)
        self.b_axis_dro_layout = QtWidgets.QHBoxLayout()
        self.b_axis_dro_layout.setSpacing(8)
        self.b_axis_dro_layout.setObjectName("b_axis_dro_layout")
        self.zero_b_button_3 = MDIButton(self.main_dro_qframe)
        self.zero_b_button_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_b_button_3.sizePolicy().hasHeightForWidth())
        self.zero_b_button_3.setSizePolicy(sizePolicy)
        self.zero_b_button_3.setMinimumSize(QtCore.QSize(50, 40))
        self.zero_b_button_3.setMaximumSize(QtCore.QSize(55, 40))
        self.zero_b_button_3.setStyleSheet("MDIButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.zero_b_button_3.setIcon(icon48)
        self.zero_b_button_3.setIconSize(QtCore.QSize(20, 20))
        self.zero_b_button_3.setObjectName("zero_b_button_3")
        self.b_axis_dro_layout.addWidget(self.zero_b_button_3)
        self.statuslabel_44 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_44.sizePolicy().hasHeightForWidth())
        self.statuslabel_44.setSizePolicy(sizePolicy)
        self.statuslabel_44.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_44.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_44.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_44.setObjectName("statuslabel_44")
        self.b_axis_dro_layout.addWidget(self.statuslabel_44)
        self.statuslabel_49 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_49.sizePolicy().hasHeightForWidth())
        self.statuslabel_49.setSizePolicy(sizePolicy)
        self.statuslabel_49.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_49.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_49.setStyleSheet("StatusLabel{\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}\n"
"\n"
"StatusLabel[style=\"unhomed\"]{\n"
"   color: red;\n"
"}\n"
"\n"
"StatusLabel[style=\"homing\"]{\n"
"   color: rgb(196, 160, 0);\n"
"}")
        self.statuslabel_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_49.setObjectName("statuslabel_49")
        self.b_axis_dro_layout.addWidget(self.statuslabel_49)
        self.statuslabel_79 = StatusLabel(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_79.sizePolicy().hasHeightForWidth())
        self.statuslabel_79.setSizePolicy(sizePolicy)
        self.statuslabel_79.setMinimumSize(QtCore.QSize(100, 35))
        self.statuslabel_79.setMaximumSize(QtCore.QSize(100, 35))
        self.statuslabel_79.setStyleSheet("StatusLabel{\n"
"    border-style: transparant;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"    padding-right: 2px;\n"
"}")
        self.statuslabel_79.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_79.setObjectName("statuslabel_79")
        self.b_axis_dro_layout.addWidget(self.statuslabel_79)
        self.axisactionbutton_4 = ActionButton(self.main_dro_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisactionbutton_4.sizePolicy().hasHeightForWidth())
        self.axisactionbutton_4.setSizePolicy(sizePolicy)
        self.axisactionbutton_4.setMinimumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_4.setMaximumSize(QtCore.QSize(60, 40))
        self.axisactionbutton_4.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"}")
        self.axisactionbutton_4.setObjectName("axisactionbutton_4")
        self.b_axis_dro_layout.addWidget(self.axisactionbutton_4)
        self.verticalLayout_4.addLayout(self.b_axis_dro_layout)
        self.main_control_screen_layout_panel.addWidget(self.main_dro_qframe)
        self.main_override_tool_qframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_override_tool_qframe.sizePolicy().hasHeightForWidth())
        self.main_override_tool_qframe.setSizePolicy(sizePolicy)
        self.main_override_tool_qframe.setMinimumSize(QtCore.QSize(370, 340))
        self.main_override_tool_qframe.setFocusPolicy(QtCore.Qt.NoFocus)
        self.main_override_tool_qframe.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"padding-left: 7px;\n"
"padding-right: 7px;\n"
"}")
        self.main_override_tool_qframe.setObjectName("main_override_tool_qframe")
        self.gridLayout = QtWidgets.QGridLayout(self.main_override_tool_qframe)
        self.gridLayout.setContentsMargins(-1, 11, -1, 2)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(13)
        self.gridLayout.setObjectName("gridLayout")
        self.statuslabel = StatusLabel(self.main_override_tool_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel.sizePolicy().hasHeightForWidth())
        self.statuslabel.setSizePolicy(sizePolicy)
        self.statuslabel.setMinimumSize(QtCore.QSize(50, 36))
        self.statuslabel.setMaximumSize(QtCore.QSize(50, 36))
        self.statuslabel.setToolTipDuration(-3)
        self.statuslabel.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel.setLineWidth(0)
        self.statuslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel.setIndent(0)
        self.statuslabel.setObjectName("statuslabel")
        self.gridLayout.addWidget(self.statuslabel, 2, 1, 1, 1)
        self.actionslider_4 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_4.setMinimumSize(QtCore.QSize(0, 50))
        self.actionslider_4.setStyleSheet("QSlider::groove:horizontal {\n"
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
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.actionslider_4.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_4.setObjectName("actionslider_4")
        self.gridLayout.addWidget(self.actionslider_4, 5, 0, 1, 1)
        self.statuslabel_2 = StatusLabel(self.main_override_tool_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_2.sizePolicy().hasHeightForWidth())
        self.statuslabel_2.setSizePolicy(sizePolicy)
        self.statuslabel_2.setMinimumSize(QtCore.QSize(50, 36))
        self.statuslabel_2.setMaximumSize(QtCore.QSize(50, 36))
        self.statuslabel_2.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_2.setLineWidth(0)
        self.statuslabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_2.setIndent(0)
        self.statuslabel_2.setObjectName("statuslabel_2")
        self.gridLayout.addWidget(self.statuslabel_2, 4, 1, 1, 1)
        self.statuslabel_3 = StatusLabel(self.main_override_tool_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_3.sizePolicy().hasHeightForWidth())
        self.statuslabel_3.setSizePolicy(sizePolicy)
        self.statuslabel_3.setMinimumSize(QtCore.QSize(50, 36))
        self.statuslabel_3.setMaximumSize(QtCore.QSize(50, 36))
        self.statuslabel_3.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_3.setLineWidth(0)
        self.statuslabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_3.setIndent(0)
        self.statuslabel_3.setObjectName("statuslabel_3")
        self.gridLayout.addWidget(self.statuslabel_3, 5, 1, 1, 1)
        self.work_column_header_3 = QtWidgets.QLabel(self.main_override_tool_qframe)
        self.work_column_header_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_3.sizePolicy().hasHeightForWidth())
        self.work_column_header_3.setSizePolicy(sizePolicy)
        self.work_column_header_3.setMinimumSize(QtCore.QSize(65, 40))
        self.work_column_header_3.setMaximumSize(QtCore.QSize(65, 40))
        self.work_column_header_3.setStyleSheet("QLabel{\n"
"color: white;\n"
"border-style: solid;\n"
"border-color: rgb(176, 179,172);\n"
"border-width: 1px;\n"
"border-radius: 4px;\n"
"background-color: rgb(90, 90, 90);\n"
"font: 13pt \"Bebas Kai\";\n"
"}")
        self.work_column_header_3.setLineWidth(0)
        self.work_column_header_3.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_3.setWordWrap(False)
        self.work_column_header_3.setIndent(0)
        self.work_column_header_3.setObjectName("work_column_header_3")
        self.gridLayout.addWidget(self.work_column_header_3, 0, 2, 1, 1)
        self.loadmeter = LoadMeter(self.main_override_tool_qframe)
        self.loadmeter.setMinimumSize(QtCore.QSize(0, 25))
        self.loadmeter.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Bebas Kai")
        font.setPointSize(14)
        self.loadmeter.setFont(font)
        self.loadmeter.setStyleSheet("")
        self.loadmeter.setMaximum(150)
        self.loadmeter.setProperty("value", 150)
        self.loadmeter.setProperty("barGradient", ['0.0, 170, 170, 236', '0.63, 85, 85, 238', '0.65, 171, 171, 158', '0.79, 227, 237, 106', '0.84, 219, 124, 55', '1.0, 209, 0, 0'])
        self.loadmeter.setObjectName("loadmeter")
        self.gridLayout.addWidget(self.loadmeter, 0, 0, 1, 2)
        self.statuslabel_4 = StatusLabel(self.main_override_tool_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_4.sizePolicy().hasHeightForWidth())
        self.statuslabel_4.setSizePolicy(sizePolicy)
        self.statuslabel_4.setMinimumSize(QtCore.QSize(50, 36))
        self.statuslabel_4.setMaximumSize(QtCore.QSize(50, 36))
        self.statuslabel_4.setToolTipDuration(-1)
        self.statuslabel_4.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 14pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_4.setLineWidth(0)
        self.statuslabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_4.setProperty("conv_factor", 60.0)
        self.statuslabel_4.setObjectName("statuslabel_4")
        self.gridLayout.addWidget(self.statuslabel_4, 1, 1, 1, 1)
        self.actionslider = ActionSlider(self.main_override_tool_qframe)
        self.actionslider.setMinimumSize(QtCore.QSize(0, 50))
        self.actionslider.setStyleSheet("QSlider::groove:horizontal {\n"
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
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.actionslider.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider.setObjectName("actionslider")
        self.gridLayout.addWidget(self.actionslider, 4, 0, 1, 1)
        self.actionbutton_28 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_28.setMinimumSize(QtCore.QSize(65, 40))
        self.actionbutton_28.setMaximumSize(QtCore.QSize(65, 40))
        self.actionbutton_28.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_28.setObjectName("actionbutton_28")
        self.gridLayout.addWidget(self.actionbutton_28, 4, 2, 1, 1)
        self.actionslider_2 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_2.setMinimumSize(QtCore.QSize(0, 50))
        self.actionslider_2.setStyleSheet("QSlider::groove:horizontal {\n"
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
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.actionslider_2.setMaximum(100)
        self.actionslider_2.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_2.setObjectName("actionslider_2")
        self.gridLayout.addWidget(self.actionslider_2, 2, 0, 1, 1)
        self.actionslider_3 = ActionSlider(self.main_override_tool_qframe)
        self.actionslider_3.setMinimumSize(QtCore.QSize(0, 50))
        self.actionslider_3.setStyleSheet("QSlider::groove:horizontal {\n"
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
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.actionslider_3.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_3.setObjectName("actionslider_3")
        self.gridLayout.addWidget(self.actionslider_3, 1, 0, 1, 1)
        self.actionbutton_29 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_29.setMinimumSize(QtCore.QSize(65, 40))
        self.actionbutton_29.setMaximumSize(QtCore.QSize(65, 40))
        self.actionbutton_29.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_29.setObjectName("actionbutton_29")
        self.gridLayout.addWidget(self.actionbutton_29, 2, 2, 1, 1)
        self.actionbutton_30 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_30.setMinimumSize(QtCore.QSize(65, 40))
        self.actionbutton_30.setMaximumSize(QtCore.QSize(65, 40))
        self.actionbutton_30.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_30.setObjectName("actionbutton_30")
        self.gridLayout.addWidget(self.actionbutton_30, 1, 2, 1, 1)
        self.actionbutton_31 = ActionButton(self.main_override_tool_qframe)
        self.actionbutton_31.setMinimumSize(QtCore.QSize(65, 40))
        self.actionbutton_31.setMaximumSize(QtCore.QSize(65, 40))
        self.actionbutton_31.setStyleSheet("QPushButton {\n"
"       font: 14pt \"Bebas Kai\";\n"
"}")
        self.actionbutton_31.setObjectName("actionbutton_31")
        self.gridLayout.addWidget(self.actionbutton_31, 5, 2, 1, 1)
        self.main_control_screen_layout_panel.addWidget(self.main_override_tool_qframe)
        self.jog_and_spindle_qframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jog_and_spindle_qframe.sizePolicy().hasHeightForWidth())
        self.jog_and_spindle_qframe.setSizePolicy(sizePolicy)
        self.jog_and_spindle_qframe.setMinimumSize(QtCore.QSize(380, 340))
        self.jog_and_spindle_qframe.setMaximumSize(QtCore.QSize(380, 16777215))
        self.jog_and_spindle_qframe.setFocusPolicy(QtCore.Qt.NoFocus)
        self.jog_and_spindle_qframe.setStyleSheet("QFrame{\n"
"color: rgb(46, 52, 54);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-width: 2px;\n"
"border-radius: 6px;\n"
"}")
        self.jog_and_spindle_qframe.setObjectName("jog_and_spindle_qframe")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.jog_and_spindle_qframe)
        self.verticalLayout_27.setContentsMargins(15, 10, 15, 3)
        self.verticalLayout_27.setSpacing(12)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setSpacing(16)
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.jogincrement = JogIncrementWidget(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jogincrement.sizePolicy().hasHeightForWidth())
        self.jogincrement.setSizePolicy(sizePolicy)
        self.jogincrement.setMinimumSize(QtCore.QSize(0, 42))
        self.jogincrement.setMaximumSize(QtCore.QSize(16777215, 42))
        self.jogincrement.setStyleSheet("QPushButton {\n"
"       font: 15pt \"Bebas Kai\";\n"
"\n"
"}\n"
"\n"
"")
        self.jogincrement.setProperty("diameter", 0)
        self.jogincrement.setObjectName("jogincrement")
        self.horizontalLayout_83.addWidget(self.jogincrement)
        self.verticalLayout_27.addLayout(self.horizontalLayout_83)
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.actionslider_5 = ActionSlider(self.jog_and_spindle_qframe)
        self.actionslider_5.setMinimumSize(QtCore.QSize(0, 50))
        self.actionslider_5.setStyleSheet("QSlider::groove:horizontal {\n"
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
"background: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(60, 60, 60, 255), stop:0.21 rgba(60, 60, 60, 255), stop:0.25 rgba(255, 255, 255, 255), stop:0.29 rgba(60, 60, 60, 255), stop:0.46 rgba(60, 60, 60, 255), stop:0.5 rgba(255, 255, 255, 255), stop:0.54 rgba(60, 60, 60, 255), stop:0.71 rgba(60, 60, 60, 255), stop:0.75 rgba(255, 255, 255, 255), stop:0.79 rgba(60, 60, 60, 255), stop:0.9 rgba(60, 60, 60, 255), stop:1 rgba(255, 255, 255, 255));\n"
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
        self.actionslider_5.setMaximum(100)
        self.actionslider_5.setProperty("value", 30)
        self.actionslider_5.setOrientation(QtCore.Qt.Horizontal)
        self.actionslider_5.setObjectName("actionslider_5")
        self.horizontalLayout_84.addWidget(self.actionslider_5)
        self.fr_override_dro_2 = QtWidgets.QSpinBox(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_override_dro_2.sizePolicy().hasHeightForWidth())
        self.fr_override_dro_2.setSizePolicy(sizePolicy)
        self.fr_override_dro_2.setMinimumSize(QtCore.QSize(48, 38))
        self.fr_override_dro_2.setMaximumSize(QtCore.QSize(42, 38))
        self.fr_override_dro_2.setStyleSheet("QSpinBox {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 75 15pt \"Bebas Kai\";\n"
"}")
        self.fr_override_dro_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_override_dro_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fr_override_dro_2.setMaximum(100)
        self.fr_override_dro_2.setProperty("value", 100)
        self.fr_override_dro_2.setObjectName("fr_override_dro_2")
        self.horizontalLayout_84.addWidget(self.fr_override_dro_2)
        self.verticalLayout_27.addLayout(self.horizontalLayout_84)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.statuslabel_6 = StatusLabel(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_6.sizePolicy().hasHeightForWidth())
        self.statuslabel_6.setSizePolicy(sizePolicy)
        self.statuslabel_6.setMinimumSize(QtCore.QSize(105, 38))
        self.statuslabel_6.setMaximumSize(QtCore.QSize(105, 38))
        self.statuslabel_6.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_6.setProperty("statusItem", "")
        self.statuslabel_6.setObjectName("statuslabel_6")
        self.horizontalLayout_85.addWidget(self.statuslabel_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem)
        self.frame_30 = QtWidgets.QFrame(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy)
        self.frame_30.setMaximumSize(QtCore.QSize(16777215, 38))
        self.frame_30.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_30.setLineWidth(0)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_110 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_110.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName("horizontalLayout_110")
        self.rpm_label_3 = QtWidgets.QLabel(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_label_3.sizePolicy().hasHeightForWidth())
        self.rpm_label_3.setSizePolicy(sizePolicy)
        self.rpm_label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.rpm_label_3.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.rpm_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.rpm_label_3.setWordWrap(False)
        self.rpm_label_3.setIndent(0)
        self.rpm_label_3.setObjectName("rpm_label_3")
        self.horizontalLayout_110.addWidget(self.rpm_label_3)
        self.rpm_label_4 = QtWidgets.QLabel(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_label_4.sizePolicy().hasHeightForWidth())
        self.rpm_label_4.setSizePolicy(sizePolicy)
        self.rpm_label_4.setMinimumSize(QtCore.QSize(5, 30))
        self.rpm_label_4.setMaximumSize(QtCore.QSize(5, 16777215))
        self.rpm_label_4.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.rpm_label_4.setText("")
        self.rpm_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rpm_label_4.setWordWrap(True)
        self.rpm_label_4.setIndent(0)
        self.rpm_label_4.setObjectName("rpm_label_4")
        self.horizontalLayout_110.addWidget(self.rpm_label_4)
        self.statuslabel_10 = StatusLabel(self.frame_30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_10.sizePolicy().hasHeightForWidth())
        self.statuslabel_10.setSizePolicy(sizePolicy)
        self.statuslabel_10.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_10.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel_10.setIndent(0)
        self.statuslabel_10.setProperty("fromat", "")
        self.statuslabel_10.setObjectName("statuslabel_10")
        self.horizontalLayout_110.addWidget(self.statuslabel_10)
        self.work_column_header_7 = QtWidgets.QLabel(self.frame_30)
        self.work_column_header_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.work_column_header_7.sizePolicy().hasHeightForWidth())
        self.work_column_header_7.setSizePolicy(sizePolicy)
        self.work_column_header_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.work_column_header_7.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.work_column_header_7.setAlignment(QtCore.Qt.AlignCenter)
        self.work_column_header_7.setWordWrap(False)
        self.work_column_header_7.setIndent(0)
        self.work_column_header_7.setObjectName("work_column_header_7")
        self.horizontalLayout_110.addWidget(self.work_column_header_7)
        self.horizontalLayout_85.addWidget(self.frame_30)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem1)
        self.statuslabel_7 = StatusLabel(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_7.sizePolicy().hasHeightForWidth())
        self.statuslabel_7.setSizePolicy(sizePolicy)
        self.statuslabel_7.setMinimumSize(QtCore.QSize(105, 38))
        self.statuslabel_7.setMaximumSize(QtCore.QSize(105, 38))
        self.statuslabel_7.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_7.setProperty("statusItem", "")
        self.statuslabel_7.setObjectName("statuslabel_7")
        self.horizontalLayout_85.addWidget(self.statuslabel_7)
        self.verticalLayout_27.addLayout(self.horizontalLayout_85)
        self.line_2 = QtWidgets.QFrame(self.jog_and_spindle_qframe)
        self.line_2.setMinimumSize(QtCore.QSize(0, 2))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.line_2.setStyleSheet("Line{\n"
"color:rgb(186, 189, 182);\n"
"border-style: solid;\n"
"border-color: rgb(186, 189, 182);\n"
"background-color: rgb(186, 189, 182);\n"
"border-width: 1px;\n"
"border-radius: 1px;\n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_27.addWidget(self.line_2)
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.statuslabel_5 = StatusLabel(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_5.sizePolicy().hasHeightForWidth())
        self.statuslabel_5.setSizePolicy(sizePolicy)
        self.statuslabel_5.setMinimumSize(QtCore.QSize(105, 38))
        self.statuslabel_5.setMaximumSize(QtCore.QSize(105, 38))
        self.statuslabel_5.setStyleSheet("QLabel {\n"
"    border-style: solid;\n"
"    border-color: rgb(96, 96, 97);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(86, 86, 87);\n"
"    font: 50 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_5.setProperty("statusItem", "")
        self.statuslabel_5.setObjectName("statuslabel_5")
        self.horizontalLayout_87.addWidget(self.statuslabel_5)
        self.rpm_label = QtWidgets.QLabel(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_label.sizePolicy().hasHeightForWidth())
        self.rpm_label.setSizePolicy(sizePolicy)
        self.rpm_label.setMaximumSize(QtCore.QSize(16777215, 38))
        self.rpm_label.setStyleSheet("QLabel{\n"
"    border: none;\n"
"    color: rgb(238, 238, 236);\n"
"    background: transparent;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.rpm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rpm_label.setWordWrap(False)
        self.rpm_label.setIndent(0)
        self.rpm_label.setObjectName("rpm_label")
        self.horizontalLayout_87.addWidget(self.rpm_label)
        self.statuslabel_9 = StatusLabel(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel_9.sizePolicy().hasHeightForWidth())
        self.statuslabel_9.setSizePolicy(sizePolicy)
        self.statuslabel_9.setMinimumSize(QtCore.QSize(105, 38))
        self.statuslabel_9.setMaximumSize(QtCore.QSize(105, 38))
        self.statuslabel_9.setStyleSheet("QLabel {\n"
"    border-style: transparent;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: black;\n"
"    background: rgb(235, 235, 235);\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.statuslabel_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statuslabel_9.setProperty("statusItem", "")
        self.statuslabel_9.setObjectName("statuslabel_9")
        self.horizontalLayout_87.addWidget(self.statuslabel_9)
        self.verticalLayout_27.addLayout(self.horizontalLayout_87)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.spindle_rev_button = ActionButton(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_rev_button.sizePolicy().hasHeightForWidth())
        self.spindle_rev_button.setSizePolicy(sizePolicy)
        self.spindle_rev_button.setMinimumSize(QtCore.QSize(100, 42))
        self.spindle_rev_button.setMaximumSize(QtCore.QSize(100, 42))
        self.spindle_rev_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_rev_button.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_rev_button.setIcon(icon6)
        self.spindle_rev_button.setIconSize(QtCore.QSize(18, 18))
        self.spindle_rev_button.setProperty("option", True)
        self.spindle_rev_button.setObjectName("spindle_rev_button")
        self.horizontalLayout_86.addWidget(self.spindle_rev_button)
        self.spindle_stop_button = ActionButton(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_stop_button.sizePolicy().hasHeightForWidth())
        self.spindle_stop_button.setSizePolicy(sizePolicy)
        self.spindle_stop_button.setMinimumSize(QtCore.QSize(90, 42))
        self.spindle_stop_button.setMaximumSize(QtCore.QSize(90, 42))
        self.spindle_stop_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_stop_button.setStyleSheet("QPushButton {\n"
"       font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_stop_button.setProperty("option", True)
        self.spindle_stop_button.setObjectName("spindle_stop_button")
        self.horizontalLayout_86.addWidget(self.spindle_stop_button)
        self.spindle_fwd_button = ActionButton(self.jog_and_spindle_qframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spindle_fwd_button.sizePolicy().hasHeightForWidth())
        self.spindle_fwd_button.setSizePolicy(sizePolicy)
        self.spindle_fwd_button.setMinimumSize(QtCore.QSize(100, 42))
        self.spindle_fwd_button.setMaximumSize(QtCore.QSize(100, 42))
        self.spindle_fwd_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spindle_fwd_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.spindle_fwd_button.setStyleSheet("QPushButton {\n"
"    text-align: right;\n"
"    padding-right: 22px;\n"
"    font: 17pt \"Bebas Kai\";\n"
"}")
        self.spindle_fwd_button.setIcon(icon7)
        self.spindle_fwd_button.setIconSize(QtCore.QSize(18, 18))
        self.spindle_fwd_button.setProperty("option", True)
        self.spindle_fwd_button.setObjectName("spindle_fwd_button")
        self.horizontalLayout_86.addWidget(self.spindle_fwd_button)
        self.verticalLayout_27.addLayout(self.horizontalLayout_86)
        self.main_control_screen_layout_panel.addWidget(self.jog_and_spindle_qframe)
        self.verticalLayout_31.addLayout(self.main_control_screen_layout_panel)
        Form.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Form)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1924, 27))
        self.menuBar.setMinimumSize(QtCore.QSize(0, 25))
        self.menuBar.setStyleSheet("QMenuBar {\n"
"color: white;\n"
"background: rgb(118, 122, 124);\n"
"font: 11pt bebas kai;\n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        self.menuRecentFiles = QtWidgets.QMenu(self.menuExit)
        self.menuRecentFiles.setObjectName("menuRecentFiles")
        self.menuMachine = QtWidgets.QMenu(self.menuBar)
        self.menuMachine.setObjectName("menuMachine")
        self.menuHoming = QtWidgets.QMenu(self.menuMachine)
        self.menuHoming.setObjectName("menuHoming")
        self.menuCooling = QtWidgets.QMenu(self.menuMachine)
        self.menuCooling.setObjectName("menuCooling")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        Form.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(Form)
        self.statusBar.setObjectName("statusBar")
        Form.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(Form)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(Form)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Form)
        self.actionClose.setObjectName("actionClose")
        self.actionReload = QtWidgets.QAction(Form)
        self.actionReload.setObjectName("actionReload")
        self.actionSave_As = QtWidgets.QAction(Form)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionHome_X = QtWidgets.QAction(Form)
        self.actionHome_X.setObjectName("actionHome_X")
        self.actionHome_Y = QtWidgets.QAction(Form)
        self.actionHome_Y.setObjectName("actionHome_Y")
        self.actionHome_Z = QtWidgets.QAction(Form)
        self.actionHome_Z.setObjectName("actionHome_Z")
        self.action_EmergencyStop_toggle = QtWidgets.QAction(Form)
        self.action_EmergencyStop_toggle.setObjectName("action_EmergencyStop_toggle")
        self.action_MachinePower_toggle = QtWidgets.QAction(Form)
        self.action_MachinePower_toggle.setProperty("_axis", 2)
        self.action_MachinePower_toggle.setObjectName("action_MachinePower_toggle")
        self.actionHome_All = QtWidgets.QAction(Form)
        self.actionHome_All.setObjectName("actionHome_All")
        self.actionRun_Program = QtWidgets.QAction(Form)
        self.actionRun_Program.setObjectName("actionRun_Program")
        self.actionFile1 = QtWidgets.QAction(Form)
        self.actionFile1.setObjectName("actionFile1")
        self.actionReport_Actual_Position = QtWidgets.QAction(Form)
        self.actionReport_Actual_Position.setCheckable(True)
        self.actionReport_Actual_Position.setObjectName("actionReport_Actual_Position")
        self.actionTest = QtWidgets.QAction(Form)
        self.actionTest.setObjectName("actionTest")
        self.action_Mist_toggle = QtWidgets.QAction(Form)
        self.action_Mist_toggle.setCheckable(True)
        self.action_Mist_toggle.setObjectName("action_Mist_toggle")
        self.action_Flood_toggle = QtWidgets.QAction(Form)
        self.action_Flood_toggle.setCheckable(True)
        self.action_Flood_toggle.setObjectName("action_Flood_toggle")
        self.menuRecentFiles.addAction(self.actionFile1)
        self.menuExit.addAction(self.actionOpen)
        self.menuExit.addAction(self.menuRecentFiles.menuAction())
        self.menuExit.addAction(self.actionReload)
        self.menuExit.addAction(self.actionClose)
        self.menuExit.addAction(self.actionSave_As)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menuHoming.addAction(self.actionHome_All)
        self.menuHoming.addAction(self.actionHome_X)
        self.menuHoming.addAction(self.actionHome_Y)
        self.menuHoming.addAction(self.actionHome_Z)
        self.menuCooling.addAction(self.action_Mist_toggle)
        self.menuCooling.addAction(self.action_Flood_toggle)
        self.menuMachine.addAction(self.action_EmergencyStop_toggle)
        self.menuMachine.addAction(self.action_MachinePower_toggle)
        self.menuMachine.addSeparator()
        self.menuMachine.addAction(self.actionRun_Program)
        self.menuMachine.addAction(self.menuHoming.menuAction())
        self.menuMachine.addAction(self.menuCooling.menuAction())
        self.menuView.addAction(self.actionReport_Actual_Position)
        self.menuView.addAction(self.actionTest)
        self.menuBar.addAction(self.menuExit.menuAction())
        self.menuBar.addAction(self.menuMachine.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_24.setCurrentIndex(0)
        self.tool_table_delete_button.clicked.connect(self.tableWidget_2.deleteSelectedTool)
        self.tool_table_reread_button.clicked.connect(self.tableWidget_2.loadToolTable)
        self.tool_table_reload_button.clicked.connect(self.tableWidget_2.loadToolTable)
        self.tool_table_add_tool_button.clicked.connect(self.tableWidget_2.insertToolBelow)
        self.x_axis_button_27.clicked.connect(self.filesystemtable.deleteFile)
        self.x_axis_button_23.clicked.connect(self.filesystemtable.goUP)
        self.x_axis_button_29.clicked.connect(self.filesystemtable.createDirectory)
        self.tool_table_save_button.clicked.connect(self.tableWidget_2.saveToolTable)
        self.x_axis_button_35.clicked.connect(self.filesystemtable_2.createDirectory)
        self.x_axis_button_33.clicked.connect(self.filesystemtable_2.deleteFile)
        self.copy_to_usb_2.clicked.connect(self.filesystemtable.doFileTransfer)
        self.copy_from_usb_2.clicked.connect(self.filesystemtable_2.doFileTransfer)
        self.x_axis_button_30.clicked.connect(self.filesystemtable_2.goUP)
        self.filesystemtable.transferFileRequest['QString'].connect(self.filesystemtable_2.transferFile)
        self.filesystemtable_2.transferFileRequest['QString'].connect(self.filesystemtable.transferFile)
        self.x_axis_button_31.clicked.connect(self.filesystemtable.newFile)
        self.x_axis_button_37.clicked.connect(self.filesystemtable_2.newFile)
        self.actionslider_5.sliderMoved['int'].connect(self.fr_override_dro_2.setValue)
        self.x_axis_button_26.clicked.connect(self.filesystemtable.loadSelectedFile)
        self.filesystemtable.gcodeFileSelected['bool'].connect(self.x_axis_button_26.setEnabled)
        self.filesystemtable.filePreviewText['QString'].connect(self.plainTextEdit.setPlainText)
        self.filesystemtable_2.filePreviewText['QString'].connect(self.plainTextEdit.setPlainText)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Probe Basic"))
        self.mdi_entry_box.setPlaceholderText(_translate("Form", "MDI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "          MAIN          "))
        self.x_axis_button_30.setText(_translate("Form", "  FOLDER UP"))
        self.x_axis_button_32.setText(_translate("Form", "EJECT USB"))
        self.x_axis_button_33.setText(_translate("Form", " DELETE"))
        self.x_axis_button_37.setText(_translate("Form", " NEW FILE"))
        self.x_axis_button_35.setText(_translate("Form", " NEW FOLDER"))
        self.x_axis_button_34.setText(_translate("Form", "RENAME"))
        self.copy_from_usb_2.setText(_translate("Form", "COPY\n"
"FROM\n"
"  USB"))
        self.copy_to_usb_2.setText(_translate("Form", "COPY\n"
"TO\n"
"USB"))
        self.x_axis_button_23.setText(_translate("Form", "  FOLDER UP"))
        self.x_axis_button_26.setText(_translate("Form", "LOAD G-CODE"))
        self.x_axis_button_27.setText(_translate("Form", " DELETE"))
        self.x_axis_button_31.setText(_translate("Form", " NEW FILE"))
        self.x_axis_button_29.setText(_translate("Form", " NEW FOLDER"))
        self.x_axis_button_28.setText(_translate("Form", "RENAME"))
        self.work_column_header_8.setText(_translate("Form", "G-CODE FILE PREVIEW"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "Select a text file to preview"))
        self.x_axis_button_36.setText(_translate("Form", "EDIT G-CODE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("Form", "          FILE          "))
        self.machine_column_header_9.setText(_translate("Form", "ATC MANUAL CONTROL PANEL"))
        self.m01_break_button_4.setText(_translate("Form", "INSERT"))
        self.m01_break_button_8.setText(_translate("Form", "DELETE ALL"))
        self.m01_break_button_9.setText(_translate("Form", "DELETE"))
        self.subcallbutton_9.setText(_translate("Form", " ATC REV"))
        self.subcallbutton_9.setProperty("sub_name", _translate("Form", "m11.ngc"))
        self.subcallbutton_3.setText(_translate("Form", " ATC FWD "))
        self.subcallbutton_3.setProperty("sub_name", _translate("Form", "m12.ngc"))
        self.subcallbutton_10.setText(_translate("Form", " ATC RETRACT"))
        self.subcallbutton_10.setProperty("sub_name", _translate("Form", "retractatc.ngc"))
        self.subcallbutton_11.setText(_translate("Form", " ATC EXTEND "))
        self.subcallbutton_11.setProperty("sub_name", _translate("Form", "extendatc.ngc"))
        self.subcallbutton_12.setText(_translate("Form", "DRAWBAR LOOSE"))
        self.subcallbutton_12.setProperty("sub_name", _translate("Form", "unclamptool.ngc"))
        self.subcallbutton_13.setText(_translate("Form", "DRAWBAR TIGHT"))
        self.subcallbutton_13.setProperty("sub_name", _translate("Form", "clamptool.ngc"))
        self.m01_break_button_10.setText(_translate("Form", "SET TC POSITION"))
        self.m01_break_button_27.setText(_translate("Form", "AIR BLAST"))
        self.subcallbutton_14.setText(_translate("Form", "REF CAROUSEL"))
        self.subcallbutton_14.setProperty("sub_name", _translate("Form", "m13.ngc"))
        self.m01_break_button_14.setText(_translate("Form", "+ +"))
        self.m01_break_button_15.setText(_translate("Form", "- -"))
        self.mdi_entry_box_3.setPlaceholderText(_translate("Form", "MDI"))
        self.label_60.setText(_translate("Form", "P9"))
        self.label_61.setText(_translate("Form", "T5"))
        self.label_67.setText(_translate("Form", "T2"))
        self.label_68.setText(_translate("Form", "T8"))
        self.label_69.setText(_translate("Form", "P2"))
        self.label_70.setText(_translate("Form", "P3"))
        self.label_71.setText(_translate("Form", "T10"))
        self.label_72.setText(_translate("Form", "P11"))
        self.label_73.setText(_translate("Form", "T4"))
        self.label_74.setText(_translate("Form", "P5"))
        self.label_75.setText(_translate("Form", "P1"))
        self.label_76.setText(_translate("Form", "P6"))
        self.label_77.setText(_translate("Form", "T3"))
        self.label_78.setText(_translate("Form", "T1"))
        self.label_79.setText(_translate("Form", "T6"))
        self.label_80.setText(_translate("Form", "P4"))
        self.label_81.setText(_translate("Form", "T9"))
        self.label_82.setText(_translate("Form", "P8"))
        self.label_83.setText(_translate("Form", "T11"))
        self.label_84.setText(_translate("Form", "P7"))
        self.label_85.setText(_translate("Form", "T12"))
        self.label_86.setText(_translate("Form", "P10"))
        self.label_87.setText(_translate("Form", "P12"))
        self.label_88.setText(_translate("Form", "T7"))
        self.tool_length_8.setText(_translate("Form", "T0"))
        self.tool_length_8.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'T\' + ch[0]\", \"name\": \"current tool\"}]"))
        self.tool_length_8.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_8.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.machine_column_header_3.setText(_translate("Form", "ATC AUTOMATIC CONTROL PANEL"))
        self.load_spindle_tool_number.setPlaceholderText(_translate("Form", "0"))
        self.load_current_tool.setText(_translate("Form", "LOAD SPINDLE"))
        self.load_current_tool.setProperty("rules", _translate("Form", "[]"))
        self.load_current_tool.setProperty("MDICommand", _translate("Form", "M61 Q#<load_spindle_tool_number>"))
        self.remove_current_tool.setText(_translate("Form", "UNLOAD SPINDLE"))
        self.remove_current_tool.setProperty("rules", _translate("Form", "[]"))
        self.remove_current_tool.setProperty("MDICommand", _translate("Form", "M61 Q0 G49"))
        self.subcallbutton_15.setText(_translate("Form", " ATC REV"))
        self.subcallbutton_15.setProperty("sub_name", _translate("Form", "m11.ngc"))
        self.subcallbutton_4.setText(_translate("Form", " ATC FWD "))
        self.subcallbutton_4.setProperty("sub_name", _translate("Form", "m12.ngc"))
        self.store_current_tool.setText(_translate("Form", "STORE CURRENT TOOL"))
        self.store_current_tool.setProperty("rules", _translate("Form", "[]"))
        self.store_current_tool.setProperty("MDICommand", _translate("Form", "M6 T0"))
        self.machine_column_header_2.setText(_translate("Form", "ELECTRONIC TOOL SETTER"))
        self.m01_break_button_24.setText(_translate("Form", "TOUCH OFF ENTIRE CAROUSEL"))
        self.m01_break_button_25.setText(_translate("Form", "TOUCH OFF CURRENT TOOL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status_tab), _translate("Form", "          ATC          "))
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "OFFSET"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "X"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Y"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Z"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "A"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "B"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("Form", "G54"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(0, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("Form", "G55"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(1, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(1, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(1, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(1, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("Form", "G56"))
        item = self.tableWidget_3.item(2, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(2, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(2, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(2, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(2, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("Form", "G57"))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(3, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(3, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(3, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(3, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(4, 0)
        item.setText(_translate("Form", "G58"))
        item = self.tableWidget_3.item(4, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(4, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(4, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(4, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(4, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(5, 0)
        item.setText(_translate("Form", "G59"))
        item = self.tableWidget_3.item(5, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(5, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(5, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(5, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(5, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(6, 0)
        item.setText(_translate("Form", "G59.1"))
        item = self.tableWidget_3.item(6, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(6, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(6, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(6, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(6, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(7, 0)
        item.setText(_translate("Form", "G59.2"))
        item = self.tableWidget_3.item(7, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(7, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(7, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(7, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(7, 5)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(8, 0)
        item.setText(_translate("Form", "G59.3"))
        item = self.tableWidget_3.item(8, 1)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(8, 2)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(8, 3)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(8, 4)
        item.setText(_translate("Form", "0.0000"))
        item = self.tableWidget_3.item(8, 5)
        item.setText(_translate("Form", "0.0000"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.x_axis_button_10.setText(_translate("Form", "CLEAR"))
        self.x_axis_button_12.setText(_translate("Form", "RE-READ"))
        self.x_axis_button_13.setText(_translate("Form", "SAVE TABLE"))
        self.x_axis_button_14.setText(_translate("Form", "RELOAD TABLE"))
        self.mdi_entry_box_6.setPlaceholderText(_translate("Form", "MDI"))
        self.machine_column_header_4.setText(_translate("Form", "WORK COORDINATE OFFSETS"))
        self.actionbutton_g54_2.setText(_translate("Form", "G54"))
        self.actionbutton_g54_2.setProperty("actionName", _translate("Form", "machine.set-work-coord:G54"))
        self.actionbutton_g55_2.setText(_translate("Form", "G55"))
        self.actionbutton_g55_2.setProperty("actionName", _translate("Form", "machine.set-work-coord:G55"))
        self.actionbutton_g56_2.setText(_translate("Form", "G56"))
        self.actionbutton_g56_2.setProperty("actionName", _translate("Form", "machine.set-work-coord:G56"))
        self.actionbutton_g57_2.setText(_translate("Form", "G57"))
        self.actionbutton_g57_2.setProperty("actionName", _translate("Form", "machine.set-work-coord:G57"))
        self.actionbutton_g58_2.setText(_translate("Form", "G58"))
        self.actionbutton_g58_2.setProperty("actionName", _translate("Form", "machine.set-work-coord:G58"))
        self.actionbutton_g59_4.setText(_translate("Form", "G59"))
        self.actionbutton_g59_4.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59"))
        self.actionbutton_g59_5.setText(_translate("Form", "G59.1"))
        self.actionbutton_g59_5.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.1"))
        self.actionbutton_g59_6.setText(_translate("Form", "G59.2"))
        self.actionbutton_g59_6.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.2"))
        self.actionbutton_g59_7.setText(_translate("Form", "G59.3"))
        self.actionbutton_g59_7.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.3"))
        self.axis_column_header_9.setText(_translate("Form", "SET TO ZERO"))
        self.axis_column_header_10.setText(_translate("Form", "AXIS"))
        self.machine_column_header_10.setText(_translate("Form", "WC CURRENT POSITION"))
        self.machine_column_header_11.setText(_translate("Form", "MACHINE\n"
"COORDS"))
        self.machine_column_header_12.setText(_translate("Form", "WC\n"
"OFFSET"))
        self.ref_coilumn_header_4.setText(_translate("Form", "G52/G92\n"
"OFFSET"))
        self.machine_column_header_13.setText(_translate("Form", "TOOL\n"
"OFFSET"))
        self.zero_x_button_2.setText(_translate("Form", "ZERO"))
        self.zero_x_button_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_x_button_2.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} X0.0"))
        self.axis_column_header_11.setText(_translate("Form", "X"))
        self.statuslabel_50.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_51.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_52.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_53.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_54.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]"))
        self.zero_y_button_2.setText(_translate("Form", "ZERO"))
        self.zero_y_button_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_y_button_2.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} Y0.0"))
        self.axis_column_header_12.setText(_translate("Form", "Y"))
        self.statuslabel_55.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_56.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_57.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_58.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_59.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]"))
        self.zero_z_button_2.setText(_translate("Form", "ZERO"))
        self.zero_z_button_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_z_button_2.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} Z0.0"))
        self.axis_column_header_13.setText(_translate("Form", "Z"))
        self.statuslabel_60.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_61.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_62.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_63.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_64.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:tool_offset\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"tool offset\"}]"))
        self.zero_a_button_2.setText(_translate("Form", "ZERO"))
        self.zero_a_button_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_a_button_2.setProperty("MDICommand", _translate("Form", "G10 L2 P{ch[0]} A0.0"))
        self.axis_column_header_14.setText(_translate("Form", "A"))
        self.statuslabel_65.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_66.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_67.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_68.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_69.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]"))
        self.zero_b_button_2.setText(_translate("Form", "ZERO"))
        self.zero_b_button_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_b_button_2.setProperty("MDICommand", _translate("Form", "G10 L2 P{ch[0]} B0.0"))
        self.axis_column_header_15.setText(_translate("Form", "B"))
        self.statuslabel_70.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_71.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:position\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_72.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_73.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]"))
        self.statuslabel_74.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4])\", \"name\": \"New Rule\"}]"))
        self.set_tool_touch_off_position_button_2.setText(_translate("Form", "SET TOOL TOUCH OFF POSITION"))
        self.set_tool_touch_off_position_button_2.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:gcodes\", \"trigger\": true}], \"property\": \"None\", \"expression\": \"\", \"name\": \"set tool touch off position\"}]"))
        self.set_tool_touch_off_position_button_2.setProperty("MDICommand", _translate("Form", "G30.1"))
        self.label_55.setText(_translate("Form", "X :"))
        self.tool_length_2.setText(_translate("Form", "0.0000"))
        self.tool_length_2.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length_2.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_2.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.label_57.setText(_translate("Form", "Y :"))
        self.tool_length_4.setText(_translate("Form", "0.0000"))
        self.tool_length_4.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length_4.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_4.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.label_58.setText(_translate("Form", "Z :"))
        self.tool_length_3.setText(_translate("Form", "0.0000"))
        self.tool_length_3.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.3f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length_3.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_3.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("Form", "        OFFSETS        "))
        self.tool_table_delete_button.setText(_translate("Form", "DELETE"))
        self.tool_table_add_tool_button.setText(_translate("Form", "ADD TOOL"))
        self.tool_table_reread_button.setText(_translate("Form", "RE-READ"))
        self.tool_table_save_button.setText(_translate("Form", "SAVE TABLE"))
        self.tool_table_reload_button.setText(_translate("Form", "RELOAD TABLE"))
        self.label_48.setText(_translate("Form", "TOOL LENGTH"))
        self.tool_length_5.setText(_translate("Form", "0.0000"))
        self.tool_length_5.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length_5.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_5.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.label_49.setText(_translate("Form", "DIAM"))
        self.tool_diameter_2.setText(_translate("Form", "0.0000"))
        self.tool_diameter_2.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]"))
        self.tool_diameter_2.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_diameter_2.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.label_56.setText(_translate("Form", "COMMENT"))
        self.tool_length_7.setText(_translate("Form", "No Tool Loaded"))
        self.tool_length_7.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?comment\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Tool Comment\"}]"))
        self.tool_length_7.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_7.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.mdi_entry_box_4.setPlaceholderText(_translate("Form", "MDI"))
        self.tool_length_6.setText(_translate("Form", "T0"))
        self.tool_length_6.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:tool_in_spindle?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'T\' + ch[0]\", \"name\": \"current tool\"}]"))
        self.tool_length_6.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length_6.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tooling_tab), _translate("Form", "          TOOL          "))
        self.label_24.setText(_translate("Form", " WORK OFFSETS"))
        self.actionbutton_11.setText(_translate("Form", "G54"))
        self.actionbutton_11.setProperty("actionName", _translate("Form", "machine.set-work-coord:G54"))
        self.actionbutton_14.setText(_translate("Form", "G55"))
        self.actionbutton_14.setProperty("actionName", _translate("Form", "machine.set-work-coord:G55"))
        self.actionbutton_15.setText(_translate("Form", "G56"))
        self.actionbutton_15.setProperty("actionName", _translate("Form", "machine.set-work-coord:G56"))
        self.actionbutton_17.setText(_translate("Form", "G59"))
        self.actionbutton_17.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59"))
        self.actionbutton_16.setText(_translate("Form", "G59.3"))
        self.actionbutton_16.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.3"))
        self.actionbutton_12.setText(_translate("Form", "G58"))
        self.actionbutton_12.setProperty("actionName", _translate("Form", "machine.set-work-coord:G58"))
        self.actionbutton_13.setText(_translate("Form", "G59.2"))
        self.actionbutton_13.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.2"))
        self.actionbutton_4.setText(_translate("Form", "G57"))
        self.actionbutton_4.setProperty("actionName", _translate("Form", "machine.set-work-coord:G57"))
        self.actionbutton_18.setText(_translate("Form", "G59.1"))
        self.actionbutton_18.setProperty("actionName", _translate("Form", "machine.set-work-coord:G59.1"))
        self.label_23.setText(_translate("Form", " Probing Parameters"))
        self.label_22.setText(_translate("Form", "Probe Tool #:"))
        self.probe_tool_number.setText(_translate("Form", "99"))
        self.label_5.setText(_translate("Form", "Step Off Width:"))
        self.step_off_width.setText(_translate("Form", "0.5000"))
        self.label_6.setText(_translate("Form", "Probe Fast FR:"))
        self.probe_fast_fr.setText(_translate("Form", "30.0"))
        self.label_7.setText(_translate("Form", "Probe Slow FR:"))
        self.probe_slow_fr.setText(_translate("Form", "5.0"))
        self.label_11.setText(_translate("Form", "Max X/Y Distance:"))
        self.max_xy_distance.setText(_translate("Form", "1.0000"))
        self.label_8.setText(_translate("Form", "X/Y Clearance:"))
        self.xy_clearance.setText(_translate("Form", "0.1000"))
        self.label_10.setText(_translate("Form", "Max Z Distance:"))
        self.max_z_distance.setText(_translate("Form", "1.0000"))
        self.label_9.setText(_translate("Form", "Z Clearance:"))
        self.z_clearance.setText(_translate("Form", "0.1000"))
        self.label_12.setText(_translate("Form", "Extra Probe Depth:"))
        self.extra_probe_depth.setText(_translate("Form", "0.0000"))
        self.label_13.setText(_translate("Form", "Calibration Dia:"))
        self.calibration_dia.setText(_translate("Form", "0.1500"))
        self.label_54.setText(_translate("Form", "EDGE WIDTH:"))
        self.step_off_width_2.setText(_translate("Form", "0.5000"))
        self.label_25.setText(_translate("Form", " Probe Results"))
        self.label_52.setText(_translate("Form", "EDGE ANGLE:"))
        self.probed_diameter_2.setText(_translate("Form", "0.0000"))
        self.label_15.setText(_translate("Form", "X Width:"))
        self.x_probed_width.setText(_translate("Form", "0.0000"))
        self.label_14.setText(_translate("Form", "X Probed Pos:"))
        self.x_probed_pos.setText(_translate("Form", "0.0000"))
        self.label_30.setText(_translate("Form", "EDGE DELTA:"))
        self.x_probed_width_2.setText(_translate("Form", "0.0000"))
        self.label_17.setText(_translate("Form", "Y Width:"))
        self.probed_diameter.setText(_translate("Form", "0.0000"))
        self.label_16.setText(_translate("Form", "Y Probed Pos:"))
        self.z_probed_pos.setText(_translate("Form", "0.0000"))
        self.label_50.setText(_translate("Form", "DIAM:"))
        self.y_probed_width.setText(_translate("Form", "0.0000"))
        self.label_18.setText(_translate("Form", "Z Probed Pos:"))
        self.y_probed_pos.setText(_translate("Form", "0.0000"))
        self.mdi_entry_box_2.setPlaceholderText(_translate("Form", "MDI"))
        self.pushButton_10.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_14.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_12.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_13.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_11.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_15.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_17.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_18.setProperty("styleClass", _translate("Form", "probeButton"))
        self.probe_front_left_top_corner.setProperty("sub_name", _translate("Form", "probe_front_left_top_corner"))
        self.probe_front_left_top_corner.setProperty("styleClass", _translate("Form", "probeButton"))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.outside_corners_tab), _translate("Form", "        OUTSIDE CORNERS        "))
        self.pushButton_19.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_25.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_22.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_21.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_20.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_24.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_23.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_26.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_27.setProperty("styleClass", _translate("Form", "probeButton"))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.inside_corners_tab), _translate("Form", "       INSIDE CORNERS       "))
        self.pushButton_35.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_33.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_34.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_32.setProperty("styleClass", _translate("Form", "probeButton"))
        self.step_increment_label_4.setText(_translate("Form", "HINT"))
        self.label_33.setText(_translate("Form", "dIAMETER:"))
        self.diameter_hint_2.setText(_translate("Form", "0.0000"))
        self.label_21.setText(_translate("Form", "X :"))
        self.x_hint_2.setText(_translate("Form", "0.0000"))
        self.label_34.setText(_translate("Form", "Y :"))
        self.y_hint_2.setText(_translate("Form", "0.0000"))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.boss_and_pocket_tab), _translate("Form", "       BOSS AND POCKETS       "))
        self.pushButton_36.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_39.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_37.setProperty("styleClass", _translate("Form", "probeButton"))
        self.pushButton_38.setProperty("styleClass", _translate("Form", "probeButton"))
        self.step_increment_label_5.setText(_translate("Form", "HINT"))
        self.label_39.setText(_translate("Form", "X :"))
        self.x_hint_3.setText(_translate("Form", "0.0000"))
        self.label_40.setText(_translate("Form", "Y :"))
        self.y_hint_3.setText(_translate("Form", "0.0000"))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.valley_and_ridge_tab), _translate("Form", "       VALLEYS AND RIDGES       "))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.rotary_axis_tab), _translate("Form", "       ROTARY AXIS         "))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.multi_axis_tab), _translate("Form", "        MULTI-AXIS         "))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.tab_7), _translate("Form", "         CALIBRATE         "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "     STEP OFF WIDTH     "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("Form", "     EXTRA PROBE DEPTH     "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "     MAX DISTANCE     "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "     CLEARANCE     "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("Form", "     PROBE FAST FR     "))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("Form", "     PROBE SLOW FR     "))
        self.probe_tab_widget.setTabText(self.probe_tab_widget.indexOf(self.probe_help_tab), _translate("Form", "        PROBE HELP        "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.probing_tab), _translate("Form", "          PROBING          "))
        self.pushButton_40.setText(_translate("Form", "`"))
        self.pushButton_16.setText(_translate("Form", "1"))
        self.pushButton_28.setText(_translate("Form", "2"))
        self.pushButton_29.setText(_translate("Form", "3"))
        self.pushButton_30.setText(_translate("Form", "4"))
        self.pushButton_31.setText(_translate("Form", "5"))
        self.pushButton_41.setText(_translate("Form", "6"))
        self.pushButton_42.setText(_translate("Form", "7"))
        self.pushButton_43.setText(_translate("Form", "8"))
        self.pushButton_44.setText(_translate("Form", "9"))
        self.pushButton_45.setText(_translate("Form", "0"))
        self.pushButton_46.setText(_translate("Form", "-"))
        self.pushButton_47.setText(_translate("Form", "="))
        self.pushButton_48.setText(_translate("Form", "BACK"))
        self.pushButton_85.setText(_translate("Form", "INSERT"))
        self.pushButton.setText(_translate("Form", "7"))
        self.pushButton_2.setText(_translate("Form", "8"))
        self.pushButton_3.setText(_translate("Form", "9"))
        self.pushButton_49.setText(_translate("Form", "÷"))
        self.pushButton_50.setText(_translate("Form", "TAB"))
        self.pushButton_51.setText(_translate("Form", "Q"))
        self.pushButton_52.setText(_translate("Form", "W"))
        self.pushButton_53.setText(_translate("Form", "E"))
        self.pushButton_54.setText(_translate("Form", "R"))
        self.pushButton_55.setText(_translate("Form", "T"))
        self.pushButton_56.setText(_translate("Form", "Y"))
        self.pushButton_57.setText(_translate("Form", "U"))
        self.pushButton_58.setText(_translate("Form", "I"))
        self.pushButton_59.setText(_translate("Form", "O"))
        self.pushButton_60.setText(_translate("Form", "P"))
        self.pushButton_61.setText(_translate("Form", "["))
        self.pushButton_62.setText(_translate("Form", "]"))
        self.pushButton_63.setText(_translate("Form", "\\"))
        self.pushButton_79.setText(_translate("Form", "DEL"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_64.setText(_translate("Form", "×"))
        self.pushButton_65.setText(_translate("Form", "CAPS"))
        self.pushButton_66.setText(_translate("Form", "A"))
        self.pushButton_67.setText(_translate("Form", "S"))
        self.pushButton_68.setText(_translate("Form", "D"))
        self.pushButton_69.setText(_translate("Form", "F"))
        self.pushButton_70.setText(_translate("Form", "G"))
        self.pushButton_71.setText(_translate("Form", "H"))
        self.pushButton_72.setText(_translate("Form", "J"))
        self.pushButton_73.setText(_translate("Form", "K"))
        self.pushButton_74.setText(_translate("Form", "L"))
        self.pushButton_75.setText(_translate("Form", ";"))
        self.pushButton_76.setText(_translate("Form", "\'"))
        self.pushButton_77.setText(_translate("Form", "ENTER"))
        self.pushButton_83.setText(_translate("Form", "HOME"))
        self.pushButton_7.setText(_translate("Form", "1"))
        self.pushButton_8.setText(_translate("Form", "2"))
        self.pushButton_9.setText(_translate("Form", "3"))
        self.pushButton_78.setText(_translate("Form", "−"))
        self.pushButton_80.setText(_translate("Form", "SHIFT"))
        self.pushButton_81.setText(_translate("Form", "Z"))
        self.pushButton_82.setText(_translate("Form", "X"))
        self.pushButton_84.setText(_translate("Form", "C"))
        self.pushButton_86.setText(_translate("Form", "V"))
        self.pushButton_87.setText(_translate("Form", "B"))
        self.pushButton_88.setText(_translate("Form", "N"))
        self.pushButton_89.setText(_translate("Form", "M"))
        self.pushButton_90.setText(_translate("Form", ","))
        self.pushButton_91.setText(_translate("Form", "."))
        self.pushButton_92.setText(_translate("Form", "/"))
        self.pushButton_93.setText(_translate("Form", "shift"))
        self.pushButton_95.setText(_translate("Form", "END"))
        self.pushButton_96.setText(_translate("Form", "0"))
        self.pushButton_97.setText(_translate("Form", "."))
        self.pushButton_99.setText(_translate("Form", "+"))
        self.pushButton_100.setText(_translate("Form", "CTRL"))
        self.pushButton_101.setText(_translate("Form", "ALT"))
        self.pushButton_103.setText(_translate("Form", "FN"))
        self.pushButton_104.setText(_translate("Form", "CTRL"))
        self.pushButton_108.setText(_translate("Form", "CANCEL"))
        self.pushButton_109.setStyleSheet(_translate("Form", "QPushButton{ \n"
"    background: rgb(97, 98, 99);\n"
"    color: white;\n"
"    font: 14pt \"Bebas Kai\";\n"
"}"))
        self.pushButton_109.setText(_translate("Form", "in/mm"))
        self.pushButton_110.setText(_translate("Form", "ENTER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "          CONVERSATIONAL          "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "          SETTINGS           "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Form", "          STATUS           "))
        self.z_plus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:z,pos"))
        self.z_minus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:z,neg"))
        self.x_plus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:x,pos"))
        self.x_minus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:x,neg"))
        self.y_minus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:y,neg"))
        self.y_plus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:y,pos"))
        self.a_minus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:a,neg"))
        self.a_plus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:a,pos"))
        self.b_minus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:b,neg"))
        self.b_plus_jogbutton.setProperty("actionName", _translate("Form", "machine.jog.axis:b,pos"))
        self.label_20.setText(_translate("Form", "MACHINE STATUS:"))
        self.statuslabel_15.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:gcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Codes\"}]"))
        self.statuslabel_16.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:mcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Mcodes\"}]"))
        self.tabWidget_24.setTabText(self.tabWidget_24.indexOf(self.tabWidget_24Page1), _translate("Form", "     JOG CONTROL     "))
        self.statuslabel_13.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:gcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Codes\"}]"))
        self.statuslabel_14.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"str\", \"url\": \"status:mcodes?text\"}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Active Mcodes\"}]"))
        self.label_19.setText(_translate("Form", "MACHINE STATUS:"))
        self.tabWidget_24.setTabText(self.tabWidget_24.indexOf(self.tab_17), _translate("Form", "       CUSTOM       "))
        self.actionbutton_3.setText(_translate("Form", "CYCLE START"))
        self.actionbutton_3.setProperty("actionName", _translate("Form", "program.run"))
        self.actionbutton_7.setText(_translate("Form", "RUN FM HERE"))
        self.actionbutton_7.setProperty("actionName", _translate("Form", "program.run-from-line"))
        self.actionbutton_10.setText(_translate("Form", "FEED HOLD"))
        self.actionbutton_10.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == \'Paused\'\", \"name\": \"check when paused\"}]"))
        self.actionbutton_10.setProperty("actionName", _translate("Form", "program.pause"))
        self.actionbutton.setText(_translate("Form", "SINGLE BLOCK"))
        self.actionbutton.setProperty("actionName", _translate("Form", "program.step"))
        self.actionbutton_5.setText(_translate("Form", "STOP"))
        self.actionbutton_5.setProperty("actionName", _translate("Form", "program.abort"))
        self.actionbutton_9.setText(_translate("Form", "Flood"))
        self.actionbutton_9.setProperty("actionName", _translate("Form", "coolant.flood.toggle"))
        self.actionbutton_6.setText(_translate("Form", "BLOCK DELETE"))
        self.actionbutton_6.setProperty("actionName", _translate("Form", "program.block-delete.toggle"))
        self.actionbutton_8.setText(_translate("Form", "Mist"))
        self.actionbutton_8.setProperty("actionName", _translate("Form", "coolant.mist.toggle"))
        self.actionbutton_2.setText(_translate("Form", "M01 BREAK"))
        self.actionbutton_2.setProperty("actionName", _translate("Form", "program.optional-stop.toggle"))
        self.power_button.setText(_translate("Form", "POWER"))
        self.power_button.setProperty("actionName", _translate("Form", "machine.power.toggle"))
        self.feedrate_2.setText(_translate("Form", "ET"))
        self.label_26.setText(_translate("Form", "0:00:00"))
        self.exit_button.setText(_translate("Form", "E-STOP"))
        self.exit_button.setProperty("actionName", _translate("Form", "machine.estop.toggle"))
        self.ref_coilumn_header_3.setText(_translate("Form", "  T"))
        self.tool_number_entry_box.setText(_translate("Form", "0"))
        self.m6_button.setText(_translate("Form", "M6"))
        self.m6_button.setProperty("MDICommand", _translate("Form", "T#<tool_number_entry_box> M6"))
        self.G43.setText(_translate("Form", "G43"))
        self.G43.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"\'G43\' in ch[0]\", \"name\": \"G43\"}, {\"channels\": [{\"url\": \"status:tool_in_spindle\", \"trigger\": false}, {\"url\": \"status:interp_state\", \"trigger\": true}, {\"url\": \"status:homed\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0] != 0\", \"name\": \"disable if no tool loaded\"}]"))
        self.G43.setProperty("MDICommand", _translate("Form", "G43"))
        self.G49.setText(_translate("Form", "G49"))
        self.G49.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:gcodes?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"\'G49\' in ch[0]\", \"name\": \"G49\"}]"))
        self.G49.setProperty("MDICommand", _translate("Form", "G49"))
        self.go_to_g30_button_2.setText(_translate("Form", "GO TO ZERO"))
        self.go_to_g30_button_2.setProperty("actionName", _translate("Form", "machine.issue-mdi:G0 X0 Y0 Z0"))
        self.go_to_g30.setText(_translate("Form", "GO TO G30"))
        self.go_to_g30.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:gcodes\", \"trigger\": true}], \"property\": \"None\", \"expression\": \"\", \"name\": \"go to g30\"}]"))
        self.go_to_g30.setProperty("MDICommand", _translate("Form", "G30"))
        self.work_column_header_4.setText(_translate("Form", "LENGTH"))
        self.tool_length.setText(_translate("Form", "0.0000"))
        self.tool_length.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?z_offset\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Length\"}]"))
        self.tool_length.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_length.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.statuslabel_8.setProperty("rules", _translate("Form", "[\n"
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
"]"))
        self.statuslabel_8.setProperty("statusItem", _translate("Form", "program_units"))
        self.work_column_header_5.setText(_translate("Form", "DIAM"))
        self.tool_diameter.setText(_translate("Form", "0.0000"))
        self.tool_diameter.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"tooltable:current_tool?diameter\", \"trigger\": true}, {\"url\": \"status:linear_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0]) if ch[1] == \'in\' else \\\"{:.4f}\\\".format(ch[0])\", \"name\": \"Tool Diameter\"}]"))
        self.tool_diameter.setProperty("format", _translate("Form", "{:.3f}"))
        self.tool_diameter.setProperty("statusItem", _translate("Form", "tool_offset.3"))
        self.statuslabel_11.setProperty("rules", _translate("Form", "[\n"
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
"]"))
        self.statuslabel_11.setProperty("statusItem", _translate("Form", "program_units"))
        self.axisactionbutton_5.setText(_translate("Form", "REFERENCE ALL"))
        self.axisactionbutton_5.setProperty("actionName", _translate("Form", "machine.home.all"))
        self.axis_column_header.setText(_translate("Form", "AXIS"))
        self.statuslabel_12.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + \' WORK\'\\n\", \"name\": \"WCS Header\"}]"))
        self.work_column_header_2.setText(_translate("Form", "MACHINE"))
        self.dtg_column_header.setText(_translate("Form", "DTG"))
        self.dtg_column_header_3.setText(_translate("Form", "REF"))
        self.zero_x_button_3.setText(_translate("Form", "X"))
        self.zero_x_button_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_x_button_3.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} X0.0"))
        self.statuslabel_40.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"(\'%.4f\' if ch[1] == \'in\' else \'%.3f\') % ch[0][0]\", \"name\": \"REL axis position\"}]"))
        self.statuslabel_45.setProperty("style", _translate("Form", "unhomed"))
        self.statuslabel_45.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][0])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[0].homed\", \"trigger\": true}, {\"url\": \"status:joint[0].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]"))
        self.statuslabel_75.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"(\'%.4f\' if ch[1] == \'in\' else \'%.3f\') % ch[0][0]\", \"name\": \"REL axis position\"}]"))
        self.axisactionbutton_6.setText(_translate("Form", "REF X"))
        self.axisactionbutton_6.setProperty("actionName", _translate("Form", "machine.home.axis:x"))
        self.zero_y_button_3.setText(_translate("Form", "Y"))
        self.zero_y_button_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_y_button_3.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} Y0.0"))
        self.statuslabel_41.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"REL axis position\"}]"))
        self.statuslabel_46.setProperty("style", _translate("Form", "unhomed"))
        self.statuslabel_46.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[1].homed\", \"trigger\": true}, {\"url\": \"status:joint[1].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]"))
        self.statuslabel_76.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][1])\", \"name\": \"REL axis position\"}]"))
        self.axisactionbutton_3.setText(_translate("Form", "REF Y"))
        self.axisactionbutton_3.setProperty("actionName", _translate("Form", "machine.home.axis:y"))
        self.zero_z_button_3.setText(_translate("Form", "Z"))
        self.zero_z_button_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_z_button_3.setProperty("MDICommand", _translate("Form", "G10 L20 P{ch[0]} Z0.0"))
        self.statuslabel_42.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"REL axis position\"}]"))
        self.statuslabel_47.setProperty("style", _translate("Form", "unhomed"))
        self.statuslabel_47.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[2].homed\", \"trigger\": true}, {\"url\": \"status:joint[2].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]"))
        self.statuslabel_77.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][2])\", \"name\": \"REL axis position\"}]"))
        self.axisactionbutton.setText(_translate("Form", "REF Z"))
        self.axisactionbutton.setProperty("actionName", _translate("Form", "machine.home.axis:z"))
        self.zero_a_button_3.setText(_translate("Form", "A"))
        self.zero_a_button_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_a_button_3.setProperty("MDICommand", _translate("Form", "G10 L2 P{ch[0]} A0.0"))
        self.statuslabel_43.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"REL axis position\"}]"))
        self.statuslabel_48.setProperty("style", _translate("Form", "unhomed"))
        self.statuslabel_48.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[3].homed\", \"trigger\": true}, {\"url\": \"status:joint[3].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]"))
        self.statuslabel_78.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][3])\", \"name\": \"REL axis position\"}]"))
        self.axisactionbutton_2.setText(_translate("Form", "REF A"))
        self.axisactionbutton_2.setProperty("actionName", _translate("Form", "machine.home.axis:a"))
        self.zero_b_button_3.setText(_translate("Form", "B"))
        self.zero_b_button_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]"))
        self.zero_b_button_3.setProperty("MDICommand", _translate("Form", "G10 L2 P{ch[0]} B0.0"))
        self.statuslabel_44.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?rel\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"REL axis position\"}]"))
        self.statuslabel_49.setProperty("style", _translate("Form", "unhomed"))
        self.statuslabel_49.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?abs\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"axis position\"}, {\"channels\": [{\"url\": \"status:joint[4].homed\", \"trigger\": true}, {\"url\": \"status:joint[4].homing\", \"trigger\": true}], \"property\": \"Style Class\", \"expression\": \"\\\"homed\\\" if ch[0] else \\\"homing\\\" if ch[1] else \\\"unhomed\\\"\", \"name\": \"homing indicator\"}]"))
        self.statuslabel_79.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"position:axis?dtg\", \"trigger\": true}, {\"url\": \"status:program_units?text\", \"trigger\": false}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][4]) if ch[1] == \'in\' else \\\"{:.3f}\\\".format(ch[0][4])\", \"name\": \"REL axis position\"}]"))
        self.axisactionbutton_4.setText(_translate("Form", "REF B"))
        self.axisactionbutton_4.setProperty("actionName", _translate("Form", "machine.home.axis:b"))
        self.statuslabel.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:feedrate\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\'{:.0%}\'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]"))
        self.statuslabel.setProperty("statusItem", _translate("Form", "feedrate"))
        self.actionslider_4.setProperty("actionName", _translate("Form", "machine.rapid-override.set"))
        self.statuslabel_2.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:spindle[0].override\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\'{:.0%}\'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]"))
        self.statuslabel_2.setProperty("statusItem", _translate("Form", "spindle.0.override"))
        self.statuslabel_3.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:rapidrate\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\'{:.0%}\'.format(ch[0])\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]"))
        self.statuslabel_3.setProperty("statusItem", _translate("Form", "rapidrate"))
        self.work_column_header_3.setText(_translate("Form", "SPINDLE\n"
"LOAD"))
        self.statuslabel_4.setProperty("rules", _translate("Form", "[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:max_velocity\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"float\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\'{:.0f}\'.format(ch[0] * 60)\",\n"
"        \"name\": \"New Rule\",\n"
"        \"property\": \"Text\"\n"
"    }\n"
"]"))
        self.statuslabel_4.setProperty("statusItem", _translate("Form", "max_velocity"))
        self.statuslabel_4.setProperty("fromat", _translate("Form", "{:.0f}"))
        self.actionslider.setProperty("actionName", _translate("Form", "spindle.override"))
        self.actionbutton_28.setText(_translate("Form", "S 100%"))
        self.actionbutton_28.setProperty("actionName", _translate("Form", "spindle.override.reset"))
        self.actionslider_2.setProperty("actionName", _translate("Form", "machine.feed-override.set"))
        self.actionslider_3.setProperty("actionName", _translate("Form", "machine.max-velocity.set"))
        self.actionbutton_29.setText(_translate("Form", "F 100%"))
        self.actionbutton_29.setProperty("actionName", _translate("Form", "machine.feed-override.reset"))
        self.actionbutton_30.setText(_translate("Form", "MV 100%"))
        self.actionbutton_30.setProperty("actionName", _translate("Form", "machine.max-velocity.reset"))
        self.actionbutton_31.setText(_translate("Form", "R 100%"))
        self.actionbutton_31.setProperty("actionName", _translate("Form", "machine.rapid-override.reset"))
        self.actionslider_5.setProperty("actionName", _translate("Form", "machine.jog.set-linear-speed-percentage"))
        self.statuslabel_6.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:current_vel\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'%.1f\' % (ch[0] * 60)\", \"name\": \"cur vel\"}]"))
        self.statuslabel_6.setProperty("format", _translate("Form", "{:.1f}"))
        self.rpm_label_3.setText(_translate("Form", "FEEDRATE"))
        self.statuslabel_10.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:program_units?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0]\", \"name\": \"Linear Units\"}]"))
        self.statuslabel_10.setProperty("statusItem", _translate("Form", "linear_units"))
        self.work_column_header_7.setText(_translate("Form", "/M"))
        self.statuslabel_7.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:settings\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'%.1f\' % ch[0][1]\", \"name\": \"F Word\"}]"))
        self.statuslabel_7.setProperty("format", _translate("Form", "{:.1f}"))
        self.statuslabel_5.setProperty("rules", _translate("Form", "[{\"channels\": [{\"trigger\": true, \"type\": \"float\", \"url\": \"status:spindle[0].speed\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.2f}\\\".format(ch[0])\", \"name\": \"Speed\"}]"))
        self.statuslabel_5.setProperty("format", _translate("Form", "{:.2f}"))
        self.rpm_label.setText(_translate("Form", "SPINDLE RPM"))
        self.statuslabel_9.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:settings\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"str( ch[0][2] )\", \"name\": \"S Word\"}]"))
        self.statuslabel_9.setProperty("format", _translate("Form", "{:.2f}"))
        self.spindle_rev_button.setText(_translate("Form", "REV"))
        self.spindle_rev_button.setProperty("actionName", _translate("Form", "spindle.reverse"))
        self.spindle_stop_button.setText(_translate("Form", "STOP"))
        self.spindle_stop_button.setProperty("actionName", _translate("Form", "spindle.off"))
        self.spindle_fwd_button.setText(_translate("Form", "FWD"))
        self.spindle_fwd_button.setProperty("actionName", _translate("Form", "spindle.forward"))
        self.menuExit.setTitle(_translate("Form", "File"))
        self.menuRecentFiles.setTitle(_translate("Form", "Recent &Files"))
        self.menuMachine.setTitle(_translate("Form", "Machine"))
        self.menuHoming.setTitle(_translate("Form", "Homing"))
        self.menuCooling.setTitle(_translate("Form", "Cooling"))
        self.menuView.setTitle(_translate("Form", "View"))
        self.actionExit.setText(_translate("Form", "Exit"))
        self.actionOpen.setText(_translate("Form", "&Open ..."))
        self.actionOpen.setShortcut(_translate("Form", "O"))
        self.actionClose.setText(_translate("Form", "Close"))
        self.actionReload.setText(_translate("Form", "&Reload"))
        self.actionReload.setShortcut(_translate("Form", "Ctrl+R"))
        self.actionSave_As.setText(_translate("Form", "Save As ..."))
        self.actionHome_X.setText(_translate("Form", "Home &X"))
        self.actionHome_Y.setText(_translate("Form", "Home &Y"))
        self.actionHome_Z.setText(_translate("Form", "Home &Z"))
        self.action_EmergencyStop_toggle.setText(_translate("Form", "Toggle E-stop"))
        self.action_EmergencyStop_toggle.setShortcut(_translate("Form", "F1"))
        self.action_MachinePower_toggle.setText(_translate("Form", "Machine Power"))
        self.action_MachinePower_toggle.setShortcut(_translate("Form", "F2"))
        self.actionHome_All.setText(_translate("Form", "Home All"))
        self.actionRun_Program.setText(_translate("Form", "Run Program"))
        self.actionRun_Program.setShortcut(_translate("Form", "R"))
        self.actionFile1.setText(_translate("Form", "File1"))
        self.actionReport_Actual_Position.setText(_translate("Form", "Report Actual Position"))
        self.actionTest.setText(_translate("Form", "Test"))
        self.action_Mist_toggle.setText(_translate("Form", "Mist On"))
        self.action_Mist_toggle.setShortcut(_translate("Form", "F7"))
        self.action_Flood_toggle.setText(_translate("Form", "Flood On"))
        self.action_Flood_toggle.setShortcut(_translate("Form", "F8"))

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
from qtpyvcp.widgets.display_widgets.gcode_backplot.gcode_backplot import GcodeBackplot
from qtpyvcp.widgets.display_widgets.load_meter import LoadMeter
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.widgets.input_widgets.action_slider import ActionSlider
from qtpyvcp.widgets.input_widgets.file_system import FileSystemTable, RemovableDeviceComboBox
from qtpyvcp.widgets.input_widgets.gcode_editor import GcodeEditor
from qtpyvcp.widgets.input_widgets.jog_increment import JogIncrementWidget
from qtpyvcp.widgets.input_widgets.mdientry_widget import MDIEntry
from qtpyvcp.widgets.input_widgets.recent_file_combobox import RecentFileComboBox
from qtpyvcp.widgets.input_widgets.tool_table import ToolTable
import probe_basic_rc
