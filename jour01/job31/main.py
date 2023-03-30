#job31
import string 

word = input('Entre un mot: ')

def check_word(word:str)-> str:
    for letter in word:
        if letter not in string.ascii_lowercase:
            return False
        return True
        
if check_word(word):
    
    def change_word(word):
    # Convertir le mot en une liste de caractères avec list()
        letters = list(word)
   
    # boucler sur la liste letter avec len()
        for i in range(len(letters)):
            next_letter = chr(ord(letters[i])+1)
            if next_letter =='{': 
                next_letter = 'a'
       # Remplacer le caractère original par le caractère suivant le plus petit si différent
            if next_letter != letters[i]:
                letters[i] = next_letter
            break  # on arrête la boucle dès qu'un caractère est changé
    
    # Si tous les caractères sont déjà 'z', ajouter un nouveau caractère 'a'
        if all(letter for letter in letters):
            letters.append('a')
    # Convertir la liste de caractères en un mot et le retourner
        return ''.join(letters)
    
    print(change_word(word))
else: 
    print("le mot est invalide")