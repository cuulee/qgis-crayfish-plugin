# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crayfish_viewer_dock_widget.ui'
#
# Created: Mon Mar 23 15:33:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(349, 565)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.btnLockCurrent = QtGui.QToolButton(self.dockWidgetContents)
        self.btnLockCurrent.setAutoRaise(True)
        self.btnLockCurrent.setObjectName(_fromUtf8("btnLockCurrent"))
        self.horizontalLayout_6.addWidget(self.btnLockCurrent)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.treeDataSets = DataSetView(self.dockWidgetContents)
        self.treeDataSets.setMinimumSize(QtCore.QSize(0, 55))
        self.treeDataSets.setObjectName(_fromUtf8("treeDataSets"))
        self.verticalLayout_2.addWidget(self.treeDataSets)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sliderTime = QtGui.QSlider(self.dockWidgetContents)
        self.sliderTime.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTime.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderTime.setTickInterval(1)
        self.sliderTime.setObjectName(_fromUtf8("sliderTime"))
        self.gridLayout_2.addWidget(self.sliderTime, 0, 0, 1, 5)
        self.cboTime = QtGui.QComboBox(self.dockWidgetContents)
        self.cboTime.setEditable(True)
        self.cboTime.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.cboTime.setObjectName(_fromUtf8("cboTime"))
        self.gridLayout_2.addWidget(self.cboTime, 1, 0, 1, 1)
        self.btnFirst = QtGui.QToolButton(self.dockWidgetContents)
        self.btnFirst.setAutoRaise(True)
        self.btnFirst.setObjectName(_fromUtf8("btnFirst"))
        self.gridLayout_2.addWidget(self.btnFirst, 1, 1, 1, 1)
        self.btnPrev = QtGui.QToolButton(self.dockWidgetContents)
        self.btnPrev.setAutoRaise(True)
        self.btnPrev.setObjectName(_fromUtf8("btnPrev"))
        self.gridLayout_2.addWidget(self.btnPrev, 1, 2, 1, 1)
        self.btnNext = QtGui.QToolButton(self.dockWidgetContents)
        self.btnNext.setAutoRaise(True)
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.gridLayout_2.addWidget(self.btnNext, 1, 3, 1, 1)
        self.btnLast = QtGui.QToolButton(self.dockWidgetContents)
        self.btnLast.setAutoRaise(True)
        self.btnLast.setObjectName(_fromUtf8("btnLast"))
        self.gridLayout_2.addWidget(self.btnLast, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.contoursGroupBox = QgsCollapsibleGroupBox(self.dockWidgetContents)
        self.contoursGroupBox.setCheckable(True)
        self.contoursGroupBox.setObjectName(_fromUtf8("contoursGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.contoursGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.contoursGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.contourTransparencySlider = QtGui.QSlider(self.contoursGroupBox)
        self.contourTransparencySlider.setMaximum(255)
        self.contourTransparencySlider.setPageStep(20)
        self.contourTransparencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.contourTransparencySlider.setObjectName(_fromUtf8("contourTransparencySlider"))
        self.horizontalLayout_2.addWidget(self.contourTransparencySlider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radContourBasic = QtGui.QRadioButton(self.contoursGroupBox)
        self.radContourBasic.setChecked(True)
        self.radContourBasic.setObjectName(_fromUtf8("radContourBasic"))
        self.horizontalLayout_3.addWidget(self.radContourBasic)
        self.cboContourBasic = QgsColorRampComboBox(self.contoursGroupBox)
        self.cboContourBasic.setObjectName(_fromUtf8("cboContourBasic"))
        self.horizontalLayout_3.addWidget(self.cboContourBasic)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.contourCustomRangeCheckBox = QtGui.QCheckBox(self.contoursGroupBox)
        self.contourCustomRangeCheckBox.setText(_fromUtf8(""))
        self.contourCustomRangeCheckBox.setObjectName(_fromUtf8("contourCustomRangeCheckBox"))
        self.horizontalLayout.addWidget(self.contourCustomRangeCheckBox)
        self.contourMinLabel = QtGui.QLabel(self.contoursGroupBox)
        self.contourMinLabel.setObjectName(_fromUtf8("contourMinLabel"))
        self.horizontalLayout.addWidget(self.contourMinLabel)
        self.contourMinLineEdit = QtGui.QLineEdit(self.contoursGroupBox)
        self.contourMinLineEdit.setEnabled(False)
        self.contourMinLineEdit.setObjectName(_fromUtf8("contourMinLineEdit"))
        self.horizontalLayout.addWidget(self.contourMinLineEdit)
        self.contourMaxLabel = QtGui.QLabel(self.contoursGroupBox)
        self.contourMaxLabel.setObjectName(_fromUtf8("contourMaxLabel"))
        self.horizontalLayout.addWidget(self.contourMaxLabel)
        self.contourMaxLineEdit = QtGui.QLineEdit(self.contoursGroupBox)
        self.contourMaxLineEdit.setEnabled(False)
        self.contourMaxLineEdit.setObjectName(_fromUtf8("contourMaxLineEdit"))
        self.horizontalLayout.addWidget(self.contourMaxLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radContourAdvanced = QtGui.QRadioButton(self.contoursGroupBox)
        self.radContourAdvanced.setObjectName(_fromUtf8("radContourAdvanced"))
        self.horizontalLayout_4.addWidget(self.radContourAdvanced)
        self.lblAdvancedPreview = QtGui.QLabel(self.contoursGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAdvancedPreview.sizePolicy().hasHeightForWidth())
        self.lblAdvancedPreview.setSizePolicy(sizePolicy)
        self.lblAdvancedPreview.setMinimumSize(QtCore.QSize(100, 0))
        self.lblAdvancedPreview.setText(_fromUtf8(""))
        self.lblAdvancedPreview.setObjectName(_fromUtf8("lblAdvancedPreview"))
        self.horizontalLayout_4.addWidget(self.lblAdvancedPreview)
        self.btnAdvanced = QtGui.QToolButton(self.contoursGroupBox)
        self.btnAdvanced.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.btnAdvanced.setAutoRaise(True)
        self.btnAdvanced.setArrowType(QtCore.Qt.NoArrow)
        self.btnAdvanced.setObjectName(_fromUtf8("btnAdvanced"))
        self.horizontalLayout_4.addWidget(self.btnAdvanced)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.contoursGroupBox)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, 7, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.displayMeshCheckBox = QtGui.QCheckBox(self.dockWidgetContents)
        self.displayMeshCheckBox.setObjectName(_fromUtf8("displayMeshCheckBox"))
        self.gridLayout.addWidget(self.displayMeshCheckBox, 1, 0, 1, 1)
        self.btnMeshColor = QgsColorButton(self.dockWidgetContents)
        self.btnMeshColor.setObjectName(_fromUtf8("btnMeshColor"))
        self.gridLayout.addWidget(self.btnMeshColor, 1, 2, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btnVectorOptions = QtGui.QToolButton(self.dockWidgetContents)
        self.btnVectorOptions.setAutoRaise(True)
        self.btnVectorOptions.setObjectName(_fromUtf8("btnVectorOptions"))
        self.horizontalLayout_5.addWidget(self.btnVectorOptions)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.displayVectorsCheckBox = QtGui.QCheckBox(self.dockWidgetContents)
        self.displayVectorsCheckBox.setObjectName(_fromUtf8("displayVectorsCheckBox"))
        self.gridLayout.addWidget(self.displayVectorsCheckBox, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.valueLabel = QtGui.QLabel(self.dockWidgetContents)
        self.valueLabel.setObjectName(_fromUtf8("valueLabel"))
        self.verticalLayout_2.addWidget(self.valueLabel)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QObject.connect(self.displayVectorsCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), DockWidget.displayVectorsButtonToggled)
        QtCore.QObject.connect(self.displayMeshCheckBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), DockWidget.displayMeshButtonToggled)
        QtCore.QObject.connect(self.btnVectorOptions, QtCore.SIGNAL(_fromUtf8("clicked()")), DockWidget.displayVectorPropsDialog)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)
        DockWidget.setTabOrder(self.treeDataSets, self.sliderTime)
        DockWidget.setTabOrder(self.sliderTime, self.cboTime)
        DockWidget.setTabOrder(self.cboTime, self.btnFirst)
        DockWidget.setTabOrder(self.btnFirst, self.btnPrev)
        DockWidget.setTabOrder(self.btnPrev, self.btnNext)
        DockWidget.setTabOrder(self.btnNext, self.btnLast)
        DockWidget.setTabOrder(self.btnLast, self.contoursGroupBox)
        DockWidget.setTabOrder(self.contoursGroupBox, self.contourTransparencySlider)
        DockWidget.setTabOrder(self.contourTransparencySlider, self.radContourBasic)
        DockWidget.setTabOrder(self.radContourBasic, self.cboContourBasic)
        DockWidget.setTabOrder(self.cboContourBasic, self.contourCustomRangeCheckBox)
        DockWidget.setTabOrder(self.contourCustomRangeCheckBox, self.contourMinLineEdit)
        DockWidget.setTabOrder(self.contourMinLineEdit, self.contourMaxLineEdit)
        DockWidget.setTabOrder(self.contourMaxLineEdit, self.radContourAdvanced)
        DockWidget.setTabOrder(self.radContourAdvanced, self.btnAdvanced)
        DockWidget.setTabOrder(self.btnAdvanced, self.displayVectorsCheckBox)
        DockWidget.setTabOrder(self.displayVectorsCheckBox, self.btnVectorOptions)
        DockWidget.setTabOrder(self.btnVectorOptions, self.displayMeshCheckBox)
        DockWidget.setTabOrder(self.displayMeshCheckBox, self.btnMeshColor)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Crayfish Viewer", None))
        self.label.setText(_translate("DockWidget", "Quantity", None))
        self.btnLockCurrent.setToolTip(_translate("DockWidget", "Lock rendering to the current dataset\n"
"\n"
"When locked, Crayfish will render contours (and vectors)\n"
"from the selected dataset.\n"
"\n"
"When unlocked, it is possible to combine rendering\n"
"of contours and vectors from different datasets\n"
"by clicking the icons next to dataset names.", None))
        self.label_2.setText(_translate("DockWidget", "Output Time", None))
        self.btnFirst.setText(_translate("DockWidget", "|<", None))
        self.btnPrev.setText(_translate("DockWidget", "<", None))
        self.btnNext.setText(_translate("DockWidget", ">", None))
        self.btnLast.setText(_translate("DockWidget", ">|", None))
        self.contoursGroupBox.setTitle(_translate("DockWidget", "Display Contours", None))
        self.label_3.setText(_translate("DockWidget", "Transparency", None))
        self.radContourBasic.setText(_translate("DockWidget", "Basic", None))
        self.contourMinLabel.setText(_translate("DockWidget", "Min", None))
        self.contourMaxLabel.setText(_translate("DockWidget", "Max", None))
        self.radContourAdvanced.setText(_translate("DockWidget", "Advanced", None))
        self.btnAdvanced.setToolTip(_translate("DockWidget", "Advanced Contour Options", None))
        self.btnAdvanced.setText(_translate("DockWidget", "...", None))
        self.displayMeshCheckBox.setText(_translate("DockWidget", "Display Mesh", None))
        self.btnVectorOptions.setToolTip(_translate("DockWidget", "Vector Options", None))
        self.btnVectorOptions.setText(_translate("DockWidget", "...", None))
        self.displayVectorsCheckBox.setText(_translate("DockWidget", "Display Vectors", None))
        self.valueLabel.setText(_translate("DockWidget", "(0.000) 0.000", None))

from crayfish_viewer_dataset_view import DataSetView
from qgis.gui import QgsColorButton, QgsColorRampComboBox
from crayfish_gui_utils import QgsCollapsibleGroupBox
