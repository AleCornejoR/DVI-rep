# main.py
"""
Módulo principal que inicia la aplicación.
"""

# Importaciones de librerías
from source.view import Interface  # Importa la clase Interface desde view.py
from source.model import Model  # Importa la clase Model desde model.py
from PyQt6.QtWidgets import QApplication  # Importa la clase QApplication desde PyQt6.QtWidgets
import sys  # Importa el módulo sys para acceder a los argumentos de la línea de comandos

def main():
    model = Model() # Instancia del modelo
    file_path = "resources/data/dataFrameA.xlsx" # Ruta del archivo Excel
    model.load_excel_data(file_path) # Carga de datos desde el archivo Excel al DataFrame del modelo
   
    app = QApplication([]) # Crea una instancia de la aplicación QApplication

    interface = Interface() # Crea una instancia de la interfaz
    interface.show() # Muestra la interfaz   

    sys.exit(app.exec()) # Ejecuta la aplicación y espera a que termine

if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente