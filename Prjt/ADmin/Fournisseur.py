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


def Add_fournisseur():
    fenetre_fournisseur = tk.Toplevel()
    fenetre_fournisseur.title("Fournisseur")

    largeur = 500
    hauteur = 400
    fenetre_fournisseur.geometry(f"{largeur}x{hauteur}")

    image_path8 = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\Dash2.png'
    background_image8 = tk.PhotoImage(file=image_path8)

    canvas3 = tk.Canvas(fenetre_fournisseur, width=largeur, height=hauteur)
    canvas3.pack()
    canvas3.create_image(0, 0, image=background_image8, anchor=tk.NW)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'
    # Charger l'icône personnalisée
    fenetre_fournisseur.iconbitmap(icone_path)

    label_ID = tk.Label(fenetre_fournisseur, text="ID de fournisseur:", bg="#ffff00")

    entry_ID = tk.Entry(fenetre_fournisseur)

    label_nom = tk.Label(fenetre_fournisseur, text="Nom fournisseur:", bg="#ffff00")

    entry_nom = tk.Entry(fenetre_fournisseur)

    label_societe = tk.Label(fenetre_fournisseur, text="Nom de la societe:", bg="#ffff00")

    entry_societe = tk.Entry(fenetre_fournisseur)

    def valider_ajout():
        Fournisseur_ID = entry_ID.get()
        Nom = entry_nom.get()
        Societe = entry_societe.get()

        # Vérifier si les champs ID et nom sont remplis
        if Fournisseur_ID and Nom and Societe:
            # Insérer les données dans la table "Fournisseur"
            sql = "INSERT INTO Fournisseur (Fournisseur_ID, Nom, Societe) VALUES (%s, %s, %s)"

            values = (Fournisseur_ID, Nom, Societe)
            cursor.execute(sql, values)
            conn.commit()

            messagebox.showinfo("Succès", "Le fournisseur a été ajouté avec succès.")

            # Fermer la fenêtre
            fenetre_fournisseur.destroy()
        else:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")


    btn_valider = tk.Button(fenetre_fournisseur, text="Valider", width=7  , command=valider_ajout, bg="Green")
    label_nom.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
    entry_nom.place(relx=0.37, rely=0.4, anchor=tk.W)

    label_ID.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    entry_ID.place(relx=0.37, rely=0.5, anchor=tk.W)

    label_societe.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
    entry_societe.place(relx=0.37, rely=0.6, anchor=tk.W)

    btn_valider.place(relx=0.78, rely=0.848)

    fenetre_fournisseur.mainloop()

