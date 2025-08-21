# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr   # Library for speech_to_text
import os                        
import threading                 # For running multiple tasks together
from colorama import Fore, Style, init   # For colored console text

init(autoreset=True)

def print_loop():
    while True:
        
        print(Fore.GREEN + "I am Listening..", end="\r", flush=True)


def Speech_To_Text():
    recognizer = sr.Recognizer()   


    recognizer.dynamic_energy_threshold = False  
    recognizer.energy_threshold = 3400           
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.5             
    recognizer.non_speaking_duration = 0.3       

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  

        while True:
            try:
                
                print(Fore.GREEN + "Listening...", end="\r", flush=True)

                
                audio = recognizer.listen(source, timeout=None)

        
                print(Fore.CYAN + "Recognizing...", end="\r", flush=True)

                
                text = recognizer.recognize_google(audio).lower()

        
                os.system("cls" if os.name == "nt" else "clear")

        
                print(Fore.YELLOW + f"You said: {text}")

            except sr.UnknownValueError:
            
                print(Fore.RED + "Could not understand audio")
            except sr.RequestError as e:
            
                print(Fore.RED + f"API error: {e}")


if __name__ == "__main__":

    stt_thread = threading.Thread(target=Speech_To_Text)

    print_thread = threading.Thread(target=print_loop, daemon=True)

    stt_thread.start()
    print_thread.start()

    stt_thread.join()
