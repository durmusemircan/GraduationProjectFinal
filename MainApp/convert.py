from PyQt5 import uic

with open("text_ui.py", "w", encoding="utf-8") as fout:
    uic.compileUi("text.ui", fout)