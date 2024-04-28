import os

mot_secret = "CODE"
compteur = 0

while True:
    guess = input("Devinez le mot secret : ").upper()
    
    if guess == mot_secret:
        print("Félicitations ! Vous avez trouvé le mot secret.")
        input()
        os.system('cls')
    else:
        if compteur == 0:
            print("Oops, ce n'est pas le mot secret. Essayez à nouveau !")
        elif compteur == 1:
            print("Hélas, ce n'est pas le mot secret. Mais ne te décourage pas !")
        elif compteur == 2:
            print("Ah zut, ce n'est pas encore ça. Continue à essayer !")
        else:
            print("Dommage, ce n'est pas le mot secret. Peut-être as-tu besoin d'un déCODEur ? Essayez encore !")
        compteur += 1