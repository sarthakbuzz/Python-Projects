#pip install pyttsx3
import pyttsx3
#take a variable and inistialized the pyttsx3
text_speech=pyttsx3.init()
#taking a input from the user
answer=input("Enter the text you want to convert into speech: ")
#say is function whice is help for convert a wriiten text to speech
text_speech.say(answer)
#runandwait function use for exit out from that program
text_speech.runAndWait()
