from pymongo import MongoClient


class Repository:
    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017")
        self.database = None

    def get_database(self, name):
        self.database = self.client[name]

    def print_collection(self, name):
        collection = self.database[name]
        persons = [person for person in collection.find({})]
        print(persons)

    def print_collection_byfield(self, collection, field):
        collection = self.database[collection]
        persons = [person[field] for person in collection.find({})]
        print(persons)