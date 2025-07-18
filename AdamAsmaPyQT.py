import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtCore import Qt


class HangmanCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.mistakes = 0

    def set_mistakes(self, mistakes):
        self.mistakes = mistakes
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Direk (sabit - gri)
        painter.setPen(QPen(Qt.GlobalColor.gray, 4))
        painter.drawLine(50, 250, 150, 250)
        painter.drawLine(100, 250, 100, 50)
        painter.drawLine(100, 50, 200, 50)
        painter.drawLine(200, 50, 200, 80)

        # Parçaları çiz
        if self.mistakes > 0:
            painter.setPen(QPen(Qt.GlobalColor.red, 4))  # Kafa
            painter.drawEllipse(180, 80, 40, 40)
        if self.mistakes > 1:
            painter.setPen(QPen(Qt.GlobalColor.blue, 4))  # Gövde
            painter.drawLine(200, 120, 200, 180)
        if self.mistakes > 2:
            painter.setPen(QPen(Qt.GlobalColor.darkGreen, 4))  # Sol kol
            painter.drawLine(200, 130, 170, 160)
        if self.mistakes > 3:
            painter.setPen(QPen(Qt.GlobalColor.darkGreen, 4))  # Sağ kol
            painter.drawLine(200, 130, 230, 160)
        if self.mistakes > 4:
            painter.setPen(QPen(Qt.GlobalColor.darkMagenta, 4))  # Sol bacak
            painter.drawLine(200, 180, 170, 220)
        if self.mistakes > 5:
            painter.setPen(QPen(Qt.GlobalColor.darkMagenta, 4))  # Sağ bacak
            painter.drawLine(200, 180, 230, 220)


class HangmanGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adam Asmaca - PyQt6 (Renkli Çizim)")
        self.setGeometry(100, 100, 500, 400)

        self.word_list = ["TELEFON", "BILGISAYAR", "MONITOR", "KAMERA", "YAZICI", "EKRAN"]
        self.reset_game()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.canvas = HangmanCanvas()
        self.canvas.setFixedHeight(270)
        main_layout.addWidget(self.canvas)

        self.word_label = QLabel(' '.join(self.guessed))
        self.word_label.setFont(QFont('Arial', 22))
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.word_label)

        info_layout = QHBoxLayout()
        self.info_label = QLabel(f"Kalan Hak: {self.attempts_left}")
        info_layout.addWidget(self.info_label)

        self.used_label = QLabel("Kullanılan Harfler: -")
        info_layout.addWidget(self.used_label)
        main_layout.addLayout(info_layout)

        self.input_field = QLineEdit()
        self.input_field.setMaxLength(1)
        self.input_field.setPlaceholderText("Harf giriniz...")
        main_layout.addWidget(self.input_field)

        self.guess_button = QPushButton("Tahmin Et")
        self.guess_button.clicked.connect(self.make_guess)
        main_layout.addWidget(self.guess_button)

        self.setLayout(main_layout)

    def make_guess(self):
        letter = self.input_field.text().upper()
        self.input_field.clear()

        if not letter.isalpha() or len(letter) != 1:
            return

        if letter in self.used_letters:
            QMessageBox.information(self, "Uyarı", f"{letter} harfi zaten kullanıldı.")
            return

        self.used_letters.append(letter)

        if letter in self.word:
            for i, c in enumerate(self.word):
                if c == letter:
                    self.guessed[i] = letter
        else:
            self.attempts_left -= 1

        self.update_ui()

        if '_' not in self.guessed:
            QMessageBox.information(self, "Tebrikler", f"Kazandınız! Kelime: {self.word}")
            self.reset_game()
        elif self.attempts_left == 0:
            QMessageBox.critical(self, "Kaybettiniz", f"Doğru Kelime: {self.word}")
            self.reset_game()

    def update_ui(self):
        self.word_label.setText(' '.join(self.guessed))
        self.info_label.setText(f"Kalan Hak: {self.attempts_left}")
        self.used_label.setText(f"Kullanılan Harfler: {', '.join(self.used_letters)}")
        self.canvas.set_mistakes(6 - self.attempts_left)

    def reset_game(self):
        self.word = random.choice(self.word_list).upper()
        self.guessed = ['_' for _ in self.word]
        self.attempts_left = 6
        self.used_letters = []

        if hasattr(self, 'word_label'):
            self.update_ui()
        if hasattr(self, 'canvas'):
            self.canvas.set_mistakes(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HangmanGame()
    window.show()
    sys.exit(app.exec())
