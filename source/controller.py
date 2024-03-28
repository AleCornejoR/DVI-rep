# source/controller.py
"""
Módulo que contiene la definición del controlador en el patrón Modelo-Vista-Controlador (MVC).
El controlador gestiona las interacciones entre la vista y el modelo.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from source.model import Model  # Importa la clase Model desde model.py

#-----------------------------------------
# CLASES PARA CONTROLADOR CONTROLLER.PY
#-----------------------------------------
class Controller:
    def __init__(self, view):
        # Constructor de la clase Controller.
        # Args:
        #     view: La instancia de la vista.

        self.model = Model()  # Inicializa una instancia del modelo
        self.view = view  # Asigna la instancia de la vista
        self.connect_signals()  # Conecta los eventos de la vista a los métodos del controlador

    def connect_signals(self):
        # Conecta los eventos de la vista a los métodos correspondientes del controlador.
        self.view.search_button.clicked.connect(self.handle_search) # Conecta el evento de hacer clic en el botón de búsqueda al método handle_search

    def handle_search(self):
        # Maneja la búsqueda.
        # Obtiene los valores de los campos de búsqueda en la vista y llama a los métodos correspondientes del modelo para imprimir los valores.
        
        sap_value = self.view.search_sap_bar.text()  # Obtiene el valor ingresado en la barra de búsqueda de SAP desde la vista
        self.model.print_sap(sap_value)  # Llama al método del modelo para imprimir el valor de SAP

        consecutive_value = self.view.search_consecutive_bar.text()  # Obtiene el valor ingresado en la barra de búsqueda consecutiva desde la vista
        self.model.print_consecutivo(consecutive_value)  # Llama al método del modelo para imprimir el valor consecutivo
