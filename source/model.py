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
import os

#-----------------------------------------
# CLASES PARA MODELO MODEL.PY
#-----------------------------------------
class Model:
    dataframe = pd.DataFrame() # Inicializa un DataFrame vacío
    suggestions_dict = {}  # Diccionario para almacenar sugerencias por columna
    column_names = [] # Lista de nombres de columnas

    def __init__(self):
        # Constructor de la clase Model.
        print("\n>> Iniciando Modelo - Model ----->\n")

        if not self.dataframe.empty:
            print("- Model -> dataframe: OK")
        else:
            print("- Model -> dataframe: NOK")
        if self.suggestions_dict:
            print("- Model -> sugerencias: OK")
        else:
            print("- Model -> sugerencias: NOK")

    def load_excel_data(self, file_path):
        print("\n> Cargando Datos ----->\n")
        try:
            new_data = pd.read_excel(file_path) 
            if new_data.empty:  # Verificar si el DataFrame cargado está vacío
                print("El archivo está vacío.")
                return 
            if self.dataframe.empty:  # Verificar si el DataFrame principal está vacío
                Model.dataframe = new_data
            else:
                # Concatenar los nuevos datos con los existentes
                Model.dataframe = pd.concat([self.dataframe, new_data], ignore_index=True)

            print(self.dataframe, "\n")
            print(self.dataframe.info(), "\n")

            Model.column_names = self.dataframe.columns.tolist()
            self.save_column_names(self.column_names)
            self.suggestions()

        except FileNotFoundError:
            print("El archivo no fue encontrado.")

    def save_column_names(self, column_names, filename="resources/data/column_names.txt"):
        print("\n> Cargando Columnas a .txt ----->\n")
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as file:
                for column_name in column_names:
                    file.write(column_name + "\n")
            print(f"> Los nombres de las columnas se han guardado en {filename}")
        except Exception as e:
            print(f"> Error al guardar los nombres de las columnas: {e}")

    def suggestions(self):
        print("\n> Generando Sugerencias ----->\n")
        if not self.dataframe.empty:
            for column in self.dataframe.columns:
                Model.suggestions_dict[column] = [str(val) for val in self.dataframe[column].unique()]  # Convertir sugerencias a texto
            print(Model.suggestions_dict)
        else:
            print("No hay datos cargados.")
    
    def get_suggestions(self):
        # Agrega el método get_suggestions() para devolver las sugerencias generadas
        print("\n> Obteniendo Sugerencias generadas----->\n")
        if self.suggestions_dict:
            print("- Model -> Sugerencias obtenidas: OK")
        else:
            print("- Model -> Sugerencias obtenidas: NOK")
        return self.suggestions_dict    
    
    
    def search_suggestions(self, search_bar_values):
        # Obtener la lista de sugerencias existente
        existing_suggestions_dict = self.get_suggestions()

        # Verificar si los valores ingresados están en las sugerencias existentes
        valid_values = {}
        for column, value in zip(self.column_names, search_bar_values):
            valid_values[column] = value in existing_suggestions_dict.get(column, [])

        print("\n> Generando nuevas Sugerencias----->\n")

        # Inicializar el DataFrame original con todas las filas
        filtered_df = self.dataframe

        # Aplicar el filtro solo si el valor ingresado pertenece a las sugerencias existentes
        for column, value in zip(self.column_names, search_bar_values):
            if valid_values[column]:
                if self.is_integer(value):
                    value = int(value)
                filtered_df = filtered_df[filtered_df[column] == value]

        # Construir un diccionario de sugerencias para cada columna
        suggestions_dict = {}
        for column in filtered_df.columns:
            suggestions_dict[column] = filtered_df[column].astype(str).unique().tolist()

        print("- Model -> Sugerencias nuevas generadas: OK")
        return suggestions_dict

    def is_integer(self, value):
        # Función auxiliar para verificar si un valor puede convertirse en un entero
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def search_column(self, value, column_name):
        print("\n> Buscando valor ----->\n")
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

    def print_value(self, column, value): # Método para imprimir el valor.
        print("\nResultados de la busqueda", column, ":\n", value, "\n")