from fpdf import FPDF

def generate_report(
    filename,
    content
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.multi_cell(
        0,
        10,
        content
    )

    pdf.output(filename)

    return filename
