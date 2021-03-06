# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolbarLayout = QtWidgets.QHBoxLayout()
        self.toolbarLayout.setContentsMargins(-1, -1, -1, 0)
        self.toolbarLayout.setObjectName("toolbarLayout")
        self.verticalLayout.addLayout(self.toolbarLayout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(12)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plotLayout = QtWidgets.QVBoxLayout()
        self.plotLayout.setObjectName("plotLayout")
        self.horizontalLayout_2.addLayout(self.plotLayout)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QComboBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.addItem("")
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)
        self.nameSelection = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameSelection.sizePolicy().hasHeightForWidth())
        self.nameSelection.setSizePolicy(sizePolicy)
        self.nameSelection.setWhatsThis("")
        self.nameSelection.setObjectName("nameSelection")
        self.gridLayout.addWidget(self.nameSelection, 0, 0, 1, 1)
        self.selectByName = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectByName.sizePolicy().hasHeightForWidth())
        self.selectByName.setSizePolicy(sizePolicy)
        self.selectByName.setObjectName("selectByName")
        self.gridLayout.addWidget(self.selectByName, 0, 1, 1, 1)
        self.createGroup = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createGroup.sizePolicy().hasHeightForWidth())
        self.createGroup.setSizePolicy(sizePolicy)
        self.createGroup.setObjectName("createGroup")
        self.gridLayout.addWidget(self.createGroup, 1, 1, 1, 1)
        self.groupName = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupName.sizePolicy().hasHeightForWidth())
        self.groupName.setSizePolicy(sizePolicy)
        self.groupName.setText("")
        self.groupName.setObjectName("groupName")
        self.gridLayout.addWidget(self.groupName, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.onlyShowSelected = QtWidgets.QCheckBox(self.layoutWidget)
        self.onlyShowSelected.setObjectName("onlyShowSelected")
        self.verticalLayout_2.addWidget(self.onlyShowSelected)
        self.spectraList = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectraList.sizePolicy().hasHeightForWidth())
        self.spectraList.setSizePolicy(sizePolicy)
        self.spectraList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.spectraList.setObjectName("spectraList")
        self.verticalLayout_2.addWidget(self.spectraList)
        self.loadLabel = QtWidgets.QLabel(self.layoutWidget)
        self.loadLabel.setText("")
        self.loadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadLabel.setObjectName("loadLabel")
        self.verticalLayout_2.addWidget(self.loadLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFlags = QtWidgets.QMenu(self.menubar)
        self.menuFlags.setObjectName("menuFlags")
        self.menuOperators = QtWidgets.QMenu(self.menubar)
        self.menuOperators.setObjectName("menuOperators")
        self.menuPlot_Metric = QtWidgets.QMenu(self.menuOperators)
        self.menuPlot_Metric.setObjectName("menuPlot_Metric")
        self.menuSelection = QtWidgets.QMenu(self.menubar)
        self.menuSelection.setObjectName("menuSelection")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPlot_Config = QtWidgets.QAction(MainWindow)
        self.actionPlot_Config.setObjectName("actionPlot_Config")
        self.actionFlag_Selection = QtWidgets.QAction(MainWindow)
        self.actionFlag_Selection.setObjectName("actionFlag_Selection")
        self.actionShow_Hide_Flagged = QtWidgets.QAction(MainWindow)
        self.actionShow_Hide_Flagged.setObjectName("actionShow_Hide_Flagged")
        self.actionExport_Flags = QtWidgets.QAction(MainWindow)
        self.actionExport_Flags.setObjectName("actionExport_Flags")
        self.actionStitch = QtWidgets.QAction(MainWindow)
        self.actionStitch.setObjectName("actionStitch")
        self.actionJump_Correct = QtWidgets.QAction(MainWindow)
        self.actionJump_Correct.setObjectName("actionJump_Correct")
        self.actionMean = QtWidgets.QAction(MainWindow)
        self.actionMean.setObjectName("actionMean")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionMode = QtWidgets.QAction(MainWindow)
        self.actionMode.setObjectName("actionMode")
        self.actionMax = QtWidgets.QAction(MainWindow)
        self.actionMax.setObjectName("actionMax")
        self.actionMin = QtWidgets.QAction(MainWindow)
        self.actionMin.setObjectName("actionMin")
        self.actionMean_2 = QtWidgets.QAction(MainWindow)
        self.actionMean_2.setObjectName("actionMean_2")
        self.actionMedian_2 = QtWidgets.QAction(MainWindow)
        self.actionMedian_2.setObjectName("actionMedian_2")
        self.actionMaximum = QtWidgets.QAction(MainWindow)
        self.actionMaximum.setObjectName("actionMaximum")
        self.actionMinimum = QtWidgets.QAction(MainWindow)
        self.actionMinimum.setObjectName("actionMinimum")
        self.actionStandard_Deviation = QtWidgets.QAction(MainWindow)
        self.actionStandard_Deviation.setObjectName("actionStandard_Deviation")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear_Selection = QtWidgets.QAction(MainWindow)
        self.actionClear_Selection.setObjectName("actionClear_Selection")
        self.actionInvert_Selection = QtWidgets.QAction(MainWindow)
        self.actionInvert_Selection.setObjectName("actionInvert_Selection")
        self.actionMove_Selection_to_Top = QtWidgets.QAction(MainWindow)
        self.actionMove_Selection_to_Top.setObjectName("actionMove_Selection_to_Top")
        self.actionFilter_Selection_by_name = QtWidgets.QAction(MainWindow)
        self.actionFilter_Selection_by_name.setObjectName("actionFilter_Selection_by_name")
        self.actionUnflag_Selection = QtWidgets.QAction(MainWindow)
        self.actionUnflag_Selection.setObjectName("actionUnflag_Selection")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionPlot_Config)
        self.menuFlags.addAction(self.actionFlag_Selection)
        self.menuFlags.addAction(self.actionUnflag_Selection)
        self.menuFlags.addAction(self.actionShow_Hide_Flagged)
        self.menuFlags.addAction(self.actionExport_Flags)
        self.menuPlot_Metric.addAction(self.actionMean_2)
        self.menuPlot_Metric.addAction(self.actionMedian_2)
        self.menuPlot_Metric.addAction(self.actionMaximum)
        self.menuPlot_Metric.addAction(self.actionMinimum)
        self.menuPlot_Metric.addAction(self.actionStandard_Deviation)
        self.menuOperators.addAction(self.actionStitch)
        self.menuOperators.addAction(self.actionJump_Correct)
        self.menuOperators.addAction(self.menuPlot_Metric.menuAction())
        self.menuSelection.addAction(self.actionClear)
        self.menuSelection.addAction(self.actionClear_Selection)
        self.menuSelection.addAction(self.actionInvert_Selection)
        self.menuSelection.addAction(self.actionMove_Selection_to_Top)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFlags.menuAction())
        self.menubar.addAction(self.menuOperators.menuAction())
        self.menubar.addAction(self.menuSelection.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpecDAL GUI"))
        self.label.setText(_translate("MainWindow", "Select Group:"))
        self.groupBox.setItemText(0, _translate("MainWindow", "--"))
        self.nameSelection.setToolTip(_translate("MainWindow", "Select Spectra by Name"))
        self.nameSelection.setPlaceholderText(_translate("MainWindow", "Select by Name"))
        self.selectByName.setText(_translate("MainWindow", "Select"))
        self.createGroup.setText(_translate("MainWindow", "Name Group"))
        self.groupName.setPlaceholderText(_translate("MainWindow", "Name for Selection"))
        self.onlyShowSelected.setText(_translate("MainWindow", "Only Show Selected"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFlags.setTitle(_translate("MainWindow", "Flags"))
        self.menuOperators.setTitle(_translate("MainWindow", "Operators"))
        self.menuPlot_Metric.setTitle(_translate("MainWindow", "Plot Metric..."))
        self.menuSelection.setTitle(_translate("MainWindow", "Selection"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPlot_Config.setText(_translate("MainWindow", "Plot Config"))
        self.actionFlag_Selection.setText(_translate("MainWindow", "Flag Selection"))
        self.actionShow_Hide_Flagged.setText(_translate("MainWindow", "Show/Hide Flagged"))
        self.actionExport_Flags.setText(_translate("MainWindow", "Export Flags"))
        self.actionStitch.setText(_translate("MainWindow", "Stitch"))
        self.actionJump_Correct.setText(_translate("MainWindow", "Jump Correct"))
        self.actionMean.setText(_translate("MainWindow", "Mean"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionMode.setText(_translate("MainWindow", "Mode"))
        self.actionMax.setText(_translate("MainWindow", "Max"))
        self.actionMin.setText(_translate("MainWindow", "Min"))
        self.actionMean_2.setText(_translate("MainWindow", "Mean"))
        self.actionMedian_2.setText(_translate("MainWindow", "Median"))
        self.actionMaximum.setText(_translate("MainWindow", "Maximum"))
        self.actionMinimum.setText(_translate("MainWindow", "Minimum"))
        self.actionStandard_Deviation.setText(_translate("MainWindow", "Standard Deviation"))
        self.actionClear.setText(_translate("MainWindow", "Select All"))
        self.actionClear_Selection.setText(_translate("MainWindow", "Clear Selection"))
        self.actionInvert_Selection.setText(_translate("MainWindow", "Invert Selection"))
        self.actionMove_Selection_to_Top.setText(_translate("MainWindow", "Move Selection to Top"))
        self.actionFilter_Selection_by_name.setText(_translate("MainWindow", "Filter Selection by name..."))
        self.actionUnflag_Selection.setText(_translate("MainWindow", "Unflag Selection"))

