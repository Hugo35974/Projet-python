
class IA:
    def __init__(self, echequier, couleur, recursivite=0):

        self.echequier = echequier

        self.couleur = couleur
        self.couleurOpposee = 'Noir' if couleur == 'Blanc' else 'Blanc'
        self.echiquierTemp = echequier
        self.recursivite = recursivite
        self.listeMouvements = []  # Ajout de l'attribut liste de mouvements

        self.valeurPieces = {
            ('Pion', self.couleur): -10,
            ('Tour', self.couleur): -50,
            ('Cavalier', self.couleur): -30,
            ('Fou', self.couleur): -30,
            ('Reine', self.couleur): -90,
            ('Roi', self.couleur): -900,
            ('Pion', self.couleurOpposee): 10,
            ('Tour', self.couleurOpposee): 50,
            ('Cavalier', self.couleurOpposee): 30,
            ('Fou', self.couleurOpposee): 30,
            ('Reine', self.couleurOpposee): 90,
            ('Roi', self.couleurOpposee): 900
        }

    def arbre_nFils_pProfondeur(self, n=2, echequier=None, p=3, niveauActuel=0):
        if echequier is None:
            echequier = self.echequier

        if niveauActuel < p and self.recursivite < n:
            print("\n_______\nrecurs : ", self.recursivite, "\n")
            self.recursivite += 1

            self.listeMouvements = self.listeTousMeilleursMouvements(echequier, echequier.current_player, niveauActuel)
            self.listeMouvements = self.trierMouvements(self.listeMouvements)[:n]

            meilleur_mouvement = None  # Nouvelle ligne ajoutée

            for mouvement in self.listeMouvements:
                if niveauActuel == 1:
                    pass

                self.echiquierTemp = echequier.clone_board()
                piece = self.echiquierTemp.get_piece(mouvement.indexDepart)
                self.echiquierTemp.move(piece, mouvement.indexArrivee)

                listeMouvementsSuivants = self.arbre_nFils_pProfondeur(n, self.echiquierTemp, p, niveauActuel + 1)
                mouvement.set_listeMouvementsSuivants(listeMouvementsSuivants)

                if (
                    listeMouvementsSuivants
                    and (meilleur_mouvement is None or mouvement.valeurPiece > meilleur_mouvement.valeurPiece)
                ):
                    meilleur_mouvement = mouvement  # Mise à jour du meilleur mouvement

            if self.listeMouvements:
                return self.listeMouvements  # Retournez la liste de mouvements
            else:
                return []  # Retournez une liste vide
        else:
            return []  # Retournez une liste vide

    def meilleurMouvement(self, listeMouvements=None, niveau=0, niveauMax=1):
        if niveau == 0:
            listeMouvements = self.arbre_nFils_pProfondeur()
            
        if listeMouvements:
            meilleurMouvementTrouve = None
            maxPoints = 0

            multiplicateur_de_niveau = dict(map(lambda x: (x, 1 - (x / niveauMax+1)), range(0, niveauMax+1)))

            for mouvement in listeMouvements:
                pointsNiveauActuel = mouvement.valeurPiece * multiplicateur_de_niveau[niveau]

                if mouvement.listeMouvementsSuivants:
                    pointsSuivants = self.meilleurMouvement(
                        listeMouvements=mouvement.listeMouvementsSuivants,
                        niveau=niveau + 1,
                        niveauMax=niveauMax
                    ).valeurPiece * multiplicateur_de_niveau[niveau + 1]
                else:
                    pointsSuivants = 0

                calculPointsMouvement = pointsNiveauActuel + pointsSuivants

                if calculPointsMouvement >= maxPoints:
                    meilleurMouvementTrouve = mouvement
                    maxPoints = calculPointsMouvement

            return meilleurMouvementTrouve
        return None



    def listeTousMeilleursMouvements(self, echequier, current_player, niveauProfondeur):
        """
        Cette fonction renvoie tous les déplacements possibles triés
        d'une couleur avec un objet de la classe mouvement contenant
        """
        listeCoupsPossibles = []

        for i in range(echequier.Rows):
            for j in range(echequier.Cols):
                piece = echequier.get_piece((i, j))
                if piece and piece.couleur == current_player:
                    for x in range(echequier.Rows):
                        for y in range(echequier.Cols):
                            position = (x, y)
                            if echequier.est_deplacement_valide(piece, position):
                                listeCoupsPossibles.append(((i, j), (x, y)))  # Utilisez des tuples pour les indices

        listeMouvements = []  # Initialisez une liste locale

        # pour tous les déplacements possibles
        for (indexDepart, indexArrivee) in listeCoupsPossibles:
            piece = echequier.get_piece(indexDepart)
            name = piece.name.split('_')
            valeurPiece = self.valeurPieces[(name[0], piece.couleur)]

            # moins de points si la pièce peut se faire manger
            valeurPiece *= echequier.coefficientPointsSiPeutEtreMangee(indexArrivee)

            # moins de points si elle n'a aucune pièce de la même couleur autour

            # ajout d'un nouveau mouvement à la liste
            listeMouvements.append(Mouvement(indexDepart, indexArrivee, valeurPiece, niveauProfondeur))

        # triez les éléments par points
        listeMouvements = self.trierMouvements(listeMouvements)

        return listeMouvements




    def trierMouvements(self, liste):

        if liste == []:
            return []

        pivot = liste[0]
        liste1 = []
        liste2 = []

        for x in liste[1:]:

            if x.valeurPiece > pivot.valeurPiece:
                liste1.append(x)
            else:
                liste2.append(x)

        return self.trierMouvements(liste1) + [pivot] + self.trierMouvements(liste2)


class Mouvement:
    def __init__(self, indexDepart, indexArrivee, valeurPiece, numeroDuTour):
        self.indexDepart = indexDepart
        self.indexArrivee = indexArrivee
        self.valeurPiece = valeurPiece
        self.numeroDuTour = numeroDuTour
        self.listeMouvementsSuivants = None

    def set_listeMouvementsSuivants(self, liste):
        if liste:
            self.listeMouvementsSuivants = liste

    def get_valeurPiece(self):
        return self.valeurPiece