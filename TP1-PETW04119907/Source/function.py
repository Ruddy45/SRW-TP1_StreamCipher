import random # Permet de crée les diffèrentes clés du chiffrement de flux

# Lit un fichier
def ReadFile(_fileName):
    res = []
    try:
        with open(_fileName, "rb") as fileToRead:
            res = fileToRead.read()
            fileToRead.close()

    except FileNotFoundError: # Si le fichier n'existe pas
        print("Le fichier " + str(_fileName) + " est introuvable.")

    finally:
        return res

# Ecrit dans un fichier
def WriteFile(_fileName, _data):
    try:
        with open(_fileName, "wb") as fileToWrite:
            fileToWrite.write(_data)
            fileToWrite.close()

    except FileNotFoundError: # Si le fichier n'existe pas
        print("Le fichier " + str(_fileName) + " est introuvable.")

# Initialise et crée le masque
def Mask(_key, _sizeOperation):
    res = []
    random.seed(_key) # Initialise le masque avec la clé pour graine
    for i in range(0, _sizeOperation): # Donne le masque pour chiffrer le message
        res.append(random.randint(0, 255))
    return res

# Dé/Chiffre le contenu d'un message
def CipherMessage(_oneLetter, _mask):
    return _oneLetter ^ _mask # XOR pour dé/chiffrer


# Affiche le contenu d'un tableau
def DisplayTab(_tabToDisplay):
    resToDisplay = ''

    for oneCell in _tabToDisplay:
        resToDisplay += str(oneCell)
        
    print(resToDisplay)

# Affiche le tableau mask
def DisplayMaskTab(_tabMask):
    resToDisplay = ''

    for oneCell in _tabMask:
        resToDisplay += str(oneCell) + " " # Espace pour que ce soit plus lisible
        
    print(resToDisplay)