# source/model.py
"""
Módulo que define el modelo en el patrón Modelo-Vista-Controlador (MVC).
El modelo representa los datos y la lógica de la aplicación.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
import pandas as pd  # Importa la librería pandas y la renombra como pd
import numpy as np  # Importa la librería numpy y la renombra como np
import os  # Importa el módulo os para interactuar con el sistema operativo

#-----------------------------------------
# CLASES PARA MODELO MODEL.PY
#-----------------------------------------
class Model:
    dataframe = pd.DataFrame() # Inicializa un DataFrame vacío
    suggestions_dict = {}  # Diccionario para almacenar sugerencias por columna
    column_names = [] # Lista de nombres de columnas

    def __init__(self): # Constructor de la clase Model.
        print("\n>> Iniciando Modelo - Model ----->")  # Mensaje de inicio del constructor

        # Verifica si hay datos en el DataFrame y en las sugerencias y muestra un mensaje correspondiente
        print("> Model -> datos en dataframe:", "~ [OK]" if not self.dataframe.empty else "~ [NOK]")
        print("> Model -> datos en sugerencias:", "~ [OK]" if self.suggestions_dict else "~ [NOK]")

    def load_excel_data(self, file_path):
        print("\n> Model -> Cargando Datos: START", end = " ") # Indica que se está cargando el archivo
        try:
            new_data = pd.read_excel(file_path) 
            if new_data.empty:  # Verificar si el DataFrame cargado está vacío
                print("~ [NOK]\n    > El archivo esta vacio.")
                return 
            if self.dataframe.empty:  # Verificar si el DataFrame principal está vacío
                Model.dataframe = new_data
            else:
                Model.dataframe = pd.concat([self.dataframe, new_data], ignore_index=True)  # Concatena los nuevos datos con los existentes
            
            # Muestra el DataFrame y su información
            print("~ [OK]\n", self.dataframe)
            print(self.dataframe.info())
            
            # Guarda los nombres de las columnas en un archivo .txt y genera sugerencias
            Model.column_names = self.dataframe.columns.tolist()#[:3]
            self.save_column_names(self.column_names)
            self.suggestions()

        except FileNotFoundError:
            print("~ [NOK]\n    > El archivo no fue encontrado.")

    def save_column_names(self, column_names, filename="resources/data/column_names.txt"):
        print("\n> Model -> Cargando Columnas a .txt: START", end=" ")  # Indica que se están guardando los nombres de las columnas

        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True) # Crea directorios si no existen y abre el archivo en modo escritura
            with open(filename, "w") as file:
                for column_name in column_names: # Escribe cada nombre de columna en una línea del archivo
                    file.write(column_name + "\n")
                    
            print(f"~ [OK]\n    > Los nombres de las columnas se han guardado en {filename}")  # Muestra mensaje de éxito

        except Exception as e:
            print(f"~ [NOK]\n    > Error al guardar los nombres de las columnas: {e}")  # Muestra mensaje de error

    def suggestions(self):
        print("\n> Model -> Generando Sugerencias: START", end = " ")
        if not self.dataframe.empty:
            for column in self.dataframe.columns:
                Model.suggestions_dict[column] = [str(val) for val in self.dataframe[column].unique()]  # Convertir sugerencias a texto
            print("~ [OK]\n", Model.suggestions_dict)
        else:
            print("~ [NOK]\n    > No hay datos cargados.")
    
    def get_suggestions(self):
        # Agrega el método get_suggestions() para devolver las sugerencias generadas
        print("\n> Model -> Obteniendo Sugerencias actuales: START", end = " ")
        if self.suggestions_dict:
            print("~ [OK]")
        else:
            print("~ [NOK]")
        return self.suggestions_dict    
    
    
    def search_suggestions(self, search_bar_values):
        # Obtener la lista de sugerencias existente
        existing_suggestions_dict = self.get_suggestions()

        # Verificar si los valores ingresados están en las sugerencias existentes
        valid_values = {}
        for column, value in zip(self.column_names, search_bar_values):
            valid_values[column] = value in existing_suggestions_dict.get(column, [])

        print("> Model -> Generando nuevas Sugerencias: START", end = " ")

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

        print("~ [OK]")
        return suggestions_dict

    def is_integer(self, value):
        # Función auxiliar para verificar si un valor puede convertirse en un entero
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def search_column(self, value, column_name):
        print("\n> Model -> Buscando valor: START", end=" ")
    
        if self.dataframe.empty:
            print("~ [NOK]\n", ">  No hay datos cargados.")
            return None
    
        if value == '':
            print("~ [NOK]\n", ">  El valor ingresado está vacío.")
            return None
    
        try:
            if self.is_integer(value):
                value = np.int64(value)
            result = self.dataframe[self.dataframe[column_name] == value]
            print("~ [OK]")
            return result
    
        except KeyError:
            print("~ [NOK]\n", f">  La columna '{column_name}' no existe en el DataFrame.")
            return None
    
        except ValueError:
            print("~ [NOK]\n", ">  El valor ingresado no es válido.")
            return None

    def print_value(self, column, value): # Método para imprimir el valor.
        print("> Model -> Resultados de la busqueda", column, ":\n", value, "\n")