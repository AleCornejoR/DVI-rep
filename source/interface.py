# interface.py

#---------------------------------------
# LIBRARIES
#---------------------------------------
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter, QLabel, QPushButton, QHBoxLayout, QDialog
from PyQt6.QtGui import QIcon
import os

class MyWindow(QMainWindow):
    def __init__(self, dataframe, dataframe_copy, setup):
        super().__init__()
        self.setWindowTitle("Data Visualitator Palmex")
        # Establecer tamaño específico para la ventana
        self.resize(400, 100)

        # Obtener la ruta del directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "..", "resources", "images", "icono ink.png")
        # Establecer el icono de la ventana
        self.setWindowIcon(QIcon(icon_path))

        # Crear un widget central y un layout vertical
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Crear una barra de búsqueda para el numero de sap
        self.search_bar_sap = QLineEdit()
        self.search_bar_sap.setPlaceholderText("Ingrese el número SAP del Molde")
        layout.addWidget(self.search_bar_sap)

        # Crear una barra de búsqueda para el numero de consecutivo
        self.search_bar_consecutive = QLineEdit()
        self.search_bar_consecutive.setPlaceholderText("Ingrese el número Consecutivo del Molde")
        layout.addWidget(self.search_bar_consecutive)

        # Crear un layout horizontal para los botones
        buttons_layout = QHBoxLayout()

        # Crear botones
        self.search_button = QPushButton("Search")
        self.edit_button = QPushButton("Edit")
        self.search_button.setEnabled(False)
        self.edit_button.setEnabled(False)

        # Establecer estilos y tamaño para los botones
        button_width = 100  # Ancho deseado para los botones
        #Establecer estilos para los botones
        self.search_button.setStyleSheet("background-color: #f0f0f0; color: white;")
        self.search_button.setMaximumWidth(button_width)
        self.edit_button.setStyleSheet("background-color: #f0f0f0; color: white;")
        self.edit_button.setMaximumWidth(button_width)

        # Configurar la acción a realizar cuando se presiona el botón Search
        self.search_button.clicked.connect(self.search_action)

        # Configurar la acción a realizar cuando se presiona el botón Edit
        self.edit_button.clicked.connect(self.edit_action)

        # Agregar los botones al layout horizontal
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addWidget(self.search_button)
        
        # Agregar el layout horizontal al layout vertical principal
        layout.addLayout(buttons_layout)

        # Configurar el autocompletado para el número de SAP
        completer_sap = QCompleter(setup[0]['No. Sap'], self.search_bar_sap)
        self.search_bar_sap.setCompleter(completer_sap)

        # Configurar el autocompletado para el número consecutivo
        completer_consecutive = QCompleter(setup[0]['CONSECUTIVO'], self.search_bar_consecutive)
        self.search_bar_consecutive.setCompleter(completer_consecutive)

        # Configurar la acción a realizar cuando se ingresa un número SAP
        self.search_bar_sap.returnPressed.connect(lambda: self.show_consecutive(dataframe_copy, self.search_bar_sap.text(), self.search_bar_consecutive))

        # Configurar la acción a realizar cuando se ingresa un número consecutivo
        self.search_bar_consecutive.returnPressed.connect(lambda: self.show_sap(dataframe_copy, self.search_bar_consecutive.text(), self.search_bar_sap))

        # Establecer el widget central
        self.setCentralWidget(central_widget)

    def show_consecutive(self, dataframe, sap_number, search_bar_consecutive):
        # Filtrar el DataFrame para encontrar el número consecutivo correspondiente al número SAP ingresado
        filtered_df = dataframe[dataframe['No. Sap'] == sap_number]
        if not filtered_df.empty:
            consecutive_number = filtered_df['CONSECUTIVO'].iloc[0]
            # Mostrar el número consecutivo en la etiqueta
            #label_consecutive.setText(f"Número Consecutivo: {consecutive_number}")
            search_bar_consecutive.setText(f"{consecutive_number}")
        else:
            search_bar_consecutive.setText("Número Consecutivo no encontrado")

        # Desactivar la edición de la barra de búsqueda del consecutivo
        search_bar_consecutive.setReadOnly(True)

        # Habilitar los botones
        self.search_button.setEnabled(True)
        self.edit_button.setEnabled(True)
        #Establecer estilos para los botones
        self.search_button.setStyleSheet("background-color: #6495ED; color: white;")
        self.edit_button.setStyleSheet("background-color: #f0f0f0; color: black;")

    def show_sap(self, dataframe, consecutive_number, search_bar_sap):
        # Filtrar el DataFrame para encontrar el número SAP correspondiente al número consecutivo ingresado
        filtered_df = dataframe[dataframe['CONSECUTIVO'] == consecutive_number]
        if not filtered_df.empty:
            sap_number = filtered_df['No. Sap'].iloc[0]
            # Mostrar el número SAP en la etiqueta
            search_bar_sap.setText(f"{sap_number}")
        else:
            search_bar_sap.setText("Número SAP no encontrado")
        
        # Desactivar la edición de la barra de búsqueda del sap
        search_bar_sap.setReadOnly(True)

        # Habilitar los botones
        self.search_button.setEnabled(True)
        self.edit_button.setEnabled(True)
        self.search_button.setStyleSheet("background-color: #6495ED; color: white;")
        self.edit_button.setStyleSheet("background-color: #f0f0f0; color: black;")

    def search_action(self):
        # Lógica para el botón Search (buscar)
        new_window = SearchResultsWindow()  # Crear una nueva ventana de resultados
        new_window.exec()  # Mostrar la ventana

    def edit_action(self):
        # Habilitar la edición de los campos
        self.search_bar_sap.setReadOnly(False)
        self.search_bar_consecutive.setReadOnly(False)

class SearchResultsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Results")
        self.resize(1000, 700)
        # Puedes agregar elementos a esta ventana como lo desees