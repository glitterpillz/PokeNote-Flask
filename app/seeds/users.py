from app.models import db, User, environment, SCHEMA
# from app.models.db import db, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    admin = User(
        username='admin_user',
        email='admin@example.com',
        password='password',
        fname='Admin',
        lname='User',
        admin=True
    )    
    demo = User(
        username='demo_user',
        email='demo@example.com',
        password='password',
        fname='Demo',
        lname='User',
        admin=False,
        disabled=False,
        profile_picture='https://i.ibb.co/bJPCvPt/profile-picture.jpg',
        banner_url='https://i.ibb.co/864V411/banner.jpg'
    )
    glitterpillz = User(
        username='glitterpillz',
        email='glitter@example.com',
        password='password',
        fname='Karen',
        lname='Hickey',
        admin=False,
        disabled=False
    )

    db.session.add(admin)
    db.session.add(demo)
    db.session.add(glitterpillz)
    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
