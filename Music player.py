import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter as ttk


# window creation
root = Tk()
root.minsize(500, 100)
root.configure(background="salmon")

#List & Gloabl variables
listofsongs = []
track_no = 0
pause = False
stop = False


#File selection
def openfile():
    openfile = askdirectory()
    os.chdir(openfile)

    for songs in os.listdir(openfile):
        if songs.endswith(".mp3"):
            listofsongs.append(songs)
            listbox.insert(END, songs)

#Play & Unpause Music
def play_music():
    global track_no
    global pause
    
    if (pause == True):
        pygame.mixer.music.unpause()
        pause = False
        statusbar['text'] = "Music Playing"
    elif (stop == True):
        play_it = listofsongs[0]
        pygame.mixer.music.load(play_it)
        pygame.mixer.music.play()
        statusbar['text'] = "Music Playing"
    else:
        pygame.init()
        pygame.mixer.music.load(listofsongs[track_no])
        pygame.mixer.music.play()
        next_track()
        statusbar['text'] = "Music Playing"

#Next song
def next_track():
    global track_no
    track_no += 1
    pygame.mixer.music.load(listofsongs[track_no])
    pygame.mixer.music.play()

#Previous song
def previous_track():
    global track_no
    track_no -= 1
    pygame.mixer.music.load(listofsongs[track_no])
    pygame.mixer.music.play()
    

#Stop song
def stop():
    global stop
    global track_no
    track_no = 0
    stop = True
    pygame.mixer.music.stop()
    statusbar['text'] = "Music Stopped"
    
#Pause song
def pause():
    global pause
    pause = True
    pygame.mixer.music.pause()
    statusbar['text'] = "Music Paused"
    
#Volume
def control_volume(value):
    pygame.init()
    volume = int(value)/100
    pygame.mixer.music.set_volume(volume)
    
#On closing window
def closing_window():
    stop()
    root.destroy()


statusbar = ttk.Label(root, text="Welcome to JukeBox")
statusbar.pack(side=BOTTOM)

label = Label(root, text="PLAY LIST")
label.pack()
listbox = Listbox(root)
listbox.pack()
openfile1 = PhotoImage(file='folder.png')
button1 = Button(root, image=openfile1, command=openfile,bg='dark salmon')
button1.pack(side="top",padx=20,pady=20)
playphoto = PhotoImage(file='play.png')
button2 = Button(root,image=playphoto, command=play_music,bg='dark salmon')
button2.pack(side="left",padx=20,pady=20)
previousphoto = PhotoImage(file='previous_track.png')
button3 = Button(root,image=previousphoto, command=previous_track,bg='dark salmon')
button3.pack(side="left",padx=20,pady=20)
pausephoto = PhotoImage(file='pause.png')
button4 = Button(root,image=pausephoto, command=pause,bg='dark salmon')
button4.pack(side="left",padx=20,pady=20)
nextphoto = PhotoImage(file='next_track.png')
button5 = Button(root,image=nextphoto, command=next_track,bg='dark salmon')
button5.pack(side="left",padx=20,pady=20)
stopphoto = PhotoImage(file='stop.png')
button6 = Button(root,image=stopphoto, command=stop,bg='dark salmon')
button6.pack(side="left",padx=20,pady=20)

vol = Scale(root,from_ = 100,to = 0,orient = VERTICAL ,command=control_volume,bg='dark salmon')
vol.set(50)
pygame.init()
pygame.mixer.music.set_volume(0.5)
vol.pack()

root.protocol("WM_DELETE_WINDOW", closing_window)
root.mainloop()
