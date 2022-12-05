from tkinter import*
from tkinter import filedialog
from moviepy import*
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

#allow user to select a path from your explorer
def select_path():
    path=filedialog.askdirectory()
    path_lable.config(text=path)
    
#downloaded function
def download_file():
    get_link= link_filed.get()
    user_path=path_lable.cget("text")
    screen.title("Downloading...")
    mp4_video=YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video,user_path)
    screen.title("Download completed!")
    
screen=Tk()
title=screen.title("Youtube Downloader")
bg_color="#074463"
canvas=Canvas(screen,width=500,height=500,bg=bg_color)
canvas.pack()

#image logo
logo_img=PhotoImage(file="YouTube_logo_png.png")
#image resize
logo_img=logo_img.subsample(2,2)
canvas.create_image(250,80, image=logo_img)



#select path for saving the file 
path_lable=Label(screen,text="Select Path for Download",font="Arial,15")
select_btn=Button(screen,text="Select",command=select_path)

#link field
link_filed=Entry(screen,width=50)
link_lable=Label(screen,text="Enter Download Link: ",font="Arial,15",padx=80,pady=2)


#add to widgets to window
canvas.create_window(250,260,window=path_lable)
canvas.create_window(250,300,window=select_btn)
#add widgets to window
canvas.create_window(250,220,window=link_lable)
canvas.create_window(250,180,window=link_filed)
#button for download
down_btn=Button(screen,text="Download File",command=download_file)
canvas.create_window(250,350,window=down_btn)









screen.mainloop()