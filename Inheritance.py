from pymongo import MongoClient

client = MongoClient()

db_name = client["Sample_db"]
collection_name = db_name["student"]


class Location:
    def __init__(self, state="Odisha", pin=765022, country="India"):
        self.state = state
        self.pin = pin
        self.country = country


class Student(Location):
    def __init__(self, name, dept):
        super().__init__()
        self.name = name
        self.dept = dept
        # self.location = vars(location())

    def update_location(self, state, pin, country):
        super().__init__(state, pin, country)


data = Student("Sourav", "CSE")
data.update_location("Jharkhand",865301,"India")
# print(vars(data))
collection_name.insert_one(vars(data))