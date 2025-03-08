import speech_recognition as sr
from PIL import Image
import requests
from io import BytesIO

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to capture voice input
def capture_voice_input():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        print("Recognizing...")
        try:
            # Convert voice to text
            text = recognizer.recognize_google(audio)
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Request failed; check your network.")
            return None

# Function to generate image from text using an image API (e.g., DALL·E, Unsplash)
def generate_image_from_text(text):
    # Example API to search for images (Replace with your chosen API)
    url = f"https://api.unsplash.com/photos/random?query={text}&client_id=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"
    response = requests.get(url)
    if response.status_code == 200:
        image_url = response.json()[0]["urls"]["regular"]
        img_response = requests.get(image_url)
        img = Image.open(BytesIO(img_response.content))
        img.show()
    else:
        print("Could not generate image.")

# Main program logic
if __name__ == "__main__":
    text_input = capture_voice_input()
    if text_input:
        generate_image_from_text(text_input)
