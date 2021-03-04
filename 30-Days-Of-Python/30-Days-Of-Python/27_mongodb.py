import pymongo

print('---------- Connecting Flask application to MongoDB Cluster ----------')
uri = "mongodb://root:123456@127.0.0.1/admin?authMechanism=SCRAM-SHA-1"
client = pymongo.MongoClient(uri)

dblist = client.list_database_names()
print(dblist)

print('---------- Creating a database and collection ----------')
# db=client['example'] # be created if db(example) doesn't exist.
db = client.example  # be created if db(example) doesn't exist.
# db.users.insert_one({'name': 'Zhang San', 'country': 'China', 'city': 'Hangzhou', 'age': 22})
print(client.list_database_names())

print('---------- Inserting many documents to collection ----------')
# users = [
#     {'name': 'Zhang San', 'country': 'China', 'city': 'Hangzhou', 'age': 22},
#     {'name': 'Li Si', 'country': 'China', 'city': 'Shanghai', 'age': 25},
#     {'name': 'Wang Wu', 'country': 'American', 'city': 'Washington', 'age': 28}
# ]
#
# for user in users:
#     db.users.insert_one(user)

print('---------- MongoDB Find ----------')
print('\t---------- find_one({"_id": ObjectId("id"}) ----------')
user = db.users.find_one()  # 返回第一条记录
print(user)

from bson.objectid import ObjectId

user = db.users.find_one({'_id': ObjectId('60408a70cd92f1f3f4581d06')})
print(user)

print('\t---------- find() ----------')
users = db.users.find()
for user in users:
    print(user)
print('\t---------- find({},{}) ----------')
# 指定返回字段，将要返回的字段对应值设置为 1。
# 除了 _id 不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
users = db.users.find({}, {"_id": 0, "name": 1, "country": 1})
for user in users:
    print(user)
# output
# {'name': 'Zhang San', 'country': 'China'}
# {'name': 'Li Si', 'country': 'China'}
# {'name': 'Wang Wu', 'country': 'American'}

print('---------- Find with Query ----------')
query = {'name': 'Li Si'}
users = db.users.find(query)
for user in users:
    print(user)
print('\t---------- 高级查询 ----------')
query = {'age': {'$gt': 22}}  # 查找年龄大于22的用户
users = db.users.find(query)
for user in users:
    print(user)
print('\t---------- 使用正则表达式查询 ----------')
query = {"name": {"$regex": "^W"}}  # 查找姓名首字母为W的用户
users = db.users.find(query)
for user in users:
    print(user)

print('---------- Limiting documents ----------')
users = db.users.find().limit(2)
for user in users:
    print(user)

print('---------- Find with sort ----------')
print('\t---------- 升序 ----------')
users = db.users.find().sort('name')
for user in users:
    print(user)
print('\t---------- 降序 ----------')
users = db.users.find().sort('name', -1)
for user in users:
    print(user)

print('---------- Update with query ----------')
query = {'name': 'Wang Wu'}
new_value = {'$set': {'age': 30}}
db.users.update_one(query, new_value)
for user in db.users.find():
    print(user)

print('---------- Delete Document ----------')
query = {'name': 'Zhang San'}
db.users.delete_one(query)
for user in db.users.find():
    print(user)

print('---------- Drop a collection ----------')
db.users.drop()
