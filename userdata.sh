#!/bin/bash
sudo yum update -y
sudo dnf update -y
sudo dnf install postgresql15 -y
sudo yum install git -y
sudo git clone https://github.com/spartan-longnguyen/aws-training-rds.git
cd aws-training-rds
export DB_USERNAME="postgres"
export DB_PASSWORD="12345678"
export DB_HOST="longnguyen-db-1.ci1xxxcuy6pi.ap-southeast-1.rds.amazonaws.com"
export DB_PORT="5432"
export DB_NAME="postgres"
sudo dnf install python3-pip -y
pip install Flask Flask-Migrate psycopg2-binary
alembic init migrations
sudo sed -i "s|sqlalchemy.url = .*|sqlalchemy.url = postgresql://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}|" alembic.ini
sudo sed -i '/# add your model.*/a from models import db' migrations/env.py
sudo sed -i 's|target_metadata = None|target_metadata = db.metadata|' migrations/env.py
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
python3 app.py