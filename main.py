from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import json
import string
from hashlib import sha256

alphabet_min = string.ascii_lowercase
alphabet_maj = string.ascii_uppercase
caracteres_speciaux = "!@#$%^&*"
chiffres = string.digits

def page_utilisateur():
    frame_accueil.pack_forget()
    frame_utilisateur.pack(pady=260) 

def page_mdp():
    nom_utilisateur = entry_utilisateur.get()
    frame_utilisateur.pack_forget()
    frame_mdp.pack(pady=180)
    label_mdp.config(text=f"Bonjour {nom_utilisateur}, saisissez votre mot de passe :")

def password_visibility():
    if show_password_var.get():
        entry_mdp.config(show="")
    else:
        entry_mdp.config(show="*")

def verification(mdp, comparateur):
    presence = False
    for lettre in mdp:
        if lettre in comparateur:
            presence = True
    return presence

def hachage(username, mdp):
    mdp_crypt = sha256(mdp.encode('utf-8')).hexdigest()
    try:
        with open('fichier_json/mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        donnees = []
    for element in donnees:
        if element['username'] == username:
            if mdp_crypt in element['mdp']:
                messagebox.showerror("Mot de passe en double", "Ce mot de passe est déjà présent dans le fichier !")
                return
            element['mdp'].append(mdp_crypt)
            messagebox.showinfo("Sauvegarde réussi", "Mot de passe enregistré !")
            break
    else:
        frame_mdp.pack_forget()
        frame_affichage.pack(pady=100)
        dico = {'username': username, 'mdp': [mdp_crypt]}
        donnees.append(dico)
        messagebox.showinfo("Sauvegarde réussi", "Utilisateur créé et mot de passe enregistré !")
    with open('fichier_json/mots_de_passe.json', 'w') as fichier:
        json.dump(donnees, fichier, indent=4)
    afficher_mdp(username)

def afficher_mdp(username):
    frame_mdp.pack_forget()
    reponse = messagebox.askquestion("Question", "Voulez-vous afficher vos mots de passe hachés ?")
    if reponse == 'yes':
        frame_affichage.pack(fill="both", expand=True, pady=40)
        with open('fichier_json/mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
        for element in donnees:
            if element['username'] == username:
                liste_mdp = ""
                for mdp in element['mdp']:
                    liste_mdp += f"=> {mdp}\n"
                label_liste = Label(frame_affichage,text=liste_mdp, font=("Helvetica", 15), fg="#0B3669", bg="#C5E8FC", justify="left")
                label_liste.pack()
                break
    else:
        frame_affichage.pack(fill="both", expand=True, pady=80)
        label_affichage.config(text="Merci de votre confiance !")
        image_pain = Image.open("images/pain_epice.png")
        image_pain = ImageTk.PhotoImage(image_pain)
        label_pain = Label(frame_affichage, image=image_pain, bg="#C5E8FC")
        label_pain.pack(pady=30)

def appeler_hachage():
    username = entry_utilisateur.get()
    mdp = mdp_var.get()
    hachage(username, mdp)

def valider_mdp(var, index, mode):
    mdp = mdp_var.get()
    label_erreur_mdp.config(fg="red")
    btn_mdp.config(cursor="arrow")
    btn_mdp.config(state=DISABLED)
    if len(mdp) < 8:
        label_erreur_mdp['text'] = "Le mot de passe doit contenir au moins 8 caractères"
    elif not verification(mdp, alphabet_min):
        label_erreur_mdp['text'] = "Le mot de passe doit contenir au moins une lettre minuscule"
    elif not verification(mdp, alphabet_maj):
        label_erreur_mdp['text'] = "Le mot de passe doit contenir au moins une lettre majuscule"
    elif not verification(mdp, chiffres):
        label_erreur_mdp['text'] = "Le mot de passe doit contenir au moins un chiffre"
    elif not verification(mdp, caracteres_speciaux):
        label_erreur_mdp['text'] = "Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)"
    else:
        label_erreur_mdp.config(fg="green")
        label_erreur_mdp['text'] = "Le mot de passe répond bien aux exigences !"
        btn_mdp.config(cursor="hand2")
        btn_mdp.config(state=NORMAL)

fenetre = Tk()
fenetre.title("Password Validator")
fenetre.geometry("940x680")
fenetre.resizable(False, False)
fenetre.configure(bg="#C5E8FC")

#Page accueil
frame_accueil = Frame(fenetre, bg="#C5E8FC")
frame_accueil.pack(fill="both", expand=True)

image_originale = Image.open("images/image_background.png")
image_redim = image_originale.resize((940, 680))
bg = ImageTk.PhotoImage(image_redim)
label_photo = Label(frame_accueil, image=bg)
label_photo.place(x=0, y=0, relwidth=1, relheight=1)

btn_start = Button(frame_accueil, text="Commencer", font=("Helvetica", 17, "bold"), bg="#0B3669", fg="white",activebackground="#D6F0FF", activeforeground="#0B3669", relief="flat", bd=0,padx=70, 
pady=15, cursor="hand2", highlightthickness=0, command=page_utilisateur)
btn_start.pack(side="bottom", pady=30)



#Page saisie nom utilisateur
frame_utilisateur = Frame(fenetre, bg="#C5E8FC")

label_utilisateur = Label(frame_utilisateur, text="Saisissez votre nom d'utilisateur :", font=("Helvetica", 27, "bold"), fg="#0B3669", bg="#C5E8FC")
label_utilisateur.pack()

entry_utilisateur = Entry(frame_utilisateur, font=("Helvetica", 20))
entry_utilisateur.pack(pady=20)

btn_utilisateur = Button(frame_utilisateur, text="Valider", font=("Helvetica", 17, "bold"), bg="#0B3669", fg="white",activebackground="#D6F0FF", activeforeground="#0B3669", relief="flat", bd=0,padx=70, 
pady=15, cursor="hand2", highlightthickness=0, command=page_mdp)
btn_utilisateur.pack()




#Page saisie mot de passe
frame_mdp = Frame(fenetre, bg="#C5E8FC")

label_mdp = Label(frame_mdp, text="", font=("Helvetica", 27, "bold"), fg="#0B3669", bg="#C5E8FC")
label_mdp.pack()

mdp_var = StringVar()
mdp_var.trace_add('write', valider_mdp)
entry_mdp = Entry(frame_mdp, font=("Helvetica", 20), show="*", textvariable=mdp_var)
entry_mdp.pack(pady=20)

show_password_var = BooleanVar()
show_password_check = Checkbutton(frame_mdp, text="Afficher le mot de passe", variable=show_password_var,command=password_visibility, 
fg="#0B3669", bg="#C5E8FC", activebackground="#C5E8FC", activeforeground="#0B3669")
show_password_check.pack()

btn_mdp = Button(frame_mdp, text="Valider", font=("Helvetica", 15, "bold"), bg="#0B3669", fg="white",activebackground="#D6F0FF", activeforeground="#0B3669", relief="flat", bd=0,padx=50, 
pady=10, cursor="arrow", highlightthickness=0, state=DISABLED, command=appeler_hachage)
btn_mdp.pack(pady=20)

label_erreur_mdp = Label(frame_mdp, text="", font=("Helvetica", 18, "bold"), fg="red", bg="#C5E8FC")
label_erreur_mdp.pack()

#Page affichage
frame_affichage = Frame(fenetre, bg="#C5E8FC")

label_affichage = Label(frame_affichage, text="Voici la liste de vos mots de passe hachés", font=("Helvetica", 27, "bold"), fg="#0B3669", bg="#C5E8FC")
label_affichage.pack()

fenetre.mainloop()