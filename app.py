import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    st.title("Multilingual AI Assistant ")

    # Option for selecting input type
    input_method = st.radio("Choose input method:", ("Voice Input", "Text Input"))

    if input_method == "Voice Input":
        if st.button("Ask me anything"):
            with st.spinner("Listening..."):
                text = voice_input()  # Call the voice input function
                response = llm_model_object(text)  # Get the model response
                text_to_speech(response)  # Convert response to speech

                # Read the audio file
                audio_file = open("speech.mp3", "rb")
                audio_bytes = audio_file.read()

                # Display response and audio
                st.text_area(label="Response:", value=response, height=350)
                st.audio(audio_bytes)
                st.download_button(label="Download Speech",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")

    elif input_method == "Text Input":
        user_input = st.text_input("Type your question:")
        if st.button("Submit"):
            if user_input:
                response = llm_model_object(user_input)  # Get the model response
                text_to_speech(response)  # Convert response to speech

                # Read the audio file
                audio_file = open("speech.mp3", "rb")
                audio_bytes = audio_file.read()

                # Display response and audio
                st.text_area(label="Response:", value=response, height=350)
                st.audio(audio_bytes)
                st.download_button(label="Download Speech",
                                   data=audio_bytes,
                                   file_name="speech.mp3",
                                   mime="audio/mp3")
            else:
                st.warning("Please enter a question.")

if __name__ == '__main__':
    main()
