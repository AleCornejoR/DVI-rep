import pandas as pd
import os

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_pdf(data, output_path):
    columnas_data = data.columns.tolist()
    # Crear un diccionario para almacenar los valores de todas las columnas de 'data'
    valores_data = {columna: data[columna].values[0] if columna in data else '' for columna in data.columns}

    # Definir un diccionario que mapea los estados de uso a texto y colores correspondientes
    estados = {
        1: {"texto": "USO", "color": colors.green},
        2: {"texto": "DESUSO", "color": colors.red},
    }

    # Determinar el estado del molde y configurar el texto y color correspondiente
    estado_info = estados.get(valores_data["USO"], {"texto": "Estado: Desconocido", "color": colors.gray})

    # Construir el encabezado
    header_text = f"Molde: {valores_data['CONSECUTIVO']}, {valores_data['SAP']} - {valores_data['PRODUCTO']}"

    output_path = create_outputh_path(valores_data, output_path)

    # Crear un objeto SimpleDocTemplate para el PDF con la página en horizontal
    doc = SimpleDocTemplate(output_path, pagesize=landscape(A4))

    # Establecer el estilo del párrafo para el encabezado
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]

    # Crear contenido para el encabezado
    header_content = Paragraph(header_text, header_style)

    # Crear un párrafo con el texto del estado
    estado_text = estado_info["texto"]
    estado_paragraph = Paragraph(f"Estado: {estado_text}", styles["Normal"])

    # Calcular el ancho máximo del cuadro basado en la longitud del texto del estado
    max_width = len(estado_info["texto"]) * 32  # Ajusta el factor de multiplicación según tus necesidades

    # Crear una tabla para contener el párrafo del estado
    estado_table = Table([[estado_paragraph]], style=[
        ('BACKGROUND', (0, 0), (-1, -1), estado_info["color"]),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black)], 
        colWidths=[max_width])  # Ajustar automáticamente el ancho de la columna

    # Construir el contenido del PDF
    content = [header_content, Spacer(1, 0.2 * inch), estado_table]

    # Agregar el contenido al PDF
    doc.build(content)

def create_outputh_path(valores_data, output_path):
    # Crear el nombre de archivo
    file_name = f"{valores_data["CONSECUTIVO"]}_{valores_data["SAP"]}_{valores_data["PRODUCTO"]}.pdf"
    # Agrega el nombre de archivo al path de salida
    output_path = os.path.join(output_path, file_name)

    return output_path


# Ejemplo de uso
if __name__ == "__main__":
    data = {
        "Nombre": "Juan Pérez",
        "Edad": "30",
        "Correo electrónico": "juan@example.com"
    }
    output_path = "../pdf/output.pdf"
    generate_pdf(data, output_path)