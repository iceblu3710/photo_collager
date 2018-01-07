from PyQt5 import QtCore, QtWidgets


class QSelectionBox(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)
        # Setup resizing variables
        self.upperLeft = QtCore.QPoint()
        self.lowerRight = QtCore.QPoint()
        self.mode = ""
        self.selection = QtWidgets.QRubberBand(
            QtWidgets.QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            pos = QtCore.QPoint(event.pos())
            # If QRubberBand isVisible then check if user is resizing
            if self.selection.isVisible():
                if (self.lowerRight - pos).manhattanLength() < 20:
                    self.mode = "dragLowerRight"
                elif (self.upperLeft - pos).manhattanLength() < 20:
                    self.mode = "dragUpperLeft"
                else:
                    # Click not near a handle, clear selection
                    self.selection.hide()
            else:
                # Start a new selection
                self.upperLeft = pos
                self.lowerRight = pos
                self.mode = "dragLowerRight"
                self.selection.show()

    def mouseMoveEvent(self, event):
        if self.isVisible():
            # Determine selection direction
            if self.mode is "dragLowerRight":
                self.lowerRight = QtCore.QPoint(event.pos())
            if self.mode is "dragUpperLeft":
                self.upperLeft = QtCore.QPoint(event.pos())
            # Force 4x3 aspect ratio
            rSize = QtCore.QSize(3, 4)
            sSize = QtCore.QRect(self.upperLeft, self.lowerRight)
            rSize.scale(sSize.size(), QtCore.Qt.KeepAspectRatio)
            self.selection.setGeometry(QtCore.QRect(
                self.upperLeft, rSize).normalized())

    def getCoverage(self):
        # Convert TL of rubber band to global coordinates, + size of band
        return QtCore.QRect(self.selection.mapToGlobal(
            self.selection.contentsRect().topLeft()), self.selection.size())

    def cropImage(self):
        gRect = self.getCoverage()
        wRect = QtCore.QRect(
            self.mapFromGlobal(gRect.topLeft()), gRect.size())
        px = self.pixmap()
        tr = QtGui.QTransform()
        tr.scale(px.size().width()*1.0/self.size().width(),
                 px.size().height()*1.0/self.size().height())
        wRect = tr.mapRect(wRect)
        self.setPixmap(px.copy(wRect))
