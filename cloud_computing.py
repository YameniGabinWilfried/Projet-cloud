def element_double(liste):
    print("Éléments en double dans la liste :")
    doublon = False  # je declare cette Variable pour pouvoir indiquer si un doublon a été trouvé

    i = 0
    while i < len(liste):
        compteur = 0
        j = 0
        while j < len(liste):           # Je Compare l'élément actuel avec les autres éléments de ma liste
            if liste[i] == liste[j]:
                compteur += 1
            j += 1      # J'affiche l'élément s'il est en double dans ma liste

        if compteur > 1 and not deja_afficher(liste, i):    # Je verifie grace à cette condition si l'élément est déjà afficher pour éviter la repetition
            print(liste[i])
            doublon = True

        i += 1

    if not doublon:
        print("Aucun doublon trouvé.")


def deja_afficher(liste, index):    # Je définie ma fonction utiliser plus haut pour vérifier si un doublon a déjà été affiché et &viter des répetions
    k = 0
    while k < index:
        if liste[k] == liste[index]:
            return True
        k += 1
    return False


def liste_utilisateur():        # Je definie une fonction pour permettre à l'utilisateur d'entrée sa propre liste au cas ou

    print("Entrez les éléments de ta liste, séparés par des espaces : ")
    elements = input().split()          # La méthode split() ici vas me permettre de demander a l'utilisateur d'entrée une liste en une seule saisr et ensuite vas diviser cette chaineen une liste d'elements distinct
    return [int(element) for element in elements]       # A parir de la liste de chaine obtenue avec split(), je la transforme en liste d'entier utilisables pour identifier les doublons


def choisir_liste_predifinie():         # Ici je prédefinie les liste pour permettre un choix à l'utilisateur

    listes = [
        [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 6],
        [10, 20, 10, 30, 40, 50, 30, "hello", "hi", "Merci"],
        [1, 1, 1, 2, 2, 3, 4, 100, 250],
        [5, 10, 15, 20, 25, 5, 30, 35, 10],
        ["Bienvenue", "Bonjour", "bonjour","great", "good", "good"]
    ]

    print("\nVoici des liste prédéfinit pour vous :")
    for index, liste in enumerate(listes):      # J'utilise la methode enumerate() pour pouvoir parcourir la liste tout en gardans une postion de chaque éléments
        print(f"{index + 1}. {liste}")

    choix = int(input("Choisissez une liste en entrant le numéro correspondant : ")) - 1
    return listes[choix]


def main():             # Ma fonction principale du programme

    print("Détection de doublons dans la liste")
    print("1. Entrer votre propre liste")
    print("2. Choisir une liste prédéfinie")
    choix = int(input("Faites votre choix en entrant soit 1 ou 2 : "))

    if choix == 1:
        liste_utilisateurs = liste_utilisateur()
    elif choix == 2:
        liste_utilisateurs = choisir_liste_predifinie()
    else:
        print("Choix invalide.")        # Si l'utilisateur entre un autre choix outre que 1 et 2 alors je l'affiche ce message
        return

    print(f"\nListe sélectionnée : {liste_utilisateurs}")
    element_double(liste_utilisateurs)


if __name__ == "__main__":                  # J'appel donc ma fonction principale pour finie
    main()
