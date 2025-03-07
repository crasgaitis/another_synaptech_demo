import streamlit as st
import speech_recognition as sr
import time

import streamlit as st
import speech_recognition as sr
import time

# Function to continuously listen and recognize speech
def continuous_speech_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # To keep track of the recognized text
    recognized_text = ""

    with mic as source:
        st.info("Start speaking. Pauses longer than 3 seconds will update the text...")
        recognizer.adjust_for_ambient_noise(source)
        
        # Continuously listen for speech
        while True:

            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            text = recognizer.recognize_google(audio)

            # Update the recognized text and display
            recognized_text += " " + text
            st.text_area("Recognized Text", recognized_text, height=200)


            time.sleep(1)

# Streamlit UI
st.title("Real-Time Speech to Text with Pause Detection")

if st.button("Start Listening"):
    continuous_speech_to_text()

