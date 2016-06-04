import sys
from functools import partial
from os.path import splitext
from SteganographyGUI import *
from PySide.QtCore import *
from PySide.QtGui import *
import scipy.misc
import numpy
import re
from Steganography import *


class SteganographyConsumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.setupUi(self)

        self.embedPayload = None
        self.embedCarrier1 = None
        self.extrCarrier2 = None
        self.scene = [QGraphicsScene(self),QGraphicsScene(self),QGraphicsScene(self),QGraphicsScene(self)]
        self.image = QImage()

        self.connect(self.chkApplyCompression,SIGNAL('stateChanged(int)'),self.compressionSetup)
        self.connect(self.slideCompression,SIGNAL('valueChanged(int)'),self.txtCompressionSetup)
        self.connect(self.slideCompression,SIGNAL('valueChanged(int)'),self.validateImages)
        self.connect(self.btnSave,SIGNAL('clicked()'),self.saveImage)
        self.connect(self.btnExtract,SIGNAL('clicked()'),self.extractPayload)
        self.connect(self.btnClean,SIGNAL('clicked()'),self.cleanCarrier)

        # Get the views that are required to have the drag-and-drop enabled.
        views = [self.viewPayload1, self.viewCarrier1, self.viewCarrier2]
        accept = lambda e: e.accept()

        for view in views:
            # We need to accept the drag event to be able to accept the drop.
            view.dragEnterEvent = accept
            view.dragMoveEvent = accept
            view.dragLeaveEvent = accept

            # Assign an event handler (a method,) to be invoked when a drop is performed.
            view.dropEvent = partial(self.processDrop, view)

        # NOTE: The line above links "all" views to the same function, and passes the view as a parameter in the
        # function. You could pass more than one widget to the function by adding more parameters to the signature,
        # in case you want to bind more than one widget together. you can even pass in another function, as a parameter,
        # which might significantly reduce the size of your code. Finally, if you prefer to have a separate function
        # for each view, where the view name is, say, "someView", you will need to:
        # 1- Create a function with a definition similar: funcName(self, e)
        # 2- Assign the function to be invoked as the event handler:
        #   self.someView.dropEvent = self.funcName

    def payloadSetup(self):
        #setup slider(compressionSetup)
        self.slideCompression.setValue(0)
        self.chkApplyCompression.setChecked(False)

        #setup size
        self.payloadSizeSetup()

    def compressionSetup(self):
        if self.chkApplyCompression.isChecked():
            self.lblLevel.setEnabled(True)
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
        else:
            self.lblLevel.setEnabled(False)
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)

        if self.embedPayload is not None:
            self.payloadSizeSetup()

    def payloadSizeSetup(self):
        self.compressionLevel = -1
        if self.txtCompression.isEnabled():
            self.compressionLevel = self.slideCompression.value()

        embParray = scipy.misc.imread(self.pathPayload1)

        self.embedPayload = Payload(embParray,self.compressionLevel,None)
        self.payloadSize = len(self.embedPayload.xml)

        self.txtPayloadSize.setText(str(self.payloadSize))


    def txtCompressionSetup(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        if self.embedPayload is not None:
            self.payloadSizeSetup()

    def processDrop(self, view, e):
        """
        Process a drop event when it occurs on the views.
        """
        mime = e.mimeData()

        # Guard against types of drops that are not pertinent to this app.
        if not mime.hasUrls():
            return

        # Obtain the file path using the OS format.
        filePath = mime.urls()[0].toLocalFile()
        _, ext = splitext(filePath)

        if not ext == ".png":
            return

        # Now the file path is ready to be processed.
        #
        # TODO: Remove the print statement and continue the implementation using the filePath.
        #


        self.path = re.search(r'([\w\:]+/){5}(?P<alpha>[\w/\.]+)',filePath)

        if view == self.viewPayload1:
            self.pathind = 0
            self.pathPayload1 = self.path.group('alpha')
            valid = self.image.load(self.pathPayload1)
        elif view == self.viewCarrier1:
            self.pathind = 1
            self.pathCarrier1 = self.path.group('alpha')
            valid = self.image.load(self.pathCarrier1)
        else:
            self.pathind = 2
            self.pathCarrier2 = self.path.group('alpha')
            valid = self.image.load(self.pathCarrier2)

        if valid:
            self.image = self.image.scaled(345,279,Qt.KeepAspectRatio)
            item = QPixmap.fromImage(self.image)
            self.scene[self.pathind].clear()
            self.scene[self.pathind].addPixmap(item)
            view.setScene(self.scene[self.pathind])
            if view == self.viewPayload1:
                self.payloadSetup()
            elif view == self.viewCarrier1:
                self.carrier1Setup()
            else:
                self.carrier2Setup()
        else:
            print('invalid image')

        self.validateImages()

    def carrier1Setup(self):
        self.carrier1SizeSetup()
        self.carrier1PayloadSetup()

    def carrier1SizeSetup(self):
        embCarray = scipy.misc.imread(self.pathCarrier1)

        self.embedCarrier1 = Carrier(embCarray)
        self.carrier1Size = self.embedCarrier1.calc_carrierSize()

        self.txtCarrierSize.setText(str(self.carrier1Size))

    def carrier1PayloadSetup(self):
        if self.embedCarrier1.payloadExists():
            self.lblPayloadFound.setText('>>>>Payload Found<<<<')
            self.chkOverride.setEnabled(True)
            self.override_flag = True
        else:
            self.lblPayloadFound.clear()
            self.chkOverride.setChecked(False)
            self.chkOverride.setDisabled(True)
            self.override_flag = False

    def validateImages(self):
        if self.embedCarrier1 is None or self.embedPayload is None:
            self.btnSave.setDisabled(True)
            return
        if self.payloadSize > self.carrier1Size:
            self.btnSave.setDisabled(True)
            return
        if self.embedCarrier1.payloadExists() and not self.chkOverride.isChecked:
            self.btnSave.setDisabled(True)
            return

        self.btnSave.setEnabled(True)

    def saveImage(self):
        filepath, _ = QFileDialog.getSaveFileName(self, caption='Save PNG file ...')

        if not filepath:
            return

        filepath = re.search(r'([\w\:]+/){5}(?P<alpha>[\w/\.]+)',filepath)
        filepath = filepath.group('alpha')

        scipy.misc.imsave(filepath,self.embedCarrier1.embedPayload(self.embedPayload,self.override_flag))

    def carrier2Setup(self):
        extCarray = scipy.misc.imread(self.pathCarrier2)
        self.extrCarrier2 = Carrier(extCarray)
        self.carrier2validate()

    def carrier2validate(self):
        if self.extrCarrier2.payloadExists():
            self.lblCarrierEmpty.clear()
            self.btnExtract.setEnabled(True)
            self.btnClean.setEnabled(True)
        else:
            self.lblCarrierEmpty.setText('>>>>Carrier Empty<<<<')
            self.btnExtract.setEnabled(False)
            self.btnClean.setEnabled(False)
            self.scene[3].clear()

    def extractPayload(self):
        self.scene[3] = QGraphicsScene()
        image = QImage()
        payload = self.extrCarrier2.extractPayload()
        scipy.misc.imsave('temp.png',payload.img)

        image.load('temp.png')
        image = image.scaled(345,279,Qt.KeepAspectRatio)
        item = QPixmap.fromImage(image)
        self.scene[3].clear()
        self.scene[3].addPixmap(item)
        self.viewPayload2.setScene(self.scene[3])

    def cleanCarrier(self):
        print('cleaning...')
        self.extrCarrier2.img = self.extrCarrier2.clean()
        self.carrier2validate()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()
