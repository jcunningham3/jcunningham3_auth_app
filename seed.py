from app import app
from models import Users, Team, db

#drop and create tables
db.drop_all()
db.create_all()