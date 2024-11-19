from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string
#engine = create_engine('mysql+pymysql://user:password@host/database')
engine = create_engine('mysql+pymysql://root:mma123@localhost/mma')
# Create a declarative base class
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# CRUD operations
# Create
new_user = User(name="John Doe", email="johndoe@example.com")
session.add(new_user)
session.commit()

# Read
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email)

# Update
user_to_update = session.query(User).filter_by(id=1).first()
user_to_update.name = "Jane Doe"
session.commit()

# Delete
# user_to_delete = session.query(User).filter_by(id=2).first()
# session.delete(user_to_delete)
# session.commit()

session.close()
