### Code Crypto Texte ###

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk
from PIL import Image as Img
from PIL import ImageTk
from tkinter.filedialog import *
import os.path
import glob
from os.path import basename, splitext

texte=str("")
mdp_cryptage=str("")
texte_cryptage=str("")
mdp=str("")
sortie=str("")
texteType=str("")
cryptage_choisi=str("")
cryptagereussi=False

#Fonction pour la saisie du texte à crypter
def interface_texte():
	labeltexte.config(text="Entrez un texte a crypter")
	labeltexte.pack()
	entree_phrase.pack()
	interface_general()

#Fonction pour la sélection du fichier txt à crypter
def interface_fichier():
	labeltexte.config(text="Choissisez un fichier a crypter")
	labeltexte.pack()
	buttonChoixFichier.pack()
	texteAvantCryptage.pack()
	interface_general()

#Fonction affichage de l'interface
def interface_general():
	LogoAff.pack_forget()
	buttonmenu_cryptage_texte.pack_forget()
	buttonmenu_cryptage_fichier.pack_forget()
	labelmdp.pack()
	entree_mdp.pack()
	labelliste.pack()
	liste.pack()
	button_cryptage.pack()
	button_decryptage.pack()
	button_retour.pack()
	sortie=""
	labelsolution.config(text=" ")
	labelsolution.pack()

#Fonction fermeture de l'interface
def interface_fermer():
	buttonmenu_cryptage_texte.pack_forget()
	buttonmenu_cryptage_fichier.pack_forget()
	labelmdp.pack_forget()
	entree_mdp.pack_forget()
	labelliste.pack_forget()
	liste.pack_forget()
	button_cryptage.pack_forget()
	button_decryptage.pack_forget()
	button_retour.pack_forget()
	labelsolution.pack_forget()
	labeltexte.pack_forget()
	buttonChoixFichier.pack_forget()
	texteAvantCryptage.pack_forget()
	labeltexte.pack_forget()
	entree_phrase.pack_forget()
	button_explication.pack_forget()
	labelexplication.pack_forget()
	labelexplicationlettre1.pack_forget()
	labelexplicationlettre.pack_forget()
	labelexplicationlettre2.pack_forget()
	labeltypecryptage.pack_forget()

#Fonction Retour
def retour():
	interface_fermer()
	LogoAff.pack()
	buttonmenu_cryptage_texte.pack()
	buttonmenu_cryptage_fichier.pack()

#Fonction pour chiffrer un texte
def cryptage():
	cryptagereussi=False
	valeur_sortie=""
	texteType=""
	text=""
	cryptage_choisi=liste.get('active')
	mdp=entree_mdp.get()
	if entree_phrase.winfo_ismapped():
		text=entree_phrase.get()
		texteType="Texte"
	else:
		text=texteAvantCryptageComplet['text']
		texteType="Fichier"
	
	if cryptage_choisi =="César": #On selectionner le moyen de chiffrer ici le césar
		if text =="" :#On verifie si il y a bien un message
			labelsolution.config(text="Vous devez saisir un message à chiffrer")
			labelsolution.pack()
		elif mdp.isdigit()and int(mdp)>=0:#on verifie si le mdp est correct
			mdp=int(mdp)%24
			labelsolution.config(text="")
			cryptagereussi=True
			for i in range(0,len(text)):#Boucle pour chiffrer chaque lettre
				tempo_letter=text[i]
				valeur_tempo=ord(tempo_letter)
				if valeur_tempo>=65 and valeur_tempo<=90:#On verifie si c'est une lettre en majuscule
					valeur_tempo=valeur_tempo+int(mdp)
					if valeur_tempo>90:
						valeur_tempo=65+(valeur_tempo-91)
					valeur_sortie=valeur_sortie+chr(valeur_tempo)
				elif valeur_tempo>=97 and valeur_tempo<=122:#On verifie si c'est une lettre en minuscule
					valeur_tempo=valeur_tempo+int(mdp)
					if valeur_tempo>122:
						valeur_tempo=97+(valeur_tempo-123)
					valeur_sortie=valeur_sortie+chr(valeur_tempo)#on ajoute le caractere au string de solution
				else:
					valeur_sortie=valeur_sortie+chr(valeur_tempo)#on ajoute le caractere au string de solution

					
		else:#Si le mdp est incorrect
			labelsolution.config(text="Le mot de passe doit être un nombre positif")
			labelsolution.pack()

	elif cryptage_choisi =="Spartiate":#On selectionne le moyen de chiffrer (ici le spartiate)
		if mdp.isdigit():
			print("c'est un nombre")
		else:
			print("Ce n'est pas un nombre")
	else:
		labelsolution.config(text="Vous devez choisir un mode cryptage")
	if cryptagereussi==True:
		button_explication.pack()
		if texteType=="Texte":
			labelsolution.config(text=valeur_sortie)
		else:
			nomFichier=NomFichier['text']
			cheminFichier=CheminFichier['text']
			
			fichier=open(cheminFichier+"/"+nomFichier+"Crypter.txt","w")
			fichier.write(valeur_sortie)
			fichier.close()
			if len(valeur_sortie)>150:
				text=""
				for i in range (0,150):
					text=text+valeur_sortie[i]
				valeur_sortie=text
			labelsolution.config(text=valeur_sortie)

