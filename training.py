from gtts import gTTS
import random
from tkinter import *
import tkinter as tk
from playsound import playsound
import time

import gtts
master = Tk()
master.title('Word Generator Software')
master.geometry("350x100")


# UNTUK MEN GENERATE DATA DARI LIST ARRAY MENJADI STRING
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        
# UNTUK MEMBUKA FILE DATA KATA2 
filenya = open('datanya.txt',"r")
kata = filenya.read().splitlines()

# UNTUK PROSES MEMAINKAN SOUND NYA
def unt():
    playsound('ashockle.mp3')
    
# UNTUK PROSES MENGAMBIL INPUT DATA DARI TKINTER LALU DIJADIKAN PARAMETER UNTUK PENGOLAHAN DATA
def aing():
    y = E1.get("1.0",'end-1c')
    # print(y.isnumeric())
    m = y.isnumeric()

    if m :
        e = int(y)    
        # print(e)
    else:
        print('bilangan bukan angka')
        return

    r = random.sample(kata, e)
    k = listToString(r)
    # print(k)
    tts = gTTS(k,lang='id')
    tts.save('ashockle.mp3')
    time.sleep(1)
    playsound('ashockle.mp3')
    B = Button(master,text="Play Again",command=unt)
    B.place(x=200,y=10)


# FUNGSI TOMBOL PADA MODULE TKINTER
B = Button(master,text="Generate",command=aing)
B.place(x=20,y=40)

E1 = Text(master, height = 1,width =5)
E1.place(x=130,y=10)
mylabeB=tk.Label(master,text="Amount of words")
mylabeB.place(x=20,y=10)


# MAIN LOOPNYA
master.mainloop()
