import random
from colorama import Fore, init

init()

replay = True

while replay == True:

    # Initalisations:

    choice_user = input(Fore.LIGHTCYAN_EX + "Entrez votre choix (pierre, feuille, ciseaux): ")
    choice_computer = random.randint(1,3)

    # Conversion des chiffre en valeur dures, pierre pour 1 etc...

    if choice_computer == 1:
        choice_computer = "pierre"
    elif choice_computer == 2:
        choice_computer = "feuille"
    elif choice_computer == 3:
        choice_computer = "ciseaux"

    # Vérifications des possiblitées:

    if choice_user == choice_computer:
        print(Fore.LIGHTYELLOW_EX + f"""Egalité !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")
    elif choice_user == "pierre" and choice_computer == "feuille":
        print(Fore.LIGHTRED_EX + f"""Défaite !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")   
    elif choice_computer == "pierre" and choice_user == "feuille":
        print(Fore.LIGHTGREEN_EX + f"""Victoire !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")  
    elif choice_user == "ciseaux" and choice_computer == "feuille":
        print(Fore.LIGHTGREEN_EX + f"""Victoire !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")     
    elif choice_computer == "ciseaux" and choice_user == "feuille":
        print(Fore.LIGHTRED_EX + f"""Défaite !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")

    # Rejouer:

    replay = input(Fore.WHITE + """Rejouer ? (y/n) 
    [>] """)
    if replay == "y":
        replay = True
    elif replay == "n":
        replay = False
    else:
        print("Erreur.")
        replay == False
