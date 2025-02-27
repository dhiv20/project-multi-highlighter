This is a Python-based prototype for multi-highlighter application which uses following technologies:  

- **PyQt5** (for GUI and transparent overlay window)  
- **Tesseract OCR** (for text recognition and extraction)  
- **Pillow & OpenCV** (for screen capturing)  
- **Pytesseract** (Python wrapper for Tesseract OCR)  

This prototype will:  
1. Capture the screen periodically.  
2. Extract text from the captured image using OCR.  
3. Highlight the user-specified keywords in an overlay window.  

### Installation Guide:

1. **Install Python** (if not installed)  
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**  
   Open a terminal or command prompt and run:
   ```sh
   pip install opencv-python numpy pytesseract mss pyqt5
   ```
   
3. **Install Tesseract OCR**  
    - Download and install Tesseract OCR from here:  
      👉 [Tesseract OCR Download](https://github.com/UB-Mannheim/tesseract/wiki)  
    - During installation, **note the installation path** (e.g., `C:\Program Files\Tesseract-OCR`).


4. **Add Tesseract to System PATH (Manually)**
    - Open **Control Panel** → **System** → **Advanced System Settings**.  
    - Click **Environment Variables**.  
    - Under **System Variables**, find `Path`, select **Edit**.  
    - Click **New**, and **add the path** to the `tesseract.exe` file:  
      ```
      C:\Program Files\Tesseract-OCR\
      ```
    - Click **OK**, restart your computer.


5. **Set the Correct Tesseract Path in Python**
    Modify the script to explicitly set the Tesseract path:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```
    Make sure the path matches your installation.


6. **Run the Application**  
   Save the script as `multi_highlighter.py` and execute:
   ```sh
   python multi_highlighter.py
   ```

If getting `[WinError 740]`, means Tesseract may need elevated permissions.
- Right-click **Command Prompt** → **Run as Administrator**.
- Then try running your script:
  ```sh
  python multi_highlighter.py
  ```

### How It Works:
- Enter keywords in the text box (comma-separated).  
- Click **Start Highlighting**.  
- The app captures your screen, extracts text, and highlights entered keywords in real time.

