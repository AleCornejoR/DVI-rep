from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data, output_path):
    # Crear un objeto SimpleDocTemplate para el PDF
    doc = SimpleDocTemplate(output_path, pagesize=letter)

    # Establecer el estilo del párrafo para el encabezado y el cuerpo
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    body_style = styles["Normal"]

    # Crear contenido para el encabezado
    header_content = Paragraph("Encabezado del Documento", header_style)

    # Crear contenido para el cuerpo del documento
    body_content = []
    body_content.append(Paragraph("Información del documento:", body_style))
    for key, value in data.items():
        body_content.append(Paragraph(f"{key}: {value}", body_style))

    # Agregar un pie de página
    footer_content = Paragraph("Pie de página - Información adicional", body_style)

    # Construir el contenido del PDF
    content = [header_content] + body_content + [Spacer(1, 0.2*inch), footer_content]

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