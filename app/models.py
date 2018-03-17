class decharge():
    def __init__(self, num, date, donneur, recepteur):
        self.num = num
        self.date = date
        self.donneur = donneur
        self.recepteur = recepteur
        self.articles = []


class decision():
    def __init__(self, num, date, lieu):
        self.num = num
        self.date = date
        self.lieu = lieu
        self.articles = []


class pv():
    def __init__(self, num, date, fournisseur, responsable, article):
        self.num = num
        self.date = date
        self.fournisseur = fournisseur
        self.responsable = responsable
        self.article = article


class article_d():
    def __init__(self, code, designation):
        self.code = code
        self.designation = designation


class article_pv():
    def __init__(self, code, designation, marque, caracteristiques, prix, tva):
        self.code = code
        self.designation = designation
        self.marque = marque
        self.caracteristiques = caracteristiques
        self.prix = prix
        self.tva = tva


class fournisseur():
    def __init__(self, nom, address, facture):
        self.nom = nom
        self.addess = address
        self. facure = facture
