import json
import string
from hashlib import sha256

alphabet_min = string.ascii_lowercase
alphabet_maj = string.ascii_uppercase
caracteres_speciaux = "!@#$%^&*"
chiffres = string.digits

def verification(mdp, comparateur):
    presence = False
    for lettre in mdp:
        if lettre in comparateur:
            presence = True
    return presence

def hachage(username, mdp):
    mdp_crypt = sha256(mdp.encode('utf-8')).hexdigest()
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        donnees = []
    for element in donnees:
        if element['username'] == username:
            if mdp_crypt in element['mdp']:
                print("\033[1;31mCe mot de passe est déjà présent dans le fichier !\033[0m")
                return
            element['mdp'].append(mdp_crypt)
            break
    else:
        dico = {'username': username, 'mdp': [mdp_crypt]}
        donnees.append(dico)
    with open('mots_de_passe.json', 'w') as fichier:
        json.dump(donnees, fichier, indent=4)

def affichage_donnees(username):
    reponse = input("Voulez-vous afficher vos mots de passe hachés (oui ou non) ? ")
    if reponse.lower() == "oui":
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
            for element in donnees:
                if element['username'] == username:
                    print(element['mdp'])

def valider_mdp(mdp):
    if len(mdp) < 8:
        return "Le mot de passe doit contenir au moins 8 caractères"
    elif not verification(mdp, alphabet_min):
        return "Le mot de passe doit contenir au moins une lettre minuscule"
    elif not verification(mdp, alphabet_maj):
        return "Le mot de passe doit contenir au moins une lettre majuscule"
    elif not verification(mdp, chiffres):
        return "Le mot de passe doit contenir au moins un chiffre"
    elif not verification(mdp, caracteres_speciaux):
        return "Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)"
    else:
        return True

utilisateur = input("Saisissez votre nom d'utilisateur : ")
def fonctionnement():
    password = input("Veuillez entrer votre mot de passe : ")
    verdict = valider_mdp(password)
    if verdict != True:
        print(f"\033[1;31m{verdict}\033[0m")
        return fonctionnement()
    hachage(utilisateur,password)
    affichage_donnees(utilisateur)

fonctionnement()