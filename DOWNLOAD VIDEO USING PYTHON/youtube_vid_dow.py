from pytube import YouTube

link= "https://www.youtube.com/watch?v=JtPbk7WvHAQ"

youtube=YouTube(link)

#print(youtube.title)#only for video title
#print(youtube.thumbnail_url)#only for thumbnail

videos=youtube.streams.all()#for video all format
#videos=youtube.streams.filter(only_audio=True)#only for audio
vid=list(enumerate(videos))

for i in vid:
    print(i)

strm=int(input("Enter: "))
videos[strm].download()
print("Video Downloaded Sucessfully")

