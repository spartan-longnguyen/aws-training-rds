from flask import Flask, jsonify, request
from models import db, User

app = Flask(__name__)

# Configure the database connection URL for Amazon RDS
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@longnguyen-db.ci1xxxcuy6pi.ap-southeast-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    try:
        with app.app_context():
            # Query a user from the database (replace with your actual query)
            user = User.query.first()
            if user:
                return jsonify({'message': 'Database connection successful!', 'user': user.username})
            else:
                return jsonify({'message': 'No users found in the database.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def get_user():
    try:
        with app.app_context():
            # Query all users from the User table
            users = User.query.all()

            # Convert the query result to a list of dictionaries for JSON serialization
            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                })

            # Return the list of users as JSON response
            return jsonify(users_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add', methods=['POST'])
def add_user():
    try:
        with app.app_context():
            # Parse data from the JSON request
            data = request.get_json()
            username = data.get('username')
            email = data.get('email')

            # Create a new User object and add it to the database
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User added successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
