import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from whoweare_ui import Ui_whoweareWindow

class whoweare(QMainWindow, Ui_whoweareWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.videoButton.clicked.connect(self.videoPageOpening)
        self.emotionButton.clicked.connect(self.textPageOpening)

    def textPageOpening(self):
        from text import AnaPencere
        self.textPage = AnaPencere()
        self.textPage.show()
        self.close() 

    def videoPageOpening(self):
        from video import video
        self.videoPage = video()
        self.videoPage.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = whoweare()
    window.show()
    sys.exit(app.exec_())