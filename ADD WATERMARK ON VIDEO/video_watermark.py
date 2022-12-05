#Add a watermark on a video
#first you import the moviepy module
from moviepy.editor import*
#make a variable and use the VideoFileClip function and given the file which you want to edit
clip=VideoFileClip("Summerhigh.mp4").subclip(0,25)
#make another variable and add text , fontsize and text color.
text_clip=TextClip("AP DHILLON",fontsize=30,color="blue")
#set the position of the text using set_position function and set a duration of the watermark by using set_duration
text_clip=text_clip.set_position("top").set_duration(20)
#by using the CompositeVideoClip you merge the video file variable and text file variable.
video=CompositeVideoClip([clip,text_clip])
#at last you give the new file name to save the watermark text video
video.write_videofile("apdhillon.mp4")