# pip install pywin32
from win32com.client import gencache
from win32com.client import constants, gencache

def createPdf(wordPath, pdfPath):
    """
    word 转 pdf
    :pargm wordPath: word文件路径
    :pargm pdfPath: pdf保存路径
    """

    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly = 1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item = constants.wdExportDocumentWithMarkup,
                            CreateBookmarks = constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)

if __name__ == "__main__":
    # 路径必须是绝对路径而不能是相对路径
    createPdf('F:/python/base_data/traffic_violation_notice.docx', 'F:/python/generate_data/21_word2pdf.pdf')

