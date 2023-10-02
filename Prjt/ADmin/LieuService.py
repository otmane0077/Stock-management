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

def ADD_lieu():
    fenetre_Type = tk.Toplevel()
    fenetre_Type.title("Lieu Service")

    largeur = 500
    hauteur = 400
    fenetre_Type.geometry(f"{largeur}x{hauteur}")

    image_path8 = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\Dash5.png'
    background_image8 = tk.PhotoImage(file=image_path8)

    canvas3 = tk.Canvas(fenetre_Type, width=largeur, height=hauteur)
    canvas3.pack()
    canvas3.create_image(0, 0, image=background_image8, anchor=tk.NW)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'
    # Charger l'icône personnalisée
    fenetre_Type.iconbitmap(icone_path)

    label_ID = tk.Label(fenetre_Type, text="ID de lieu service:", bg="#1ABC9C")

    entry_ID = tk.Entry(fenetre_Type)

    label_nomlieu = tk.Label(fenetre_Type, text=" Lieu de Service:", bg="#1ABC9C")

    entry_nomlieu = tk.Entry(fenetre_Type)

    def valider_ajout():
        Lieuaffectation_ID = entry_ID.get()
        Nom = entry_nomlieu.get()

        # Vérifier si les champs ID et nom sont remplis
        if Lieuaffectation_ID and Nom:
            # Insérer les données dans la table "Fournisseur"
            sql = "INSERT INTO lieuaffectation (Lieuaffectation_ID, Nom) VALUES (%s, %s)"

            values = (Lieuaffectation_ID, Nom)
            cursor.execute(sql, values)
            conn.commit()

            messagebox.showinfo("Succès", "Le Lieu de service a été ajouté avec succès.")

            # Fermer la fenêtre
            fenetre_Type.destroy()
        else:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")

    label_type = tk.Label(fenetre_Type, text="Lieu service deja disponible:", bg="paleturquoise")

    try:

        cursor.execute("SELECT Nom FROM Lieuaffectation")

        options_type = [f[0] for f in cursor.fetchall()]  # Récupérer tous les résultats
        conn.commit()

    except mysql.connector.Error as err:
        # En cas d'erreur lors de la récupération des fournisseurs depuis la base de données
        messagebox.showerror("Erreur", f"Erreur lors de la récupération des lieu : {err}")
        return

    choix_type = tk.StringVar(fenetre_Type)
    choix_type.set(options_type[0])  # Définir la première option comme valeur initiale

    menu_type = tk.OptionMenu(fenetre_Type, choix_type, *options_type)
    menu_type.pack()

    btn_valider = tk.Button(fenetre_Type, text="Valider", width=7  , command=valider_ajout, bg="Green")
    label_nomlieu.place(relx=0.23, rely=0.4, anchor=tk.CENTER)
    entry_nomlieu.place(relx=0.35, rely=0.4, anchor=tk.W)

    label_ID.place(relx=0.23, rely=0.5, anchor=tk.CENTER)
    entry_ID.place(relx=0.35, rely=0.5, anchor=tk.W)

    label_type.place(x=60, y=250)
    menu_type.place(x=250, y=250)

    btn_valider.place(relx=0.78, rely=0.79)

    fenetre_Type.mainloop()

