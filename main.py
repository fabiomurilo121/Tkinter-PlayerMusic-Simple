import os
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from pygame import mixer

class Player:

    def __init__(self, root):
        root.geometry("400x200");root.iconbitmap(r"img/boombox.ico");root.title("TkinPlayer")
        # Creating a photoimage object to use image
        play = PhotoImage(file=r"img/play-button.png")
        pause = PhotoImage(file=r"img/pause.png")
        help = PhotoImage(file=r"img/about.png")
        exit = PhotoImage(file=r"img/shutdown.png")
        load = PhotoImage(file=r"img/folder.png")

        # Redimensionamento da imagem para caber no botão
        self.playImg = play.subsample(4, 4)
        self.pauseImg = pause.subsample(4, 4)
        self.loadImg = load.subsample(4, 4)
        self.helpImg = help.subsample(7, 7)
        self.exitImg = exit.subsample(7, 7)


    # ///////////////////////////////////////////////////////////////////////////////
    # ////////////////////////////////// Interface //////////////////////////////////
    # ///////////////////////////////////////////////////////////////////////////////

        Label(root, text='Player de Música Simples', font=('Verdana', 15)).place(x=63, y=0)

        Play = Button(root, image=self.playImg, compound=CENTER, command=self.play).place(x=80, y=30)
        Pause = Button(root, image=self.pauseImg, compound=CENTER, command=self.pause).place(x=160, y=30)
        Load = Button(root, image=self.loadImg, compound=CENTER, command=self.load).place(x=240, y=30)

        Help = Button(root, image=self.helpImg, command=self.about_us).place(x=60, y=165)
        Exit = Button(root, image=self.exitImg, command=root.destroy).place(x=30, y=165)


        #Label(root, text=texto, font=('Verdana', 11)).place(x=180, y=170)

    #///////////////////////////////////////////////////////////////////////////////
    #////////////////////////////////// Functions //////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        texto = (self.music_file)

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            print("aqui")
            mixer.music.unpause()
            self.playing_state = False

    def about_us(self):
        tkinter.messagebox.showinfo('Sobre Tkinter Music',
                                    'Esse player de música foi feito usando Python Tkinter')

root = Tk()
app = Player(root)
root.mainloop()

