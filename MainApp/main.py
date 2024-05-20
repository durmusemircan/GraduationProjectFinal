import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.videoButton.clicked.connect(self.videoPageOpening)
        self.textButton.clicked.connect(self.textPageOpening)

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
    window = main()
    window.show()
    sys.exit(app.exec_())