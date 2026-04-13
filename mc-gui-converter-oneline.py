import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QFont

class ConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Налаштування вікна
        self.setWindowTitle('Bite MC Converter GUI')
        self.setGeometry(300, 300, 500, 400)
        self.setStyleSheet("background-color: #1e1e2e; color: #cdd6f4;") # Стиль під твій Neovim

        layout = QVBoxLayout()

        # Заголовок
        self.label = QLabel('Введіть текст для конвертації:')
        self.label.setFont(QFont('JetBrainsMono Nerd Font', 12))
        layout.addWidget(self.label)

        # Поле введення
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Наприклад: Hello")
        self.input_field.setStyleSheet("background-color: #313244; border: 1px solid #45475a; padding: 5px;")
        layout.addWidget(self.input_field)

        # Кнопка
        self.btn = QPushButton('Конвертувати')
        self.btn.setStyleSheet("background-color: #89b4fa; color: #11111b; font-weight: bold; padding: 10px;")
        self.btn.clicked.connect(self.convert_text)
        layout.addWidget(self.btn)

        # Область виводу (як термінал)
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setFont(QFont('JetBrainsMono Nerd Font', 10))
        self.result_area.setStyleSheet("background-color: #181825; border: 1px solid #45475a;")
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def convert_text(self):
        user_input = self.input_field.text()
        if not user_input:
            self.result_area.setText("Будь ласка, введіть текст!")
            return

        # Твоя логіка з mc-converter.py
        binary_result = []
        output_text = f"{'Char':<8} | {'Decimal':<10} | {'Binary':<20}\n"
        output_text += "-" * 40 + "\n"

        for char in user_input:
            decimal_val = ord(char)
            binary_val = format(decimal_val, '08b')
            output_text += f"{char:<8} | {decimal_val:<10} | {binary_val:<20}\n"
            binary_result.append(binary_val)

        output_text += "\nFull Machine Code:\n"
        output_text += " ".join(binary_result)
        
        # Виводимо в GUI
        self.result_area.setText(output_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterGUI()
    ex.show()
    sys.exit(app.exec())
