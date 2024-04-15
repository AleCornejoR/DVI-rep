# source/controller.py
"""
Módulo que contiene la definición del controlador en el patrón Modelo-Vista-Controlador (MVC).
El controlador gestiona las interacciones entre la vista y el modelo.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from source.model import Model  # Importa la clase Model desde model.py
from PyQt6.QtCore import QTimer

#-----------------------------------------
# CLASES PARA CONTROLADOR CONTROLLER.PY
#-----------------------------------------
class Controller:

    def __init__(self, view):
        # Constructor de la clase Controller.
        # Args:
        #     view: La instancia de la vista.
        print("\n>> Iniciando Controldor - Controller ----->")

        self.model = Model() # Inicializa una instancia del modelo
        self.view = view # Asigna la instancia de la vista
        self.connect_signals() # Conecta los eventos de la vista a los métodos del controlador
        self.load_suggestions() # Carga las sugerencias iniciales
        self.update_search_button_state() # Llamamos a esta función para establecer el estado inicial del botón


    def connect_signals(self):
        # Conecta los eventos de la vista a los métodos correspondientes del controlador.
        print("\n> Controller -> Conectando Señales: START", end = " ")
        self.view.search_button.clicked.connect(self.handle_search) # Conecta el evento de hacer clic en el botón de búsqueda al método handle_search
        self.view.pdf_button.clicked.connect(self.generate_pdf) # Conecta el evento de hacer clic en el botón de búsqueda al método generate_pdf

        search_bars = [column.lower() for column in self.model.column_names]

         # Conecta las señales textChanged de las barras de búsqueda al método handle_text_changed
        for bar_name in search_bars:
            search_bar = getattr(self.view, f"search_{bar_name}_bar")
            search_bar.textChanged.connect(self.handle_text_changed)

        self.view.enterPressed.connect(self.handle_enter_key)  # Conectar la señal de la vista al método del controlador
        print("~ [OK]")

    def load_suggestions(self):
        print("\n> Controller -> Cargando Sugerencias: START")
        suggestions_dict = self.model.get_suggestions()  # Obtener el diccionario de sugerencias del modelo
        if suggestions_dict:
            print("\n> Controller -> Cargando Sugerencias: [OK]")
        else:
            print("\n> Controller -> Cargando Sugerencias: [NOK]")
        self.view.setup_completers(self.model.column_names, suggestions_dict)  # Pasar el diccionario de sugerencias a la vista
    
    def handle_text_changed(self):
        # Método llamado cuando cambia el texto en alguna de las barras de búsqueda
        print("\n> Controller -> Verificando Barras de Busqueda: START")
        self.update_search_button_state()

    def obtain_text_in_search_bars(self):
        text_in_search_bars = []
        for column in self.model.column_names:
            search_text = getattr(self.view, f"search_{column.lower()}_bar").text()
            if ": " in search_text:
                text_in_search_bars.append(search_text.split(": ")[1])
            else:
                text_in_search_bars.append(search_text)
        return text_in_search_bars
    
    def search_suggestions(self):
        # Lista de valores a buscar
        print("\n> Controller -> Valores Buscados")

        actual_value_list = self.obtain_text_in_search_bars()
        print(actual_value_list)

        actual_suggestions_dict = self.model.search_suggestions(actual_value_list)
        
        print("\n> Controller -> Sugerencias Nuevas Obtenidas")
        print(actual_suggestions_dict)

        self.autocomplete_search_bars(actual_suggestions_dict)
        
        self.view.setup_completers(self.model.column_names, actual_suggestions_dict)  # Actualizar las sugerencias en la vista
    
    def autocomplete_search_bars(self, actual_suggestions_dict):
        print("\n> Controller -> Autocompletando Barras de Búsqueda: START")

        # Iterar sobre las sugerencias para cada columna
        for column, suggestions in actual_suggestions_dict.items():
            if len(suggestions) == 1:  # Verificar si solo hay una sugerencia
                search_bar = getattr(self.view, f"search_{column.lower()}_bar")  # Obtener la barra de búsqueda correspondiente
                search_bar.setText(f"{search_bar.placeholderText()}: {suggestions[0]}")  # Rellenar la barra de búsqueda con la única sugerencia
                search_bar.setReadOnly(True)  # Bloquear la barra de búsqueda
                print(f"> Controller -> Autocompletando y bloqueando la barra de búsqueda de {column} con valor {suggestions[0]}")

                search_bar.setStyleSheet(
                    """
                    QLineEdit {
                        border-radius: 10px;  /* Establece las esquinas redondeadas */
                        padding: 5px;  /* Añade un pequeño relleno */
                        background-color: #E0E9FF;  /* Cambia el color de fondo */
                    }
                    """
                )
            else:
                print(f"> Controller -> No se puede autocompletar ni bloquear la barra de búsqueda de {column} ya que hay múltiples sugerencias")

        print("> Controller -> Autocompletando Barras de Búsqueda: END")

    def update_search_button_state(self):
        # Verifica si todas las barras de búsqueda tienen texto y actualiza el estado del botón de búsqueda
        print("> Controller -> Actualizando Boton de Busqueda: START", end = " ")
        self.view.search_button.setEnabled(all(self.obtain_text_in_search_bars()))  # Habilita/deshabilita el botón de búsqueda
        self.view.pdf_button.setEnabled(all(self.obtain_text_in_search_bars()))  # Habilita/deshabilita el botón de búsqueda
        print("~ [OK]")

    def handle_enter_key(self):
        # Maneja la activación de la búsqueda al presionar Enter
        self.view.search_button.click()  # Simula un clic en el botón de búsqueda
        self.search_suggestions()
        self.view.search_button.setStyleSheet(
            """
            QPushButton {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                background-color: #0D47A1;  /* Color de fondo */
                color: white;  /* Color del texto */
                padding: 5px 5px;  /* Relleno interno */
                min-width: 100px;  /* Ancho mínimo del botón */
                max-width: 100px;  /* Ancho máximo del botón */
            }
            """
        )
        # Volver a configurar el estilo del botón después de un breve retraso
        QTimer.singleShot(200, self.view.set_search_button_style)

    def handle_search(self):
        # Maneja la búsqueda.
        # Obtiene los valores de los campos de búsqueda en la vista y llama a los métodos correspondientes del modelo para imprimir los valores.
        print("\n> Controller -> Administrando Busqueda: START")
        actual_value_list = self.obtain_text_in_search_bars() #Actual list

        for column_name, search_value in zip(self.model.column_names, actual_value_list):
            result = self.model.search_column(search_value, column_name)
            if result is not None:
                self.model.print_value(column_name, result)  # Llama al método del modelo para imprimir el valor correspondiente
        
        self.view.show_result_window()

    def generate_pdf(self):
        print("\n> Controller -> Administrando Busqueda: START", end = " ")
        self.model.generate_pdf(self.model.dataframe, "resources/pdf/output.pdf")
        print("~ [OK]")