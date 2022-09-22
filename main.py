from PyPDF2 import PdfReader
import sys


def main():
    # pdf = sys.argv[1]
    reader = PdfReader("sample.pdf")
    number_of_pages = len(reader.pages)

    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        print(page.extract_text())


main()
