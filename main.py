# main.py
from source.view import Interface
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication([])
    interface = Interface()
    interface.show()
    app.exec()

if __name__ == "__main__":
    main()