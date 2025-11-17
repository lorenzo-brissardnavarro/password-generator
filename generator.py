import json
import string
from hashlib import sha256

alphabet_min = string.ascii_lowercase
alphabet_maj = string.ascii_uppercase
caracteres_speciaux = "!@#$%^&*"
chiffres = "0123456789"

def verification_min(mdp):
    presence_min = False
    for lettre in mdp:
        if lettre in alphabet_min:
            presence_min = True
    return presence_min

def verification_maj(mdp):
    presence_maj = False
    for lettre in mdp:
        if lettre in alphabet_maj:
            presence_maj = True
    return presence_maj

def verification_caracteres(mdp):
    presence_caractere = False
    for lettre in mdp:
        if lettre in caracteres_speciaux:
            presence_caractere = True
    return presence_caractere

def verification_chiffres(mdp):
    presence_chiffre = False
    for lettre in mdp:
        if lettre in chiffres:
            presence_chiffre = True
    return presence_chiffre

def hachage(mdp):
    mdp_crypt = sha256(mdp.encode('utf-8')).hexdigest()
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            data = json.load(fichier)
    except FileNotFoundError:
        data = []
    data.append(mdp_crypt)
    with open('mots_de_passe.json', 'w') as fichier:
        json.dump(data, fichier, indent=4)


while True:
    password = input("Veuillez entrer votre mot de passe : ")
    if len(password) < 8:
        print("\033[1;31mLe mot de passe doit contenir au moins 8 caractères\033[0m")
    elif not verification_min(password):
        print("\033[1;31mLe mot de passe doit contenir au moins une lettre minuscule\033[0m")
    elif not verification_maj(password):
        print("\033[1;31mLe mot de passe doit contenir au moins une lettre majuscule\033[0m")
    elif not verification_chiffres(password):
        print("\033[1;31mLe mot de passe doit contenir au moins un chiffre\033[0m")
    elif not verification_caracteres(password):
        print("\033[1;31mLe mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)\033[0m")
    else:
        print("\033[1;32mVotre mot de passe est correct\033[0m")
        hachage(password)
        break