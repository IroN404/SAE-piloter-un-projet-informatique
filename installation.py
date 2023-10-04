import ast
import subprocess

# Installation de tous les paquets nécessaires dans le code main
print("Installation des dépendances...")
with open("main.py", "r") as f:
    for line in f.readlines():
        if line.startswith("import"):
            pass
        elif line.startswith("from"):
            subprocess.run(["pip", "install", line.split()[1]])
        else:
            break



print("Installation des dépendances terminée.")
