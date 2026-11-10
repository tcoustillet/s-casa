# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scasaMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 776)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.browseButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        self.tableView.setMinimumSize(QSize(180, 0))

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        font = QFont()
        font.setBold(False)
        self.fileNameLabel.setFont(font)

        self.horizontalLayout_5.addWidget(self.fileNameLabel)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(-1)
        self.gridLayout_2.setContentsMargins(-1, 40, -1, 15)
        self.frameCountValue = QLabel(self.centralwidget)
        self.frameCountValue.setObjectName(u"frameCountValue")

        self.gridLayout_2.addWidget(self.frameCountValue, 0, 1, 1, 1)

        self.frameIntervalLabel = QLabel(self.centralwidget)
        self.frameIntervalLabel.setObjectName(u"frameIntervalLabel")
        font1 = QFont()
        font1.setUnderline(True)
        self.frameIntervalLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.frameIntervalLabel, 1, 0, 1, 1)

        self.frameCountLabel = QLabel(self.centralwidget)
        self.frameCountLabel.setObjectName(u"frameCountLabel")
        self.frameCountLabel.setFont(font1)

        self.gridLayout_2.addWidget(self.frameCountLabel, 0, 0, 1, 1)

        self.frameIntervalLineEdit = QLineEdit(self.centralwidget)
        self.frameIntervalLineEdit.setObjectName(u"frameIntervalLineEdit")
        sizePolicy.setHeightForWidth(self.frameIntervalLineEdit.sizePolicy().hasHeightForWidth())
        self.frameIntervalLineEdit.setSizePolicy(sizePolicy)
        self.frameIntervalLineEdit.setMaximumSize(QSize(75, 16777215))
        self.frameIntervalLineEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_2.addWidget(self.frameIntervalLineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 70, 20, 70)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setUnderline(True)
        self.label.setFont(font2)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.meanSignalLabel = QLabel(self.centralwidget)
        self.meanSignalLabel.setObjectName(u"meanSignalLabel")
        self.meanSignalLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.meanSignalLabel)

        self.stdSignalLabel = QLabel(self.centralwidget)
        self.stdSignalLabel.setObjectName(u"stdSignalLabel")
        self.stdSignalLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.stdSignalLabel)

        self.durationSignalLabel = QLabel(self.centralwidget)
        self.durationSignalLabel.setObjectName(u"durationSignalLabel")
        self.durationSignalLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.durationSignalLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, -1, 100, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.prominenceDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.prominenceDoubleSpinBox.setObjectName(u"prominenceDoubleSpinBox")
        self.prominenceDoubleSpinBox.setKeyboardTracking(False)
        self.prominenceDoubleSpinBox.setDecimals(3)
        self.prominenceDoubleSpinBox.setMaximum(1.500000000000000)
        self.prominenceDoubleSpinBox.setSingleStep(0.001000000000000)
        self.prominenceDoubleSpinBox.setValue(0.077000000000000)

        self.gridLayout.addWidget(self.prominenceDoubleSpinBox, 4, 1, 1, 1)

        self.widthDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.widthDoubleSpinBox.setObjectName(u"widthDoubleSpinBox")
        self.widthDoubleSpinBox.setKeyboardTracking(False)
        self.widthDoubleSpinBox.setDecimals(3)
        self.widthDoubleSpinBox.setMaximum(4.000000000000000)
        self.widthDoubleSpinBox.setSingleStep(0.001000000000000)

        self.gridLayout.addWidget(self.widthDoubleSpinBox, 5, 1, 1, 1)

        self.distanceSlider = QSlider(self.centralwidget)
        self.distanceSlider.setObjectName(u"distanceSlider")
        self.distanceSlider.setMinimum(1)
        self.distanceSlider.setMaximum(600)
        self.distanceSlider.setValue(1)
        self.distanceSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.distanceSlider, 3, 2, 1, 1)

        self.heightValue = QLabel(self.centralwidget)
        self.heightValue.setObjectName(u"heightValue")

        self.gridLayout.addWidget(self.heightValue, 1, 3, 1, 1)

        self.heightDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.heightDoubleSpinBox.setObjectName(u"heightDoubleSpinBox")
        self.heightDoubleSpinBox.setKeyboardTracking(False)
        self.heightDoubleSpinBox.setDecimals(3)
        self.heightDoubleSpinBox.setMinimum(0.000000000000000)
        self.heightDoubleSpinBox.setMaximum(1.500000000000000)
        self.heightDoubleSpinBox.setSingleStep(0.001000000000000)
        self.heightDoubleSpinBox.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.heightDoubleSpinBox, 1, 1, 1, 1)

        self.thresholdSlider = QSlider(self.centralwidget)
        self.thresholdSlider.setObjectName(u"thresholdSlider")
        self.thresholdSlider.setMaximum(1500)
        self.thresholdSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.thresholdSlider, 2, 2, 1, 1)

        self.widthValue = QLabel(self.centralwidget)
        self.widthValue.setObjectName(u"widthValue")

        self.gridLayout.addWidget(self.widthValue, 5, 3, 1, 1)

        self.distanceLabel = QLabel(self.centralwidget)
        self.distanceLabel.setObjectName(u"distanceLabel")
        font3 = QFont()
        font3.setBold(True)
        self.distanceLabel.setFont(font3)
        self.distanceLabel.setStyleSheet(u"color: \"#d62728\";")

        self.gridLayout.addWidget(self.distanceLabel, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 4, 1, 1)

        self.thresholdValue = QLabel(self.centralwidget)
        self.thresholdValue.setObjectName(u"thresholdValue")

        self.gridLayout.addWidget(self.thresholdValue, 2, 3, 1, 1)

        self.heightSlider = QSlider(self.centralwidget)
        self.heightSlider.setObjectName(u"heightSlider")
        self.heightSlider.setStyleSheet(u"")
        self.heightSlider.setMaximum(1500)
        self.heightSlider.setSingleStep(1)
        self.heightSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.heightSlider, 1, 2, 1, 1)

        self.heightLabel = QLabel(self.centralwidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setFont(font3)
        self.heightLabel.setStyleSheet(u"color: \"#1f77b4\";")

        self.gridLayout.addWidget(self.heightLabel, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.distanceSpinBox = QSpinBox(self.centralwidget)
        self.distanceSpinBox.setObjectName(u"distanceSpinBox")
        self.distanceSpinBox.setKeyboardTracking(False)
        self.distanceSpinBox.setMinimum(1)
        self.distanceSpinBox.setMaximum(600)
        self.distanceSpinBox.setValue(1)

        self.gridLayout.addWidget(self.distanceSpinBox, 3, 1, 1, 1)

        self.thresholdLabel = QLabel(self.centralwidget)
        self.thresholdLabel.setObjectName(u"thresholdLabel")
        self.thresholdLabel.setFont(font3)
        self.thresholdLabel.setStyleSheet(u"color: \"#2ca02c\";")

        self.gridLayout.addWidget(self.thresholdLabel, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.prominenceValue = QLabel(self.centralwidget)
        self.prominenceValue.setObjectName(u"prominenceValue")

        self.gridLayout.addWidget(self.prominenceValue, 4, 3, 1, 1)

        self.distanceValue = QLabel(self.centralwidget)
        self.distanceValue.setObjectName(u"distanceValue")

        self.gridLayout.addWidget(self.distanceValue, 3, 3, 1, 1)

        self.setHeightPushButton = QPushButton(self.centralwidget)
        self.setHeightPushButton.setObjectName(u"setHeightPushButton")
        self.setHeightPushButton.setFont(font)

        self.gridLayout.addWidget(self.setHeightPushButton, 0, 2, 1, 1)

        self.prominenceLabel = QLabel(self.centralwidget)
        self.prominenceLabel.setObjectName(u"prominenceLabel")
        self.prominenceLabel.setFont(font3)
        self.prominenceLabel.setStyleSheet(u"color: \"#ff7f0e\"")

        self.gridLayout.addWidget(self.prominenceLabel, 4, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.prominenceSlider = QSlider(self.centralwidget)
        self.prominenceSlider.setObjectName(u"prominenceSlider")
        self.prominenceSlider.setMaximum(1500)
        self.prominenceSlider.setValue(77)
        self.prominenceSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.prominenceSlider, 4, 2, 1, 1)

        self.thresholdDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.thresholdDoubleSpinBox.setObjectName(u"thresholdDoubleSpinBox")
        self.thresholdDoubleSpinBox.setKeyboardTracking(False)
        self.thresholdDoubleSpinBox.setDecimals(3)
        self.thresholdDoubleSpinBox.setMaximum(1.500000000000000)
        self.thresholdDoubleSpinBox.setSingleStep(0.001000000000000)

        self.gridLayout.addWidget(self.thresholdDoubleSpinBox, 2, 1, 1, 1)

        self.widthSlider = QSlider(self.centralwidget)
        self.widthSlider.setObjectName(u"widthSlider")
        self.widthSlider.setMaximum(4000)
        self.widthSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.widthSlider, 5, 2, 1, 1)

        self.widthLabel = QLabel(self.centralwidget)
        self.widthLabel.setObjectName(u"widthLabel")
        self.widthLabel.setFont(font3)
        self.widthLabel.setStyleSheet(u"color: \"#9467bd\"")

        self.gridLayout.addWidget(self.widthLabel, 5, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plotButton = QPushButton(self.centralwidget)
        self.plotButton.setObjectName(u"plotButton")
        sizePolicy.setHeightForWidth(self.plotButton.sizePolicy().hasHeightForWidth())
        self.plotButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.plotButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.detrendCheckBox = QCheckBox(self.centralwidget)
        self.detrendCheckBox.setObjectName(u"detrendCheckBox")

        self.horizontalLayout_2.addWidget(self.detrendCheckBox)

        self.detrendComboBox = QComboBox(self.centralwidget)
        self.detrendComboBox.addItem("")
        self.detrendComboBox.addItem("")
        self.detrendComboBox.setObjectName(u"detrendComboBox")

        self.horizontalLayout_2.addWidget(self.detrendComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.prominenceCheckBox = QCheckBox(self.centralwidget)
        self.prominenceCheckBox.setObjectName(u"prominenceCheckBox")

        self.verticalLayout_2.addWidget(self.prominenceCheckBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.resultsLabel = QLabel(self.centralwidget)
        self.resultsLabel.setObjectName(u"resultsLabel")
        font4 = QFont()
        font4.setBold(True)
        font4.setUnderline(True)
        self.resultsLabel.setFont(font4)

        self.verticalLayout_2.addWidget(self.resultsLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.amplitudeLabel = QLabel(self.centralwidget)
        self.amplitudeLabel.setObjectName(u"amplitudeLabel")

        self.verticalLayout_2.addWidget(self.amplitudeLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.frequenceLabel = QLabel(self.centralwidget)
        self.frequenceLabel.setObjectName(u"frequenceLabel")

        self.verticalLayout_2.addWidget(self.frequenceLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.plotprocessedWidget = PlotWidget(self.centralwidget)
        self.plotprocessedWidget.setObjectName(u"plotprocessedWidget")
        sizePolicy1.setHeightForWidth(self.plotprocessedWidget.sizePolicy().hasHeightForWidth())
        self.plotprocessedWidget.setSizePolicy(sizePolicy1)
        self.plotprocessedWidget.setMinimumSize(QSize(0, 222))

        self.verticalLayout_4.addWidget(self.plotprocessedWidget)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1182, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"S-CaSa: A Standardized method for Calcium Signal Analysis ", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Loaded file: </span>????</p></body></html>", None))
        self.frameCountValue.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.frameIntervalLabel.setText(QCoreApplication.translate("MainWindow", u"Frame interval (ms):", None))
        self.frameCountLabel.setText(QCoreApplication.translate("MainWindow", u"Number of detected frames:", None))
        self.frameIntervalLineEdit.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Signal features", None))
        self.meanSignalLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Signal mean =</span> ????</p></body></html>", None))
        self.stdSignalLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Signal standard deviation =</span> ????</p></body></html>", None))
        self.durationSignalLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Signal total duration =</span> ????</p></body></html>", None))
        self.heightValue.setText("")
        self.widthValue.setText("")
        self.distanceLabel.setText(QCoreApplication.translate("MainWindow", u"distance", None))
        self.thresholdValue.setText("")
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"height", None))
        self.thresholdLabel.setText(QCoreApplication.translate("MainWindow", u"threshold", None))
        self.prominenceValue.setText("")
        self.distanceValue.setText("")
        self.setHeightPushButton.setText(QCoreApplication.translate("MainWindow", u"Set height = mean + standard deviation \u2935\ufe0e", None))
        self.prominenceLabel.setText(QCoreApplication.translate("MainWindow", u"prominence", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"width", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot figure", None))
        self.detrendCheckBox.setText(QCoreApplication.translate("MainWindow", u"Detrend signal", None))
        self.detrendComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"linear", None))
        self.detrendComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"constant", None))

        self.prominenceCheckBox.setText(QCoreApplication.translate("MainWindow", u"Show prominences", None))
        self.resultsLabel.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.amplitudeLabel.setText(QCoreApplication.translate("MainWindow", u"Mean amplitude =", None))
        self.frequenceLabel.setText(QCoreApplication.translate("MainWindow", u"Frequency = ", None))
    # retranslateUi

