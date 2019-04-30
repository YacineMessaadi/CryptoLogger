### Code Interface ###

from tkinter import *
import random
from PIL import Image as Img
from PIL import ImageTk


#Création de la fonction liée au bouton mot de passe
def launch_mdp():
	global Mafenetre
	Mafenetre.destroy()
	print("mdp")
	#on importe le programme mdp
	import mdpgenerator.py

#Création de la fonction liée au bouton Cryptage
def launch_crypt():
	global Mafenetre
	Mafenetre.destroy()
	print("cryptage")
	#on importe le programme Cryptage
	import Cryptage.py
#Création de la fonction liée au bouton Image
def launch_img():
	global Mafenetre
	Mafenetre.destroy()
	print("img")
	#on importe le programme CryptoLoggerImages
	import CryptoLoggerImages_v3.pyw

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('CryptoLogger')
#definition de la largeur et de la hauteur
larg = 500
haut = 700
#Création de la variable liée à la taille de la fenêtre
sGeo = str(larg)+"x"+str(haut)
Mafenetre.geometry(sGeo)

Logo= "Logo.png"
Logopres = Img.open(Logo)
Logopres = Logopres.resize((500,285), Img.ANTIALIAS)
LogopresTk = ImageTk.PhotoImage(Logopres)
LogoAf=Label(Mafenetre, image = LogopresTk) 
LogoAf.pack()

#Creation du bouton qui va lancer le porgramme mdp.py
Bou_mdp = Button(Mafenetre, text= "Créer un mot de passe", command = launch_mdp).pack()

#Creation du bouton qui va lancer le programme Cryptage.py
Bou_crypt = Button(Mafenetre, text= "Crypter un message", command = launch_crypt).pack()
#Creation du bouton qui va lancer le programme image.py
Bou_img = Button(Mafenetre, text= "Crypter une image", command = launch_img).pack()
        
# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy , background='#C00707').pack()

Mafenetre.mainloop()


