import csv
import PypDF2
import re

def csvFile():
    #open the file
    data = open('example.csv',encoding = 'utf-8')

    #csv.reader
    csv_data = csv.reader(data)

    #reformat it into a python object list of lists
    data_lines = list(csv_data)

    allemails = []
    for line in data_lines:
        allemails.append(line[3])           #all emails

    file2output = open('to_save_file.csv',mode='w', newline='')
    csv_writer = csv.writer(file2output,delimiter = ',')

    csv_writer.writerow(['a','b','c'])

    file2output.close()

def pdf():
    f = open('Working_Business_Proposal.pdf','rb')

    #read from a file
    pdf_reader = PypDF2.PdfFileReader(f)
    page_one = pdf_reader.getPage(0) # get a page 1, we can make a loop to read through pages

    page_one_text = page_one.extractText()

    #add to a PDF file
    pdf_writer = PypDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)

    pdf_output = open('Some_BrandNew_Doc.pdf','wb')
    pdf_writer.write(pdf_output)

    f.close()
    pdf_output.close()


def exercisePuzzle():
    data = open('Exercise_Files/find_the_link.csv',encoding='utf=8')
    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    link_Str = ''

    for row_num, data in enumerate(data_lines):
        link_Str += data[row_num]

    f = open('Exercise_Files/find_the_link.csv','rb')
    pdf = PypDF2.PdfFileReader(f)

    pattern = r'\d{3}.d{4}.d{4}'

    all_text = ''

    for n in range(pdf.numPages):
        page = pdf.getPage(n)
        page_text = page.extractText()

        all_text = all_text + ' ' + page_text

    for match in re.finditer(pattern,all_text):
        print(match)


if __name__ == '__main__':
    csvFile()
    pdf()
    exercisePuzzle()
    print('PyCharm')
