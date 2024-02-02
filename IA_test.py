import sys

class IA:
    def __init__(self, echequier, couleur):
        self.echequier = echequier
        self.couleur = couleur
        self.couleurOpposee = 'Noir' if couleur == 'Blanc' else 'Blanc'

        self.recursivite = 0
        self.listeMouvementsIA = []
        self.meilleurCoupAdversaire = []

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
        # sys.setrecursionlimit(10000)
        # print(sys.getrecursionlimit())

    def arbre_nFils_pProfondeur(self, n=2, echequier=None, p=3):
        if echequier is None:
            echequier = self.echequier

        stack = [(echequier.copy(), self.echequier.current_player, 0, [])]
        result = []

        while stack:
            current_echequier, current_player, current_level, current_path = stack.pop()

            if current_level < p:
                current_moves = self.listeTousMeilleursMouvements(current_echequier, current_player, current_level)
                current_moves = current_moves[0:n]

                for move in current_moves:
                    new_echequier = current_echequier.copy()
                    new_echequier.deplacerPieceEnIndex(move.indexDepart, move.indexArrivee)

                    new_path = current_path + [move]

                    next_moves = self.listeTousMeilleursMouvements(new_echequier, current_echequier.current_player,
                                                                   current_level + 1)
                    stack.append(
                        (new_echequier, current_echequier.current_player, current_level + 1, new_path + next_moves))

            elif current_path:
                result.append(current_path)

        return result

    def listeTousMeilleursMouvements(self, echequier, current_player, niveauProfondeur):
        listeCoupsPossibles = []

        for i in range(echequier.Rows):
            for j in range(echequier.Cols):
                piece = echequier.get_piece((i, j))
                if piece and piece.couleur == current_player:
                    for x in range(echequier.Rows):
                        for y in range(echequier.Cols):
                            position = (x, y)
                            if self.echequier.est_deplacement_valide(piece, position):
                                listeCoupsPossibles.append(((i, j), (x, y)))

        listeTousMeilleursMouvements = []

        for (indexDepart, indexArrivee) in listeCoupsPossibles:
            piece = echequier.get_piece(indexDepart)
            name = piece.name.split('_')
            valeurPiece = self.valeurPieces[(name[0], piece.couleur)]

            valeurPiece *= echequier.coefficientPointsSiPeutEtreMangee(indexArrivee)

            listeTousMeilleursMouvements.append(Mouvement(indexDepart, indexArrivee, valeurPiece, niveauProfondeur))

        return self.trierMouvements(listeTousMeilleursMouvements)

    def meilleurMouvement(self, listeMouvements=None, niveau=0, niveauMax=None):
        # Define a maximum depth to avoid infinite loops
        MAX_DEPTH = 10

        if niveau == 0:
            self.arbre_nFils_pProfondeur()

        if self.listeMouvementsIA and niveauMax is None:
            niveauMax = 0
            premier_fils = self.listeMouvementsIA[0]

            while premier_fils.listeMouvementsSuivants is not None and niveauMax < MAX_DEPTH:
                print(f"Niveau: {niveauMax}, Premier Fils: {premier_fils}")
                premier_fils = premier_fils.listeMouvementsSuivants[0]
                niveauMax += 1

        if niveauMax is not None:
            multiplicateur_de_niveau = dict(map(lambda x: (x, 1 - (x / niveauMax + 1)), range(niveauMax + 1)))
        else:
            multiplicateur_de_niveau = {}

        maxPoints = 0
        meilleurMouvementTrouve = None

        for mouvement in self.listeMouvementsIA:
            pointsNiveauActuel = mouvement.valeurPiece * multiplicateur_de_niveau.get(niveau, 0)

            if mouvement.listeMouvementsSuivants is not None:
                pointsSuivants = self.meilleurMouvement(
                    listeMouvements=mouvement.listeMouvementsSuivants,
                    niveau=niveau + 1,
                    niveauMax=niveauMax
                ).valeurPiece * multiplicateur_de_niveau.get(niveau + 1, 0)
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
