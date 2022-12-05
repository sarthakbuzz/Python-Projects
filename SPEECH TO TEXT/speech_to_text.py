#pip install Speech_Recognation
import speech_recognition as sr

#this will help to recognize our audio
r=sr.Recognizer()
#we are initialize our source to sr.microphone.
with sr.Microphone()as source:
    print("speak anything")#print a noraml command
    audio=r.listen(source)#it will listen to the audio and save into a text
    try:
        text=r.recognize_google(audio)#this will convert audio into text
        print("you said : {} ".format(text))
    except:
        print("sorry your voice could not recognize") #if your audio or voice will not clear then this will show   