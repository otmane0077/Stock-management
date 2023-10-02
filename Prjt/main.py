import tkinter as tk
from ADmin import Admin
from G_sorties import Gestion_sorties

fenetre_principale = tk.Tk()

fenetre_principale.title("PGFIT")

largeur = 500
hauteur = 400
fenetre_principale.geometry(f"{largeur}x{hauteur}")
image_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\FIRST.PNG'
background_image = tk.PhotoImage(file=image_path)
icone_path = 'C:\\Users\\WD\\Desktop\\stage\\Prjt\\ADmin\\imgs\\nose_120696.ico'

# Charger l'icône personnalisée
fenetre_principale.iconbitmap(icone_path)
# Création d'un canevas pour afficher l'image en tant que fond d'écran
canvas = tk.Canvas(fenetre_principale, width=largeur, height=hauteur)
canvas.pack()

canvas.create_image(0, 0, image=background_image, anchor=tk.NW)

# Coordonnées des boutons sur l'image de fond
btn_gestion_articles_coords = (350, 182)
btn_gestion_commandes_coords = (350, 250)
btn_gestion_Admin = tk.Button(canvas, text="ADMIN", bg="darkslategray",
                              fg="white", width=12, command=Admin.adminpanel,
                              font=("Helvetica", 10))

btn_gestion_Utilisateur = tk.Button(canvas, text="Gestion Sortie",
                                   bg="darkslategray", fg="white", width=12,
                                   font=("Helvetica", 10), command=Gestion_sorties.gestion_panel)


# Placement des boutons et des autres widgets sur l'image de fond
canvas.create_window(btn_gestion_articles_coords[0], btn_gestion_articles_coords[1], window=btn_gestion_Admin)
canvas.create_window(btn_gestion_commandes_coords[0], btn_gestion_commandes_coords[1], window=btn_gestion_Utilisateur)



fenetre_principale.mainloop()