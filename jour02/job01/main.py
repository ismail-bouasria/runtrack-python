#job01

# Class Personne
class Personne(object):
    
    # Le constructeur de la classe
    def __init__(self, nom: str, prenom: str) -> None:
        self.nom = nom
        self.prenom = prenom
        
    # Methode se présenter()
    def se_presenter(self) -> None:
        print("Je m'appelle " + self.nom + " " + self.prenom)
    
    # Accesseur = Getter pour l'attribut nom
    def get_nom(self) -> str:
        return self.nom
    
    # Accesseur = Getter pour l'attribut prenom
    def get_prenom(self) -> str:
        return self.prenom
    
    # Mutateur = Setter pour l'attribut nom
    def set_nom(self, new_nom: str) -> None:
        self.nom = new_nom
        
    # Mutateur = Setter pour l'attribut prenom
    def set_prenom(self, new_prenom: str) -> None:
        self.prenom = new_prenom
        
        
# Class Auteur
class Auteur(Personne):
    def __init__(self, nom: str, prenom: str):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def lister_oeuvre(self):
        if self.oeuvre:
            print(f"L'oeuvre de {self.nom} {self.prenom} :")
            for livre in self.oeuvre:
                livre.afficher_titre()
        else:
            print(f"{self.nom} {self.prenom} n'a encore rien écrit !")

    def ecrire_un_livre(self, titre: str):
        nouveau_livre = Livre(titre, self)
        self.oeuvre.append(nouveau_livre)
        print(f"{self.nom} {self.prenom} vient d'écrire un nouveau livre : {titre}")


# Class Livre 
class Livre(Auteur):
    
   def __init__(self, titre: str, auteur,):
        self.titre = titre
        self.auteur = Auteur(auteur.nom, auteur.prenom)


   def afficher_titre(self):
        print(f"Titre : {self.titre}")
        
    
        
# Instanciation de la classe Personne
livre1= Livre('La marche de la Bête', Auteur('Bouasria','Ismail'))
livre1.auteur.ecrire_un_livre('La danse des tombaux')
livre1.auteur.ecrire_un_livre('La rivière de la vie')
livre1.auteur.ecrire_un_livre('La marche déséquilibré')
livre1.auteur.lister_oeuvre()



