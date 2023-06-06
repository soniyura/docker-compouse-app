from pymongo import MongoClient
from pprint import pprint

"""
змінній задається ссилка на порт на якому працює монго по дефолту
//mongo імя сервісу який будем юзать в докер компоус ямл 
"""
MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
pprint(dbs_list)