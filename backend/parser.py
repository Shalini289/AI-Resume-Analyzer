from pypdf import PdfReader

def extract_text(pdf_file):
    """
    Extract text from uploaded PDF resume.
    """

    try:
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error extracting PDF: {str(e)}"
