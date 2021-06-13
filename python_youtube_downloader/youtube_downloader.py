import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
from pytube import YouTube

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.initUI()

    def download(self):
        url = self.txt_url.text()
        YouTube(url).streams.first().download()
    
    def initUI(self):
        self.setWindowTitle("Youtube Downloader")
        self.setGeometry(200,200,750,100)
        self.setWindowIcon(QIcon("youtube_logo.png"))

        self.lbl_url = QtWidgets.QLabel(self)
        self.lbl_url.resize(400,40)
        self.lbl_url.setText("Enter YouTube Video's URL:")
        self.lbl_url.move(50,30)

        self.txt_url = QtWidgets.QLineEdit(self)
        self.txt_url.move(190,35)
        self.txt_url.resize(400,30)

        self.btn_download = QtWidgets.QPushButton(self)
        self.btn_download.setText("Download")
        self.btn_download.move(600,35)
        self.btn_download.clicked.connect(self.download)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())