#Fonction pour décrypter les textes en fonction de la méthode
def decryptage():
	cryptagereussi=False
	valeur_sortie=""
	texteType=""
	text=""
	cryptage_choisi=liste.get('active')
	mdp=entree_mdp.get()
	if entree_phrase.winfo_ismapped():
		text=entree_phrase.get()
		texteType="Texte"
	else:
		text=texteAvantCryptageComplet['text']
		texteType="Fichier"

	if cryptage_choisi =="César":#On selectionner le moyen de chiffrer ici le césar
		if text=="":#On verifie si il y a bien un message
			labelsolution.config(text="Vous devez saisir un message à déchiffrer")
		elif mdp.isdigit()and int(mdp)>=0:
			mdp=int(mdp)%24
			for i in range(0,len(text)):#Boucle pour chiffrer chaque lettre
				tempo_letter=text[i]
				valeur_tempo=ord(tempo_letter)
				cryptagereussi=True
				if valeur_tempo>=65 and valeur_tempo<=90:#On verifie si c'est une lettre en majuscule
					valeur_tempo=valeur_tempo-int(mdp)
					if valeur_tempo<65:
						valeur_tempo=91-(65-valeur_tempo)
					valeur_sortie=valeur_sortie+chr(valeur_tempo)
				elif valeur_tempo>=97 and valeur_tempo<=122:#On verifie si c'est une lettre en minuscule
					valeur_tempo=valeur_tempo-int(mdp)
					if valeur_tempo<97:
						valeur_tempo=123-(97-valeur_tempo)
					valeur_sortie=valeur_sortie+chr(valeur_tempo)#on ajoute le caractere au string de solution
				else:
					valeur_sortie=valeur_sortie+chr(valeur_tempo)#on ajoute le caractere au string de solution
			labelsolution.config(text=valeur_sortie)
		else:#Si le mdp est incorrect
			labelsolution.config(text="Le mot de passe doit être un nombre positif")

	else:
		labelsolution.config(text="vous devez choisir un mode de cryptage")

	if cryptagereussi==True:
		if texteType=="Texte":
			labelsolution.config(text=valeur_sortie)
		else:
			nomFichier=NomFichier['text']
			cheminFichier=CheminFichier['text']
			
			fichier=open(cheminFichier+"/"+nomFichier+"Décrypter.txt","w")
			fichier.write(valeur_sortie)
			fichier.close()
			if len(valeur_sortie)>150:
				text=""
				for i in range (0,150):
					text=text+valeur_sortie[i]
				valeur_sortie=text
			labelsolution.config(text=valeur_sortie)
					
					
#Fonction pour le cryptage par fichier	
def fichierchoix():
	lienfichier = askopenfilename(title="Choissisez un fichier",filetype=[('txt Files','.txt')])
	if len(lienfichier) == 0:
				print("aucun fichier choisi")
	else:
		f= open(lienfichier, "r")
		lien=splitext(basename(lienfichier))[0]
		NomFichier.config(text=lien)
		chemin=os.path.dirname(lienfichier)
		CheminFichier.config(text=chemin)
		texte_cryptage=f.read()
		texteAvantCryptageComplet.config(text=texte_cryptage)
		text=""
		for i in range (0,150):
			text=text+texte_cryptage[i]
		texteAvantCryptage.config(text=text)
		
