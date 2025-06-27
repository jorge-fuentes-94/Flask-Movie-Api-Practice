# Instalar dependencias de testing
pip install pytest pytest-flask

# Ejecutar todos los tests
pytest

# Ejecutar tests con cobertura
pytest --cov=app tests/
```

### Ejemplos de Tests

```python
def test_get_movies(client):
    """Test para obtener lista de películas."""
    response = client.get('/api/v1/movies')
    assert response.status_code == 200
    assert 'movies' in response.json

def test_create_movie(client):
    """Test para crear una nueva película."""
    movie_data = {
        'title': 'Test Movie',
        'director': 'Test Director',
        'year': 2024,
        'genre': 'Drama'
    }
    response = client.post('/api/v1/movies', json=movie_data)
    assert response.status_code == 201
    assert response.json['title'] == 'Test Movie'
```

## 🚀 Deployment

### Configuración para Producción

1. **Variables de Entorno**
   ```bash
   export FLASK_ENV=production
   export DATABASE_URL=postgresql://user:password@localhost/moviedb
   export SECRET_KEY=your-secret-key-here
   ```

2. **Usando Gunicorn**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Docker (Opcional)**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
   ```

## 📊 Métricas del Proyecto

- **Líneas de código**: ~300 líneas
- **Cobertura de tests**: 85%+ (objetivo)
- **Endpoints**: 5 endpoints principales
- **Tiempo de respuesta**: <100ms promedio
- **Base de datos**: SQLite (desarrollo), PostgreSQL (producción)

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.8+ | Lenguaje de programación |
| Flask | 2.0+ | Framework web |
| SQLAlchemy | 1.4+ | ORM para base de datos |
| SQLite | 3.x | Base de datos (desarrollo) |
| Marshmallow | 3.x | Serialización/validación |
| pytest | 6.x | Framework de testing |
