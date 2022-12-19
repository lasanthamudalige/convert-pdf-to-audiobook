import PyPDF2
from gtts import gTTS
import sys


def main():
    try:
        # Passing pdf file as an argument variable
        pdf = sys.argv[1]

        try:
            reader = PyPDF2.PdfReader(pdf)

            number_of_pages = len(reader.pages)

            text = ""

            # Add all text to text variable in every page
            for page_number in range(number_of_pages):
                page = reader.pages[page_number]
                text += page.extract_text()

            # Language in which you want to convert
            language = 'en'

            # Passing the text and language to the engine,
            # here we have marked slow=False. Which tells
            # the module that the converted audio should
            # have a high speed
            audio_object = gTTS(text=text, lang=language, slow=False)

            # Saving the converted audio in a mp3 file with the file name
            pdf_name = pdf.split(".")[0]

            audio_object.save(f"{pdf_name}.mp3")

            # Show the complete message
            print(f"{pdf_name}.mp3 saved successfully")

        except PyPDF2.errors.PdfReadError:
            print("Invalid file type")

    except IndexError:
        print("Pdf file not found")


main()
