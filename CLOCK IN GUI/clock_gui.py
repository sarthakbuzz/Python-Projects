import tkinter
from time import strftime
def clock():
    time1=strftime("%H : %M : %S %p")
    bg_color="#074463" 
    lable.config(text=time1,font="arial 120 bold",bg=bg_color)
    lable.after(1000,clock)

root=tkinter.Tk()
lable=tkinter.Label(root)
root.title("Time")
lable.pack()
clock()

root.mainloop()