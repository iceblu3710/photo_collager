# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 652)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tabImages = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabImages.sizePolicy().hasHeightForWidth())
        self.tabImages.setSizePolicy(sizePolicy)
        self.tabImages.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabImages.setObjectName("tabImages")
        self.tabImage1 = QtWidgets.QWidget()
        self.tabImage1.setObjectName("tabImage1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabImage1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphic_tabImage1 = QtWidgets.QLabel(self.tabImage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphic_tabImage1.sizePolicy().hasHeightForWidth())
        self.graphic_tabImage1.setSizePolicy(sizePolicy)
        self.graphic_tabImage1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_tabImage1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphic_tabImage1.setText("")
        self.graphic_tabImage1.setScaledContents(False)
        self.graphic_tabImage1.setAlignment(QtCore.Qt.AlignCenter)
        self.graphic_tabImage1.setObjectName("graphic_tabImage1")
        self.verticalLayout.addWidget(self.graphic_tabImage1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.push_tabImage1_open = QtWidgets.QPushButton(self.tabImage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tabImage1_open.sizePolicy().hasHeightForWidth())
        self.push_tabImage1_open.setSizePolicy(sizePolicy)
        self.push_tabImage1_open.setAutoDefault(False)
        self.push_tabImage1_open.setDefault(False)
        self.push_tabImage1_open.setObjectName("push_tabImage1_open")
        self.horizontalLayout.addWidget(self.push_tabImage1_open)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.push_tabImage1_rotate = QtWidgets.QPushButton(self.tabImage1)
        self.push_tabImage1_rotate.setObjectName("push_tabImage1_rotate")
        self.horizontalLayout.addWidget(self.push_tabImage1_rotate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.push_tabImage1_save = QtWidgets.QPushButton(self.tabImage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tabImage1_save.sizePolicy().hasHeightForWidth())
        self.push_tabImage1_save.setSizePolicy(sizePolicy)
        self.push_tabImage1_save.setObjectName("push_tabImage1_save")
        self.horizontalLayout.addWidget(self.push_tabImage1_save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabImages.addTab(self.tabImage1, "")
        self.tabImage2 = QtWidgets.QWidget()
        self.tabImage2.setObjectName("tabImage2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabImage2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphic_tabImage2 = QtWidgets.QLabel(self.tabImage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphic_tabImage2.sizePolicy().hasHeightForWidth())
        self.graphic_tabImage2.setSizePolicy(sizePolicy)
        self.graphic_tabImage2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_tabImage2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphic_tabImage2.setText("")
        self.graphic_tabImage2.setAlignment(QtCore.Qt.AlignCenter)
        self.graphic_tabImage2.setObjectName("graphic_tabImage2")
        self.verticalLayout_2.addWidget(self.graphic_tabImage2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_tabImage2_open = QtWidgets.QPushButton(self.tabImage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tabImage2_open.sizePolicy().hasHeightForWidth())
        self.push_tabImage2_open.setSizePolicy(sizePolicy)
        self.push_tabImage2_open.setObjectName("push_tabImage2_open")
        self.horizontalLayout_2.addWidget(self.push_tabImage2_open)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.push_tabImage2_rotate = QtWidgets.QPushButton(self.tabImage2)
        self.push_tabImage2_rotate.setObjectName("push_tabImage2_rotate")
        self.horizontalLayout_2.addWidget(self.push_tabImage2_rotate)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.push_tabImage2_save = QtWidgets.QPushButton(self.tabImage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_tabImage2_save.sizePolicy().hasHeightForWidth())
        self.push_tabImage2_save.setSizePolicy(sizePolicy)
        self.push_tabImage2_save.setObjectName("push_tabImage2_save")
        self.horizontalLayout_2.addWidget(self.push_tabImage2_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabImages.addTab(self.tabImage2, "")
        self.tabCollage = QtWidgets.QWidget()
        self.tabCollage.setObjectName("tabCollage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabCollage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tabCollage)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboPrintSize = QtWidgets.QComboBox(self.tabCollage)
        self.comboPrintSize.setObjectName("comboPrintSize")
        self.comboPrintSize.addItem("")
        self.horizontalLayout_3.addWidget(self.comboPrintSize)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.push_collage_generate = QtWidgets.QPushButton(self.tabCollage)
        self.push_collage_generate.setObjectName("push_collage_generate")
        self.horizontalLayout_3.addWidget(self.push_collage_generate)
        self.push_collage_save = QtWidgets.QPushButton(self.tabCollage)
        self.push_collage_save.setObjectName("push_collage_save")
        self.horizontalLayout_3.addWidget(self.push_collage_save)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.graphic_collage = QtWidgets.QLabel(self.tabCollage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphic_collage.sizePolicy().hasHeightForWidth())
        self.graphic_collage.setSizePolicy(sizePolicy)
        self.graphic_collage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_collage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.graphic_collage.setLineWidth(1)
        self.graphic_collage.setText("")
        self.graphic_collage.setScaledContents(False)
        self.graphic_collage.setAlignment(QtCore.Qt.AlignCenter)
        self.graphic_collage.setObjectName("graphic_collage")
        self.gridLayout_6.addWidget(self.graphic_collage, 0, 0, 1, 1)
        self.tabImages.addTab(self.tabCollage, "")
        self.gridLayout_8.addWidget(self.tabImages, 0, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabImages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_tabImage1_open.setText(_translate("MainWindow", "Open Image"))
        self.push_tabImage1_rotate.setText(_translate("MainWindow", "Rotate"))
        self.push_tabImage1_save.setText(_translate("MainWindow", "Save Resized"))
        self.tabImages.setTabText(self.tabImages.indexOf(self.tabImage1), _translate("MainWindow", "Image 1"))
        self.push_tabImage2_open.setText(_translate("MainWindow", "Open Image"))
        self.push_tabImage2_rotate.setText(_translate("MainWindow", "Rotate"))
        self.push_tabImage2_save.setText(_translate("MainWindow", "Save Resized"))
        self.tabImages.setTabText(self.tabImages.indexOf(self.tabImage2), _translate("MainWindow", "Image 2"))
        self.label.setText(_translate("MainWindow", "Print Size:"))
        self.comboPrintSize.setItemText(0, _translate("MainWindow", "4 x 6"))
        self.push_collage_generate.setText(_translate("MainWindow", "Generate"))
        self.push_collage_save.setText(_translate("MainWindow", "Save self.collage"))
        self.tabImages.setTabText(self.tabImages.indexOf(self.tabCollage), _translate("MainWindow", "self.collage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


