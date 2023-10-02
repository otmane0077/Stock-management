import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    database="fmpdf"
)
cursor = conn.cursor()


def Add_pro():

    fenetre_ADD = tk.Toplevel()
    fenetre_ADD.title("Data Entry Form")
    fenetre_ADD.geometry("530x250")

    # Création d'un widget de niveau supérieur pour afficher l'image de fond
    bg_frame = tk.Frame(fenetre_ADD)
    bg_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Image
    image_path8 = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\Dash3.png'
    background_image8 = Image.open(image_path8)
    background_image8 = background_image8.resize((550, 250), Image.LANCZOS)
    background_image_tk = ImageTk.PhotoImage(background_image8)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'
    # Charger l'icône personnalisée
    fenetre_ADD.iconbitmap(icone_path)
    # Affichage de l'image sur la toile du widget de niveau supérieur
    canvas = tk.Canvas(bg_frame, width=550, height=350)
    canvas.pack(fill='both', expand=True)
    canvas.create_image(0, 0, image=background_image_tk, anchor=tk.NW)

    # Ajout des éléments à la fenêtre principale
    frame = tk.Frame(canvas, bg="#0C3338")  # Set the background color around the frame to "blue"
    frame.pack()

    # Saving User Info
    user_info_frame = tk.LabelFrame(frame, text="User Information")  # Set the background color to "light gray"
    user_info_frame.grid(row=0, column=0, padx=20, pady=20)


    Nom_Article_label = ttk.Label(user_info_frame, text="Nom Article")
    Nom_Article_label.grid(row=0, column=0)

    first_name_entry = ttk.Entry(user_info_frame)


    first_name_entry.grid(row=1, column=0)


    title_label = ttk.Label(user_info_frame, text="Fournisseur")
    title_combobox = ttk.Combobox(user_info_frame, values=[])  # Combobox vide pour les sociétés de fournisseurs
    title_label.grid(row=0, column=2)
    title_combobox.grid(row=1, column=2)

    age_label = ttk.Label(user_info_frame, text="Quantite")
    age_spinbox = ttk.Spinbox(user_info_frame, from_=1, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    nationality_label = ttk.Label(user_info_frame, text="Type Article")
    nationality_combobox = ttk.Combobox(user_info_frame, values=[])  # Combobox vide pour les types d'articles
    nationality_label.grid(row=2, column=1)
    nationality_combobox.grid(row=3, column=1)

    date_label = ttk.Label(user_info_frame, text="Date")
    date_entry = DateEntry(user_info_frame)
    date_label.grid(row=2, column=2)
    date_entry.grid(row=3, column=2)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Récupérer les sociétés de la table "Fournisseur"
    cursor.execute("SELECT Societe FROM Fournisseur")
    fournisseurs = cursor.fetchall()  # Récupérer tous les enregistrements

    # Liste des sociétés de fournisseurs
    societes = [fournisseur[0] for fournisseur in fournisseurs]

    # Mettre à jour les valeurs de la combobox avec les sociétés de fournisseurs
    title_combobox['values'] = societes

    # Récupérer les types d'articles de la table "Type"
    cursor.execute("SELECT Nom FROM Type")
    types_articles = cursor.fetchall()  # Récupérer tous les enregistrements

    # Liste des types d'articles
    types = [type_article[0] for type_article in types_articles]

    # Mettre à jour les valeurs de la combobox avec les types d'articles
    nationality_combobox['values'] = types

    def enter_data():
        # Récupérer les valeurs saisies par l'utilisateur
        nom_article = first_name_entry.get()
        fournisseur_nom = title_combobox.get()
        quantite_entree = age_spinbox.get()
        type_nom = nationality_combobox.get()
        date_entree = date_entry.get()

        # Vérifier que toutes les valeurs obligatoires sont saisies
        if not (nom_article and fournisseur_nom and quantite_entree and type_nom and date_entree):
            # Afficher un message d'erreur si certaines valeurs sont manquantes
            tk.messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        try:
            # Récupérer la clé primaire (ID) du fournisseur sélectionné
            sql_fournisseur_id = "SELECT Fournisseur_ID FROM Fournisseur WHERE Societe = %s"
            cursor.execute(sql_fournisseur_id, (fournisseur_nom,))
            fournisseur_id = cursor.fetchone()[0]

            # Récupérer la clé primaire (ID) du type d'article sélectionné
            sql_type_id = "SELECT Type_ID FROM Type WHERE Nom = %s"
            cursor.execute(sql_type_id, (type_nom,))
            type_id = cursor.fetchone()[0]

            # Exécuter la requête SQL pour insérer les valeurs dans la table "equipement"
            sql_insert = "INSERT INTO equipement (Nom, Type_ID, Fournisseur_ID, QuantiteEntree, DateEntree, QuantiteSortie, QuantiteDispo) " \
                         "VALUES (%s, %s, %s, %s, %s, 0, %s)"  # La colonne "QuantiteSortie" est initialisée à 0
            cursor.execute(sql_insert,
                           (nom_article, type_id, fournisseur_id, quantite_entree, date_entree, quantite_entree))

            # Committer la transaction pour sauvegarder les changements
            conn.commit()

            # Afficher un message de succès
            tk.messagebox.showinfo("Succès", "L'équipement a été ajouté avec succès.")
        except mysql.connector.Error as err:
            # En cas d'erreur, annuler les changements
            conn.rollback()
            # Afficher un message d'erreur
            tk.messagebox.showerror("Erreur", f"Une erreur s'est produite : {err}")

    # Le reste du code reste inchangé

    btn_valider = tk.Button(fenetre_ADD, text="Valider", width=8, command=enter_data, bg="Green")
    btn_valider.place(relx=0.834, rely=0.840)

    fenetre_ADD.mainloop()

