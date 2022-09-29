import pymongo
client = pymongo.MongoClient("mongodb+srv://jkellellu27:Rebirth9616@cluster0.3aqsejm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name" : "judith",
    "email" : "jkell@gmail.com",
    "surname" : "kellellu"
}

db1= client['mongotest']
coll = db1['test']
coll.insert_one(d )