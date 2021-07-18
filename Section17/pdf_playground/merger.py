import PyPDF2
import sys


inputs = sys.argv[1:]


def merge_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('./output_pdf/merge.pdf')


merge_pdf(inputs)
