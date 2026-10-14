# 3. Install an external module and use it to perform an operation of your interest. 

import pyttsx3  # ye bolta hain

engine = pyttsx3.init()
engine.say("i will speak this text")
engine.runAndWait()