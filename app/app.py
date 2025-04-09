import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection
mysql_host = os.environ.get('MYSQL_HOST', 'mysql-db')
mysql_user = os.environ.get('MYSQL_USER', 'flaskuser')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'flaskpass')
mysql_db = os.environ.get('MYSQL_DB', 'flaskdb')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Flask app with MySQL is running!"})

@app.route('/users')
def get_users():
    users = User.query.all()
    result = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
