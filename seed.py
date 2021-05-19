from models import Tweet, User, db
from app import app

# create all tables
db.drop_all()
db.create_all()

u1 = User(username="Billy Jenkins", password="gluecruise1")
u2 = User(username="Willy Jenkins", password="icantquitglue!")

t1 = Tweet(text="I am what I am and what I am is the bomb!!", user_id=1)
t2 = Tweet(text="Its nothing but rainbows and avatars!!", user_id=2)

db.session.add(u1)
db.session.add(u2)
db.session.add(t1)
db.session.add(t2)

db.session.commit()
