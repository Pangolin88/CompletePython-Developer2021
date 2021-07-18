import PyPDF2


# my solution
with open('./pdf/twopage.pdf', 'rb') as file, open('./pdf/wtr.pdf', 'rb') as watermark_file:
    reader = PyPDF2.PdfFileReader(file)
    watermark_reader = PyPDF2.PdfFileReader(watermark_file)
    writer = PyPDF2.PdfFileWriter()

    for i in range(reader.numPages):
        page = reader.getPage(i)
        page.mergePage(watermark_reader.getPage(0))
        writer.addPage(page)

    with open('./output_pdf/watermark.pdf', 'wb') as new_file:
        writer.write(new_file)


# teacher's solution
template = PyPDF2.PdfFileReader(open('./pdf/twopage.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./pdf/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('./output_pdf/watermark.pdf', 'wb') as file:
        output.write(file)
