from tkinter import * 
from pygame import *
from random import*
from os import*

#mixer launcher
mixer.init()


#playlist
directory = 'C:/Users/vitor/OneDrive/Desktop/MY_Projets/projets_for_git/player_de_music/musics/'
ways = [path.join(directory, nome) for nome in listdir(directory)]
files = [arq for arq in ways if path.isfile(arq)]
playlist = [arq for arq in files if arq.lower().endswith(".mp3")]

#generate an idex for a random song
def index_generator():
    return randrange(0,len(playlist))

#divides the name of the song and the band and prints them on the screen
def print_music_and_band_on_screen(music):
    divider = music.find('musics/')
    name_of_music_and_band = music[divider + 7 :]

    end = name_of_music_and_band.find('.mp3')
    middle = name_of_music_and_band.find('_')
    
    band = name_of_music_and_band[:middle]
    just_music = name_of_music_and_band[middle+1:end].title()
    
    band_name.config(text=band)
    music_name.config(text=just_music.replace('-',' '))

#initialize the music
def initialize_the_music(music):
    #path and music initialization
    directory = music
    mixer.music.load(directory)
    mixer.music.play(loops=0)
   
    #music volume
    mixer.music.set_volume(0.5)
    print_volume()


#play button function      
def play():
    global restart
    restart = 0

    global paused
    paused = False

    global index_music 
    index_music = index_generator()

    global previos_song
    previos_song = index_music 

    music = playlist[index_music]
    print_music_and_band_on_screen(music)
    initialize_the_music(music)


#next music button function
def next_music():
    global restart
    restart = 0

    global paused
    paused = False

    index =  index_generator()
    if index == index_music:
        while index == index_music:
            index = index_generator()

        #music volume
        mixer.music.set_volume(0.5)

    elif index != index_music: 
        #music volume
        mixer.music.set_volume(0.5)

        music = playlist[index]
        print_music_and_band_on_screen(music)
        initialize_the_music(music)
        
paused = False
#pause and unpause button function
def pause(is_paused):
    global restart
    restart = 0

    global paused 
    paused = is_paused

    if (paused == True):
        #unpause
        mixer.music.unpause()
        paused = False

    elif(paused == False):
        #pause
        mixer.music.pause()
        paused = True
        
#back music button function      
def back_music():
    global restart
    if restart == 0:
        mixer.music.rewind()
        mixer.music.set_volume(0.5)
        restart += 1

    elif restart == 1 :
        #music volume
        mixer.music.set_volume(0.5)

        musica = playlist[previos_song]
        print_music_and_band_on_screen(musica)
        initialize_the_music(musica)
        restart = 0

def get_volume():
    return mixer.music.get_volume()

def decrease_the_volume():
    mixer.music.set_volume(get_volume() - 0.1)
    print_volume()

def turn_up_the_volume():
    mixer.music.set_volume(get_volume() + 0.1)
    print_volume()
    
        
def print_volume():
    global volume
    volume = round(get_volume()*10)
    volume_space.config(text=volume)

#graphic interface 
#create application window
root  = Tk()
root.title('Player De Musica')
root.geometry('355x350')

#create the buttons
band_name = Label(root,text='***********')
music_name = Label(root,text='***********')
volume_space = Label(root,text='5')
button_play    = Button(root, text='Play', command= play, padx=20, pady=10)
button_pause   = Button(root, text='pause', command= lambda: pause(paused), padx=20, pady=10)
button_back_music    = Button(root, text='back', command= back_music, padx=20, pady=10)
button_next_music = Button(root, text='next', command= next_music, padx=20, pady=10)
button_decrease_the_volume = Button(root,text='-',command=decrease_the_volume, padx=20, pady=10)
button_turn_up_the_volume = Button(root,text='+',command=turn_up_the_volume,padx=20, pady=10)

#grid
band_name.grid(column=1 , row=0, columnspan=4)
music_name.grid(column=1 , row=1, columnspan=4)
volume_space.grid(column=5,row=1)
button_play.grid(column = 1, row = 2)
button_pause.grid(column = 2, row = 2)
button_back_music.grid(column = 3, row = 2)
button_next_music.grid(column =4 , row =2)
button_decrease_the_volume.grid(column=5,row=3)
button_turn_up_the_volume.grid(column=5,row=2)

#keep application window open
root.mainloop()