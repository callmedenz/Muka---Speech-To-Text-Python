# pip install SpeechRecognition
# pip install pyaudio
#pip install selenium
#pip install webdriver-manager

import speech_recognition as sr                                         # Library for speech_to_text
import os                        
import threading                                                        # For running multiple tasks together
from colorama import Fore, Style, init                                  # For colored console text
from selenium import webdriver                                          #Use for automation of the website
from selenium.webdriver.common.by import By                             #To get the id
from selenium.webdriver.support.ui import WebDriverWait                 #Will wait untill the element is loaded
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd                                                   #To find the file which we are going to automate

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")           #To bypass the permission of mic
#chrome_options.add_argument("--headless=new")                           #To open website on background not in front

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)      #To install all Chromedriver automatically which we did manually and set own path

website = f"file:///{getcwd()}\\index.html"
driver.get(website)


rec_file = f"{getcwd()}\\input.txt"

def listen():
    try:
        start_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'start')))
        start_button.click()
        print("Listening....")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Listening...." in start_button.text:
                is_second_click = False
                if current_text != output_text:
                    output_text = current_text
                    with open(rec_file,"w") as file:
                        file.write(output_text.lower())
                        print("USER : " + output_text)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
listen()

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
