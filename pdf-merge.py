import PyPDF2
pdffiles=["1.pdf","2.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdffiles:
    pdffile=open(filename,'rb')
    pdfreader=PyPDF2.PdfReader(pdffile)
    merger.append(pdfreader)
pdffile.close()
merger.write('merged.pdf')