### Code Crypto Images ###
# -*-coding:Utf-8 -*
import os
from tkinter import *
from tkinter.filedialog import * 
from PIL import Image as Img
from PIL import ImageTk
from PIL.Image import *             ## On importe les bibliothèques nécessaires
from PIL import ImageDraw
from PIL import ImageFont
import generation
import sys




## Fonction d'affichage de l'interface
def interface():
	#Affichage des éléments
	Introduction.pack_forget()
	boutonIntro.pack_forget()
	texteaencoder.pack()
	eSecret.pack(fill=X, padx = 10)
	fichierdebase.pack()
	boutonfichierbase.pack()
	eFichierBase.pack(fill=X, padx = 10)
	nomimageencodee.pack()
	boutonrechercheimage.pack()
	eFichierEncode.pack(fill=X,padx = 10) 
	boutonlancement.pack()
	boutondecryptage.pack()
	boutonPixel.pack()

## Définition de la classe de l'image de base ##
class ImageBlank:

	def chercherFichier(ImageBlank):
			
			ImageBlank.filepath = str(askopenfilename(title="Ouvrir une image",filetypes=[("all files","*.*"),]))
			fichier_base.set(ImageBlank.filepath)
			chemin_temp = os.path.dirname(ImageBlank.filepath)
			nom_temp = os.path.basename(ImageBlank.filepath)
			nom_temp2, ext_temp = os.path.splitext(nom_temp)
			nom_temp2 = nom_temp2+"_2"+ext_temp
			nom_temp2 = os.path.join(chemin_temp,nom_temp2)
			if fichier_encode.get() == "":
					fichier_encode.set(nom_temp2)
                        ## On affiche l'image de base
			ImageBlank.presentation = Img.open(ImageBlank.filepath)
			ImageBlank.presentation = ImageBlank.presentation.resize((300,180), Img.ANTIALIAS)
			ImageBlank.presentationTk = ImageTk.PhotoImage(ImageBlank.presentation)
			global panel
			panel=Label(fen_princ, image = ImageBlank.presentationTk) 
			panel.pack(side = "bottom", fill = "both", expand = "yes")

imagefile= ImageBlank()
## Définition de la fonction de création de l'image encodée ##
def creerImage():
	####################################
	# INITIALISATION
	####################################
	compteur =0 # Compte les nombres de caractères qu'on encode au cours du programme
	texte_a_coder = texte_utilisateur.get()
	longueur =len(texte_a_coder)

	####################################
	# CREATION DES DEUX OBJETS-IMAGES
	####################################
	# On crée deux images initialement identiques en créant deux objets-image à partir du même fichier fichier_1.
	test = True
	fichier_1 = imagefile.filepath
	fichier_2 = fichier_encode.get()
	global image_1
	global image_2
	global nbr_couches
	try:
		image_1 =Img.open(fichier_1)
	except:
		test = False
	if test:
		image_2 =Img.open(fichier_1)
		nbr_couches = len(image_1.getbands())
		# Nous verrons des moyens de sécuriser l'ouverture et la fermeture plus tard
		nLargeur = image_1.width # On va chercher la largeur de l'image 1, identique à la largeur de l'image 2.
		nHauteur = image_1.height # On va chercher la hauteur de l'image 1, identique à la largeur de l'image 2.
		####################################
		# LECTURE DES PIXELS DES IMAGES
		####################################
		# On lit les intensités des pixels jusqu'à  voir trois pixels identiques (fin_de_transmission = 3)
		for y in range(nHauteur) : # Pour y variant de 0 jusqu'à  nHauteur exclus
			for x in range(nLargeur): # Pour x variant de 0 jusqu'à  nLargeur exclus
				if (compteur < longueur):
					if nbr_couches == 3:
						r,g,b = image_1.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
					elif nbr_couches ==4:
						r,g,b,a = image_1.getpixel((x,y))
					elif nbr_couches ==1:
						intensite = image_1.getpixel((x,y))
					if (nbr_couches==3 or nbr_couches==4):
						codage = ord(texte_a_coder[compteur])
						centaine = codage//100
						codage = codage - centaine*100
						dizaine = codage//10
						unite = codage - dizaine*10
						if (r+centaine)<256:
							r2=r+centaine
						else:
							r2=r-centaine
						if (g+dizaine)<256:
							g2=g+dizaine
						else:
							g2=g-dizaine
						if (b+unite)<256:
							b2=b+unite
						else:
							b2=b-unite
						if (nbr_couches ==3):
							image_2.putpixel((x,y),(r2,g2,b2))
						else:
							image_2.putpixel((x,y),(r2,g2,b2,a))
					elif (nbr_couches ==1):
						codage = ord(texte_a_coder[compteur])
						if (intensite+codage)<256:
							intensite=intensite+codage
							image_2.putpixel((x,y),(intensite))
						elif (intensite-codage)>0:
							intensite=intensite-codage
							image_2.putpixel((x,y),(intensite))
						else:
							compteur=longueur+2
					compteur = compteur+1
				else:
					break
			if (compteur >= longueur):
				break
		try:
			image_2.save(fichier_2)
		except:
			test=False

		if (compteur == longueur and test):
			print("SUCCES : Texte encodé dans l'image. Création de l'image encodée sous le nom indiqué.")
			
		else:
			print("ECHEC DE L'ENCODAGE")
	else:
		print("ECHEC : FICHIERS NON OUVERTS")
			

      
## Fonction Décryptage

def ouvrirDécryptage():
## Disparition des élements de la fenêtre de cryptage
	texteaencoder.pack_forget()
	eSecret.pack_forget()
	fichierdebase.pack_forget()
	boutonfichierbase.pack_forget()
	eFichierBase.pack_forget()
	nomimageencodee.pack_forget()
	boutonrechercheimage.pack_forget()
	eFichierEncode.pack_forget()
	boutonlancement.pack_forget()
	boutondecryptage.pack_forget()
	boutonPixel.pack_forget()
	if 'panel' in globals():
			panel.pack_forget()

## Remplacement par le programme de décryptage
	texte=""
	filepath=""
	filepath2=""
	def lireimage():

		texte=""
		monImg=Img.open(monImage)
		monMess=Img.open(monMessage) 
		nLargeur = monImg.width # On va chercher la largeur de l'image
		nHauteur = monImg.height # On va chercher la hauteur de l'image
		mLargeur = monMess.width # On va chercher la largeur de l'image
		mHauteur = monMess.height # On va chercher la hauteur de l'image
		nbr_couches = len(monImg.getbands()) # On va chercher le nombre de couches (rgb ou rgba)
		if nbr_couches==3:
				for y in range(nHauteur) : # Pour y variant de 0 jusqu'à nHauteur exclus
						for x in range(nLargeur): # Pour x variant de 0 jusqu'à nLargeur exclus
								r,g,b = monImg.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
								r2,g2,b2 = monMess.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x2,y2) de monMessage
								rcodé=r2-r
								gcodé=g2-g
								bcodé=b2-b
								codage=rcodé*100+gcodé*10+bcodé
								if (codage !=0):
										texte= texte+chr(codage) 
		elif nbr_couches==4:
				for y in range(nHauteur) : # Pour y variant de 0 jusqu'à nHauteur exclus
						for x in range(nLargeur): # Pour x variant de 0 jusqu'à nLargeur exclus
								r,g,b,a = monImg.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
								r2,g2,b2,a2 = monMess.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x2,y2) de monMessage
								rcodé=r2-r
								gcodé=g2-g
								bcodé=b2-b
								codage=rcodé*100+gcodé*10+bcodé
								if (codage !=0):
										texte= texte+chr(codage) 
		annonce= Label(fen_princ, text="Le message caché est:" ,font=("Calibri", 11), anchor=W).pack()
		maSolution = StringVar() 
		maSolution.set(texte)
		maSalution= Label(fen_princ, textvariable=maSolution, wraplength= 800, font=("Calibri", 11)) #wraplenght permet de fixer le nombre de caractères par ligne
		maSalution.pack() 
		generation.fichiertxt(texte,"texteSecret")
                
	def chercherFichier():
			global monImage
			monImage = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),])


	def chercherFichier2():
			global monMessage
			monMessage = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),]) 

	# CREATIONS DE LA FENETRE ET DES WIDGETS QUI LA COMPOSE  
	# CREATION DE L'OBJET FENETRE  	
	fen_princ.title("Décryptage de l'image encodée")
	# Widget (label fixe) 
	Label(fen_princ, text="Fichier image modifiée :" ,font=("Helvetica", 10), anchor=W).pack() 
	# Création du bouton de recherche d'image 
	Button(fen_princ, text="Chercher l'image de base", command=chercherFichier).pack() 
	# Création du bouton de recherche d'image 
	Button(fen_princ, text="Chercher l'image modifiée", command=chercherFichier2).pack() 
	# CREATION DE LA ZONE LABEL-TITRE
	monTitreTK = StringVar()# On cree un objet StringVar(chaine de caracteres variable)
	monTitreTK.set("Lecture de l'image modifiée")# On definit le texte
	wid_affichage = Label(fen_princ, textvariable=monTitreTK)# Creation de l'objet-Label associee à mon_titre
	wid_affichage.pack()# On rajoute le widget à la fenetre
	# Creation d'un Button lancant le décodage
	wid_boutonDecode = Button(fen_princ, text="Lancer le décodage !", command=lireimage)# Creation de l'objet-Button qui activera la fonction rot13 
	wid_boutonDecode.pack()# On rajoute le widget à la fenetre 
	# Lancement de la boucle de surveillance sur la fenetre fen_princ
	fen_princ.mainloop()
	os.system("pause")

## Fin de la fonction Décryptage

## Fonction Explication
def Explication():
## Disparition des élements de la fenêtre de cryptage
		texteaencoder.pack_forget()
		eSecret.pack_forget()
		fichierdebase.pack_forget()
		boutonfichierbase.pack_forget()
		eFichierBase.pack_forget()
		nomimageencodee.pack_forget()
		boutonrechercheimage.pack_forget()
		eFichierEncode.pack_forget()
		boutonlancement.pack_forget()
		boutondecryptage.pack_forget()
		boutonPixel.pack_forget()
		if 'panel' in globals():
			panel.pack_forget()

		lambda: Pixels(x,y,nbr_couches,image_1,image_2,fen_princ)
		#Variables globales
		#On demande à l'utilisateur de rentrer les coordonnées
		x = IntVar() 
		EntreeX = Label(fen_princ, text="Quelle est l'abscisse X du pixel à analyser ?" ,font=("Calibri", 11), anchor=W).pack()
		x1 = Entry(fen_princ, textvariable=x)
		x1.pack(fill=X, padx = 10)
		EntreeY = Label(fen_princ, text="Quelle est l'ordonnée Y du pixel à analyser ?" ,font=("Calibri", 11), anchor=W).pack()
		y = IntVar() 
		y1 = Entry(fen_princ, textvariable=y)
		y1.pack(fill=X, padx = 10)
		x=int(x.get())
		y=int(y.get())
		# Création du bouton pour afficher les pixels
		boutonAffichagePixel = Button(fen_princ, text="Afficher les pixels", command=lambda: Pixels(x,y,nbr_couches,image_1,image_2,fen_princ))
		boutonAffichagePixel.pack()
		fen_princ.mainloop()
		
## Fonction permettant d'afficher les pixels correspondant aux coordonnées x et y
def Pixels(x,y,nbr_couches,image_1,image_2,fen_princ):
	if nbr_couches == 3:
		r,g,b = image_1.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_base = Img.new("RGB",(400,400), (r,g,b))
		r2,g2,b2 = image_2.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_finale = Img.new("RGB",(400,400), (r2,g2,b2))
	elif nbr_couches ==4:
		r,g,b,a = image_1.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_base = Img.new("RGB",(400,400), (r,g,b,a))
		r2,g2,b2,a = image_2.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_finale = Img.new("RGB",(400,400), (r2,g2,b2,a))
	elif nbr_couches ==1:
		intensite = image_1.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_base = Img.new("RGB",(400,400), (intensite))
		intensite2 = image_2.getpixel((x,y)) # Place dans r,g et b les RGB du pixel (x,y) de monImage
		image_finale = Img.new("RGB",(400,400), (intensite2))

		image_1.close()
		image_2.close()

	r=str(r)
	g=str(g)  ## On convertit les valeurs en strings
	b=str(b)
	couleurs= ("Pixel original: "+"R="+r+" G="+g+" B="+b)
	print(couleurs) ## On affiche les valeurs dans le pixel agrandi
	r2=str(r2)
	g2=str(g2)
	b2=str(b2)
	couleurs2= ("Pixel modifié: "+"R="+r2+" G="+g2+" B="+b2)
	print(couleurs2)

	## Affichage des pixels

	image_baseTk = ImageTk.PhotoImage(image_base)
	global pixel
	pixel= Label(fen_princ, image=image_baseTk, text=couleurs, compound=CENTER)
	pixel.pack(side = "left", fill = "both", expand = "yes")
	
	image_finaleTk = ImageTk.PhotoImage(image_finale)
	global pixel2
	
	pixel2= Label(fen_princ, image=image_finaleTk, text=couleurs2, compound=CENTER)    
	pixel2.pack(side = "right", fill = "both", expand = "yes")
	
	fen_princ.mainloop()


## Fin de la fonction d'affichage des pixels

## Fonction chercher le nom du fichier encodé ##
def chercherFichier2():
	filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png')])
	fichier_encode.set(filepath)


## Création de la fenêtre ##

fen_princ = Tk()
fen_princ.title("Création de l'image encodée")
fen_princ.geometry('1000x700')
Titre = Label(fen_princ, text="Cryptage de l'image" ,font=("Calibri", 15))

## Affichage du Logo CryptoLogger ##
Logo= "LogoImages.png"
Logopresentation = Img.open(Logo)
Logopresentation = Logopresentation.resize((500,285), Img.ANTIALIAS)
LogopresentationTk = ImageTk.PhotoImage(Logopresentation)
LogoAff=Label(fen_princ, image = LogopresentationTk) 
LogoAff.pack()

# Introduction
intro = ("Bienvenue dans le programme CryptoLogger Images! Vous pourrez sélectionner une image au format PNG pour y cacher votre message. Ensuite, quand vous aurez besoin de retrouver votre message, vous devrez sélectionner le mode 'Décryptage'. Vous pourrez visualiser les changements effectués dans le menu 'Détails du cryptage'.")
monIntro = StringVar()
monIntro.set(intro)
Introduction = Label(fen_princ, textvariable=monIntro, wraplength= 800, font=("Calibri", 14)) #wraplenght permet de fixer le nombre de caractères par ligne
boutonIntro = Button(fen_princ, text="Suivant", command=interface)
Introduction.pack()
boutonIntro.pack()
# Widget (label fixe) 
texteaencoder = Label(fen_princ, text="Quel est le texte à  encoder ?" ,font=("Helvetica", 10), anchor=W)

# Widget Entry permettant de rentrer le texte
texte_utilisateur = StringVar() 
texte_utilisateur.set("") 
eSecret = Entry(fen_princ, textvariable=texte_utilisateur) 


## Fichier de base ##
fichierdebase = Label(fen_princ, text="Fichier image de base :" ,font=("Helvetica", 10), anchor=W)

boutonfichierbase = Button(fen_princ, text="Chercher l'image de base dans vos dossiers", command=imagefile.chercherFichier) 

# Widget Entry permettant de rentrer le texte
fichier_base = StringVar()
fichier_base.set("")
eFichierBase = Entry(fen_princ, textvariable=fichier_base)
   
# Widget (label fixe) 
nomimageencodee = Label(fen_princ, text="Quel nom voulez-vous pour l'image encodée ?" ,font=("Helvetica", 10), anchor=W)
# Création du bouton de recherche d'image
boutonrechercheimage = Button(fen_princ, text="Utiliser un nom d'image existante ?", command=chercherFichier2)
# Widget Entry permettant de rentrer le texte
fichier_encode = StringVar()
fichier_encode.set("")
eFichierEncode = Entry(fen_princ, textvariable=fichier_encode)



# Création du bouton de lancement
boutonlancement = Button(fen_princ, text="Créer le fichier encodé", command=creerImage)

# Création du bonton pour la fenêtre Décryptage
boutondecryptage = Button(fen_princ, text="Effectuer un décryptage", command=ouvrirDécryptage)

#Bouton
boutonPixel = Button(fen_princ, text="Détails du cryptage", command=Explication)



# Lancement de la boucle de surveillance sur la fenetre principale
fen_princ.mainloop()
