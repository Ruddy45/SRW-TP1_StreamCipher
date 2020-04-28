#!/usr/bin/python3
#coding: utf8
import sys # Permet de prendre les arguments des commandes utilisateurs
import function # Ajoute le fichier fonction

key = "" # Clé de dé/chiffrement
filename = "" # Contient le nom du fichier à dé/chiffrer

keyMinValue = 0 # Valeur minimale autorisée pour la clé
keyMaxValue = 9999 # Valeur maximale autorisée pour la clé
contentFile = [] # Contenu du fichier
mask = [] # Contiendra la chaine pour crypter le message
cipherMessage = [] # Contient le message chiffrer en string
byteMessage = bytearray(1) # Initialise la variable
messageBadKeyValue = "La clé doit être un entier compris entre " + str(keyMinValue) + " et " + str(keyMaxValue) + "."

if 2 < len(sys.argv):  # S'il y a tout les arguments 
    try:
        key = int(sys.argv[1]) # Permet de savoir si la donnée émise par l'utilisateur est un entier, sinon exception
        
        if keyMinValue <= key and key <= keyMaxValue: # Clé entier dans la borne voulue
            filename = str(sys.argv[2])
            contentFile = function.ReadFile(filename)
            
            if contentFile: # Si le fichier a des données
                mask = function.Mask(key, len(contentFile)) # Crée le masque
                feedbackUser = open("feedbackUser.txt", "wb") # Donne à l'utilisateur un feedback sur le texte

                for i in range(len(contentFile)):
                    byteMessage[0] = function.CipherMessage(contentFile[i], mask[i]) # Dé/chiffre le message
                    cipherMessage.append(str(byteMessage)[12:-2]) # Feedback utilisateur
                    feedbackUser.write(byteMessage)
                
                function.DisplayTab(cipherMessage) # Affiche le message
                feedbackUser.close()

            else:
                print("Le fichier est vide.")
                feedbackUser.close()
                sys.exit()
        else:
            print(messageBadKeyValue)
            feedbackUser.close()
            sys.exit()

    except ValueError as e: # Gère l'exception avec la conversion string to int de key
        print(messageBadKeyValue)
        feedbackUser.close()
        sys.exit()

else:
    print("Il manque des arguments pour continuer le programme. (la clé et le nom du fichier à chiffrer)")
    feedbackUser.close()
    sys.exit()