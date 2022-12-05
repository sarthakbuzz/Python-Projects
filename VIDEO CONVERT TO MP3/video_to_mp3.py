import moviepy.editor

video=moviepy.editor.VideoFileClip("Summerhigh.mp4")

audio=video.audio

audio.write_audiofile("summerhigh.mp3")
