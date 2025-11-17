from tkinter import *
from PIL import Image, ImageTk

fenetre = Tk()
fenetre.title("Password Validator")
fenetre.geometry("940x680")
fenetre.resizable(False, False)
fenetre.configure(bg="black")

frame_accueil = Frame(fenetre, bg="black")
frame_accueil.pack(fill="both", expand=True)

image_originale = Image.open("image_background.png")
image_redim = image_originale.resize((940, 680))
bg = ImageTk.PhotoImage(image_redim)
label_photo = Label(frame_accueil, image=bg)
label_photo.place(x=0, y=0, relwidth=1, relheight=1)








fenetre.mainloop()