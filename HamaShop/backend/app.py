from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# 🔧 créer base de données
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            numero TEXT,
            total INTEGER
        )
    """)
    
    conn.commit()
    conn.close()

init_db() 



# 📦 enregistrer commande
@app.route("/commande", methods=["POST"])
def commande():
    data = request.json

    nom = data["nom"]
    numero = data["numero"]
    total = data["total"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO commandes (nom, numero, total) VALUES (?, ?, ?)",
              (nom, numero, total))
    conn.commit()
    conn.close()

    return jsonify({"message": "Commande enregistrée"})

# 📋 voir commandes (ADMIN)
@app.route("/commandes", methods=["GET"])
def get_commandes():
    token = request.headers.get("Authorization")

    if token not in tokens:
        return jsonify({"error": "Non autorisé"}), 403

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM commandes")
    data = c.fetchall()
    conn.close()

    return jsonify(data)

    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

import bcrypt

ADMIN_USER = "admin"

# mot de passe hashé (1234)
ADMIN_PASS_HASH = bcrypt.hashpw("1234".encode(), bcrypt.gensalt())

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data["user"] == ADMIN_USER and bcrypt.checkpw(
        data["pass"].encode(),
        ADMIN_PASS_HASH
    ):
        token = str(uuid.uuid4())
        tokens.append(token)

        return jsonify({"success": True, "token": token})

    return jsonify({"success": False})
@app.route("/produits", methods=["POST"])
def add_product():
    data = request.json

    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("INSERT INTO produits (nom, prix, image) VALUES (?, ?, ?)",
              (data["nom"], data["prix"], data["image"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "Produit ajouté"})
@app.route("/produits", methods=["GET"])
def get_products():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM produits")
    data = c.fetchall()

    conn.close()

    return jsonify(data)
    import os

