import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from text_ui import Ui_textWindow
import joblib
import numpy as np

# Duygu tahmin modeli ve emoji sözlüğünü yükleyin
pipe_lr = joblib.load(open("model/text_emotion.pkl", "rb"))

emotions_emoji_dict = {
    "anger": "😠", "disgust": "🤮", "fear": "😨😱",
    "happy": "🤗", "joy": "😂", "neutral": "😐",
    "sad": "😔", "sadness": "😔", "shame": "😳", "surprise": "😮"
}


def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]


def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results


class AnaPencere(QMainWindow, Ui_textWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backButton_2.clicked.connect(self.butonaTiklandi)
        self.videoDetectorButton.clicked.connect(self.videoPageOpening)
        self.backButton.clicked.connect(self.mainPageOpening)
        self.whoWeAreButton.clicked.connect(self.whoweareOpening)

    def butonaTiklandi(self):
        metin = self.textEdit_4.toPlainText()
        if metin.strip():
            self.textBrowser_5.clear()
            self.textBrowser_5.append("I guess that's")

            self.textBrowser_3.append(f"User: {metin}")

            prediction = predict_emotions(metin)
            probability = get_prediction_proba(metin)
            emoji_icon = emotions_emoji_dict[prediction]
            confidence = np.max(probability)

            self.textBrowser_3.append(f"Prediction: {prediction} {emoji_icon}")
            self.textBrowser_3.append(f"Confidence: {confidence:.2f}")
            self.textEdit_4.clear()

            self.textBrowser_5.append(f"{prediction} {emoji_icon}")
            self.textBrowser_5.append("Try again?")
        else:
            self.textBrowser_5.clear()
            self.textBrowser_5.append("Please type something before submitting!")

    def videoPageOpening(self):
        from video import video
        self.videoPage = video()
        self.videoPage.show()
        self.close()

    def mainPageOpening(self):
        from main import main
        self.mainPage = main()
        self.mainPage.show()
        self.close()

    def whoweareOpening(self):
        from whoweare import whoweare
        self.mainPage = whoweare()
        self.mainPage.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())
