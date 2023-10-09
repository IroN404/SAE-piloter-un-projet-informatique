import os
import subprocess
import ast

# Mettre à jour pip
subprocess.call(['pip', 'install', '--upgrade', 'pip'])

# Chemin vers le fichier main.py
main_file = 'main.py'

# Fonction pour extraire les imports du fichier main.py
def extract_imports(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
        imports = [node for node in ast.walk(tree) if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)]
        return imports

# Récupérer les imports du fichier main.py
imports = extract_imports(main_file)

# Installer les modules importés avec pip
for imp in imports:
    for alias in imp.names:
        module_name = alias.name
        subprocess.call(['pip', 'install', module_name])
        print(f"Module '{module_name}' installé avec succès.")

print("Tous les modules ont été installés avec succès.")
