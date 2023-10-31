# Utilisez une image Python
FROM python:3.11

# Copiez app.py dans le conteneur
COPY app.py /app.py

# Installez les dépendances nécessaires
RUN pip install flet -y

# Commande par défaut pour exécuter l'application Python
CMD ["python", "/app.py"]