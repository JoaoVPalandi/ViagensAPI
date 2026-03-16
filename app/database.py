from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = f'mysql+pymysql://{getenv("DB_USER")}:{getenv("DB_PSWD")}@{getenv("DB_HOST")}'


engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()


# DATABASE_URL = f'mysql+pymysql://root:admin@localhost/series_api'
DATABASE_URL = f'mysql+pymysql://{getenv("DB_USER")}:{getenv("DB_PSWD")}@{getenv("DB_HOST")}/{getenv("DB_NAME")}'

# Criar um 'Motor' que fará o gerenciamneto da conexão
engine = create_engine(DATABASE_URL)

# Criando uma sessão para executar os comandos SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria um objeto da base de dados manipulada pelo
# SQLAlchemy
Base =  declarative_base()

# Injeção de dependência para criar uma sessão e garantir que ela 
# seja fechada após o uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()