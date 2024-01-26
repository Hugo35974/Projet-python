
class IA:
    def __init__(self, echequier, couleur):

        self.echequier = echequier

        self.couleur = couleur
        self.couleurOpposee = 'Noir' if couleur == 'Blanc' else 'Blanc'

        self.valeurPieces = {
            ('Pion', self.couleur): -10,
            ('Tour', self.couleur): -50,
            ('Cavalier', self.couleur): -30,
            ('Fou', self.couleur): -30,
            ('Dame', self.couleur): -90,
            ('Roi', self.couleur): -900,
            ('Pion', self.couleurOpposee): 10,
            ('Tour', self.couleurOpposee): 50,
            ('Cavalier', self.couleurOpposee): 30,
            ('Fou', self.couleurOpposee): 30,
            ('Dame', self.couleurOpposee): 90,
            ('Roi', self.couleurOpposee): 900
        }

    def arbre_nFils_pProfondeur(self, n=5, echequier=None, p=3, niveauActuel=0):
        """
            Cette fonction permet d'optenir un TREE par recursivite.

            Elle renvoie les n meilleurs mouvements à realiser à partir
            d'un nombre de points.
        """

        if echequier is None:
            echequier = self.echequier

        listeMouvements = []
        niveauActuel += 1

        if not niveauActuel > 3:
            # Vous devez passer le joueur actuel (self.current_player) comme troisième argument
            listeMouvements = self.listeTousMeilleursMouvements(echequier, self.echequier.current_player, niveauActuel)

            listeMouvements = listeMouvements[0:n]

            for mouvement in listeMouvements:
                if niveauActuel == 1:
                    print((
                        echequier.indexToNomCase(mouvement.indexDepart),
                        echequier.indexToNomCase(mouvement.indexArrivee)
                    ))

                echiquierTemp = echequier.copy()  # Utilisez une copie de l'échiquier

                echiquierTemp.deplacerPieceEnIndex(mouvement.indexDepart, mouvement.indexArrivee)

                meilleurCoupAdversaire = self.listeTousMeilleursMouvements(echiquierTemp, self.echequier.current_player,
                                                                           niveauActuel)
                meilleurCoupAdversaire = meilleurCoupAdversaire[0]

                echiquierTemp.deplacerPieceEnIndex(meilleurCoupAdversaire.indexDepart,
                                                   meilleurCoupAdversaire.indexArrivee)

                listeMouvementsSuivants = self.arbre_nFils_pProfondeur(n, echiquierTemp, p, niveauActuel)
                mouvement.set_listeMouvementsSuivants(listeMouvementsSuivants)

            return listeMouvements

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
                            if self.echequier.est_deplacement_valide(piece, position):
                                listeCoupsPossibles.append(((i, j), (x, y)))  # Utilisez des tuples pour les indices

        listeMouvements = []  # Initialisez la listeMouvements ici

        # pour tous les déplacements possibles
        for (indexDepart, indexArrivee) in listeCoupsPossibles:
            piece = echequier.get_piece(indexDepart)
            name = piece.name.split('_')
            print(name)
            valeurPiece = self.valeurPieces[(name[0], piece.couleur)]

            # moins de points si la pièce peut se faire manger
            valeurPiece *= echequier.coefficientPointsSiPeutEtreMangee(indexArrivee)

            # moins de points si elle n'a aucune pièce de la même couleur autour

            # ajout d'un nouveau mouvement à la liste
            listeMouvements.append(Mouvement(indexDepart, indexArrivee, valeurPiece, niveauProfondeur))

        # triez les éléments par points
        listeMouvements = self.trierMouvements(listeMouvements)

        return listeMouvements

    def meilleurMouvement(self, listeMouvements=None, niveau=0, niveauMax=None):

        """
        Cette fonction retourne le meilleur mouvement à realiser d'apres
        le nombre de points qu'il rapporte
        """

        #        print(listeMouvements)
        # à l'initialisation
        if niveau == 0:
            listeMouvements = self.arbre_nFils_pProfondeur()
        #            print('=====')

        #        print(listeMouvements)

        if niveauMax is None:
            niveauMax = 0
            premier_fils = listeMouvements[0]
            while not premier_fils.listeMouvementsSuivants == None:
                premier_fils = premier_fils.listeMouvementsSuivants[0]
                niveauMax += 1

        multiplicateur_de_niveau = dict(map(lambda x: (x, 1 - (x / niveauMax + 1)), range(niveauMax + 1)))
        #        print(multiplicateur_de_niveau)
        # ex pour niveauMax = 5 : {0: 1., 1: .8, 2: .6, 3: .4, 4: .2}

        maxPoints = 0

        for mouvement in listeMouvements:

            # si le meilleur chemin est sup à la valeur max

            # calcul des points pour ce mouvement avec le meilleur chemin
            pointsNiveauActuel = mouvement.valeurPiece * multiplicateur_de_niveau[niveau]

            if not mouvement.listeMouvementsSuivants is None:
                #                print('niveau actuel : ' + str(niveau))
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
        self.listeMouvementsSuivants = liste

    def get_valeurPiece(self):
        return self.valeurPiece