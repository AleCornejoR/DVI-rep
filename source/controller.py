# source/controller.py
from source.model import Model  # Importa la clase Model desde model.py


class Controller:
    def __init__(self, view):
        self.model = Model()
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.search_button.clicked.connect(self.handle_search)

    def handle_search(self):
        consecutivo_value = self.view.search_bar.text()
        self.model.print_consecutivo(consecutivo_value)