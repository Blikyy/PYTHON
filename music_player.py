from tkinter import *
from tkinter import filedialog
import tkinter as tk
import pygame
from pygame import mixer


music_player = Tk()
  
music_player.geometry('450x350')
music_player.title('Music player') 
music_player.resizable(0,0)
music_player.configure(bg="gray")

song_path_list = []
song_list = Listbox(music_player, bg="black", fg="white", width=60)
song_list.pack(pady=20)

pygame.mixer.init()

def load_song():

    load = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
    song_path_list.append(load)
    load = load[load.rfind('/') + 1:].replace(".mp3", "")
    song_list.insert(END, load)

def load_songs():

    load = filedialog.askopenfilenames(filetypes=(("mp3 Files", "*.mp3"), ))

    for loads in load:
        song_path_list.append(loads)
        loads = loads[loads.rfind('/') + 1:].replace(".mp3", "")
        song_list.insert(END, loads) 

def play_song():

    song = song_list.get(ACTIVE)

    for i in range(len(song_path_list)):
        _song = song_path_list[i]
        if song in _song:
            song = _song

    if (loop_var.get() == TRUE & loop_var.get() != FALSE):

        mixer.music.load(song)
        mixer.music.play(loops=999999)

    else:
        
        mixer.music.load(song)
        mixer.music.play(loops=0)

pause_status = False

def pause_song():

    global pause_status

    if pause_status:
        mixer.music.unpause()
        pause_status = False
    else:
        mixer.music.pause()
        pause_status = True
    
def stop_song():

    mixer.music.stop()

def song_volume(_NONE):

    mixer.music.set_volume(volume.get())

loop_var = tk.BooleanVar()

play_button = Button(music_player, text = 'Play',  width = 10,font = ('Halvetica', 10), command= play_song)
pause_button = Button(music_player,text = 'Pause',  width = 10, font = ('Halvetica', 10), command= pause_song)
stop_button = Button(music_player,text = 'Stop',  width = 10, font = ('Halvetica', 10), command= stop_song)
volume = Scale(music_player, from_=0, to=1, orient=HORIZONTAL, resolution= .01,length= 300,command=song_volume)
check_button = Checkbutton(music_player, text="LOOP",font=('Verdana', 10),variable= loop_var ,onvalue= TRUE,offvalue= False ,relief= tk.GROOVE)
check_button.pack()

play_button.place(x=80,y=200)
pause_button.place(x=175,y=200)
stop_button.place(x=270,y=200) 
volume.place(x=80, y=300)
check_button.place(x=185,y=250)

song_menu = Menu(music_player)
music_player.config(menu=song_menu)

add_song = Menu(song_menu)
song_menu.add_cascade(label="add song", menu= add_song)
add_song.add_command(label="add song to play", command= load_song)
add_song.add_command(label="add more then one song to play", command= load_songs)

music_player.mainloop()
