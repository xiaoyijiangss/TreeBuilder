# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/software_development_workspace/tools/File_tree.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_File_tree(object):
    def setupUi(self, File_tree):
        File_tree.setObjectName("File_tree")
        File_tree.resize(780, 982)
        self.gridLayout = QtWidgets.QGridLayout(File_tree)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(File_tree)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 3, 1)
        self.pushButton = QtWidgets.QPushButton(File_tree)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(File_tree)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)

        self.retranslateUi(File_tree)
        QtCore.QMetaObject.connectSlotsByName(File_tree)

    def retranslateUi(self, File_tree):
        _translate = QtCore.QCoreApplication.translate
        File_tree.setWindowTitle(_translate("File_tree", "Form"))
        self.pushButton.setText(_translate("File_tree", "Refresh"))
        self.pushButton_2.setText(_translate("File_tree", "Export"))
