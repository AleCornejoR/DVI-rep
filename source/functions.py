# functions.py

#---------------------------------------
# LIBRARIES
#---------------------------------------
import pandas as pd

def prepare_numidsuggestions(dataframe, column_name):
    # Reemplazar valores vacíos con 0 en la columna deseada
    dataframe.fillna({column_name: 0}, inplace=True)
    # Convertir la columna deseada a enteros y luego a texto (str)
    dataframe[column_name] = dataframe[column_name].astype(int)
    dataframe[column_name] = dataframe[column_name].astype(str)
    suggestions = dataframe[column_name].unique().tolist()
    return suggestions

def read_excel_file(file_path):
    print("Attempting to read file:", file_path)  # Debugging print
    
    # Check if the file exists
    try:
        # Read the Excel file and load the data into a DataFrame
        df = pd.read_excel(file_path)

        # Create a DataFrame copy
        df_copy = df.copy()        
        print("File found!")
        print("DataFrame Header:")
        print(df.head())  # Show the DataFrame header
        return df, df_copy
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None
    
def setup_file(dataframe):
    suggestions = {}  # Inicializar como un diccionario vacío
    sugg_column_list = [
    "No. Sap",
    "CONSECUTIVO",
    ]
    
    # Obtener los valores únicos de la columna deseada para autocompletar
    if dataframe is not None:
        for column in sugg_column_list:
            suggestions[column] = prepare_numidsuggestions(dataframe, column)
    else:
        suggestions = []

    setup = [suggestions]
    #print(suggestions)

    return setup