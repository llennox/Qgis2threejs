# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis3\python\developing_plugins\Qgis2threejs\ui\exporttowebdialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportToWebDialog(object):
    def setupUi(self, ExportToWebDialog):
        ExportToWebDialog.setObjectName("ExportToWebDialog")
        ExportToWebDialog.resize(486, 232)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExportToWebDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ExportToWebDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_Template = QtWidgets.QComboBox(ExportToWebDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Template.sizePolicy().hasHeightForWidth())
        self.comboBox_Template.setSizePolicy(sizePolicy)
        self.comboBox_Template.setObjectName("comboBox_Template")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_Template)
        self.label_2 = QtWidgets.QLabel(ExportToWebDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_OutputDir = QtWidgets.QLineEdit(ExportToWebDialog)
        self.lineEdit_OutputDir.setObjectName("lineEdit_OutputDir")
        self.horizontalLayout.addWidget(self.lineEdit_OutputDir)
        self.pushButton_Browse = QtWidgets.QPushButton(ExportToWebDialog)
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.horizontalLayout.addWidget(self.pushButton_Browse)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(ExportToWebDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_Filename = QtWidgets.QLineEdit(ExportToWebDialog)
        self.lineEdit_Filename.setObjectName("lineEdit_Filename")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Filename)
        self.verticalLayout.addLayout(self.formLayout)
        self.groupBox = QtWidgets.QGroupBox(ExportToWebDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_MND = QtWidgets.QLabel(self.groupBox)
        self.label_MND.setWordWrap(True)
        self.label_MND.setObjectName("label_MND")
        self.gridLayout.addWidget(self.label_MND, 1, 0, 1, 1)
        self.lineEdit_MND = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_MND.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_MND.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_MND.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_MND.setObjectName("lineEdit_MND")
        self.gridLayout.addWidget(self.lineEdit_MND, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_AllVisible = QtWidgets.QLabel(ExportToWebDialog)
        self.label_AllVisible.setWordWrap(True)
        self.label_AllVisible.setObjectName("label_AllVisible")
        self.verticalLayout.addWidget(self.label_AllVisible)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.checkBox_openPage = QtWidgets.QCheckBox(ExportToWebDialog)
        self.checkBox_openPage.setChecked(True)
        self.checkBox_openPage.setObjectName("checkBox_openPage")
        self.verticalLayout.addWidget(self.checkBox_openPage)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_Export = QtWidgets.QPushButton(ExportToWebDialog)
        self.pushButton_Export.setDefault(True)
        self.pushButton_Export.setObjectName("pushButton_Export")
        self.horizontalLayout_3.addWidget(self.pushButton_Export)
        self.pushButton_Cancel = QtWidgets.QPushButton(ExportToWebDialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ExportToWebDialog)
        QtCore.QMetaObject.connectSlotsByName(ExportToWebDialog)
        ExportToWebDialog.setTabOrder(self.comboBox_Template, self.lineEdit_OutputDir)
        ExportToWebDialog.setTabOrder(self.lineEdit_OutputDir, self.pushButton_Browse)
        ExportToWebDialog.setTabOrder(self.pushButton_Browse, self.lineEdit_Filename)
        ExportToWebDialog.setTabOrder(self.lineEdit_Filename, self.lineEdit_MND)
        ExportToWebDialog.setTabOrder(self.lineEdit_MND, self.checkBox_openPage)
        ExportToWebDialog.setTabOrder(self.checkBox_openPage, self.pushButton_Export)
        ExportToWebDialog.setTabOrder(self.pushButton_Export, self.pushButton_Cancel)

    def retranslateUi(self, ExportToWebDialog):
        _translate = QtCore.QCoreApplication.translate
        ExportToWebDialog.setWindowTitle(_translate("ExportToWebDialog", "Export to Web"))
        self.label.setText(_translate("ExportToWebDialog", "Template"))
        self.label_2.setText(_translate("ExportToWebDialog", "Output Directory"))
        self.lineEdit_OutputDir.setToolTip(_translate("ExportToWebDialog", "Leave this empty to export files to temporary directory."))
        self.lineEdit_OutputDir.setPlaceholderText(_translate("ExportToWebDialog", "[Temporary directory]"))
        self.pushButton_Browse.setText(_translate("ExportToWebDialog", "Browse..."))
        self.label_3.setText(_translate("ExportToWebDialog", "HTML Filename"))
        self.lineEdit_Filename.setText(_translate("ExportToWebDialog", "index.html"))
        self.groupBox.setTitle(_translate("ExportToWebDialog", "Template Settings"))
        self.label_MND.setText(_translate("ExportToWebDialog", "Magnetic North Direction (clockwise from the upper direction of the map, in degrees)"))
        self.lineEdit_MND.setText(_translate("ExportToWebDialog", "0"))
        self.label_AllVisible.setText(_translate("ExportToWebDialog", "Ragardless of \"Visible on load\" layer setting, all exported layers are displayed on page load."))
        self.checkBox_openPage.setText(_translate("ExportToWebDialog", "Open exported page in web browser"))
        self.pushButton_Export.setText(_translate("ExportToWebDialog", "Export"))
        self.pushButton_Cancel.setText(_translate("ExportToWebDialog", "Cancel"))

