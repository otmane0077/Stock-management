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

def SUPP_pro():
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

    cursor.execute("SELECT Nom FROM equipement")
    produits_disponibles = cursor.fetchall()
    produits = [produit[0] for produit in produits_disponibles]
    produit_selectionne_var = tk.StringVar(fenetre_Type)
    produit_selectionne_var.set(produits[0])

    menu_produits = tk.OptionMenu(fenetre_Type, produit_selectionne_var, *produits)
    menu_produits.place(relx=0.61, rely=0.47, anchor=tk.CENTER)

    def valider():
        choix_recherche = var.get()

        if choix_recherche == 1:  # Suppression par ID
            produit_id = entry_ID.get()
            try:
                produit_id = int(produit_id)
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez saisir un ID valide (entier).")
                return

            # Supprimer les enregistrements associés dans la table "sortie" avant de supprimer le produit
            cursor.execute("DELETE FROM sortie WHERE Equipement_ID = %s", (produit_id,))
            conn.commit()

            # Effectuer la suppression du produit dans la table "equipement"
            cursor.execute("DELETE FROM equipement WHERE Equipement_ID = %s", (produit_id,))
            conn.commit()

            messagebox.showinfo("Suppression réussie", "Le produit a été supprimé avec succès.")

        elif choix_recherche == 2:  # Suppression par liste
            produit_selectionne = produit_selectionne_var.get()
            # Supprimer les enregistrements associés dans la table "sortie" avant de supprimer le produit
            cursor.execute("DELETE FROM sortie WHERE Equipement_ID = %s", (produit_selectionne,))
            conn.commit()

            # Effectuer la suppression du produit dans la table "equipement"
            cursor.execute("DELETE FROM equipement WHERE Nom = %s", (produit_selectionne,))
            conn.commit()

            messagebox.showinfo("Suppression réussie", "Le produit a été supprimé avec succès.")

    var = tk.IntVar()

    radio_ID = tk.Radiobutton(fenetre_Type, text="Supprimer par ID", variable=var, value=1, bg="#1ABC9C")
    radio_liste = tk.Radiobutton(fenetre_Type, text="Supprimer par liste", variable=var, value=2, bg="#1ABC9C")

    radio_ID.place(relx=0.37, rely=0.269, anchor=tk.CENTER)
    radio_liste.place(relx=0.38, rely=0.47, anchor=tk.CENTER)

    btn_valider = tk.Button(fenetre_Type, text="Valider", width=7, command=valider, bg="Green")
    btn_valider.place(relx=0.78, rely=0.79)

    fenetre_Type.mainloop()