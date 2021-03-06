from flask import Flask, jsonify, request
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import config

Base = declarative_base()


DATABASE_URI = config.DATABASE_URI
engine = create_engine(DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)
db = Session()


def create_app():
    app = Flask(__name__)
    Base.metadata.create_all(engine)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

    return app


app = create_app()
__import__('app.models')
__import__('app.api')

if __name__ == '__main__':
    app.run()
