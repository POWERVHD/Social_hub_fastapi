from sqlmodel import create_engine, Session

import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine = create_engine(DATABASE_URL, echo=True)

# Session dependency for FastAPI or general usage
def get_session():
    with Session(engine) as session:
        yield session




#THIS IS THE pg4 ADMIN SETUP IN LOCAL HOST

# while True:              # Since we are using SQLModel to connect to database
#     try:
#         conn = psycopg2.connect(host = 'localhost',database = 'fastapi',user = 'postgres',password = 'Bittoo#110',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()

#         print("Connected Sucessfully")
#         break

#     except Exception as e:
#         print("Connection Failed")
#         print("Error: ",e)
#         time.sleep(2)



#THIS IS supabase db SETUP 

# import os
# from dotenv import load_dotenv

# load_dotenv()

# while True:
#     try:
#         conn = psycopg2.connect(
#             host=os.getenv("DB_HOST"),
#             database=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             port=os.getenv("DB_PORT", 5432),
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("✅ Connected to Supabase PostgreSQL")
#         break

#     except Exception as e:
#         print("❌ Connection Failed")
#         print("Error:", e)
#         time.sleep(2)





