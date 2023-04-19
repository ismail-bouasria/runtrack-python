#job01

# Class Personne
class Personne:
    
    # Le constructeur de la classe
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    # Methode se présenter()
    def se_presenter(self):
        print("Je m'appelle " + self.nom + " " + self.prenom)
    
    # Accesseur = Getter pour l'attribut nom
    def get_nom(self):
        return self.nom
    
    # Accesseur = Getter pour l'attribut prenom
    def get_prenom(self):
        return self.prenom
    
    # Mutateur = Setter pour l'attribut nom
    def set_nom(self, new_nom):
        self.nom = new_nom
        
    # Mutateur = Setter pour l'attribut prenom
    def set_prenom(self, new_prenom):
        self.prenom = new_prenom


# Class Auteur
class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    def lister_oeuvre(self):
        if self.oeuvre:
            print(f"L'oeuvre de {self.nom} {self.prenom} :")
            for livre in self.oeuvre:
                livre.afficher_titre()
        else:
            print(f"{self.nom} {self.prenom} n'a encore rien écrit !")

    def ecrire_un_livre(self, titre):
        nouveau_livre = Livre(titre, self)
        self.oeuvre.append(nouveau_livre)
        print(f"{self.nom} {self.prenom} vient d'écrire un nouveau livre : {titre}")


# Class Livre 
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def afficher_titre(self):
        print(f"Titre : {self.titre}")
        
    
# Class Client
class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.collection = []

    def inventaire(self):
        if self.collection:
            print(f"{self.nom} {self.prenom} a les livres suivants :")
            for livre in self.collection:
                livre.afficher_titre()
        else:
            print(f"{self.nom} {self.prenom} n'a aucun livre !")

        
# Class Bibliotheque
class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                if titre in self.catalogue:
                    self.catalogue[titre] += quantite
                else:
                    self.catalogue[titre] = quantite
                print(f"{self.nom} a acheté {quantite} exemplaire(s) du livre '{titre}' de {auteur.nom} {auteur.prenom}.")
                return
        print(f"{auteur.nom} {auteur.prenom} n'a pas écrit le livre '{titre}'.")

    def inventaire(self):
        if self.catalogue:
            print(f"Catalogue de {self.nom} :")
            for titre, quantite in self.catalogue.items():
                print(f"{titre} : {quantite}")
        else:
            print(f"{self.nom} n'a aucun livre !")
