import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow


img1 = QtGui.QImage()
img2 = QtGui.QImage()
collage = None


def updateCollage():
    global collage

    img1Height = img1.height()
    img2Height = img2.height()
    # calculate which image is the smallest in height and use
    # that to set the canvas. width = minHeight / 4 * 6
    # 300dpi 4in x 6in image = 1200x1800
    if (img1Height < img2Height):
        height = img1Height
    else:
        height = img2Height
    
    # set collage print size
    size = ui.comboPrintSize.currentText()
    size = size.split()
    size.remove('x')
    
    width = height / int(size[0]) * int(size[1])
    collage = QtGui.QPixmap(width, height)
    left_canvas = QtCore.QRect(0, 0, width/2, height)
    right_canvas = QtCore.QRect(width/2, 0, width/2, height)
    
    painter = QtGui.QPainter(collage)
    painter.drawImage(left_canvas, img1)
    painter.drawImage(right_canvas, img2)  
    ui.graphic_collage.setPixmap(collage)
    painter.end()


def openImage1():  
    global img1
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
        "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
    if fileName:
        img1.load(fileName)
        if img1.height > 800:
            img1 = img1.scaled(1000, 800, 1, 1)
        ui.graphic_tabImage1.setPixmap(QtGui.QPixmap.fromImage(img1))
    else:
        pass


def rotateImage1():
    global img1

    img1 = img1.transformed(QtGui.QTransform().rotate(90))
    ui.graphic_tabImage1.setPixmap(QtGui.QPixmap.fromImage(img1))


def saveImage1():
    print("Save image 1")


def openImage2():
    global img2
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
        "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
    if fileName:
        img2.load(fileName)
        if img2.height > 800:
            img2 = img2.scaled(1000, 800, 1, 1)
        ui.graphic_tabImage2.setPixmap(QtGui.QPixmap.fromImage(img2))
    else:
        pass


def rotateImage2():
    global img2

    img2 = img2.transformed(QtGui.QTransform().rotate(90))
    ui.graphic_tabImage2.setPixmap(QtGui.QPixmap.fromImage(img2))


def saveImage2():
    print("Save image 2")


def saveCollage():
    global collage

    fileName, fileType = QtWidgets.QFileDialog.getSaveFileName(MainWindow,
        "Save Image", ".", "Image Files (*.png *.jpg *.bmp)")
    if fileName:
        image = collage.toImage()
        image.save(fileName)
    else:
        pass


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# load debug images
DEBUG = True
if(DEBUG == True):
    img1.load('/home/uminded/Programming/qt5/python/Print_Collager/20170831_121950.jpg')
    img2.load('/home/uminded/Programming/qt5/python/Print_Collager/20170831_121950.jpg') #20170831_122023
    ui.graphic_tabImage1.setPixmap(QtGui.QPixmap.fromImage(img1))
    ui.graphic_tabImage2.setPixmap(QtGui.QPixmap.fromImage(img2))

# application code here
ui.push_tabImage1_open.clicked.connect(openImage1)
ui.push_tabImage1_rotate.clicked.connect(rotateImage1)
ui.push_tabImage1_save.clicked.connect(saveImage1)
ui.push_tabImage2_open.clicked.connect(openImage2)
ui.push_tabImage2_rotate.clicked.connect(rotateImage2)
ui.push_tabImage2_save.clicked.connect(saveImage2)
ui.push_collage_generate.clicked.connect(updateCollage)
ui.push_collage_save.clicked.connect(saveCollage)

# save each pixmap to a resized variable for the collage

sys.exit(app.exec_())
