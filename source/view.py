# source/view.py
"""
Este módulo contiene la definición de la clase View y la clase Interface.
La clase View proporciona la interfaz gráfica de usuario para la aplicación de búsqueda.
La clase Interface se encarga de crear una instancia de la clase View y del controlador asociado.
"""
#-----------------------------------------
# LIBRERIAS
#-----------------------------------------
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QCompleter, QLineEdit
from PyQt6.QtGui import QIcon # Importa la clase QIcon desde PyQt6.QtGui
from PyQt6.QtCore import Qt, pyqtSignal
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
        # Asigna un tamaño específico a la ventana
        self.setFixedSize(300, 300)  # Asigna un ancho de 400 píxeles y una altura de 300 píxeles
        self.initUI()
    
    def initUI(self):
        # Inicializa la interfaz de usuario
        print("\n> Iniciando Interfaz ----->")

        icon_path = "resources/images/icono-ink.ico"  # Ruta de la imagen del icono
        self.setWindowIcon(QIcon(icon_path)) # Configura el icono de la ventana
        self.setupLayout()  # Configura el diseño de la interfaz

    def setupLayout(self):
        print("> Configurando Ventana ----->")

        # Configura el diseño de la ventana
        self.vertical_layout = QVBoxLayout()  # Crea un layout vertical
        self.central_widget = QWidget()  # Crea un widget central
        self.central_widget.setLayout(self.vertical_layout)  # Asigna el layout al widget central
        self.setCentralWidget(self.central_widget)  # Establece el widget central de la ventana principal
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)  # Centra horizontal y verticalmente los widgets en el layout

        self.setupSearchPlantaBar()
        self.setupSearchConsecutiveBar()  # Configura la barra de búsqueda
        self.setupSearchSapBar()  # Configura la barra de búsqueda
        self.setupSearchMoldeBar()  # Configura la barra de búsqueda
        self.setupSearchUsoBar()
        self.setupSearchTiempoDeVidaBar()
        self.setupSearchProductoBar()
        self.setupSearchButton()  # Configura el botón de búsqueda

    def setupSearchSapBar(self):
        print("> Configurando Barra de Busqueda SAP ----->")

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
        print("> Configurando Barra de Busqueda CONSECUTIVO ----->")

        # Configura la barra de búsqueda
        self.search_consecutivo_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_consecutivo_bar.setPlaceholderText("Número Consecutivo")  # Establece el texto previo
        self.search_consecutivo_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_consecutivo_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchMoldeBar(self):
        print("> Configurando Barra de Busqueda MOLDE ----->")

        # Configura la barra de búsqueda
        self.search_molde_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_molde_bar.setPlaceholderText("Número de Molde")  # Establece el texto previo
        self.search_molde_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_molde_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchPlantaBar(self):
        print("> Configurando Barra de Busqueda Planta ----->")

        # Configura la barra de búsqueda
        self.search_planta_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_planta_bar.setPlaceholderText("Planta")  # Establece el texto previo
        self.search_planta_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_planta_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchUsoBar(self):
        print("> Configurando Barra de Busqueda USO ----->")

        # Configura la barra de búsqueda
        self.search_uso_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_uso_bar.setPlaceholderText("Uso")  # Establece el texto previo
        self.search_uso_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_uso_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchTiempoDeVidaBar(self):
        print("> Configurando Barra de Busqueda TIEMPO DE VIDA ----->")

        # Configura la barra de búsqueda
        self.search_tiempo_de_vida_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_tiempo_de_vida_bar.setPlaceholderText("Tiempo de Vida")  # Establece el texto previo
        self.search_tiempo_de_vida_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_tiempo_de_vida_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchProductoBar(self):
        print("> Configurando Barra de Busqueda Producto ----->")

        # Configura la barra de búsqueda
        self.search_producto_bar = QLineEdit()  # Crea una barra de búsqueda
        self.search_producto_bar.setPlaceholderText("Poducto")  # Establece el texto previo
        self.search_producto_bar.setStyleSheet(
            """
            QLineEdit {
                border-radius: 10px;  /* Establece las esquinas redondeadas */
                padding: 5px;  /* Añade un pequeño relleno */
            }
            """
        )
        self.vertical_layout.addWidget(self.search_producto_bar)  # Añade la barra de búsqueda al layout vertical

    def setupSearchButton(self):
        print("> Configurando Boton de Busqueda ----->\n")

        # Configura el botón de búsqueda
        self.search_button = QPushButton("Search")  # Crea un botón de búsqueda con el texto "Search"

        # Añade un icono al botón
        search_icon = QIcon("resources/images/icono busqueda.png")  # Reemplaza "ruta/al/icono.png" con la ruta de tu icono
        self.search_button.setIcon(search_icon)
        self.set_search_button_style()

        self.vertical_layout.addWidget(self.search_button)  # Añade el botón de búsqueda al layout vertical

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
    
    def setup_completers(self, suggestions_dict):
        print("\n> Configurando Autocompletar de Barras de Busqueda ----->\n")

        if suggestions_dict:
            print("- View -> Sugerencias recibidas en la vista: OK")
        else:
            print("- View -> Sugerencias recibidas en la vista: NOK")

        search_bar_list = [
            "PLANTA",
            "CONSECUTIVO",
            "SAP", 
            "MOLDE",
            "USO",
            "TIEMPO_DE_VIDA",
            "PRODUCTO"]

        for column in search_bar_list:
            search_bar = getattr(self, f"search_{column.lower()}_bar")
            suggestions = suggestions_dict.get(column)
            if suggestions is not None:
                completer = QCompleter(suggestions, search_bar)
                search_bar.setCompleter(completer)
    

class Interface:
    def __init__(self):
        #Constructor de la clase Interface
        print("\n>> Iniciando Ventana ----->\n")

        self.view = View()  # Inicializa una instancia de la clase View
        self.controller = Controller(self.view)  # Inicializa una instancia del controlador asociado a la vista

    def show(self):
        print("\n> Mostrando Ventana ----->\n")
        # Método para mostrar la interfaz de usuario
        self.view.show()  # Muestra la ventana principal de la interfaz de usuario
