# import requests
# endpoint = "http://127.0.0.1:8000/users/me"
# headers = {"Authorization": "Bearer alice"}
from dotenv import load_dotenv

load_dotenv()
# print(requests.get(endpoint,  headers=headers).json())
import rsa
# publicKey, privateKey = rsa.newkeys(256)
#
# print(publicKey)
# print("\n\n",privateKey)
import os
# # this is the string that we will be encrypting
publicKey = eval(os.getenv('PASSWORD_PUBLIC_KEY'))
# print(publicKey)
publicKey =rsa.PublicKey(publicKey[0], publicKey[1])
message = "hello geeks"

encMessage = rsa.encrypt(message.encode(),publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

privateKey = rsa.PrivateKey(67634772045169674503796337432762216161803426619267504065148718510123767184847, 65537, 67047558939691829243978827995356755046088569083245454287208603218710256811457, 63792476103509172509452648129482610955533, 1060231177348031179535638235447254859)

encMessage = b'\x85\xcf\xc4{\xd0TN\xa3\x05\xb7l\xd4\xf5a\xb8\x0e&\x15\xd8\x17=\xdc*6c\xa8S\x04\x94\x94\xf5\xc4'
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)



import os

from sqlalchemy import (Column, DateTime, Integer, String, Table, create_engine, MetaData)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database

# Database url if none is passed the default one is used
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost/fastapi")
# DATABASE_URL = "postgresql://root:root@localhost/testzaps"
# # SQLAlchemy
# from sqlalchemy.orm import sessionmaker
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# metadata = MetaData()
# blogs = Table(
#     "blogs",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String(50)),
#     Column("description", String(50)),
#     Column("created_date", DateTime, default=func.now(), nullable=False)
# )
#
# # Databases query builder
# print(engine.url)