import os
from sqlalchemy import create_engine, Column, Integer, Text, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
from pgvector.sqlalchemy import Vector
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Text, nullable=False)
    role = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    

class DocumentChunks(Base):
    __tablename__ = "document_chunks"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    metadata_info = Column(JSONB, nullable=True)
    embedding = Column(Vector(768), nullable=False)


def initialize_database():
    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    Base.metadata.create_all(engine)


def add_message(user_id, role, content):
    with SessionLocal() as session:
        message = Message(
            user_id = user_id,
            role = role,
            content = content
        )
        
        session.add(message)
        session.commit()
 
def get_messages(user_id):
    with SessionLocal() as session:
        messages = (
            session.query(Message)
            .filter(Message.user_id == user_id)
            .order_by(Message.id)
            .all()
        )
        
        return [(message.role, message.content) for message in messages]