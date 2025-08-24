let startBtn = document.getElementById("start");
let outputDiv = document.getElementById("output");

let recognition;
let isListening = false;

if ("webkitSpeechRecognition" in window) {
  recognition = new webkitSpeechRecognition();
} else if ("SpeechRecognition" in window) {
  recognition = new SpeechRecognition();
} else {
  alert("Speech Recognition not supported in this browser.");
}

if (recognition) {
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = "en-US";

  recognition.onstart = () => {
    startBtn.innerText = "Listening....";
    isListening = true;
  };

  recognition.onend = () => {
    startBtn.innerText = "Start Listening";
    isListening = false;
  };

  recognition.onresult = (event) => {
  let transcript = "";
  for (let i = event.resultIndex; i < event.results.length; i++) {
    transcript += event.results[i][0].transcript;
    if (event.results[i].isFinal) {
      outputDiv.innerText = transcript.trim();
    }
  }
};


  startBtn.addEventListener("click", () => {
    if (isListening) {
      recognition.stop();
    } else {
      recognition.start();
    }
  });
}
