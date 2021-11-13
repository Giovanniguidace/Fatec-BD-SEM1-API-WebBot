from pymongo import MongoClient


class DataBase:
    def __init__(self):
        db = MongoClient('mongodb+srv://admin:admin@cluster0-vuh1j.azure.mongodb.net/test?retryWrites=true&w=majority')
        db = db.get_database('BD_EMPRESAS')
        self.collection = db.empresas
        self.collection.count_documents({})

    def insertOne(self, empresas):
        self.collection.insert_one(empresas)

    def insertMultiple(self, empresas):
        self.collection.insert_many(empresas)