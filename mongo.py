from pymongo import MongoClient

client = MongoClient()
db_name = client['Sample_db']
collect_name = db_name['student']


class User:
    def __init__(self, name):
        self.name = name


s1 = User("Sourav")
collect_name.insert_one(vars(s1))
