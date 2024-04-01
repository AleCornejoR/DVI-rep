# source/model.py
"""
Módulo que define el modelo en el patrón Modelo-Vista-Controlador (MVC).
El modelo representa los datos y la lógica de la aplicación.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
import pandas as pd
import numpy as np

#-----------------------------------------
# CLASES PARA MODELO MODEL.PY
#-----------------------------------------
class Model:
    def __init__(self):
        # Constructor de la clase Model.
        Model.dataframe = pd.DataFrame()  # Inicializa un DataFrame vacío
        Model.suggestions_dict = {}  # Diccionario para almacenar sugerencias por columna

    def load_excel_data(self, file_path):
        try:
            new_data = pd.read_excel(file_path) 
            if new_data.empty:  # Verificar si el DataFrame cargado está vacío
                print("El archivo está vacío.")
                return
            if Model.dataframe.empty:  # Verificar si el DataFrame principal está vacío
                Model.dataframe = new_data
            else:
                # Concatenar los nuevos datos con los existentes
                Model.dataframe = pd.concat([Model.dataframe, new_data], ignore_index=True)

            print(Model.dataframe.head())
            print(Model.dataframe.info())
            self.suggestions()

        except FileNotFoundError:
            print("El archivo no fue encontrado.")

    def suggestions(self):
        if not self.dataframe.empty:
            for column in self.dataframe.columns:
                Model.suggestions_dict[column] = self.dataframe[column].unique().tolist()
            print(Model.suggestions_dict)
        else:
            print("No hay datos cargados.")
        
    def search_column(self, value, column_name):
        if not self.dataframe.empty:
            if value != '':  # Verificar si value no está vacío
                try:
                    value = np.int64(value)  # Convertir a int64
                    result = self.dataframe[self.dataframe[column_name] == value]
                    return result
                except KeyError:
                    print(f"La columna '{column_name}' no existe en el DataFrame.")
                    return None
                except ValueError:
                    print("El valor ingresado no es válido.")
                    return None
            else:
                print("El valor ingresado está vacío.")
                return None
        else:
            print("No hay datos cargados.")
            return None

    def print_sap(self, sap_value): # Método para imprimir el valor consecutivo.
        print("Resultados de la búsqueda SAP:")
        print(sap_value)
        

    def print_consecutivo(self, consecutive_value): # Método para imprimir el valor de SAP.
        print("Resultados de la búsqueda de consecutivo:")
        print(consecutive_value)

    def print_molde(self, molde_value): # Método para imprimir el valor de molde.
        print("Resultados de la búsqueda del molde:")
        print(molde_value)
        
