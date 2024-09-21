def split_pdf(path):
    from PyPDF3 import PdfFileReader, PdfFileWriter

    pdf = PdfFileReader(open(path, 'rb'))

    for i, page in enumerate(pdf.pages):
        write = PdfFileWriter()
        write.addPage(page)
        with open(f'./generate_data/24_split_pdf{i+1}.pdf', 'wb') as out:
            write.write(out)

if __name__ == "__main__":
    split_pdf('./generate_data/23_merge_pdf_files.pdf')