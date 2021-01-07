from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create an engine
engine = create_engine('mysql+mysqlconnector://invitao:secret123@localhost:3306/app_db')
#conn = engine.connect()
#engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

# create the base class for our classes definitions
Base = declarative_base()

# create a configured "Session" class
Session = sessionmaker(bind=engine)

Session.configure(bind=engine)

# create a Session
session = Session()

