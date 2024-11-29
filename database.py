# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def setup_database():
    engine = create_engine('postgresql://postgres:post@localhost:5432/postgres')  # Update with your DB credentials
    Session = sessionmaker(bind=engine)
    return Session
