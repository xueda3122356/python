def merge_pdf(path1, path2):
    from PyPDF3 import PdfFileReader, PdfFileWriter
    write = PdfFileWriter()
    for path in [path1, path2]:
        temp_pdf = PdfFileReader(open(path, 'rb'))
        for page in temp_pdf.pages:
            write.addPage(page)
        
    with open('./generate_data/23_merge_pdf_files.pdf', 'wb') as out:
        write.write(out)

if __name__ == "__main__":
    merge_pdf('./generate_data/21_word2pdf.pdf', './generate_data/21_word2pdf.pdf')