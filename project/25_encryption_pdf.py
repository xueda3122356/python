def encrypt(path, password):
    from PyPDF3 import PdfFileReader, PdfFileWriter

    pdf = PdfFileReader(open(path, 'rb'))
    write = PdfFileWriter()

    write.encrypt(password)

    for page in pdf.pages:
        write.addPage(page)
    
    with open('./generate_data/25_encryption_pdf.pdf', 'wb') as target:
        write.write(target)
    
if __name__ == "__main__":
    encrypt('./generate_data/23_merge_pdf_files.pdf', '123456')