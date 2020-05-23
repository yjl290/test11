import pymongo

myclient = pymongo.MongoClient("mongodb://172.17.10.223:27017/")
mydb = myclient["bison_math_new"]
mycol = mydb["handout"]
list = mycol.find({}, {"grade": 33})
for x in list:
    print(x)
    print(x)
    print(1)