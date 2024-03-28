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
from PyQt6.QtCore import Qt
from source.controller import Controller  # Importamos el controlador

#-----------------------------------------
# CLASES PARA INTERFACES VIEW.PY
#-----------------------------------------
class View(QMainWindow):
    def __init__(self):
        # Constructor de la clase View
        super().__init__()
        self.setWindowTitle("Search Interface")
        # Asigna un tamaño específico a la ventana
        self.setFixedSize(400, 100)  # Asigna un ancho de 400 píxeles y una altura de 300 píxeles
        self.initUI()
    
    def initUI(self):
        # Inicializa la interfaz de usuario
        icon_path = "resources/images/icono ink.png"  # Ruta de la imagen del icono
        self.setWindowIcon(QIcon(icon_path)) # Configura el icono de la ventana
        self.setupLayout()  # Configura el diseño de la interfaz

    def setupLayout(self):
        # Configura el diseño de la ventana
        self.vertical_layout = QVBoxLayout()  # Crea un layout vertical
        self.central_widget = QWidget()  # Crea un widget central
        self.central_widget.setLayout(self.vertical_layout)  # Asigna el layout al widget central
        self.setCentralWidget(self.central_widget)  # Establece el widget central de la ventana principal
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Centra horizontal y verticalmente los widgets en el layout

        self.setupSearchSapBar()  # Configura la barra de búsqueda
        self.setupSearchConsecutiveBar()  # Configura la barra de búsqueda
        self.setupSearchButton()  # Configura el botón de búsqueda

    def setupSearchSapBar(self):
        # Configura la barra de búsqueda
        self.search_sap_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_sap_bar.setPlaceholderText("Número de SAP")  # Establece el texto previo
        self.search_sap_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_sap_bar)  # Añade la barra de búsqueda al layout vertical
    
    def setupSearchConsecutiveBar(self):
        # Configura la barra de búsqueda
        self.search_consecutive_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_consecutive_bar.setPlaceholderText("Número Consecutivo")  # Establece el texto previo
        self.search_consecutive_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_consecutive_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchButton(self):
        # Configura el botón de búsqueda
        self.search_button = QPushButton("Search")  # Crea un botón de búsqueda con el texto "Search"
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
            """
        )
        self.vertical_layout.addWidget(self.search_button)  # Añade el botón de búsqueda al layout vertical

class Interface:
    def __init__(self):
        #Constructor de la clase Interface
        self.view = View()  # Inicializa una instancia de la clase View
        self.controller = Controller(self.view)  # Inicializa una instancia del controlador asociado a la vista

    def show(self):
        # Método para mostrar la interfaz de usuario
        self.view.show()  # Muestra la ventana principal de la interfaz de usuario
