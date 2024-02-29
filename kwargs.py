from mongo import MongoClient
client = MongoClient()

db_name = client["Sample_db"]
collection_name = db_name["student"]


class User:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs


s1 = User("Sourav", country_code=+91, phone_no=98272069)
collection_name.insert_one(vars(s1))