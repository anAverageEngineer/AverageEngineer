import sounddevice as sd
import numpy as np
import keyboard
from tkinter import *
from PIL import Image, ImageTk
import random

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("500x500")
win.title("AverageEngineer")
def getRand():
   u = random.randint(0, 100)
   if u < 88:
      return 0
   else:
      return random.randint(-1, 1)

def change_img_normal():
   y = getRand()
   Original_Image = Image.open("normal.png")
   rotated_image1 = Original_Image.rotate(y)
   img2=ImageTk.PhotoImage(rotated_image1)
   label.configure(image=img2)
   label.image=img2


def change_img_quiet():
   img1=ImageTk.PhotoImage(Image.open("quiet.png"))
   label.configure(image=img1)
   label.image=img1


img1= ImageTk.PhotoImage(Image.open("quiet.png"))

#Create a Label widget
label= Label(win,image= img1)
label.pack()


def set_image(volu):
    print(volu)
    if volu < 500:
        print("Quiet")
        change_img_quiet()

    elif volu >= 500 & volu < 3000:
        print("Normal")
        change_img_normal()
    else:
        print("Loud")
        #img = Image.open("test.png")

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*550
    x = int(volume_norm)
    set_image(x)
    #print (x)



def main():
        with sd.Stream(callback=print_sound):
                win.mainloop()
                sd.sleep(100000)
        #win.mainloop()


main()
