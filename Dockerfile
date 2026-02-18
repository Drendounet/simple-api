# Image de base Python officielle (légère)
FROM python:3.12-slim

# Évite les fichiers .pyc et force les logs en temps réel
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier des dépendances
COPY requirements.txt .

# Installe les dépendances

RUN pip install --no-cache-dir -r requirements.txt

# Copie le code de l'application
COPY ./app ./app

# Expose le port 8000
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]