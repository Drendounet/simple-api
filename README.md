📝 README.md Simple et Direct

# Simple API - Todo Application

API REST simple avec FastAPI pour gérer des todos.

# 🚀 Lancer l'application

## Avec Docker Compose (recommandé)
```bash
git clone https://github.com/Drendounet/simple-api.git
cd simple-api
docker compose up -d
```

## Avec Docker uniquement

docker pull drendounet/simple-api:latest \
docker run -d -p 8000:8000 drendounet/simple-api:latest


## Sans Docker

git clone https://github.com/Drendounet/simple-api.git \
cd simple-api\
python -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


## 📡 Accéder à l'API

Interface web : http://localhost:8000/docs \
API : http://localhost:8000/


## 🎯 Endpoints principaux

### Voir tous les todos
curl http://localhost:8000/todos

### Créer un todo
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Mon todo", "description": "Ma description", "completed": false}'

### Modifier un todo
curl -X PUT http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Todo modifié", "description": "Nouvelle description", "completed": true}'

### Supprimer un todo
curl -X DELETE http://localhost:8000/todos/1 \
1 = TODO ID


### 🐳 Docker Hub

docker pull drendounet/simple-api:latest

Lien : https://hub.docker.com/r/drendounet/simple-api

### 🛠 Commandes Docker Compose utiles

docker compose up -d      # Lancer\
docker compose logs -f    # Voir les logs\
docker compose down       # Arrêter\
docker compose ps         # Status


### 👤 Auteur

Drendounet - GitHub