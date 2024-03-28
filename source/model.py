# source/model.py
"""
Módulo que define el modelo en el patrón Modelo-Vista-Controlador (MVC).
El modelo representa los datos y la lógica de la aplicación.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
import pandas as pd

#-----------------------------------------
# CLASES PARA MODELO MODEL.PY
#-----------------------------------------
class Model:
    def __init__(self):
        # Constructor de la clase Model.
        self.dataframe = pd.DataFrame()  # Inicializa un DataFrame vacío

    def load_excel_data(self, file_path):
        try:
            self.dataframe = pd.read_excel(file_path)
            print(self.dataframe.head())
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            self.dataframe = None
        
    def search_column(self, value, column_name):
        if self.dataframe is not None:
            try:
                result = self.dataframe[self.dataframe[column_name] == value]
                return result
            except KeyError:
                print(f"La columna '{column_name}' no existe en el DataFrame.")
                return None
        else:
            print("No hay datos cargados.")
            return None

    def print_consecutivo(self, sap_value): # Método para imprimir el valor consecutivo.
        print("Resultados de la búsqueda SAP:")
        print(sap_value)
        

    def print_sap(self, consecutive_value): # Método para imprimir el valor de SAP.
        print("Resultados de la búsqueda de consecutivo:")
        print(consecutive_value)
        