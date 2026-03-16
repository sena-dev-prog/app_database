from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from dotenv import load_dotenv
import os

#load_dotenv(dotenv_path='.env')

# Construir la URL de conexión
#DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_NAME')}"
#DB_URL = f"mysql+pymysql://prueba:{os.getenv('DB_PASSWORD')}@localhost:3306/prueba"
# DB_URL = f"mysql+pymysql://prueba:prueba@localhost:3306/prueba"
DB_URL = f"mysql+pymysql://root:yUjjseWVPGTBmWVjrKyZeoLDtGaKGGwt@caboose.proxy.rlwy.net:59513/railway"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        