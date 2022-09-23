from PyPDF2 import PdfReader
import sys
from google.cloud import texttospeech


"""Free google speech to text is limited to 5000 characters"""


def main():
    # Passing pdf file as an argument variable
    pdf = sys.argv[1]
    reader = PdfReader(pdf)

    number_of_pages = len(reader.pages)

    text = ""

    # Add all text to text variable in every page
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()

    """Synthesizes speech from the input string of text or ssml.
    Make sure to be working in a virtual environment.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Split name from the '.' and get first item from the list
    audio_book = pdf.split(".")[0]

    # If there the file is on a different location split it with forward slash
    audio_book_name = audio_book.split("/")

    if audio_book_name != "":
        audio_book_name = audio_book_name[-1]
    # If the file is in the same directory
    else:
        audio_book_name = audio_book

    # The response's audio_content is binary.
    with open(f"{audio_book_name}.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{audio_book_name}.mp3"')


main()
