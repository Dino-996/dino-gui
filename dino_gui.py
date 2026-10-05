"""App desktop veloce (PyQt6) per calcolare il peso supportato dal DINO.

Avvio:
    pip install -r requirements.txt
    python dino_peso_gui.py
"""
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from service import POSIZIONI, calcola_peso_supportato  # riusa la logica, non la duplica

PESO_MIN, PESO_MAX = 0.0, 14000.0

STYLE_SHEET = """
QWidget {
    background-color: #10221c;
    color: #e8f1ec;
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    font-size: 13px;
}

QLabel#titolo {
    font-size: 19px;
    font-weight: 600;
    color: #7fd6a3;
    padding-bottom: 2px;
}

QLabel#sottotitolo {
    font-size: 11px;
    color: #7b968a;
    padding-bottom: 6px;
}

QFrame#card {
    background-color: #16302a;
    border: 1px solid #244138;
    border-radius: 10px;
}

QLabel#campoLabel {
    color: #a9c4b8;
    font-size: 12px;
}

QDoubleSpinBox, QComboBox {
    background-color: #0c1a15;
    border: 1px solid #2c4d41;
    border-radius: 6px;
    padding: 6px 8px;
    color: #e8f1ec;
    selection-background-color: #2f7a52;
}

QDoubleSpinBox:focus, QComboBox:focus {
    border: 1px solid #4fbf85;
}

QComboBox::drop-down {
    border: none;
    width: 22px;
}

QComboBox QAbstractItemView {
    background-color: #0c1a15;
    border: 1px solid #2c4d41;
    selection-background-color: #2f7a52;
    outline: none;
}

QPushButton#calcolaBtn {
    background-color: #2f7a52;
    border: none;
    border-radius: 6px;
    padding: 10px 0;
    font-weight: 600;
    font-size: 13px;
    color: #f2fbf6;
}

QPushButton#calcolaBtn:hover {
    background-color: #3a9364;
}

QPushButton#calcolaBtn:pressed {
    background-color: #256242;
}

QLabel#risultatoCaption {
    color: #7b968a;
    font-size: 11px;
    padding-top: 10px;
}

QLabel#risultatoValore {
    font-size: 26px;
    font-weight: 700;
    color: #7fd6a3;
}
"""


class DinoPesoWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Deinosuchus grab calculator")
        self.setFixedWidth(360)
        self.setStyleSheet(STYLE_SHEET)

        titolo = QLabel("\U0001F40A  Deinosuchus grab calculator")
        titolo.setObjectName("titolo")

        sottotitolo = QLabel("The Isle \u2022 Evrima")
        sottotitolo.setObjectName("sottotitolo")

        card = QFrame()
        card.setObjectName("card")

        self.peso_input = QDoubleSpinBox()
        self.peso_input.setRange(PESO_MIN, PESO_MAX)
        self.peso_input.setSuffix(" kg")
        self.peso_input.setDecimals(1)
        self.peso_input.setValue(1000.0)

        self.posizione_input = QComboBox()
        self.posizione_input.addItems(POSIZIONI.keys())

        peso_label = QLabel("Peso attuale")
        peso_label.setObjectName("campoLabel")

        posizione_label = QLabel("Posizione")
        posizione_label.setObjectName("campoLabel")

        form = QFormLayout()
        form.setVerticalSpacing(10)
        form.setContentsMargins(18, 18, 18, 10)
        form.addRow(peso_label, self.peso_input)
        form.addRow(posizione_label, self.posizione_input)

        calcola_btn = QPushButton("CALCOLA")
        calcola_btn.setObjectName("calcolaBtn")
        calcola_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        calcola_btn.setDefault(True)
        calcola_btn.clicked.connect(self.on_calcola)

        risultato_caption = QLabel("PESO MASSIMO AFFERRABILE")
        risultato_caption.setObjectName("risultatoCaption")
        risultato_caption.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.risultato_label = QLabel("\u2014")
        self.risultato_label.setObjectName("risultatoValore")
        self.risultato_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout = QVBoxLayout()
        card_layout.setSpacing(4)
        card_layout.addLayout(form)
        btn_wrapper = QVBoxLayout()
        btn_wrapper.setContentsMargins(18, 4, 18, 18)
        btn_wrapper.addWidget(calcola_btn)
        btn_wrapper.addWidget(risultato_caption)
        btn_wrapper.addWidget(self.risultato_label)
        card_layout.addLayout(btn_wrapper)
        card.setLayout(card_layout)

        root = QVBoxLayout()
        root.setContentsMargins(20, 20, 20, 20)
        root.setSpacing(2)
        root.addWidget(titolo)
        root.addWidget(sottotitolo)
        root.addSpacing(10)
        root.addWidget(card)
        self.setLayout(root)

    def on_calcola(self) -> None:
        peso = self.peso_input.value()
        posizione = self.posizione_input.currentText()
        risultato = calcola_peso_supportato(peso, posizione)
        self.risultato_label.setText(f"{risultato:.2f} kg")


def main() -> None:
    app = QApplication(sys.argv)
    window = DinoPesoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()