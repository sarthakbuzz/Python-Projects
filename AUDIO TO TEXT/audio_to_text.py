import speech_recognition as sr


#this will help to recognize our audio
r=sr.Recognizer()

audio_file=sr.AudioFile("Goosebumps.wav")#folder and the name of the audio..

with audio_file as source:
    r.adjust_for_ambient_noise(source)#remove the noise from this audio file..
    audio=r.record(source)
    
result=r.recognize_google(audio)#this is stored in google recognize...

#convertion into a text file using this command..
with open("test.txt",mode="w") as file :
    file.write("recognize text:")
    file.write("\n")
    file.write(result)
    print("conversion done!")