import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow


class Photo_Collager(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # class globals
        self.img1 = QtGui.QImage()
        self.img2 = QtGui.QImage()
        self.collage = QtGui.QPixmap()
        # init ui
        self.setupUi(self)
        self.show()
        # init QLabel Pixmaps
        self.graphic_tabImage1.setPixmap(QtGui.QPixmap())
        self.graphic_tabImage2.setPixmap(QtGui.QPixmap())
        self.graphic_collage.setPixmap(QtGui.QPixmap())
        # init buttons
        self.push_tabImage1_open.clicked.connect(self.openImage)
        self.push_tabImage1_crop.clicked.connect(self.cropImage)
        self.push_tabImage1_rotate.clicked.connect(self.rotateImage)
        self.push_tabImage1_save.clicked.connect(self.saveImage)
        self.push_tabImage2_open.clicked.connect(self.openImage)
        self.push_tabImage2_crop.clicked.connect(self.cropImage)
        self.push_tabImage2_rotate.clicked.connect(self.rotateImage)
        self.push_tabImage2_save.clicked.connect(self.saveImage)
        self.push_collage_generate.clicked.connect(self.updateCollage)
        self.push_collage_save.clicked.connect(self.saveImage)
        # QLabel needs to strech to fit pixmap
        self.graphic_tabImage1.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        self.verticalLayout.setAlignment(
            self.graphic_tabImage1, QtCore.Qt.AlignCenter)
        self.graphic_tabImage2.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        self.verticalLayout_2.setAlignment(
            self.graphic_tabImage2, QtCore.Qt.AlignCenter)
        self.graphic_collage.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        self.gridLayout_6.setAlignment(
            self.graphic_collage, QtCore.Qt.AlignCenter)

    def cropImage(self):
        tab = self.tabImages.currentWidget().objectName()
        if tab == 'tabImage1':
            label = self.graphic_tabImage1
            image = self.img1
        elif tab == 'tabImage2':
            label = self.graphic_tabImage2
            image = self.img2
        else:
            return

        # do the cropping
        gRect = label.getCoverage()
        wRect = QtCore.QRect(
            label.mapFromGlobal(gRect.topLeft()), gRect.size())
        px = label.pixmap()
        tr = QtGui.QTransform()
        tr.scale(px.size().width()*1.0/label.size().width(),
                px.size().height()*1.0/label.size().height())
        wRect = tr.mapRect(wRect)
        label.setPixmap(px.copy(wRect))

        # regen QImage from cropped size
        if tab == 'tabImage1':
            self.img1 = px.toImage()
        elif tab == 'tabImage2':
            self.img2 = px.toImage()

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
        size = self.comboPrintSize.currentText()
        size = size.split()
        size.remove('x')

        width = height / int(size[0]) * int(size[1])
        self.collage = QtGui.QPixmap(width, height)
        left_canvas = QtCore.QRect(0, 0, width/2, height)
        right_canvas = QtCore.QRect(width/2, 0, width/2, height)

        painter = QtGui.QPainter(self.collage)
        painter.drawImage(left_canvas, self.img1)
        painter.drawImage(right_canvas, self.img2)
        self.graphic_collage.setPixmap(self.collage)
        painter.end()

    def scaleQImage(self, image):
        height = QtWidgets.QApplication.desktop()
        height = height.screenGeometry().height() - 200
        if image.height() > height:
            return image.scaled(1000, height,
                QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        else:
            return image

    def openImage(self):
        tab = self.tabImages.currentWidget().objectName()

        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(
         self, "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")

        if fileName:
            image = QtGui.QImage(fileName)
            image = self.scaleQImage(image)
            if tab == 'tabImage1':
                self.img1 = image            
                self.graphic_tabImage1.setPixmap(
                    QtGui.QPixmap.fromImage(self.img1))
            elif tab == 'tabImage2':
                self.img2 = image
                self.graphic_tabImage2.setPixmap(
                    QtGui.QPixmap.fromImage(self.img2))
            else:
                print(tab, 'not implemented')
        else:
            pass

    def rotateImage(self):
        tab = self.tabImages.currentWidget().objectName()

        if tab == 'tabImage1':
            self.img1 = self.img1.transformed(QtGui.QTransform().rotate(90))
            image = self.scaleQImage(self.img1)
            self.graphic_tabImage1.setPixmap(
                QtGui.QPixmap.fromImage(image))
        elif tab == 'tabImage2':
            self.img2 = self.img2.transformed(QtGui.QTransform().rotate(90))
            image = self.scaleQImage(self.img2)
            self.graphic_tabImage2.setPixmap(
                QtGui.QPixmap.fromImage(image))
        else:
            print(tab, 'not implemented')

    def saveImage(self):
        tab = self.tabImages.currentWidget().objectName()

        fileName, fileType = QtWidgets.QFileDialog.getSaveFileName(
         self, "Save Image", ".", "Image Files (*.png *.jpg *.bmp)")
        
        if fileName:
            # add extention if required
            if os.path.splitext(fileName)[-1].lower() == '':
                fileName += ".jpg"
            # what tab wants to save?
            if tab == 'tabImage1':
                px = self.graphic_tabImage1
            elif tab == 'tabImage2':
                px = self.graphic_tabImage2
            elif tab == 'tabCollage':
                px = self.graphic_collage
            else:
                print(f"{tab} has no save funtion")    
            # save the image, fail gracefully
            try:
                image = px.pixmap().toImage()
                image.save(fileName)
            except AttributeError as error:
                print(f"{error}\n\tNo image content to save.")
        else:
            pass


myProgram = QtWidgets.QApplication(sys.argv)
app = Photo_Collager()
sys.exit(myProgram.exec_())
