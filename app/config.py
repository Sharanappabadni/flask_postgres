import os

user = 'postgres'
password = 'Test@1234'
host = 'localhost'
port= 5432
database = 'books'

DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'