# Flask Movie API

API REST sencilla con [Flask](https://flask.palletsprojects.com/) para practicar un CRUD de películas. Los datos viven en una lista en memoria, así que se reinician cada vez que arranca el servidor.

## Endpoints

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/movies` | Lista todas las películas |
| GET | `/movies/<id>` | Devuelve una película (404 si no existe) |
| POST | `/movies` | Crea una película; `title`, `director` y `year` son obligatorios (400 si falta alguno) |
| PUT | `/movies/<id>` | Actualiza los campos que se envíen |
| DELETE | `/movies/<id>` | Borra una película |

## Cómo probarlo

```bash
python -m venv venv
venv\Scripts\activate        # en Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

```bash
curl http://127.0.0.1:5000/movies
curl -X POST http://127.0.0.1:5000/movies -H "Content-Type: application/json" -d "{\"title\": \"Alien\", \"director\": \"Ridley Scott\", \"year\": 1979}"
```

## Limitaciones

- Sin base de datos: todo se pierde al reiniciar. `models.py` está vacío, preparado para añadir una.
- El id nuevo es `len(movies) + 1`, así que puede repetirse después de borrar una película.
- Sin tests ni autenticación.
