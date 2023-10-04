import ast
import subprocess

#mise a jour de pip
subprocess.check_call('pip3 install --upgrade pip')

# script Python
script_path = 'main.py'

# Lire le contenu du script
with open(script_path, 'r') as file:
    code = file.read()

# Analyser le code source pour extraire les noms des modules importés
tree = ast.parse(code)
imports = []


for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for name in node.names:
            imports.append(name.name)
    elif isinstance(node, ast.ImportFrom):
        module = node.module
        for name in node.names:
            imports.append(f"{module}.{name.name}")

# Installer les modules importés via pip
for module in imports:
    try:
        subprocess.check_call(['pip3', 'install', module])
    except subprocess.CalledProcessError:
        print(f"Impossible d'installer le module {module}")

print("Installation des dépendances terminée.")
