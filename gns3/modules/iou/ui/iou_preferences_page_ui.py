# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/modules/iou/ui/iou_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IOUPreferencesPageWidget(object):
    def setupUi(self, IOUPreferencesPageWidget):
        IOUPreferencesPageWidget.setObjectName("IOUPreferencesPageWidget")
        IOUPreferencesPageWidget.resize(400, 300)
        self.vboxlayout = QtWidgets.QVBoxLayout(IOUPreferencesPageWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiTabWidget = QtWidgets.QTabWidget(IOUPreferencesPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.uiGeneralSettingsTabWidget = QtWidgets.QWidget()
        self.uiGeneralSettingsTabWidget.setObjectName("uiGeneralSettingsTabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiGeneralSettingsTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiLocalServerGroupBox = QtWidgets.QGroupBox(self.uiGeneralSettingsTabWidget)
        self.uiLocalServerGroupBox.setObjectName("uiLocalServerGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiLocalServerGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiIouyapPathLineEdit = QtWidgets.QLineEdit(self.uiLocalServerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiIouyapPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiIouyapPathLineEdit.setSizePolicy(sizePolicy)
        self.uiIouyapPathLineEdit.setObjectName("uiIouyapPathLineEdit")
        self.horizontalLayout_6.addWidget(self.uiIouyapPathLineEdit)
        self.uiIouyapPathToolButton = QtWidgets.QToolButton(self.uiLocalServerGroupBox)
        self.uiIouyapPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIouyapPathToolButton.setObjectName("uiIouyapPathToolButton")
        self.horizontalLayout_6.addWidget(self.uiIouyapPathToolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 0, 1, 2)
        self.uiIouyapPathLabel = QtWidgets.QLabel(self.uiLocalServerGroupBox)
        self.uiIouyapPathLabel.setObjectName("uiIouyapPathLabel")
        self.gridLayout_3.addWidget(self.uiIouyapPathLabel, 4, 0, 1, 1)
        self.uiLicensecheckBox = QtWidgets.QCheckBox(self.uiLocalServerGroupBox)
        self.uiLicensecheckBox.setChecked(True)
        self.uiLicensecheckBox.setObjectName("uiLicensecheckBox")
        self.gridLayout_3.addWidget(self.uiLicensecheckBox, 3, 0, 1, 1)
        self.uiUseLocalServercheckBox = QtWidgets.QCheckBox(self.uiLocalServerGroupBox)
        self.uiUseLocalServercheckBox.setChecked(True)
        self.uiUseLocalServercheckBox.setObjectName("uiUseLocalServercheckBox")
        self.gridLayout_3.addWidget(self.uiUseLocalServercheckBox, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiLocalServerGroupBox)
        self.uiAnyServerGroupBox = QtWidgets.QGroupBox(self.uiGeneralSettingsTabWidget)
        self.uiAnyServerGroupBox.setObjectName("uiAnyServerGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiAnyServerGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiIOURCPathLabel = QtWidgets.QLabel(self.uiAnyServerGroupBox)
        self.uiIOURCPathLabel.setObjectName("uiIOURCPathLabel")
        self.gridLayout_4.addWidget(self.uiIOURCPathLabel, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiIOURCPathLineEdit = QtWidgets.QLineEdit(self.uiAnyServerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiIOURCPathLineEdit.sizePolicy().hasHeightForWidth())
        self.uiIOURCPathLineEdit.setSizePolicy(sizePolicy)
        self.uiIOURCPathLineEdit.setObjectName("uiIOURCPathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiIOURCPathLineEdit)
        self.uiIOURCPathToolButton = QtWidgets.QToolButton(self.uiAnyServerGroupBox)
        self.uiIOURCPathToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOURCPathToolButton.setObjectName("uiIOURCPathToolButton")
        self.horizontalLayout_5.addWidget(self.uiIOURCPathToolButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiAnyServerGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.uiTabWidget.addTab(self.uiGeneralSettingsTabWidget, "")
        self.vboxlayout.addWidget(self.uiTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(164, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(IOUPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.vboxlayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(IOUPreferencesPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IOUPreferencesPageWidget)

    def retranslateUi(self, IOUPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        IOUPreferencesPageWidget.setWindowTitle(_translate("IOUPreferencesPageWidget", "IOS on UNIX"))
        self.uiLocalServerGroupBox.setTitle(_translate("IOUPreferencesPageWidget", "Local server"))
        self.uiIouyapPathToolButton.setText(_translate("IOUPreferencesPageWidget", "&Browse..."))
        self.uiIouyapPathLabel.setText(_translate("IOUPreferencesPageWidget", "Path to iouyap:"))
        self.uiLicensecheckBox.setText(_translate("IOUPreferencesPageWidget", "Check for a valid IOU license key"))
        self.uiUseLocalServercheckBox.setText(_translate("IOUPreferencesPageWidget", "Use the local server (Linux only)"))
        self.uiAnyServerGroupBox.setTitle(_translate("IOUPreferencesPageWidget", "Any server"))
        self.uiIOURCPathLabel.setText(_translate("IOUPreferencesPageWidget", "Path to IOURC (license, pushed to servers):"))
        self.uiIOURCPathToolButton.setText(_translate("IOUPreferencesPageWidget", "&Browse..."))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.uiGeneralSettingsTabWidget), _translate("IOUPreferencesPageWidget", "General settings"))
        self.uiRestoreDefaultsPushButton.setText(_translate("IOUPreferencesPageWidget", "Restore defaults"))

