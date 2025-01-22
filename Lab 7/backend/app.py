from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # To enable CORS for all routes

# Database connection
def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="names_db",
        user="user",
        password="password"
    )

@app.route('/names', methods=['POST'])
def add_name():
    data = request.json
    name = data.get('name')

    if not name:
        return "Name is required", 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

    return f"Name '{name}' added successfully!"

@app.route('/names', methods=['GET'])
def get_names():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM names")
    names = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify([name[0] for name in names])

# New route to render names in HTML
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM names")
    names = cursor.fetchall()
    cursor.close()
    conn.close()

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Names List</title>
    </head>
    <body>
        <h1>Names in Database</h1>
        <ul>
        {% for name in names %}
            <li>{{ name }}</li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html_template, names=[name[0] for name in names])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
