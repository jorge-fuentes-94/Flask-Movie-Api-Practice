from flask import Flask, jsonify, request

app =Flask(__name__)

movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"id": 2, "title": "The Matrix", "director": "The Wachowskis", "year": 1999}
]

@app.route("/")
def home():
    return "Bienvenido al sistema de gestión de películas."

@app.route('/movies', methods=["GET"])
def get_movies():
    return jsonify({"movies": movies})

@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()

    if not data.get("title") or not data.get("director") or not data.get("year"):
        return jsonify({"error": "Missing data"}), 400
    
    new_movie = {
        "id": len(movies) + 1,  # Generamos un nuevo ID, el siguiente en la secuencia
        "title": data["title"],
        "director": data["director"],
        "year": data["year"]
    }

    movies.append(new_movie)
    return jsonify(new_movie),201

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    # Buscamos la película por ID en la lista de películas
    movie = next((movie for movie in movies if movie['id'] == id), None)
    
    if movie is None:
        return jsonify({'error': 'Movie not found'}), 404
    
    return jsonify(movie)

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = next((movie for movie in movies if movie['id'] == id), None)
    
    if movie is None:
        return jsonify({'error': 'Movie not found'}), 404
    
    data = request.get_json()

    movie['title'] = data.get('title', movie['title'])
    movie['director'] = data.get('director', movie['director'])
    movie['year'] = data.get('year', movie['year'])
    
    return jsonify(movie)

@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = next((movie for movie in movies if movie['id'] == id), None)
    
    if movie is None:
        return jsonify({'error': 'Movie not found'}), 404
    
    movies.remove(movie)
    
    return jsonify({'message': 'Movie deleted successfully'}), 200

if __name__ == "__main__":
    app.run(debug=True)
