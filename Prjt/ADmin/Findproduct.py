import tkinter as tk
from tkinter import messagebox

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    database="fmpdf"
)
cursor = conn.cursor()

def Find_pro():
    fenetre_Type = tk.Toplevel()
    fenetre_Type.title("Find product")

    largeur = 500
    hauteur = 400
    fenetre_Type.geometry(f"{largeur}x{hauteur}")

    image_path8 = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\Dash4.png'
    background_image8 = tk.PhotoImage(file=image_path8)

    canvas3 = tk.Canvas(fenetre_Type, width=largeur, height=hauteur)
    canvas3.pack()
    canvas3.create_image(0, 0, image=background_image8, anchor=tk.NW)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'
    # Charger l'icône personnalisée
    fenetre_Type.iconbitmap(icone_path)


    entry_ID = tk.Entry(fenetre_Type)
    entry_ID.place(relx=0.52, rely=0.269, anchor=tk.W)

    # Obtenir la liste des produits disponibles depuis la base de données
    cursor.execute("SELECT Nom FROM equipement")
    produits_disponibles = cursor.fetchall()  # Récupérer tous les enregistrements

    # Liste des produits disponibles
    produits = [produit[0] for produit in produits_disponibles]

    # Variable pour stocker le produit sélectionné dans le menu déroulant
    produit_selectionne_var = tk.StringVar(fenetre_Type)
    produit_selectionne_var.set(produits[0])  # Par défaut, le premier produit est sélectionné

    # Menu déroulant pour afficher les produits disponibles
    menu_produits = tk.OptionMenu(fenetre_Type, produit_selectionne_var, *produits)
    menu_produits.place(relx=0.61, rely=0.47, anchor=tk.CENTER)

    def valider():
        # Récupérer la méthode de recherche sélectionnée
        choix_recherche = var.get()

        if choix_recherche == 1:  # Recherche par ID
            # Récupérer l'ID saisi dans la zone de saisie
            produit_id = entry_ID.get()

            # Vérifier que l'ID est un entier valide
            try:
                produit_id = int(produit_id)
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir un ID valide (entier).")
                return

            # Effectuer la recherche par ID dans la base de données
            cursor.execute("SELECT * FROM equipement WHERE Equipement_ID = %s", (produit_id,))
            produit = cursor.fetchone()

            if produit:
                # Afficher les détails du produit trouvé
                messagebox.showinfo("Produit trouvé", f"ID : {produit[0]}\nNom : {produit[1]}\nType_ID : {produit[2]}\nFournisseur_ID : {produit[3]}\nQuantiteDisponible : {produit[4]}\nDateEntree : {produit[5]}")
            else:
                messagebox.showinfo("Produit non trouvé", "Aucun produit trouvé avec cet ID.")

        elif choix_recherche == 2:  # Recherche par liste
            # Récupérer le produit sélectionné dans le menu déroulant
            produit_selectionne = produit_selectionne_var.get()

            # Effectuer la recherche par nom du produit dans la base de données
            cursor.execute("SELECT * FROM equipement WHERE Nom = %s", (produit_selectionne,))
            produit = cursor.fetchone()

            if produit:
                # Afficher les détails du produit trouvé
                messagebox.showinfo("Produit trouvé", f"ID : {produit[0]}\nNom : {produit[1]}\nType_ID : {produit[2]}\nFournisseur_ID : {produit[3]}\nQuantiteDisponible : {produit[4]}\nDateEntree : {produit[5]}")
            else:
                messagebox.showinfo("Produit non trouvé", "Aucun produit trouvé avec ce nom.")

    # Variable pour stocker le choix de recherche (1 pour ID, 2 pour liste)
    var = tk.IntVar()

    # Radiobuttons pour choisir le type de recherche
    radio_ID = tk.Radiobutton(fenetre_Type, text="Rechercher par ID", variable=var, value=1, bg="#1ABC9C")
    radio_liste = tk.Radiobutton(fenetre_Type, text="Rechercher par liste", variable=var, value=2, bg="#1ABC9C")

    radio_ID.place(relx=0.37, rely=0.269, anchor=tk.CENTER)
    radio_liste.place(relx=0.38, rely=0.47, anchor=tk.CENTER)

    btn_valider = tk.Button(fenetre_Type, text="Valider", width=7, command=valider, bg="Green")
    btn_valider.place(relx=0.78, rely=0.79)

    fenetre_Type.mainloop()