#Fonction qui affiche l'explication pour l'utilisateur
def explication():
	cryptage_choisi=liste.get('active')
	if entree_phrase.winfo_ismapped():
		text=entree_phrase.get()
	else:
		text=texteAvantCryptage['text']
	solution=labelsolution.cget("text")
		
	mdp=entree_mdp.get()
	interface_fermer()
	labeltypecryptage.config(text="Vous avez choisi le cryptage : "+cryptage_choisi )
	labeltypecryptage.pack()
	if cryptage_choisi=="César":
		labelexplication.config(text="Le cryptage par césar décale les lettres d'un certain nombre de rangs qui est en fait le code pour dechiffrer le message. Lorsque l'on code le message on va dans l'ordre logique de l'alphabet (abc) et lorsque l'on décrypte on va dans l'autre sens (cba).")
		labelexplication.pack()
		labelexplicationlettre1.config(text=text[0]+text[1]+text[2])
		labelexplicationlettre1.pack()
		labelexplicationlettre.config(text="On décale donc les lettres "+text[0]+text[1]+text[2]+" de "+mdp+ " rang(s).")
		labelexplicationlettre.pack()
		labelexplicationlettre2.config(text=solution[0]+solution[1]+solution[2])
		labelexplicationlettre2.pack()
		button_retour.pack()
		
		
		
	
	
# - - - - - - - - - - -

# PROGRAMME AFFICHAGE

# - - - - - - - - - - -

#Création de la page
fen_princ = Tk()
fen_princ.geometry('500x500')

Logo= "LogoCryptage.png"
Logopresentation = Img.open(Logo)
Logopresentation = Logopresentation.resize((500,285), Img.ANTIALIAS)
LogopresentationTk = ImageTk.PhotoImage(Logopresentation)
LogoAff=Label(fen_princ, image = LogopresentationTk) 
LogoAff.pack()

#Button du menu de choix
buttonmenu_cryptage_texte=Button(fen_princ,width=20,height=3, text="Faire du cryptage de texte", command=interface_texte)
buttonmenu_cryptage_texte.pack()

buttonmenu_cryptage_fichier=Button(fen_princ,width=20,height=3, text="Cryptage par fichier", command=interface_fichier)
buttonmenu_cryptage_fichier.pack()

#Affichage pour les cryptages
labeltexte = Label(fen_princ, text="")

labelmdp=Label(fen_princ, text="Entrez un mot de cryptage ou un chiffre de cryptage")
entree_mdp= Entry(fen_princ, textvariable=mdp_cryptage, width=30)
labelliste= Label(fen_princ, text="Choisissez un mode de cryptage")
liste = Listbox(fen_princ)
liste.insert(1, "César")
button_cryptage=Button(fen_princ,width=20,height=3, text="Chriffrement par phrase", command=cryptage)
button_decryptage=Button(fen_princ,width=20,height=3, text="Déchiffrage par phrase", command=decryptage)
button_explication=Button(fen_princ,width=20,height=3, text="Explication du cryptage", command=explication)

labelsolution= Label(fen_princ, text="",wraplength=500)

#Boutton pour retour au menu
button_retour=Button(fen_princ,width=20,height=3, text="Retour à la page initiale", command=retour)

#Affichage uniquement pour le cryptage texte

entree_phrase= Entry(fen_princ, textvariable=texte_cryptage, width=30)

#Affichage uniquement pour le cryptage fichier
NomFichier=Label(fen_princ,text="")
CheminFichier=Label(fen_princ,text="")
buttonChoixFichier=Button(fen_princ, text="Choisissez un fichier (.txt) à crypter",command=fichierchoix)
texteAvantCryptage=Label(fen_princ,text="",wraplength=500)
texteAvantCryptageComplet=Label(fen_princ,text="")

#Affichage pour les explications
labeltypecryptage=Label(fen_princ, text="", wraplength=500)
labelexplication=Label(fen_princ, text="", wraplength=500)
labelexplicationlettre1=Label(fen_princ,text="",font=("Courier", 100))
labelexplicationlettre=Label(fen_princ,text="",font=("Courier", 20), wraplength=500)
labelexplicationlettre2=Label(fen_princ,text="",font=("Courier", 100))
 
#Boucle de surveillance de la fenêtre
fen_princ.mainloop()
