import pymongo
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://root:password@localhost:27017/')
db = client['twitter']
collection = db['tweets']

data = list(collection.find().limit(10))

df = pd.DataFrame(data)
print(df)
