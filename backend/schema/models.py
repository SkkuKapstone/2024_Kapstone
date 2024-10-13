from sqlalchemy import Column, String, Integer

from backend.db.session import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, name="user_id", primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

class Session(Base):
    __tablename__ = "session"
    session_id = Column(Integer, name="session_id", primary_key=True)
    session_name = Column(String(20))
    # user_id = Column() Foreign key
    # create_time = Column(TIME_TIMEZONE)

class Document(Base):
    __tablename__ = "document"

    document_id = Column(Integer, name="document_id", primary_key=True)
    document_name = Column(String(50))
    # session_id = foreign key

class Quiz(Base):
    __tablename__ = "quiz"

    quiz_id = Column(Integer, name="quiz_id", primary_key=True)
    # session_id = Column() Foreign key