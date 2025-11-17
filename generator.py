import json
import string
from hashlib import sha256

alphabet_min = string.ascii_lowercase
alphabet_maj = string.ascii_uppercase
caracteres_speciaux = "!@#$%^&*"
chiffres = "0123456789"

def verification(mdp, comparateur):
    presence = False
    for lettre in mdp:
        if lettre in comparateur:
            presence = True
    return presence

def hachage(mdp):
    mdp_crypt = sha256(mdp.encode('utf-8')).hexdigest()
    with open('mots_de_passe.json', 'r') as fichier:
        datas = json.load(fichier)
    for data in datas:
        if data == mdp_crypt:
            print("\033[1;31mCe mot de passe est déjà présent dans le fichier !\033[0m")
            return
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            datas = json.load(fichier)
    except FileNotFoundError:
        datas = []
    datas.append(mdp_crypt)
    with open('mots_de_passe.json', 'w') as fichier:
        json.dump(datas, fichier, indent=4)

def affichage_donnees():
    reponse = input("Voulez-vous afficher vos mots de passe hachés (oui ou non) ? ")
    if reponse.lower() == "oui":
        with open('mots_de_passe.json', 'r') as fichier:
            datas = json.load(fichier)
            for mdp in datas:
                print(mdp)


while True:
    password = input("Veuillez entrer votre mot de passe : ")
    if len(password) < 8:
        print("\033[1;31mLe mot de passe doit contenir au moins 8 caractères\033[0m")
    elif not verification(password, alphabet_min):
        print("\033[1;31mLe mot de passe doit contenir au moins une lettre minuscule\033[0m")
    elif not verification(password, alphabet_maj):
        print("\033[1;31mLe mot de passe doit contenir au moins une lettre majuscule\033[0m")
    elif not verification(password, chiffres):
        print("\033[1;31mLe mot de passe doit contenir au moins un chiffre\033[0m")
    elif not verification(password, caracteres_speciaux):
        print("\033[1;31mLe mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)\033[0m")
    else:
        print("\033[1;32mVotre mot de passe respecte les exigences\033[0m")
        hachage(password)
        affichage_donnees()
        break