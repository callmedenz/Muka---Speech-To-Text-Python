# 🎤 Speech-to-Text Automation  

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)  

A **speech-to-text application** that combines **Python, Selenium, and Web Speech API**.  
It listens to your voice, displays it live in the browser, and saves the recognized text into `input.txt`.  

---

## ✨ Features
✅ Live speech recognition in the browser  
✅ Automates Chrome using Selenium  
✅ Saves recognized speech into a file (`input.txt`)  
✅ Simple & clean **dark mode UI**  
✅ Easily extendable for chatbots, automation, or AI projects  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Install Python  
- Make sure you have **Python 3.8+** installed.  
- You can check with:
  ```bash
  python --version
  ```

### 3️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Mac/Linux
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

⚠️ If you face issues with **PyAudio** on Windows:  
```bash
pip install pipwin
pipwin install pyaudio
```

### 5️⃣ Run the App
```bash
python speech_to_text.py
```

This will:
- Launch **Chrome**  
- Open `index.html`  
- Click "Start Listening" automatically  
- Show recognized speech on the webpage  
- Save it into `input.txt`  

---

## 🛠️ Requirements
- Python 3.8 or higher  
- Google Chrome installed  
- Dependencies (see `requirements.txt`):  
  ```
  SpeechRecognition
  pyaudio
  selenium
  webdriver-manager
  colorama
  ```._  

---

## 🤝 Contributing
Contributions are welcome! 🎉  
- Fork the repo  
- Create a new branch (`feature-xyz`)  
- Commit your changes  
- Submit a Pull Request  

---

## 📜 License
This project is for **learning purposes**.  
Feel free to modify and use it as you like.
