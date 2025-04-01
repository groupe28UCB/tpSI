import time

# Système de fichiers simulé
filesystem = {
    "name": "filesystem_bac1_2025",
    "version": "v1.0",
    "structure": {
        "root": {
            "documents": {},
            "images": {},
            "videos": {},
        }
    }
}

# Répertoire courant
repertoire_courant = "/root"

# Fonction pour créer un fichier
def creer_fichier(chemin, contenu=""):
    dossier = acceder_dossier(chemin)
    if dossier is not None:
        nom = input("Entrez le nom du fichier (avec extension): ")
        if not nom.endswith(".txt"):
            nom += ".txt"
        if nom in dossier:
            print("Le fichier existe déjà. Veuillez choisir un autre nom.")
            return
        dossier[nom] = {"type": "file", "contenu": contenu}
        print(f"Fichier '{nom}' créé dans {chemin}.")
    else:
        print("Chemin invalide.")

# Fonction pour créer un dossier
def creer_dossier(chemin, nom):
    dossier = acceder_dossier(chemin)
    if dossier is not None:
        dossier[nom] = {}
        print(f"Dossier '{nom}' créé dans {chemin}.")
    else:
        print("Chemin invalide.")

# Fonction pour accéder à un dossier
def acceder_dossier(chemin):
    chemin_split = chemin.strip("/").split("/")
    dossier = filesystem["structure"]
    for dossier_nom in chemin_split:
        if dossier_nom in dossier:
            dossier = dossier[dossier_nom]
        else:
            return None
    return dossier

# Fonction pour changer de répertoire
def changer_dossier(chemin):
    global repertoire_courant
    if chemin == "..":
        # Remonter d'un niveau
        if repertoire_courant != "/root":
            repertoire_courant = "/".join(repertoire_courant.strip("/").split("/")[:-1])
            if not repertoire_courant.startswith("/"):
                repertoire_courant = "/" + repertoire_courant
        print(f"Répertoire courant : {repertoire_courant}")
    else:
        # Naviguer vers un sous-dossier
        nouveau_chemin = repertoire_courant + "/" + chemin if not chemin.startswith("/") else chemin
        if acceder_dossier(nouveau_chemin):
            repertoire_courant = nouveau_chemin
            print(f"Répertoire courant : {repertoire_courant}")
        else:
            print("Chemin invalide.")

# Fonction pour écrire dans un fichier
def ecrire_fichier(chemin, nom, contenu):
    dossier = acceder_dossier(chemin)
    if dossier and nom in dossier and dossier[nom]["type"] == "file":
        dossier[nom]["contenu"] = contenu
        print(f"Écriture dans le fichier '{nom}' terminée.")
    else:
        print("Fichier introuvable.")

# Fonction pour lire un fichier
def lire_fichier(chemin, nom):
    dossier = acceder_dossier(chemin)
    if dossier and nom in dossier and dossier[nom]["type"] == "file":
        print(f"Contenu du fichier '{nom}':")
        print(dossier[nom]["contenu"])
    else:
        print("Fichier introuvable.")

# Fonction pour lister un dossier
def lister_dossier(chemin):
    dossier = acceder_dossier(chemin)
    if dossier is not None:
        print(f"Contenu de '{chemin}':", list(dossier.keys()))
    else:
        print("Dossier introuvable.")

# Fonction pour supprimer un fichier ou un dossier
def supprimer_element(chemin, nom):
    dossier = acceder_dossier(chemin)
    if dossier and nom in dossier:
        del dossier[nom]
        print(f"'{nom}' supprimé de {chemin}.")
    else:
        print("Élément introuvable.")

# Menu interactif
def menu():
    global repertoire_courant
    while True:
        print("\n--- Menu ---")
        print(f"Répertoire courant : {repertoire_courant}")
        print("1. Créer un fichier")
        print("2. Créer un dossier")
        print("3. Lire un fichier")
        print("4. Écrire dans un fichier")
        print("5. Lister un dossier")
        print("6. Supprimer un élément")
        print("7. Changer de répertoire (cd)")
        print("8. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            contenu = input("Entrez le contenu du fichier : ")
            creer_fichier(repertoire_courant, contenu)
        elif choix == "2":
            nom = input("Entrez le nom du nouveau dossier : ")
            creer_dossier(repertoire_courant, nom)
        elif choix == "3":
            nom = input("Entrez le nom du fichier : ")
            lire_fichier(repertoire_courant, nom)
        elif choix == "4":
            nom = input("Entrez le nom du fichier : ")
            contenu = input("Entrez le nouveau contenu : ")
            ecrire_fichier(repertoire_courant, nom, contenu)
        elif choix == "5":
            lister_dossier(repertoire_courant)
        elif choix == "6":
            nom = input("Entrez le nom de l'élément à supprimer : ")
            supprimer_element(repertoire_courant, nom)
        elif choix == "7":
            chemin = input("Entrez le chemin ou '..' pour remonter : ")
            changer_dossier(chemin)
        elif choix == "8":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Lancer le menu
menu()