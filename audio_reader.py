import pyttsx3
import PyPDF2

with open('Shortstory.pdf',"rb") as book:
    reader = PyPDF2.PdfReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate",100)

    for page in range(len(reader.pages)):
        next_page = reader.pages[page]
        content = next_page.extract_text()

        audio_reader.save_to_file(content,"myaudiobook.mp3")
        audio_reader.runAndWait()
        
        
