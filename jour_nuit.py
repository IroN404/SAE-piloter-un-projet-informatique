import tkinter as tk
from PIL import Image, ImageTk

def toggle_day_night(event):
    global is_night_mode
    if is_night_mode:
        # Passage en mode jour
        canvas.configure(bg="white")
        label.configure(fg="black", bg="white")
        canvas.itemconfig(logo, image=day_image_resized)
        is_night_mode = False
    else:
        # Passage en mode nuit
        canvas.configure(bg="black")
        label.configure(fg="white", bg="black")
        canvas.itemconfig(logo, image=night_image_resized)
        is_night_mode = True

# Créez la fenêtre principale
root = tk.Tk()
root.title("Mode Jour/Nuit")

# Définissez la taille de la fenêtre
root.geometry("300x300")

# Créez un canevas pour afficher le logo
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Chargez le logo initial pour le mode jour
day_image = Image.open("logo_day.png")

# Redimensionnez l'image du jour pour l'adapter à la taille du canevas
width, height = 150, 150
day_image_resized = ImageTk.PhotoImage(day_image.resize((width, height)))

# Affichez le logo initial (jour)
logo = canvas.create_image(width // 2, height // 2, image=day_image_resized)

# Créez un label pour afficher du texte
label = tk.Label(root, text="Cliquez sur le logo pour basculer entre le mode jour et nuit", fg="black", bg="white")
label.pack()

# Attachez un événement de clic au logo sur le canevas
canvas.tag_bind(logo, '<Button-1>', toggle_day_night)

# Chargez le logo pour le mode nuit
night_image = Image.open("logo_night.png")

# Redimensionnez l'image de nuit pour l'adapter à la taille du canevas
night_image_resized = ImageTk.PhotoImage(night_image.resize((width, height)))

# Définissez une variable pour suivre le mode actuel (jour ou nuit)
is_night_mode = False

root.mainloop()
