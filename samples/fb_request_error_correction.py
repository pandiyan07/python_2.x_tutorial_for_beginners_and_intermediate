from Tkinter import *

master = Tk()
whatever_you_do = "AJ"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )

import os
import pyaudio
import speech_recognition as sr
doss = os.getcwd()
i=0
n=0
while (i<1):
	r = sr.Recognizer()

with sr.Microphone() as source:
	audio = r.adjust_for_ambient_noise(source)
	n=(n+1) 
	print("Say something!")
	audio = r.listen(source)

# interprete audio (Google Speech Recognition)

try:
	s = (r.recognize_google(audio))
	message = (s.lower())
	print (message)
except sr.UnknownValueError:
	print("$could not understand audio")
except sr.RequestError as e:
	print("Could not request results$; {0}".format(e))

mainloop( )





"""


import os
import pyaudio
import speech_recognition as sr
doss = os.getcwd()
i=0
n=0
while (i<1):
	r = sr.Recognizer()
	with sr.Microphone() as source:
	audio = r.adjust_for_ambient_noise(source)
	n=(n+1) 
	print("Say something!")
	audio = r.listen(source)

# interprete audio (Google Speech Recognition)
try:
	s = (r.recognize_google(audio))
	message = (s.lower())
	print (message)
except sr.UnknownValueError:
	print("$could not understand audio")
	except sr.RequestError as e:
	print("Could not request results$; {0}".format(e))
"""
