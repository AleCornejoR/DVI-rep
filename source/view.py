# source/view.py
"""
Este módulo contiene la definición de la clase View y la clase Interface.
La clase View proporciona la interfaz gráfica de usuario para la aplicación de búsqueda.
La clase Interface se encarga de crear una instancia de la clase View y del controlador asociado.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
import sys
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QCompleter, QLineEdit, QDialog, QLabel, QGridLayout
from PyQt6.QtGui import QIcon, QPixmap, QImage # Importa la clase QIcon desde PyQt6.QtGui
from PyQt6.QtCore import Qt, pyqtSignal
import os
from source.controller import Controller  # Importamos el controlador

#-----------------------------------------
# CLASES PARA INTERFACES VIEW.PY
#-----------------------------------------
class View(QMainWindow):
    enterPressed = pyqtSignal()  # Señal personalizada para indicar que se ha presionado la tecla Enter

    def __init__(self):
        # Constructor de la clase View
        print("\n>> Iniciando Vista - View ----->")

        super().__init__()
        self.setWindowTitle("Buscador")
        self.initUI()
    
    def initUI(self):
        # Inicializa la interfaz de usuario
        print("> View -> Iniciando Interfaz")

        icon_path = "resources/images/icono-ink.ico"  # Ruta de la imagen del icono
        self.setWindowIcon(QIcon(icon_path)) # Configura el icono de la ventana
        self.setupLayout()  # Configura el diseño de la interfaz
  

    def setupLayout(self):
        print("> View -> Configurando Ventana: START")

        # Configura el diseño de la ventana
        self.vertical_layout = QVBoxLayout()  # Crea un layout vertical
        self.central_widget = QWidget()  # Crea un widget central
        self.central_widget.setLayout(self.vertical_layout)  # Asigna el layout al widget central
        self.setCentralWidget(self.central_widget)  # Establece el widget central de la ventana principal
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Centra horizontal y verticalmente los widgets en el layout

        search_bar_names = self.readSearchBarNamesFromFile("resources/data/column_names.txt")
        for column in search_bar_names:
            self.setupSearchBar(column)

        self.setupSearchButton()  # Configura el botón de búsqueda

        # Asigna un tamaño específico a la ventana
        search_bar_names = self.readSearchBarNamesFromFile("resources/data/column_names.txt")
        height_size = 35 * (1 + len(search_bar_names))
        self.setFixedSize(300, height_size)  # Asigna un ancho de 400 píxeles y una altura de 300 píxeles
        
        print("> View -> Configurando Ventana: [OK]")

    def readSearchBarNamesFromFile(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
        
    def setupSearchBar(self, column):
        print(f"> View -> Configurando Barra de Busqueda {column}: START", end = " ")

        # Configura la barra de búsqueda
        search_bar = QLineEdit()  # Crea una barra de búsqueda
        formatted_column = column.capitalize().replace("_", " ")
        search_bar.setPlaceholderText(f"{formatted_column}")  # Establece el texto previo
        self.set_search_bar_style(search_bar)

        setattr(self, f"search_{column.lower()}_bar", search_bar)  # Agrega la barra de búsqueda al objeto self con el nombre adecuado
        self.vertical_layout.addWidget(search_bar)  # Añade la barra de búsqueda al layout vertical
        print("~ [OK]")

    def setupSearchButton(self):
        print("> View -> Configurando Boton de Busqueda: START", end = " ")

        # Configura el botón de búsqueda
        self.search_button = QPushButton("Search")  # Crea un botón de búsqueda con el texto "Search"

        # Añade un icono al botón
        search_icon = QIcon("resources/images/icono busqueda.png")  # Reemplaza "ruta/al/icono.png" con la ruta de tu icono
        self.search_button.setIcon(search_icon)
        self.set_search_button_style()

        self.vertical_layout.addWidget(self.search_button)  # Añade el botón de búsqueda al layout vertical
        print("~ [OK]")

    def set_search_bar_style(self, search_bar):
        # Definimos el estilo del botón con esquinas redondeadas
        search_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
                background-color: #FFFFFF;  /* Cambia el color de fondo a blanco */
            }
            """
        )
    
    def set_search_button_style(self):
        # Definimos el estilo del botón con esquinas redondeadas
        self.search_button.setStyleSheet(
            """
            QPushButton {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                background-color: #2196F3;  /* Color de fondo */
                color: white;  /* Color del texto */
                padding: 5px 5px;  /* Relleno interno */
                min-width: 100px;  /* Ancho mínimo del botón */
                max-width: 100px;  /* Ancho máximo del botón */
            }
            QPushButton:hover {
                background-color: #1976D2;  /* Color de fondo cuando se pasa el cursor sobre el botón */
            }
            QPushButton:pressed {
                background-color: #0D47A1;  /* Color de fondo cuando se presiona el botón */
            }
            QPushButton:disabled {
                background-color: #CCCCCC;  /* Color de fondo cuando el botón está deshabilitado (gris) */
            }
            """
        )

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.enterPressed.emit()  # Emitir la señal cuando se presiona Enter
    
    def setup_completers(self, search_bar_list, suggestions_dict):
        print("\n> View -> Configurando Autocompletar de Barras de Busqueda: START", end = " ")

        print("~ [OK]" if suggestions_dict else "~ [NOK]")

        for column in search_bar_list:
            search_bar = getattr(self, f"search_{column.lower()}_bar")
            suggestions = suggestions_dict.get(column)
            if suggestions is not None:
                completer = QCompleter(suggestions, search_bar)
                search_bar.setCompleter(completer)
    
    def show_result_window(self):
        # Crear una instancia de la ventana emergente y mostrarla
        popup_window = ResultWindow()
        popup_window.exec()
    
class ResultWindow(QDialog):
    def __init__(self):
        # Constructor de la clase ResultWindow
        print("\n>> Iniciando Vista - ResultWindow ----->")

        super().__init__()

        self.setWindowTitle("Resultado")
        self.initUI()

    def initUI(self):
        # Inicializa la ventana de resultados
        print("> ResultWindow -> Iniciando Interfaz")

        icon_path = "resources/images/icono-ink.ico"  # Ruta de la imagen del icono
        self.setWindowIcon(QIcon(icon_path)) # Configura el icono de la ventana
        self.setupLayout()  # Configura el diseño de la interfaz

    def setupLayout(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.etiqueta_mensaje = QLabel("Molde encontrado")
        layout.addWidget(self.etiqueta_mensaje)

        boton_abrir_pdf = QPushButton("Abrir PDF")
        boton_abrir_pdf.clicked.connect(self.open_pdf)
        layout.addWidget(boton_abrir_pdf)

    def open_pdf(self):
        ruta_pdf = os.path.join("resources", "PDF", "Test1.pdf")
        if os.path.exists(ruta_pdf):
            print("El archivo existe en la ruta especificada.")
            os.startfile(ruta_pdf)  # Abre el PDF con el programa predeterminado asociado en Windows
        else:
            print("El archivo no existe en la ruta especificada.")
        

        self.accept()  # Cerrar la ventana emergente después de abrir el PDF

class Interface:
    def __init__(self):
        #Constructor de la clase Interface
        print("\n>> Iniciando Ventana - Interface ----->")

        self.view = View()  # Inicializa una instancia de la clase View
        self.controller = Controller(self.view)  # Inicializa una instancia del controlador asociado a la vista

    def show(self):
        print("\n> Interface -> Mostrando Ventana")
        # Método para mostrar la interfaz de usuario
        self.view.show()  # Muestra la ventana principal de la interfaz de usuario
