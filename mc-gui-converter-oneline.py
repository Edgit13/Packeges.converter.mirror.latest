import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel

class ConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Bite MC GUI v0.2')
        self.resize(500, 400)
        self.setStyleSheet("background-color: #1e1e2e; color: #cdd6f4; font-family: 'Monospace';")

        layout = QVBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type text here...")
        self.input.setStyleSheet("background-color: #313244; border: 1px solid #45475a; padding: 5px;")
        
        layout.addWidget(QLabel("Input:"))
        layout.addWidget(self.input)

        self.btn = QPushButton("Convert")
        self.btn.setStyleSheet("background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px;")
        self.btn.clicked.connect(self.convert)
        layout.addWidget(self.btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background-color: #181825; border: 1px solid #45475a;")
        
        layout.addWidget(QLabel("Binary Output:"))
        layout.addWidget(self.output)

        self.setLayout(layout)

    def convert(self):
        text = self.input.text()
        if text:
            binary_str = " ".join([format(ord(c), '08b') for c in text])
            self.output.setText(binary_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterGUI()
    window.show()
    sys.exit(app.exec())
