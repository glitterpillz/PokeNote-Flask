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
        admin=True,
        profile_picture='https://i.ibb.co/V2wFFqS/profile-pic-2.jpg',
        banner_url='https://i.ibb.co/n6G7jzs/banner-2.jpg'

    )    
    demo = User(
        username='demo_user',
        email='demo@example.com',
        password='password',
        fname='Demo',
        lname='User',
        admin=False,
        disabled=False,
        profile_picture='https://i.ibb.co/y8f3Cng/profile-pic-1.jpg',
        banner_url='https://i.ibb.co/0cdxsb5/banner-1.jpg'
    )
    leeroyjenkins = User(
        username='leeroyjenkins',
        email='leeroy@example.com',
        password='password',
        fname='Leeroy',
        lname='Jenkins',
        admin=False,
        disabled=False,
        profile_picture='https://i.ibb.co/prYvyVY/profile-pic-4.jpg',
        banner_url='https://i.ibb.co/5kV46mr/banner-4.jpg'
    )
    glitterpillz = User(
        username='glitterpillz',
        email='glitter@example.com',
        password='password',
        fname='Karen',
        lname='Hickey',
        admin=False,
        disabled=False,
        profile_picture='https://i.ibb.co/hKPB9hM/profile-pic-3.jpg',
        banner_url='https://i.ibb.co/5kV46mr/banner-4.jpg'
    )

    db.session.add(admin)
    db.session.add(demo)
    db.session.add(leeroyjenkins)
    db.session.add(glitterpillz)
    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
