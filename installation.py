import ast
import subprocess


# Exécute la commande pour mettre à jour pip
subprocess.run(["pip3", "install", "--upgrade", "pip"])

# Installation de tous les paquets nécessaires dans le code main
print("Installation des dépendances...")
with open("main.py", "r") as f:
    for line in f.readlines():
        if line.startswith("import"):
            pass
        elif line.startswith("from"):
            subprocess.run(["pip3", "install", line.split()[1]])
        else:
            break

# Une fois l'installation terminée, créez un fichier d'indicateur pour indiquer que l'installation est terminée
with open("installation.txt", "w") as indicator_file:
    indicator_file.write("Installation terminée")


print("Installation des dépendances terminée.")
