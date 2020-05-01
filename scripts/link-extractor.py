import PyPDF2
import re
pdfFileObj = open('./Springer-Ebooks.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pattern = re.compile('http://link.springer.com/openurl\?genre=book\&isbn=\w+-\w+-\w+-\w+-\w+')

links = []

i = 0
while i < pdfReader.numPages:
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extractText()
    links.extend(re.findall(pattern,pageText))
    i += 1

linksFile = open('./files/links.txt','w')

for link in links:
    linksFile.write(link+'\n')