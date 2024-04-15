import pandas as pd
import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib import utils

def generate_pdf(data, output_path):
    # Extraer los valores relevantes de 'data'
    molde_consecutivo = data.get('CONSECUTIVO', '').values[0] if 'CONSECUTIVO' in data else ''
    molde_sap = data.get('SAP', '').values[0] if 'SAP' in data else ''
    molde_producto = data.get('PRODUCTO', '').values[0] if 'PRODUCTO' in data else ''
    molde_uso = data.get('USO', '').values[0] if 'USO' in data else ''

    # Construir el encabezado
    header_text = f"Molde: {molde_consecutivo},{molde_sap}-{molde_producto}"

    # Determinar el estado
    estado_text = "Estado: "
    if molde_uso == 1:
        estado_text += "USO"
    elif molde_uso == 2:
        estado_text += "DESUSO"
    else:
        estado_text += "Desconocido"

    # Crear el nombre de archivo
    file_name = f"{molde_consecutivo}_{molde_sap}_{molde_producto}.pdf"
    # Agrega el nombre de archivo al path de salida
    output_path = os.path.join(output_path, file_name)

    # Crear un objeto SimpleDocTemplate para el PDF con la página en horizontal
    doc = SimpleDocTemplate(output_path, pagesize=landscape(letter))

    # Crear un objeto SimpleDocTemplate para el PDF con la página en horizontal
    doc = SimpleDocTemplate(output_path, pagesize=landscape(letter))

    # Establecer el estilo del párrafo para el encabezado y el cuerpo
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    body_style = styles["Normal"]

    # Crear contenido para el encabezado
    header_content = Paragraph(header_text, header_style)

    # Crear contenido para el cuerpo del documento
    body_content = []
    body_content.append(Paragraph("Información del documento:", body_style))
    for key, value in data.items():
        # Agregar solo el valor al contenido del cuerpo
        body_content.append(Paragraph(f"{key}: {value.values[0] if isinstance(value, pd.Series) else value}", body_style))

    # Agregar un pie de página
    footer_content = Paragraph("Pie de página - Información adicional", body_style)

    # Construir el contenido del PDF
    content = [header_content] + body_content + [Spacer(1, 0.2*inch), footer_content]

    # Determinar el estado para el rectángulo
    estado_color = colors.green if molde_uso == 1 else colors.red if molde_uso == 2 else colors.red

    # Crear el rectángulo
    estado_rect = Table([["Estado: USO" if molde_uso == 1 else "Estado: DESUSO" if molde_uso == 2 else "Estado: Desconocido"]], 
                        style=[
                            ('BACKGROUND', (0, 0), (0, 0), estado_color),
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
                        ])

    # Agregar el rectángulo al contenido
    content.insert(1, estado_rect)

    # Agregar el contenido al PDF
    doc.build(content)



# Ejemplo de uso
if __name__ == "__main__":
    data = {
        "Nombre": "Juan Pérez",
        "Edad": "30",
        "Correo electrónico": "juan@example.com"
    }
    output_path = "../pdf/output.pdf"
    generate_pdf(data, output_path)