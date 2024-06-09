import os
import platform
import vlc
import time

mot_secret = "CODE"
compteur = 0

def play_sound(file):
    player = vlc.MediaPlayer(file)
    player.play()
    time.sleep(1)  # Laissez le temps au lecteur de commencer
    while player.is_playing():
        time.sleep(0.1)
    player.stop()

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

while True:
    guess = input("Devinez le mot secret : ").upper()
    
    if guess == mot_secret:
        print("Félicitations ! Vous avez trouvé le mot secret.")
        play_sound("Victory.mp3")
        clear_screen()
    else:
        if compteur == 0:
            print("Oops, ce n'est pas le mot secret. Essayez à nouveau !")
        elif compteur == 1:
            print("Hélas, ce n'est pas le mot secret. Mais ne te décourage pas !")
        elif compteur == 2:
            print("Ah zut, ce n'est encore pas ça. Continue à essayer !")
        else:
            print("Dommage, ce n'est pas le mot secret. Peut-être as-tu besoin d'un déCODEur ? Essayez encore !")
        compteur += 1
