import os
import tkinter
from tkinter.constants import FLAT
from pygame.mixer import music
from pygame import mixer
from tkinter import Label, messagebox, PhotoImage, StringVar, filedialog, ttk, Tk
import re

#---------------------------- Class Queue ------------------------------#
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def search(self, data):
        current = self.head
        while current:
            if self.head:
                if self.head.next:
                    search = re.search(f"{data}$", current.data)
                    if search:
                        return current.data
                    else:
                        current = current.next
                else:
                    current.data
            else:
                return "♦ Not Exist Any Node For Delete ! ♦"

#------------------------------ Opertion Section ------------------------------#
def Start():
    b1['text'] = 'Browse...'
    b1['command'] = Operation


def check(ls):
    tmp_ls = []
    for i in range(len(ls)):
        test_file = re.search('.mp3$', ls[i])
        if test_file:
            tmp_ls.append(ls[i])
        else:
            continue
    return tmp_ls


def Exit():
    answer = messagebox.askyesno("Warning", 'Are You Sure ?')
    if answer:
        win.destroy()


def Operation():
    def play():
        q = Queue()
        mixer.init()
        b3['state'] = 'enable'
        b6['state'] = 'enable'
        for i in range(len(add_music)):
            add = add_music[i]
            test_file = re.search('.mp3$', add)
            if test_file:
                q.enqueue("{0}\\{1}".format(dir, add))
            else:
                continue
        data = drop['text']
        add_full = q.search(data)
        music.load(add_full)
        music.play()
        print(f"{data} is Playing !")

    def pause():
        music.pause()
        b4.destroy()
        b5 = ttk.Button(win, text='⏯', command=resume, width=5, padding=10)
        b5.pack()
        b5.place(x=220, y=115)

    def resume():
        music.unpause()
        b5.destroy()
        b4 = ttk.Button(win, text='▶', command=play, width=5, padding=10)
        b4.pack()
        b4.place(x=220, y=115)

    def stop():
        music.stop()
        b3['state'] = 'disabled'
        b6['state'] = 'disabled'
        b5.destroy()
        b4 = ttk.Button(win, text='▶', command=play, width=5, padding=10)
        b4.pack()
        b4.place(x=220, y=115)

    dir = filedialog.askdirectory()
    add_music = os.listdir(dir)
    add_music = check(add_music)
    default_text = StringVar()  # for set default text
    default_text.set(add_music[0])
    drop = ttk.OptionMenu(win, default_text,*add_music)
    drop.pack()
    drop.place(x=0, y=0)
    b1.destroy()
    b3 = ttk.Button(win, text='||', command=pause, width=5, padding=10)
    b3['state'] = 'disabled'
    b4 = ttk.Button(win, text='▶', command=play, width=5, padding=10)
    b5 = ttk.Button(win, text='⏯', command=resume, width=5, padding=10)
    b6 = ttk.Button(win, text='■', command=stop, width=5, padding=10)
    b6['state'] = 'disabled'
    b3.pack()
    b4.pack()
    b6.pack()
    b3.place(x=140, y=115)
    b4.place(x=220, y=115)
    b6.place(x=300, y=115)


#------------------ Make Window Section ------------------#
win = Tk()

img1 = PhotoImage(
    file="G:\\Project\\Python_Project\\py test\\music.png")
win.iconphoto(False, img1)
win.geometry("500x333")
win.title('MUSIC PLAYER')
win.config(background="white")

img2 = PhotoImage(
    file="G:\\Project\\Python_Project\\py test\\jun.png")
lab = Label(win, image=img2)  # set background
lab.place(x=-2, y=-2)
b1 = tkinter.Button(win, text='START', command=Start, width=20)
b2 = ttk.Button(win, text='Exit', command=Exit, width=20)
b1.pack()
b2.pack()
b1.place(x=185, y=135)
b2.place(x=185, y=165)
win.mainloop()
