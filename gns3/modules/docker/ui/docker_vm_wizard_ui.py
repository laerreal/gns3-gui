# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'docker_vm_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets

class Ui_DockerVMWizard(object):
    def setupUi(self, DockerVMWizard):
        DockerVMWizard.setObjectName("DockerVMWizard")
        DockerVMWizard.resize(514, 367)
        DockerVMWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiCloudRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiCloudRadioButton.setObjectName("uiCloudRadioButton")
        self.horizontalLayout.addWidget(self.uiCloudRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_8.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_8.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        DockerVMWizard.addPage(self.uiServerWizardPage)
        self.uiDockerWizardPage = QtWidgets.QWizardPage()
        self.uiDockerWizardPage.setObjectName("uiDockerWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiDockerWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiImageListLabel = QtWidgets.QLabel(self.uiDockerWizardPage)
        self.uiImageListLabel.setObjectName("uiImageListLabel")
        self.gridLayout.addWidget(self.uiImageListLabel, 0, 0, 1, 1)
        self.uiImageListComboBox = QtWidgets.QComboBox(self.uiDockerWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiImageListComboBox.sizePolicy().hasHeightForWidth())
        self.uiImageListComboBox.setSizePolicy(sizePolicy)
        self.uiImageListComboBox.setObjectName("uiImageListComboBox")
        self.gridLayout.addWidget(self.uiImageListComboBox, 0, 1, 1, 1)
        DockerVMWizard.addPage(self.uiDockerWizardPage)

        self.retranslateUi(DockerVMWizard)
        QtCore.QMetaObject.connectSlotsByName(DockerVMWizard)

    def retranslateUi(self, DockerVMWizard):
        _translate = gns3.qt.translate
        DockerVMWizard.setWindowTitle(_translate("DockerVMWizard", "New Docker VM template"))
        self.uiServerWizardPage.setTitle(_translate("DockerVMWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose a server type to run your new Docker VM."))
        self.uiServerTypeGroupBox.setTitle(_translate("DockerVMWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("DockerVMWizard", "Remote"))
        self.uiCloudRadioButton.setText(_translate("DockerVMWizard", "Cloud"))
        self.uiLocalRadioButton.setText(_translate("DockerVMWizard", "Local"))
        self.uiRemoteServersGroupBox.setTitle(_translate("DockerVMWizard", "Remote servers"))
        self.uiRemoteServersLabel.setText(_translate("DockerVMWizard", "Run on server:"))
        self.uiDockerWizardPage.setTitle(_translate("DockerVMWizard", "Docker Virtual Machine"))
        self.uiDockerWizardPage.setSubTitle(_translate("DockerVMWizard", "Please choose a Docker virtual machine from the list."))
        self.uiImageListLabel.setText(_translate("DockerVMWizard", "Image list:"))

