# source/view.py
"""
Este módulo contiene la definición de la clase View y la clase Interface.
La clase View proporciona la interfaz gráfica de usuario para la aplicación de búsqueda.
La clase Interface se encarga de crear una instancia de la clase View y del controlador asociado.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon  # Importa la clase QIcon desde PyQt6.QtGui
from source.controller import Controller  # Importamos el controlador

#-----------------------------------------
# CLASES PARA INTERFACES VIEW.PY
#-----------------------------------------

class View(QMainWindow):
    def __init__(self):
        # Constructor de la clase View
        super().__init__()
        self.setWindowTitle("Search Interface")
        self.initUI()
    
    def initUI(self):
        # Inicializa la interfaz de usuario
        icon_path = "resources/images/icono ink.png"  # Ruta de la imagen del icono
        self.setWindowIcon(QIcon(icon_path)) # Configura el icono de la ventana
        self.setupLayout()  # Configura el diseño de la interfaz

    def setupLayout(self):
        # Configura el diseño de la ventana
        self.layout = QVBoxLayout()  # Crea un layout vertical
        self.central_widget = QWidget()  # Crea un widget central
        self.central_widget.setLayout(self.layout)  # Asigna el layout al widget central
        self.setCentralWidget(self.central_widget)  # Establece el widget central de la ventana principal

        self.setupSearchBar()  # Configura la barra de búsqueda
        self.setupSearchButton()  # Configura el botón de búsqueda

    def setupSearchBar(self):
        # Configura la barra de búsqueda
        self.search_bar = QLineEdit()  # Crea una barra de búsqueda
        self.layout.addWidget(self.search_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchButton(self):
        # Configura el botón de búsqueda
        self.search_button = QPushButton("Search")  # Crea un botón de búsqueda con el texto "Search"
        self.layout.addWidget(self.search_button)  # Añade el botón de búsqueda al layout vertical

class Interface:
    def __init__(self):
        #Constructor de la clase Interface
        self.view = View()  # Inicializa una instancia de la clase View
        self.controller = Controller(self.view)  # Inicializa una instancia del controlador asociado a la vista

    def show(self):
        # Método para mostrar la interfaz de usuario
        self.view.show()  # Muestra la ventana principal de la interfaz de usuario
