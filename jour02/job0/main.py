#job 0

class Personne(object):
    
#le constructeur de la clase

    def __init__(self,nom:str,prenom:str)->str:
        
        self.nom = nom
        self.prenom = prenom
        
# Methode se présenter()

    def se_presenter(self):
    
        return print("Je m'apelle "+self.nom+self.prenom)
    
    # Accesseur = Getter pour l'attribut
    def get_nom(self):
        return self.nom
    
    def get_prenom(self):
        return self.prenom
    
    # Mutateur = Setter pour l'attribut
    def set_nom(self,new_nom):
        self.nom = new_nom
        
    def set_prenom(self,new_prenom):
        self.prenom = new_prenom
# Instanciation de la classe MaClasse
    
personne1 = Personne('BOUASRIA','Ismail')
personne2 = Personne('Ralf','Lacasse')
personne3 = Personne('Math', 'Hilda')

# Appel d'une méthode de la classe sur l'objet créé
personne1.se_presenter()
personne2.se_presenter()
personne3.se_presenter()


