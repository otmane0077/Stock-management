import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    database="fmpdf"
)
cursor = conn.cursor()


def gestion_panel():
    def valider():
        # Récupérer les valeurs sélectionnées par l'utilisateur
        equipement = equipement_menu_var.get()
        lieu_service = lieu_service_menu_var.get()
        nom_service = nom_service_menu_var.get()
        quantite = Q_spinbox.get()

        # Vérifier que toutes les valeurs sont sélectionnées
        if not (equipement and lieu_service and nom_service and quantite):
            tk.messagebox.showerror("Erreur", "Veuillez sélectionner toutes les valeurs.")
            return

        try:
            # Récupérer l'ID de l'équipement sélectionné
            sql_equipement_id = "SELECT Equipement_ID, QuantiteDispo FROM equipement WHERE Nom = %s"
            cursor.execute(sql_equipement_id, (equipement,))
            equipement_data = cursor.fetchone()
            if not equipement_data:
                raise ValueError("Équipement non trouvé dans la base de données.")

            equipement_id, quantite_dispo = equipement_data

            # Convert the quantity to an integer
            try:
                quantite = int(quantite)
            except ValueError:
                tk.messagebox.showerror("Erreur", "La quantité doit être un nombre entier.")
                return

            # Check if the entered quantity is greater than the available quantity
            if quantite > quantite_dispo:
                tk.messagebox.showerror("Erreur", "La quantité demandée est supérieure à la quantité disponible.")
                return

            # Rest of the code (fetching IDs, inserting data, updating quantities, etc.)
            # Récupérer l'ID du lieu de service sélectionné
            sql_lieu_service_id = "SELECT LieuAffectation_ID FROM LieuAffectation WHERE Nom = %s"
            cursor.execute(sql_lieu_service_id, (lieu_service,))
            lieu_service_id = cursor.fetchone()[0]

            # Fetch results before executing the next query
            conn.commit()

            try:
                # Récupérer l'ID du service sélectionné
                sql_service_id = "SELECT Service_ID FROM Service WHERE Nom = %s"
                cursor.execute(sql_service_id, (nom_service,))
                service_id = cursor.fetchone()[0]
            except TypeError:
                # Si le nom de service n'est pas trouvé dans la base de données
                raise ValueError("Service non trouvé dans la base de données.")

            # Exécuter la requête SQL pour insérer les valeurs dans la table "Sortie"
            sql_insert = "INSERT INTO Sortie (Equipement_ID, QuantiteDonnee, LieuAffectation_ID, Service_ID) " \
                         "VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (equipement_id, quantite, lieu_service_id, service_id))

            # Mettre à jour la quantité disponible de l'équipement dans la table "Equipement"
            sql_update = "UPDATE equipement SET QuantiteSortie = QuantiteSortie + %s, QuantiteDispo = QuantiteEntree - QuantiteSortie " \
                         "WHERE Equipement_ID = %s"
            cursor.execute(sql_update, (quantite, equipement_id))

            # Committer la transaction pour sauvegarder les changements
            conn.commit()

            # Afficher un message de succès
            tk.messagebox.showinfo("Succès", "La sortie a été enregistrée avec succès.")
        except (mysql.connector.Error, ValueError) as err:
            # En cas d'erreur, annuler les changements
            conn.rollback()
            # Afficher un message d'erreur personnalisé
            tk.messagebox.showerror("Erreur", f"Une erreur s'est produite : {err}")

    def update_service_menu(*args):
        selected_lieu_service = lieu_service_menu_var.get()
        if selected_lieu_service:
            cursor.execute("SELECT Nom FROM Service WHERE LieuAffectation_ID IN "
                           "(SELECT LieuAffectation_ID FROM LieuAffectation WHERE Nom = %s)", (selected_lieu_service,))
            services = [service[0] for service in cursor.fetchall()]
            nom_service_menu['menu'].delete(0, 'end')
            for service in services:
                nom_service_menu['menu'].add_command(label=service, command=tk._setit(nom_service_menu_var, service))



    fenetre_Gestion = tk.Toplevel()
    fenetre_Gestion.title("PGFIT")

    largeur = 500
    hauteur = 400
    fenetre_Gestion.geometry(f"{largeur}x{hauteur}")
    image_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\G_sorties\\imgs\\Dash.png'
    background_image = tk.PhotoImage(file=image_path)
    icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\G_sorties\\imgs\\nose_120696.ico'

    # Charger l'icône personnalisée
    fenetre_Gestion.iconbitmap(icone_path)
    # Création d'un canevas pour afficher l'image en tant que fond d'écran
    canvas = tk.Canvas(fenetre_Gestion, width=largeur, height=hauteur)
    canvas.pack()

    label_1 = tk.Label(fenetre_Gestion, text="Equipement :", bg="#1ABC9C")
    label_2 = tk.Label(fenetre_Gestion, text="Lieu serivce :", bg="#1ABC9C")
    label_3 = tk.Label(fenetre_Gestion, text="Nom Service :", bg="#1ABC9C")
    label_4 = tk.Label(fenetre_Gestion, text="La Quantite :", bg="#1ABC9C")
    Q_spinbox = tk.Spinbox(fenetre_Gestion, from_=1, to=110)

    label_1.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
    label_2.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    label_3.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
    label_4.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
    Q_spinbox.place(relx=0.37, rely=0.7, anchor=tk.W)

    # Récupérer les noms des équipements, lieux de service et services disponibles
    cursor.execute("SELECT Nom FROM equipement")
    equipements = [equipement[0] for equipement in cursor.fetchall()]
    cursor.execute("SELECT Nom FROM LieuAffectation")
    lieux_services = [lieu_service[0] for lieu_service in cursor.fetchall()]

    # Variables pour les menus déroulants
    equipement_menu_var = tk.StringVar()
    lieu_service_menu_var = tk.StringVar()
    nom_service_menu_var = tk.StringVar()

    # Ajouter un trace à la variable du lieu de service pour mettre à jour le menu de service lors de la sélection
    lieu_service_menu_var.trace('w', update_service_menu)

    # Menu déroulant pour les équipements
    equipement_menu = tk.OptionMenu(fenetre_Gestion, equipement_menu_var, *equipements)
    equipement_menu.place(relx=0.37, rely=0.4, anchor=tk.W)

    # Menu déroulant pour les lieux de service
    lieu_service_menu = tk.OptionMenu(fenetre_Gestion, lieu_service_menu_var, *lieux_services)
    lieu_service_menu.place(relx=0.37, rely=0.5, anchor=tk.W)

    # Créer le menu déroulant pour les services (vide pour l'instant)
    nom_service_menu = tk.OptionMenu(fenetre_Gestion, nom_service_menu_var, "")
    nom_service_menu.place(relx=0.37, rely=0.6, anchor=tk.W)

    canvas.create_image(0, 0, image=background_image, anchor=tk.NW)
    btn_Valider_coords= (420, 328)
    btn_Valider = tk.Button(canvas, text="ENTREZ", bg="Green", fg="white", width=7 , command=valider)

    # Placement des boutons et des autres widgets sur l'image de fond
    canvas.create_window(btn_Valider_coords[0], btn_Valider_coords[1], window=btn_Valider)
    fenetre_Gestion.mainloop()

    fenetre_Gestion.mainloop()
