from pymongo import MongoClient

from project.settings import MONGODB


def connect_db():
    db = MongoClient(**MONGODB['connection'])[MONGODB['dbname']]

    return db


db = connect_db()
