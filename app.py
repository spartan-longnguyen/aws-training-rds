from flask import Flask, jsonify, request
from models import db, User
import os

app = Flask(__name__)

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    try:
        with app.app_context():
            user = User.query.first()
            if user:
                return jsonify({'message': 'Database connection successful!', 'user': user.username})
            else:
                return jsonify({'message': 'No users found in the database.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/users')
def get_user():
    try:
        with app.app_context():
            users = User.query.all()

            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                })

            return jsonify(users_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add', methods=['POST'])
def add_user():
    try:
        with app.app_context():
            data = request.get_json()
            username = data.get('username')
            email = data.get('email')

            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User added successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
