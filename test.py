import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_MainWindow


img1 = QtGui.QImage()
img2 = QtGui.QImage()


def updateCollage():
    print("img1: ", img1.size())
    print("img2: ", img2.size())
    img1Height = img1.height()
    img2Height = img2.height()
    # calculate which image is the smallest in height and use
    # that to set the canvas. width = minHeight / 4 * 6
    # 300dpi 4in x 6in image = 1200x1800
    if (img1Height < img2Height):
        height = img1Height
    else:
        height = img2Height
    width = height / 4 * 6
    canvas = QtGui.QPixmap(width, height)
    left_canvas = QtCore.QRect(0, 0, width/2, height)
    right_canvas = QtCore.QRect(width/2, 0, width/2, height)
    
    painter = QtGui.QPainter(canvas)
    painter.drawImage(left_canvas, img1)
    painter.drawImage(right_canvas, img2)
    
    try:
        ui.graphic_collage.setPixmap(canvas)
    except:
        pass
    
    painter.end()


def openImage1():  
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
        "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
    if fileName:
        img1.load(fileName)
        ui.graphic_tabImage1.setPixmap(QtGui.QPixmap.fromImage(img1))
    else:
        pass


def saveImage1():
    print("Save image 1")


def openImage2():
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(MainWindow,
        "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
    if fileName:
        img2.load(fileName)
        ui.graphic_tabImage2.setPixmap(QtGui.QPixmap.fromImage(img2))
    else:
        pass


def saveImage2():
    print("Save image 2")


def saveCollage():
    print("Save collage")


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
ui.push_tabImage1_save.clicked.connect(saveImage1)
ui.push_tabImage2_open.clicked.connect(openImage2)
ui.push_tabImage2_save.clicked.connect(saveImage2)
ui.push_collage_save.clicked.connect(updateCollage)

# save each pixmap to a resized variable for the collage

# updateCollage() when the collage tab is cliked

sys.exit(app.exec_())
