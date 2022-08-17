import pymongo
client = pymongo.MongoClient("mongodb+srv://laizinv:<PASSWORD>@cluster0.j7mdzpr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d ={
    "name" : "laizin",
    "number" : "8113937942",
    "mail_id" : "laizin2107@gmail.com"
   }
database1 = client['test_database']
collections_1 = database1['test_database']
collections_1.insert_one(d)
