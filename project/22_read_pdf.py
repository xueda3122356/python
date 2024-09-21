def read_pdf1(path):
    # pip install pypdf2, pypdf3
    from PyPDF3 import PdfFileReader

    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number = pdf.getNumPages()
        for i in range(number):
            print(pdf.getPage(i).extractText())
    
    print(info)
    print(number)

def read_pdf2(path):
    # pip install pdfplumber
    import pdfplumber

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            print(page.extract_text())

if __name__ == "__main__":
    #read_pdf1('./generate_data/21_word2pdf.pdf')
    read_pdf2('./generate_data/21_word2pdf.pdf')