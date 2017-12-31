import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow


class Photo_Collager(Ui_MainWindow):
    def __init__(self):
        self.img1 = QtGui.QImage()
        self.img2 = QtGui.QImage()
        self.collage = None

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def run(self):
        # application code here
        self.ui.push_tabImage1_open.clicked.connect(self.openImage)
        self.ui.push_tabImage1_rotate.clicked.connect(self.rotateImage)
        self.ui.push_tabImage1_save.clicked.connect(self.saveImage)
        self.ui.push_tabImage2_open.clicked.connect(self.openImage)
        self.ui.push_tabImage2_rotate.clicked.connect(self.rotateImage)
        self.ui.push_tabImage2_save.clicked.connect(self.saveImage)
        self.ui.push_collage_generate.clicked.connect(self.updateCollage)
        self.ui.push_collage_save.clicked.connect(self.saveImage)

    def updateCollage(self):
        img1Height = self.img1.height()
        img2Height = self.img2.height()
        # calculate which image is the smallest in height and use
        # that to set the canvas. width = minHeight / 4 * 6
        # 300dpi 4in x 6in image = 1200x1800
        if (img1Height < img2Height):
            height = img1Height
        else:
            height = img2Height

        # set self.collage print size
        size = self.ui.comboPrintSize.currentText()
        size = size.split()
        size.remove('x')

        width = height / int(size[0]) * int(size[1])
        self.collage = QtGui.QPixmap(width, height)
        left_canvas = QtCore.QRect(0, 0, width/2, height)
        right_canvas = QtCore.QRect(width/2, 0, width/2, height)

        painter = QtGui.QPainter(self.collage)
        painter.drawImage(left_canvas, self.img1)
        painter.drawImage(right_canvas, self.img2)
        self.ui.graphic_collage.setPixmap(self.collage)
        painter.end()

    def openImage(self):
        tab = self.ui.tabImages.currentIndex()

        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
         self.MainWindow, "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")

        if fileName:
            if tab == 0:
                self.img1.load(fileName)
                if self.img1.height > 800:
                    self.img1 = self.img1.scaled(1000, 800, 1, 1)
                self.ui.graphic_tabImage1.setPixmap(
                    QtGui.QPixmap.fromImage(self.img1))
            else:
                self.img2.load(fileName)
                if self.img2.height > 800:
                    self.img2 = self.img2.scaled(1000, 800, 1, 1)
                self.ui.graphic_tabImage2.setPixmap(
                    QtGui.QPixmap.fromImage(self.img2))
        else:
            pass

    def rotateImage(self):
        tab = self.ui.tabImages.currentIndex()

        if tab == 0:
            self.img1 = self.img1.transformed(QtGui.QTransform().rotate(90))
            self.ui.graphic_tabImage1.setPixmap(
                QtGui.QPixmap.fromImage(self.img1))
        else:
            self.img2 = self.img2.transformed(QtGui.QTransform().rotate(90))
            self.ui.graphic_tabImage2.setPixmap(
                QtGui.QPixmap.fromImage(self.img2))

    def saveImage(self):
        tab = self.ui.tabImages.currentIndex()

        fileName, fileType = QtWidgets.QFileDialog.getSaveFileName(
         self.MainWindow, "Save Image", ".", "Image Files (*.png *.jpg *.bmp)")

        if fileName:
            if tab == 0:
                print("Save image 1")
            elif tab == 1:
                print("Save image 2")
            elif tab == 2:
                image = self.collage.toImage()
                image.save(fileName)
        else:
            pass


program = QtWidgets.QApplication(sys.argv)
app = Photo_Collager()
app.run()
sys.exit(program.exec_())
