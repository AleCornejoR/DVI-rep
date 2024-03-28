# main.py
"""
Módulo principal que inicia la aplicación.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from source.view import Interface  # Importa la clase Interface desde view.py
from source.model import Model # Importa la clase Model desde model.py
from PyQt6.QtWidgets import QApplication  # Importa la clase QApplication desde PyQt6.QtWidgets
import sys  # Importa el módulo sys para acceder a los argumentos de la línea de comandos

#-----------------------------------------
# CICLO PRINCIPAL
#-----------------------------------------
def main():
    model = Model()  # Instancia el modelo
    app = QApplication([])  # Crea una instancia de la aplicación QApplication
    interface = Interface()  # Crea una instancia de la interfaz

    file_path = "resources/data/dataFrameA.xlsx"  # Ruta del archivo Excel
    model.load_excel_data(file_path)  # Carga los datos del archivo de Excel en el DataFrame

    interface.show()  # Muestra la interfaz
    sys.exit(app.exec())
    
    #app.exec()  # Ejecuta la aplicación

if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente