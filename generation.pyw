import os
from test import *


def fichiertxt(text,nom_fichier):
        test=0            
        try:
                with open('texteSecret.txt'):
                        test=1

                        ## Test de l'existence du fichier texte
                
        except IOError:
            print ("Le fichier n'existe pas encore.","Le fichier txt a été créé dans le dossier.")
        if test==1:                            ## S'il existe, on ajoute un 2 au nom
                fichier = open(nom_fichier+"-2"+".txt", "a")
                fichier.write(text) 
                fichier.close()

        else:                               ## S'il n'existe pas, on le crée sous le nom texteSecret
                fichier = open(nom_fichier+".txt", "a")
                fichier.write(text)
                fichier.close()

