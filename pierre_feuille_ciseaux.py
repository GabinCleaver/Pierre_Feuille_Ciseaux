import random

replay = True

while replay == True:
    choice_user = input("Entrez votre choix (pierre, feuille, ciseaux): ")
    choice_computer = random.randint(1,3)

    if choice_computer == 1:
        choice_computer = "pierre"
    elif choice_computer == 2:
        choice_computer = "feuille"
    elif choice_computer == 3:
        choice_computer = "ciseaux"

    if choice_user == choice_computer:
        print(f"""Egalité !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")
    elif choice_user == "pierre" and choice_computer == "feuille":
        print(f"""Défaite !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")   
    elif choice_computer == "pierre" and choice_user == "feuille":
        print(f"""Victoire !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")  
    elif choice_user == "ciseaux" and choice_computer == "feuille":
        print(f"""Victoire !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")     
    elif choice_computer == "ciseaux" and choice_user == "feuille":
        print(f"""Défaite !
        Voici le résultat: 
        Toi: {choice_user}
        Ordinateur: {choice_computer}""")
    replay = input("""Rejouer ? (y/n) 
    [>] """)
    if replay == "y":
        replay = True
    elif replay == "n":
        replay = False
    else:
        print("Erreur.")
        replay == False