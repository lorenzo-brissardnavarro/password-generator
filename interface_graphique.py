from tkinter import *
from PIL import Image, ImageTk

def page_utilisateur():
    frame_accueil.pack_forget()
    frame_utilisateur.pack(pady=260) 

def page_mdp():
    nom_utilisateur = entry_utilisateur.get()
    frame_utilisateur.pack_forget()
    frame_mdp.pack(pady=100)
    label_mdp.config(text=f"Bonjour {nom_utilisateur}, saisissez votre mot de passe :")

fenetre = Tk()
fenetre.title("Password Validator")
fenetre.geometry("940x680")
fenetre.resizable(False, False)
fenetre.configure(bg="#C5E8FC")

#Page accueil
frame_accueil = Frame(fenetre, bg="#C5E8FC")
frame_accueil.pack(fill="both", expand=True)

image_originale = Image.open("image_background.png")
image_redim = image_originale.resize((940, 680))
bg = ImageTk.PhotoImage(image_redim)
label_photo = Label(frame_accueil, image=bg)
label_photo.place(x=0, y=0, relwidth=1, relheight=1)

btn_start = Button(frame_accueil, text="Commencer", font=("Helvetica", 17, "bold"), bg="#0B3669", fg="white",activebackground="#D6F0FF", activeforeground="#0B3669", relief="flat", bd=0,padx=70, 
pady=15, cursor="hand2", highlightthickness=0, command=page_utilisateur)
btn_start.pack(side="bottom", pady=30)



#Page demande nom utilisateur
frame_utilisateur = Frame(fenetre, bg="#C5E8FC")

label_utilisateur = Label(frame_utilisateur, text="Saisissez votre nom d'utilisateur :", font=("Helvetica", 27, "bold"), fg="#0B3669", bg="#C5E8FC")
label_utilisateur.pack()

entry_utilisateur = Entry(frame_utilisateur, font=("Helvetica", 20))
entry_utilisateur.pack(pady=20)

btn_utilisateur = Button(frame_utilisateur, text="Valider", font=("Helvetica", 17, "bold"), bg="#0B3669", fg="white",activebackground="#D6F0FF", activeforeground="#0B3669", relief="flat", bd=0,padx=70, 
pady=15, cursor="hand2", highlightthickness=0, command=page_mdp)
btn_utilisateur.pack()




#Page choix utilisateur
frame_mdp = Frame(fenetre, bg="#C5E8FC")

label_mdp = Label(frame_mdp, text="", font=("Helvetica", 27, "bold"), fg="#0B3669", bg="#C5E8FC")
label_mdp.pack()

entry_mdp = Entry(frame_mdp, font=("Helvetica", 20), show="*")
entry_mdp.pack(pady=20)

def password_visibility():
    if show_password_var.get():
        entry_mdp.config(show="")
    else:
        entry_mdp.config(show="*")

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

show_password_var = BooleanVar()
show_password_check = Checkbutton(frame_mdp, text="Afficher le mot de passe", variable=show_password_var,command=password_visibility, 
fg="#0B3669", bg="#C5E8FC", activebackground="#C5E8FC", activeforeground="#0B3669")
show_password_check.pack(pady=5)

fenetre.mainloop()