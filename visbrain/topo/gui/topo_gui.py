# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/etienne/Toolbox/visbrain/visbrain/topo/gui/topo_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1188, 907)
        font = QtGui.QFont()
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.q_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q_widget.sizePolicy().hasHeightForWidth())
        self.q_widget.setSizePolicy(sizePolicy)
        self.q_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.q_widget.setMaximumSize(QtCore.QSize(450, 16777215))
        self.q_widget.setObjectName("q_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.q_widget)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.QuickSettings = QtWidgets.QTabWidget(self.q_widget)
        self.QuickSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.QuickSettings.setAutoFillBackground(False)
        self.QuickSettings.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.QuickSettings.setMovable(True)
        self.QuickSettings.setObjectName("QuickSettings")
        self.q_Detection = QtWidgets.QWidget()
        self.q_Detection.setObjectName("q_Detection")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.q_Detection)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.groupBox_3 = QtWidgets.QGroupBox(self.q_Detection)
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 0, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.groupBox_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_4.addWidget(self.line_6, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_4.addWidget(self.doubleSpinBox_6, 1, 2, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.verticalLayout_22.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.q_Detection)
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_5.addWidget(self.doubleSpinBox_7, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.groupBox_4)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_5.addWidget(self.line_8, 2, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_6.addWidget(self.doubleSpinBox_8, 0, 1, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout_6.addWidget(self.doubleSpinBox_9, 1, 1, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout_6.addWidget(self.doubleSpinBox_10, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 2, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.groupBox_4)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_5.addWidget(self.line_9, 0, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.groupBox_4)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_5.addWidget(self.line_10, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.verticalLayout_22.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.q_Detection)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_2.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_2.addWidget(self.doubleSpinBox_3, 1, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_22.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.q_Detection)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 0, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_3.addWidget(self.doubleSpinBox_5, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout_22.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem2)
        self.QuickSettings.addTab(self.q_Detection, "")
        self.verticalLayout_4.addWidget(self.QuickSettings)
        self.horizontalLayout_2.addWidget(self.q_widget)
        self._TopoLayout = QtWidgets.QVBoxLayout()
        self._TopoLayout.setObjectName("_TopoLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._TopoLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self._TopoLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionCortical_repartition = QtWidgets.QAction(MainWindow)
        self.actionCortical_repartition.setObjectName("actionCortical_repartition")
        self.actionCortical = QtWidgets.QAction(MainWindow)
        self.actionCortical.setObjectName("actionCortical")
        self.actionSagittal = QtWidgets.QAction(MainWindow)
        self.actionSagittal.setObjectName("actionSagittal")
        self.actionAxial = QtWidgets.QAction(MainWindow)
        self.actionAxial.setObjectName("actionAxial")
        self.actionCamera = QtWidgets.QAction(MainWindow)
        self.actionCamera.setObjectName("actionCamera")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(MainWindow)
        self.actionRight.setObjectName("actionRight")
        self.menuDispSettings = QtWidgets.QAction(MainWindow)
        self.menuDispSettings.setCheckable(True)
        self.menuDispSettings.setChecked(True)
        self.menuDispSettings.setObjectName("menuDispSettings")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionProjection = QtWidgets.QAction(MainWindow)
        self.actionProjection.setObjectName("actionProjection")
        self.actionRepartition = QtWidgets.QAction(MainWindow)
        self.actionRepartition.setObjectName("actionRepartition")
        self.actionShortcuts = QtWidgets.QAction(MainWindow)
        self.actionShortcuts.setCheckable(True)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionUi_settings = QtWidgets.QAction(MainWindow)
        self.actionUi_settings.setCheckable(True)
        self.actionUi_settings.setChecked(False)
        self.actionUi_settings.setObjectName("actionUi_settings")
        self.actionNdPlt = QtWidgets.QAction(MainWindow)
        self.actionNdPlt.setCheckable(True)
        self.actionNdPlt.setObjectName("actionNdPlt")
        self.actionOnedPlt = QtWidgets.QAction(MainWindow)
        self.actionOnedPlt.setCheckable(True)
        self.actionOnedPlt.setObjectName("actionOnedPlt")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setCheckable(True)
        self.actionImage.setObjectName("actionImage")
        self.actionColormap = QtWidgets.QAction(MainWindow)
        self.actionColormap.setCheckable(True)
        self.actionColormap.setObjectName("actionColormap")
        self.menuShortcut = QtWidgets.QAction(MainWindow)
        self.menuShortcut.setObjectName("menuShortcut")
        self.menuDocumentation = QtWidgets.QAction(MainWindow)
        self.menuDocumentation.setObjectName("menuDocumentation")
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionSave_hypnogram = QtWidgets.QAction(MainWindow)
        self.actionSave_hypnogram.setObjectName("actionSave_hypnogram")
        self.actionSave_infos = QtWidgets.QAction(MainWindow)
        self.actionSave_infos.setObjectName("actionSave_infos")
        self.actionSave_scoring = QtWidgets.QAction(MainWindow)
        self.actionSave_scoring.setObjectName("actionSave_scoring")
        self.actionSave_detection = QtWidgets.QAction(MainWindow)
        self.actionSave_detection.setObjectName("actionSave_detection")
        self.actionSave_all = QtWidgets.QAction(MainWindow)
        self.actionSave_all.setObjectName("actionSave_all")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.actionLoad_hypnogram = QtWidgets.QAction(MainWindow)
        self.actionLoad_hypnogram.setObjectName("actionLoad_hypnogram")
        self.menuSaveInfoTable = QtWidgets.QAction(MainWindow)
        self.menuSaveInfoTable.setObjectName("menuSaveInfoTable")
        self.menuSaveScoringTable = QtWidgets.QAction(MainWindow)
        self.menuSaveScoringTable.setObjectName("menuSaveScoringTable")
        self.actionAll = QtWidgets.QAction(MainWindow)
        self.actionAll.setObjectName("actionAll")
        self.menuLoadHypno = QtWidgets.QAction(MainWindow)
        self.menuLoadHypno.setObjectName("menuLoadHypno")
        self.menuLoadData = QtWidgets.QAction(MainWindow)
        self.menuLoadData.setEnabled(False)
        self.menuLoadData.setObjectName("menuLoadData")
        self.actionHypnogram_figure = QtWidgets.QAction(MainWindow)
        self.actionHypnogram_figure.setObjectName("actionHypnogram_figure")
        self.menuLoadConfig = QtWidgets.QAction(MainWindow)
        self.menuLoadConfig.setObjectName("menuLoadConfig")
        self.menuSaveConfig = QtWidgets.QAction(MainWindow)
        self.menuSaveConfig.setObjectName("menuSaveConfig")
        self.menuDownload_pdf_doc = QtWidgets.QAction(MainWindow)
        self.menuDownload_pdf_doc.setObjectName("menuDownload_pdf_doc")
        self.menuSaveHypnogramFigure = QtWidgets.QAction(MainWindow)
        self.menuSaveHypnogramFigure.setObjectName("menuSaveHypnogramFigure")
        self.menuSaveHypnogramData = QtWidgets.QAction(MainWindow)
        self.menuSaveHypnogramData.setObjectName("menuSaveHypnogramData")
        self.menuSaveDetectAll = QtWidgets.QAction(MainWindow)
        self.menuSaveDetectAll.setObjectName("menuSaveDetectAll")
        self.menuSaveDetectSelected = QtWidgets.QAction(MainWindow)
        self.menuSaveDetectSelected.setObjectName("menuSaveDetectSelected")
        self.menuSaveScreenshotEntire = QtWidgets.QAction(MainWindow)
        self.menuSaveScreenshotEntire.setObjectName("menuSaveScreenshotEntire")
        self.menuSaveScreenshotSelected = QtWidgets.QAction(MainWindow)
        self.menuSaveScreenshotSelected.setEnabled(False)
        self.menuSaveScreenshotSelected.setObjectName("menuSaveScreenshotSelected")
        self.menuLoadDetectAll = QtWidgets.QAction(MainWindow)
        self.menuLoadDetectAll.setObjectName("menuLoadDetectAll")
        self.menuLoadDetectSelect = QtWidgets.QAction(MainWindow)
        self.menuLoadDetectSelect.setObjectName("menuLoadDetectSelect")
        self.menuDispSpec = QtWidgets.QAction(MainWindow)
        self.menuDispSpec.setCheckable(True)
        self.menuDispSpec.setChecked(True)
        self.menuDispSpec.setObjectName("menuDispSpec")
        self.menuDispHypno = QtWidgets.QAction(MainWindow)
        self.menuDispHypno.setCheckable(True)
        self.menuDispHypno.setChecked(True)
        self.menuDispHypno.setObjectName("menuDispHypno")
        self.menuDispNavbar = QtWidgets.QAction(MainWindow)
        self.menuDispNavbar.setCheckable(True)
        self.menuDispNavbar.setChecked(True)
        self.menuDispNavbar.setObjectName("menuDispNavbar")
        self.menuDispTimeax = QtWidgets.QAction(MainWindow)
        self.menuDispTimeax.setCheckable(True)
        self.menuDispTimeax.setChecked(True)
        self.menuDispTimeax.setObjectName("menuDispTimeax")
        self.menuDispTopo = QtWidgets.QAction(MainWindow)
        self.menuDispTopo.setCheckable(True)
        self.menuDispTopo.setObjectName("menuDispTopo")
        self.menuDispIndic = QtWidgets.QAction(MainWindow)
        self.menuDispIndic.setCheckable(True)
        self.menuDispIndic.setChecked(True)
        self.menuDispIndic.setObjectName("menuDispIndic")
        self.actionZoom_mode = QtWidgets.QAction(MainWindow)
        self.actionZoom_mode.setCheckable(True)
        self.actionZoom_mode.setObjectName("actionZoom_mode")
        self.menuDispZoom = QtWidgets.QAction(MainWindow)
        self.menuDispZoom.setCheckable(True)
        self.menuDispZoom.setObjectName("menuDispZoom")
        self.menuSettingCleanHyp = QtWidgets.QAction(MainWindow)
        self.menuSettingCleanHyp.setObjectName("menuSettingCleanHyp")
        self.menuSaveAnnotations = QtWidgets.QAction(MainWindow)
        self.menuSaveAnnotations.setObjectName("menuSaveAnnotations")
        self.menuLoadAnnotations = QtWidgets.QAction(MainWindow)
        self.menuLoadAnnotations.setObjectName("menuLoadAnnotations")
        self.menuScreenshot = QtWidgets.QAction(MainWindow)
        self.menuScreenshot.setObjectName("menuScreenshot")
        self.menuFile.addAction(self.menuScreenshot)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.QuickSettings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Topo"))
        self.QuickSettings.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Markers"))
        self.label_9.setText(_translate("MainWindow", "Form"))
        self.label_10.setText(_translate("MainWindow", "Size"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Title"))
        self.label_11.setText(_translate("MainWindow", "Font\n"
"size"))
        self.label_12.setText(_translate("MainWindow", "Text\n"
"offset"))
        self.label_13.setText(_translate("MainWindow", "dy"))
        self.label_14.setText(_translate("MainWindow", "dy"))
        self.label_15.setText(_translate("MainWindow", "dx"))
        self.label_16.setText(_translate("MainWindow", "Color"))
        self.groupBox.setTitle(_translate("MainWindow", "Text"))
        self.label.setText(_translate("MainWindow", "Font\n"
"size"))
        self.label_2.setText(_translate("MainWindow", "Text\n"
"offset"))
        self.label_4.setText(_translate("MainWindow", "dy"))
        self.label_5.setText(_translate("MainWindow", "dy"))
        self.label_3.setText(_translate("MainWindow", "dx"))
        self.label_8.setText(_translate("MainWindow", "Color"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Border"))
        self.label_6.setText(_translate("MainWindow", "Color"))
        self.label_7.setText(_translate("MainWindow", "Width"))
        self.QuickSettings.setTabText(self.QuickSettings.indexOf(self.q_Detection), _translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionCortical_repartition.setText(_translate("MainWindow", "Cortical repartition"))
        self.actionCortical.setText(_translate("MainWindow", "Cortical"))
        self.actionSagittal.setText(_translate("MainWindow", "Sagittal"))
        self.actionAxial.setText(_translate("MainWindow", "Axial"))
        self.actionCamera.setText(_translate("MainWindow", "Camera"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.menuDispSettings.setText(_translate("MainWindow", "Quick settings"))
        self.menuDispSettings.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionProjection.setText(_translate("MainWindow", "Projection"))
        self.actionProjection.setToolTip(_translate("MainWindow", "<html><head/><body><p>Find all vertices under a distance of t_radius with each source and project s_data to the surface</p></body></html>"))
        self.actionProjection.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionRepartition.setText(_translate("MainWindow", "Repartition"))
        self.actionRepartition.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionShortcuts.setText(_translate("MainWindow", "Shortcuts"))
        self.actionShortcuts.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionUi_settings.setText(_translate("MainWindow", "Ui settings"))
        self.actionNdPlt.setText(_translate("MainWindow", "Nd-plot"))
        self.actionOnedPlt.setText(_translate("MainWindow", "1d-plot"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionColormap.setText(_translate("MainWindow", "Colormap"))
        self.menuShortcut.setText(_translate("MainWindow", "Shortcuts"))
        self.menuShortcut.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.menuDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.menuDocumentation.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.actionScreenshot.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave_hypnogram.setText(_translate("MainWindow", "Save hypnogram data"))
        self.actionSave_infos.setText(_translate("MainWindow", "Save infos table"))
        self.actionSave_scoring.setText(_translate("MainWindow", "Save scoring table"))
        self.actionSave_detection.setText(_translate("MainWindow", "Save detection table"))
        self.actionSave_all.setText(_translate("MainWindow", "Save all"))
        self.menuExit.setText(_translate("MainWindow", "Exit"))
        self.menuExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionLoad_hypnogram.setText(_translate("MainWindow", "Load hypnogram"))
        self.menuSaveInfoTable.setText(_translate("MainWindow", "Stats info table"))
        self.menuSaveScoringTable.setText(_translate("MainWindow", "Scoring table"))
        self.actionAll.setText(_translate("MainWindow", "All"))
        self.actionAll.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuLoadHypno.setText(_translate("MainWindow", "Hypnogram"))
        self.menuLoadData.setText(_translate("MainWindow", "Data"))
        self.actionHypnogram_figure.setText(_translate("MainWindow", "Hypnogram figure"))
        self.menuLoadConfig.setText(_translate("MainWindow", "GUI config"))
        self.menuSaveConfig.setText(_translate("MainWindow", "GUI config"))
        self.menuDownload_pdf_doc.setText(_translate("MainWindow", "Download pdf doc"))
        self.menuSaveHypnogramFigure.setText(_translate("MainWindow", "Figure"))
        self.menuSaveHypnogramData.setText(_translate("MainWindow", "Data"))
        self.menuSaveDetectAll.setText(_translate("MainWindow", "All detections"))
        self.menuSaveDetectSelected.setText(_translate("MainWindow", "Selected detection"))
        self.menuSaveScreenshotEntire.setText(_translate("MainWindow", "Entire window"))
        self.menuSaveScreenshotSelected.setText(_translate("MainWindow", "Selected canvas"))
        self.menuLoadDetectAll.setText(_translate("MainWindow", "All"))
        self.menuLoadDetectSelect.setText(_translate("MainWindow", "Selected"))
        self.menuDispSpec.setText(_translate("MainWindow", "Spectrogram"))
        self.menuDispSpec.setShortcut(_translate("MainWindow", "S"))
        self.menuDispHypno.setText(_translate("MainWindow", "Hypnogram"))
        self.menuDispHypno.setShortcut(_translate("MainWindow", "H"))
        self.menuDispNavbar.setText(_translate("MainWindow", "Navigation bar"))
        self.menuDispNavbar.setShortcut(_translate("MainWindow", "P"))
        self.menuDispTimeax.setText(_translate("MainWindow", "Time axis"))
        self.menuDispTimeax.setShortcut(_translate("MainWindow", "X"))
        self.menuDispTopo.setText(_translate("MainWindow", "Topoplot"))
        self.menuDispTopo.setShortcut(_translate("MainWindow", "T"))
        self.menuDispIndic.setText(_translate("MainWindow", "Time indicators"))
        self.menuDispIndic.setShortcut(_translate("MainWindow", "I"))
        self.actionZoom_mode.setText(_translate("MainWindow", "Zoom mode"))
        self.actionZoom_mode.setShortcut(_translate("MainWindow", "Z"))
        self.menuDispZoom.setText(_translate("MainWindow", "Zoom mode"))
        self.menuDispZoom.setShortcut(_translate("MainWindow", "Z"))
        self.menuSettingCleanHyp.setText(_translate("MainWindow", "Clean hypnogram"))
        self.menuSaveAnnotations.setText(_translate("MainWindow", "Annotation"))
        self.menuLoadAnnotations.setText(_translate("MainWindow", "Annotations"))
        self.menuScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.menuScreenshot.setShortcut(_translate("MainWindow", "Ctrl+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

