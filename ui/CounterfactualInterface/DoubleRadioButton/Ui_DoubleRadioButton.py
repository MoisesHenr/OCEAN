# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Moises\Documents\GitHub\interfaceCounterfactual\INF2102\CounterfactualInterface\DoubleRadioButton\DoubleRadioButton.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoubleRadioButton(object):
    def setupUi(self, DoubleRadioButton):
        DoubleRadioButton.setObjectName("DoubleRadioButton")
        DoubleRadioButton.resize(426, 74)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DoubleRadioButton.sizePolicy().hasHeightForWidth())
        DoubleRadioButton.setSizePolicy(sizePolicy)
        DoubleRadioButton.setMaximumSize(QtCore.QSize(500, 140))
        self.gridLayout = QtWidgets.QGridLayout(DoubleRadioButton)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFeatureName = QtWidgets.QLabel(DoubleRadioButton)
        self.labelFeatureName.setMinimumSize(QtCore.QSize(0, 25))
        self.labelFeatureName.setStyleSheet("QLabel {\n"
"    font-weight: bold;\n"
"}")
        self.labelFeatureName.setText("")
        self.labelFeatureName.setObjectName("labelFeatureName")
        self.gridLayout.addWidget(self.labelFeatureName, 0, 0, 1, 1)
        self.checkBoxActionability = QtWidgets.QCheckBox(DoubleRadioButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxActionability.sizePolicy().hasHeightForWidth())
        self.checkBoxActionability.setSizePolicy(sizePolicy)
        self.checkBoxActionability.setMinimumSize(QtCore.QSize(0, 25))
        self.checkBoxActionability.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxActionability.setChecked(True)
        self.checkBoxActionability.setObjectName("checkBoxActionability")
        self.gridLayout.addWidget(self.checkBoxActionability, 0, 1, 1, 1)
        self.radioButtonValue0 = QtWidgets.QRadioButton(DoubleRadioButton)
        self.radioButtonValue0.setMinimumSize(QtCore.QSize(0, 25))
        self.radioButtonValue0.setText("")
        self.radioButtonValue0.setObjectName("radioButtonValue0")
        self.gridLayout.addWidget(self.radioButtonValue0, 1, 0, 1, 1)
        self.radioButtonValue1 = QtWidgets.QRadioButton(DoubleRadioButton)
        self.radioButtonValue1.setMinimumSize(QtCore.QSize(0, 25))
        self.radioButtonValue1.setText("")
        self.radioButtonValue1.setObjectName("radioButtonValue1")
        self.gridLayout.addWidget(self.radioButtonValue1, 1, 1, 1, 1)

        self.retranslateUi(DoubleRadioButton)
        QtCore.QMetaObject.connectSlotsByName(DoubleRadioButton)

    def retranslateUi(self, DoubleRadioButton):
        _translate = QtCore.QCoreApplication.translate
        DoubleRadioButton.setWindowTitle(_translate("DoubleRadioButton", "Form"))
        self.checkBoxActionability.setText(_translate("DoubleRadioButton", "actionable"))
