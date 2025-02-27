import tkinter as tk
from tkinter import scrolledtext
import cv2
import numpy as np
import pytesseract
import mss

class MultiHighlighterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Highlighter")
        
        tk.Label(root, text="Enter Keywords (comma-separated):").pack()
        self.keyword_entry = tk.Entry(root, width=50)
        self.keyword_entry.pack()
        
        self.highlight_button = tk.Button(root, text="Highlight", command=self.highlight_text)
        self.highlight_button.pack()
        
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
        self.text_area.pack()
    
    def capture_screen_text(self):
        with mss.mss() as sct:
            screenshot = sct.grab(sct.monitors[1])
            img = np.array(screenshot)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            return text
    
    def highlight_text(self):
        self.text_area.delete(1.0, tk.END)
        screen_text = self.capture_screen_text()
        keywords = [kw.strip().lower() for kw in self.keyword_entry.get().split(',')]
        
        for word in screen_text.split():
            if word.lower() in keywords:
                self.text_area.insert(tk.END, word + " ", "highlight")
            else:
                self.text_area.insert(tk.END, word + " ")
        
        self.text_area.tag_config("highlight", background="yellow", foreground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiHighlighterApp(root)
    root.mainloop()