import pymongo
client = pymongo.MongoClient("mongodb+srv://nilutpalDAS992:s729Ti-!AxVvvpG@cluster0.n7rw4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "nilutpal", "emailid" : "nilutpaldas@gmail.com", "surname" : "das"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
