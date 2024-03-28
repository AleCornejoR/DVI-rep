# main.py
"""
Módulo principal que inicia la aplicación.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from source.view import Interface  # Importa la clase Interface desde view.py
from PyQt6.QtWidgets import QApplication  # Importa la clase QApplication desde PyQt6.QtWidgets

#-----------------------------------------
# CICLO PRINCIPAL
#-----------------------------------------
def main():
    app = QApplication([])  # Crea una instancia de la aplicación QApplication
    interface = Interface()  # Crea una instancia de la interfaz
    interface.show()  # Muestra la interfaz
    app.exec()  # Ejecuta la aplicación

if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente
