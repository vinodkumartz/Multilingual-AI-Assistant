import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

def voice_input():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
        return None
    except sr.RequestError as e:
        print("Could not request result from Google Speech Recognition service: {0}".format(e))
        return None

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    # Save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

def llm_model_object(user_text):
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(user_text)
    
    result = response.text
    
    return result

def process_input(user_input):
    if user_input:
        response = llm_model_object(user_input)  # Get the model response
        text_to_speech(response)  # Convert response to speech
        
        return response
    else:
        return "Please provide valid input."

# Example usage (if this were part of a Streamlit app):
if __name__ == '__main__':
    print("Welcome to the Multilingual AI Assistant! Choose your input method.")
    
    input_method = input("Type '1' for Voice Input or '2' for Text Input: ")
    
    if input_method == '1':
        # Voice input method
        text = voice_input()
        response = process_input(text)
        print("Response:", response)
        
    elif input_method == '2':
        # Text input method
        user_input = input("Type your question: ")
        response = process_input(user_input)
        print("Response:", response)
        
    else:
        print("Invalid selection. Please choose 1 or 2.")
