import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port= os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DB']

DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'