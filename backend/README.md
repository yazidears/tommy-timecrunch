# Tommy Timecrunch Backend - Docker Setup

Dieses Projekt kann als Docker-Container ausgeführt werden. Hier sind die verschiedenen Optionen:

## 🐳 Docker Build & Run

### Option 1: Automatisches Build-Skript
```bash
./build-docker.sh
```

### Option 2: Manueller Docker Build
```bash
# Image erstellen
docker build -t tommy-timecrunch-backend .

# Container starten
docker run -p 5000:5000 tommy-timecrunch-backend
```

### Option 3: Docker Compose (Empfohlen)
```bash
# Entwicklung
docker-compose up

# Im Hintergrund
docker-compose up -d

# Mit Nginx Reverse Proxy (Production)
docker-compose --profile production up
```

## 📋 Verfügbare Endpunkte

Nach dem Start ist die API verfügbar unter:
- **Direct**: http://localhost:5000
- **Mit Nginx**: http://localhost:80 (nur bei production profile)

### Wichtige API-Endpunkte:
- `GET /` - Health check
- `POST /api/register` - Benutzer registrieren
- `POST /api/login` - Benutzer anmelden
- `GET /api/me` - Benutzer-Profil (Auth erforderlich)
- `GET /api/game/state` - Spielstatus
- `GET /api/leaderboard` - Bestenliste

## 🔧 Konfiguration

### Umgebungsvariablen
Sie können die folgenden Umgebungsvariablen in der `docker-compose.yml` anpassen:

```yaml
environment:
  - FLASK_ENV=production
  - SECRET_KEY=your-secret-key-here
  - JWT_SECRET_KEY=your-jwt-secret-key-here
```

### Datenbank-Persistierung
Die SQLite-Datenbank wird im `./instance` Verzeichnis gespeichert und bleibt zwischen Container-Neustarts erhalten.

## 🧪 API Testing

Sie können die API mit dem bereitgestellten Test-Skript testen:

```bash
# Außerhalb des Containers
python test_api.py

# Oder mit curl
curl http://localhost:5000/
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass"}'
```

## 🚀 Production Deployment

Für den Production-Einsatz:

1. **Verwenden Sie sichere Secret Keys**:
   ```bash
   export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')
   export JWT_SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex())')
   ```

2. **Starten Sie mit Production Profile**:
   ```bash
   docker-compose --profile production up -d
   ```

3. **Überwachen Sie die Logs**:
   ```bash
   docker-compose logs -f
   ```

## 🛠️ Development

Für die Entwicklung können Sie das Backend auch lokal ohne Docker starten:

```bash
# Abhängigkeiten installieren
pip install -r requirements.txt

# Datenbank initialisieren
python -c "from app import create_app; from app.extensions import db; app = create_app(); app.app_context().push(); db.create_all()"

# Server starten
python run.py
```

## 📝 Logs & Debugging

```bash
# Container-Logs ansehen
docker-compose logs tommy-backend

# In Container einsteigen
docker-compose exec tommy-backend bash

# Datenbank direkt ansehen
docker-compose exec tommy-backend sqlite3 instance/database.db
```
