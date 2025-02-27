import sys
import cv2
import numpy as np
import pytesseract
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
from mss import mss

# Set Tesseract OCR Path (Modify if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class HighlighterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sct = mss()
        self.keywords = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_screen)

    def initUI(self):
        self.setWindowTitle("Multi-Highlighter")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        
        self.keyword_input = QTextEdit(self)
        self.keyword_input.setPlaceholderText("Enter keywords (comma-separated)")
        layout.addWidget(self.keyword_input)
        
        self.start_button = QPushButton("Start Highlighting", self)
        self.start_button.clicked.connect(self.start_highlighting)
        layout.addWidget(self.start_button)
        
        self.overlay_label = QLabel(self)
        layout.addWidget(self.overlay_label)
        
        self.central_widget.setLayout(layout)
    
    def start_highlighting(self):
        self.keywords = [kw.strip().lower() for kw in self.keyword_input.toPlainText().split(',')]
        if self.keywords:
            self.timer.start(2000)  # Capture screen every 2 seconds
    
    def process_screen(self):
        screenshot = self.sct.grab(self.sct.monitors[1])
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        
        text_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        for i, word in enumerate(text_data['text']):
            if word.lower() in self.keywords:
                (x, y, w, h) = (text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.overlay_label.setPixmap(QPixmap.fromImage(qimg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HighlighterApp()
    window.show()
    sys.exit(app.exec_())
