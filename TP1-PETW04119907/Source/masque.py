#!/usr/bin/python3
#coding: utf8
import sys # Permet de prendre les arguments des commandes utilisateurs
import function # Ajoute le fichier fonction

key = "" # Clé de dé/chiffrement
sizeMask = "" # Nombre de fois que le masque doit s'opérer

keyMinValue = 0 # Valeur minimale autorisée pour la clé
keyMaxValue = 9999 # Valeur maximale autorisée pour la clé
mask = [] # Contiendra la chaine pour crypter le message

if 2 < len(sys.argv):  # S'il y a tout les arguments 
    try:
        key = int(sys.argv[1]) # Permet de savoir si la donnée émise par l'utilisateur est un entier, sinon exception
        
        if keyMinValue <= key and key <= keyMaxValue: # Clé entier dans la borne voulu
            sizeMask = int(sys.argv[2])
            
            if 0 < sizeMask: # Si la taille du masque est positive
                mask = function.Mask(key, sizeMask) # Crée le masque
                function.DisplayMaskTab(mask) # Affiche le masque

            else:
                print("La taille du masque doit être supérieure à zéro.")
                sys.exit()
        else:
            print("La clé doit être un entier compris entre " + str(keyMinValue) + " et " + str(keyMaxValue) + ".")
            sys.exit()

    except ValueError as e: # Gère l'exception avec la conversion string to int de key
        print(str(e))
        sys.exit()

else:
    print("Il manque des arguments pour continuer le programme. (la clé et le nom du fichier à chiffrer)")
    sys.exit()