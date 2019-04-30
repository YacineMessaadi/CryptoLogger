### Code Généerateur de mot de passe ###

import random                                   
import string                                   
from tkinter import *                            
from string import ascii_letters        ### Importation les bibliothèques nécessaires
from string import digits                        
from string import punctuation               
from random import *
from PIL import Image as Img
from PIL import ImageTk


alphabet = ascii_letters #Création d'une liste contenant toutes les lettres de l'alphabet en minuscule et majuscule.
chiffre = digits #Création d'une liste contenantles tout les chiffres.
caracteres_speciaux = punctuation #Création d'une liste contenant tout les caractères spéciaux.


password="" #Création d'une chaîne de caractère vide pour l'affichage du mot de passe
sortie="" 
nb_caractere="" #Création d'une chaîne de caractère pour stocker le nombre de caractère

def gen_mdp():


	nb_chiffre = int(entree_phrase1.get()) #Définition du nombre de chiffres dans le mot de passe
	nb_lettre = int(entree_phrase2.get())   #Pareil pour les lettres
	nb_special = int(entree_phrase3.get()) #Et les caractères spéciaux

	
	chiffres = sample(chiffre, nb_chiffre) #La méthode sample permet d'extraire n elements d'une liste.
	alpha= sample(alphabet, nb_lettre) #on prend autant de caractère qu'on veut dans la liste "alphabet"
	special= sample(caracteres_speciaux, nb_special)
	
	
	mdp=[]                   ## Création d'une liste vide pour contenir les caraceteres du mot de passe
	for n in chiffres:
		mdp.append(n[0]) ## On prend n caractères dans la liste chiffres pour les ajouter dans la liste mdp
		
	for k in alpha: 
		mdp.append(k[0]) ## On prend n caractères dans la liste alpha pour les ajouter dans la liste mdp
		
	for x in special:
		mdp.append(x[0]) ## On prend n caractères dans la liste special pour les ajouter dans la liste mdp

	mdpEnString="" 
	shuffle(mdp)  ## On mélange les éléments de la liste
	for element in mdp: 
		mdpEnString = mdpEnString + element[0] 
		
	shuffle(mdp) 
	print(mdpEnString) 
	password = mdpEnString #Préparation de l'affichage du mot de passe pour tkinter 
	longueur = str(len(mdp)) 

	print("Votre mot de passe contient",longueur,"caractères.") 

	#Affichage du texte dans la fenêtre


	mdpEnString = StringVar() ## On déclare le Stringvar mdpEnString pour pouvoir le modifier par la suite
	mdpEnString.set(password) ## On lui assigne la variable password
	mdpEnString2= Label(fen_princ, textvariable = mdpEnString,font=("Arial Black", 29), height = 3, width=20)  
	mdpEnString2.place(x=0,y=0) 

   
	
	#On "oublie" les place. Cela les fait disparaître de la fenêtre pour afficher le mdp
	labelsolution.place_forget() 
	entree_phrase1.place_forget() 
	labelsolution2.place_forget() 
	entree_phrase2.place_forget() 
	labelsolution3.place_forget() 
	entree_phrase3.place_forget() 
	Bouton1.place_forget() 

	#Ecrit du text dans le press-papier pour copier/coller le mot de passe
	
	fen_princ.clipboard_clear()  # efface le presse-papier
	fen_princ.clipboard_append(password)  # met le mot de passe dans le presse-papier


    
    
    
    
## Création de la fenêtre ##
		
fen_princ = Tk()
fen_princ.title("Création du mot de passe") 
fen_princ.geometry('500x500')


monAffichage = Label(fen_princ, text=password ,font=("Arial Black", 29), height = 5, width=13).place(x=1, y=20)

# Création d'un widget Button (bouton Quitter)
Bouton2 = Button(fen_princ, text = 'Quitter', command = fen_princ.destroy, width=60 , height= 2, background='#C00707')

#Placement du bouton
Bouton2.place(x=50, y=200)
monAffichage = Label(fen_princ, text= password,height = 5, width=13).place(x=0, y=20)

############Nombre de chiffres#################################
labelsolution = Label(fen_princ, text=sortie)
labelsolution.place(x=0, y=10)
labelsolution.config(text="Veuillez rentrer le nombre de chiffres que vous désirez dans votre mot de passe.")

entree_phrase1 = Entry(fen_princ, textvariable=nb_caractere, width=5)
entree_phrase1.place(x=60, y= 30)

###############################################################
##############Nb de lettres###################################
labelsolution2= Label(fen_princ, text=sortie)
labelsolution2.place(x=0, y=50)
labelsolution2.config(text="Veuillez rentrer le nombre de lettres que vous désirez dans votre mot de passe.")

entree_phrase2 = Entry(fen_princ, textvariable=nb_caractere, width=5)
entree_phrase2.place(x=60, y= 70)
###############################################################
##############Nb de caraceteres speciaux###################################
labelsolution3= Label(fen_princ, text=sortie)
labelsolution3.place(x=0, y=90)
labelsolution3.config(text="Veuillez rentrer le nombre de caractères spéciaux que vous désirez dans votre mot de passe.")

entree_phrase3 = Entry(fen_princ, textvariable=nb_caractere, width=5)
entree_phrase3.place(x=60, y=110)
###############################################################

# Création d'un widget Button (bouton creation mdp)
Bouton1 = Button(fen_princ, text = 'Génerer votre mot de passe', command = gen_mdp, width=60 , height= 3)
#Placement du bouton
Bouton1.place(x=50, y=150)

# Lancement de la boucle de surveillance sur la fenetre principale
fen_princ.mainloop()

