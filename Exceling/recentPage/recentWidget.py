from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel
from .workCard import Card


class RecentView(QFrame):
    def __init__(self):
        super().__init__()
        main_layout = QGridLayout(self)
        main_layout.addWidget(Card("WorkNamea", "image1", "Excel", self), 0, 0)
        main_layout.addWidget(Card("WorkNameAB", "image1", "Word", self), 0, 1)
        main_layout.addWidget(Card("WorkNameABC", "image1", "Access", self), 0, 2)
        main_layout.addWidget(Card("WorkName", "image1", "Word", self), 1, 0)
        main_layout.addWidget(Card("WorkName", "image1", "Word", self), 1, 1)
        main_layout.addWidget(Card("WorkName", "image1", "Excel", self), 1, 2)
        # main_layout.addWidget(QLabel("HELLO"), 1, 0)
        self.setLayout(main_layout)

        self.setStyleSheet(
            "background-color: #141518;"
        )
