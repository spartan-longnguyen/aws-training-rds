from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)
