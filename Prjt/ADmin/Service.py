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

def ADD_services():
    fenetre_Service = tk.Toplevel()
    fenetre_Service.title("Services")

    largeur = 500
    hauteur = 400
    fenetre_Service.geometry(f"{largeur}x{hauteur}")

    image_path8 = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\Dash6.png'
    background_image8 = tk.PhotoImage(file=image_path8)

    canvas3 = tk.Canvas(fenetre_Service, width=largeur, height=hauteur)
    canvas3.pack()
    canvas3.create_image(0, 0, image=background_image8, anchor=tk.NW)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'
    # Charger l'icône personnalisée
    fenetre_Service.iconbitmap(icone_path)

    label_servicedispo = tk.Label(fenetre_Service, text="Lieu Services:", bg="paleturquoise")

    label_ID = tk.Label(fenetre_Service, text="ID de service:", bg="#1ABC9C")
    entry_ID = tk.Entry(fenetre_Service)

    label_nom_service = tk.Label(fenetre_Service, text=" Nom de Service:", bg="#1ABC9C")
    entry_nom_service = tk.Entry(fenetre_Service)

    label_chefservice = tk.Label(fenetre_Service, text="Chef de Service:", bg="#1ABC9C")
    entry_chefservice = tk.Entry(fenetre_Service)

    # Obtenir la liste des lieux de service disponibles depuis la base de données
    cursor.execute("SELECT Nom FROM LieuAffectation")
    lieux_services_disponibles = cursor.fetchall()  # Récupérer tous les enregistrements

    # Liste des lieux de service disponibles
    lieux_services = [lieu[0] for lieu in lieux_services_disponibles]

    # Variable pour stocker le lieu de service sélectionné dans le menu déroulant
    lieu_service_selectionne_var = tk.StringVar(fenetre_Service)
    lieu_service_selectionne_var.set(lieux_services[0])  # Par défaut, le premier lieu de service est sélectionné

    # Menu déroulant pour afficher les lieux de service disponibles
    menu_lieux_services = tk.OptionMenu(fenetre_Service, lieu_service_selectionne_var, *lieux_services)
    menu_lieux_services.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    def valider():
        Service_ID = entry_ID.get()
        Nom = entry_nom_service.get()
        ChefService = entry_chefservice.get()
        LieuAffectation = lieu_service_selectionne_var.get()

        # Vérifier que toutes les valeurs obligatoires sont saisies
        if not (Service_ID and Nom and ChefService):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        try:
            # Récupérer la clé primaire (ID) du lieu de service sélectionné
            sql_lieu_id = "SELECT LieuAffectation_ID FROM LieuAffectation WHERE Nom = %s"
            cursor.execute(sql_lieu_id, (LieuAffectation,))
            lieu_id = cursor.fetchone()[0]

            # Exécuter la requête SQL pour insérer les valeurs dans la table "service"
            sql_insert = "INSERT INTO service (Service_ID, Nom, ChefService, LieuAffectation_ID) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (Service_ID, Nom, ChefService, lieu_id))

            # Committer la transaction pour sauvegarder les changements
            conn.commit()

            # Afficher un message de succès
            messagebox.showinfo("Succès", "Le service a été ajouté avec succès.")
            fenetre_Service.destroy()
        except mysql.connector.Error as err:
            # En cas d'erreur, annuler les changements
            conn.rollback()
            # Afficher un message d'erreur
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {err}")

    btn_valider = tk.Button(fenetre_Service, text="Valider", width=7, command=valider, bg="Green")

    label_ID.place(relx=0.23, rely=0.5, anchor=tk.CENTER)
    entry_ID.place(relx=0.35, rely=0.5, anchor=tk.W)

    label_chefservice.place(relx=0.23, rely=0.4, anchor=tk.CENTER)
    entry_chefservice.place(relx=0.35, rely=0.4, anchor=tk.W)

    label_nom_service.place(relx=0.23, rely=0.6, anchor=tk.CENTER)
    entry_nom_service.place(relx=0.35, rely=0.6, anchor=tk.W)

    label_servicedispo.place(relx=0.27, rely=0.7, anchor=tk.CENTER)

    btn_valider.place(relx=0.78, rely=0.79)

    fenetre_Service.mainloop()