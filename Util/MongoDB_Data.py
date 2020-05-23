from bson import ObjectId
import pymongo
myclient = pymongo.MongoClient("mongodb://172.17.10.223:27017/")
mydb = myclient["bison_math_new"]
mydb1 = myclient["account"]
mycol_handout = mydb["handout"]
mycol_ItemCart = mydb["ItemCart"]
mycol_division = mydb1["division"]


class Mongo_Data():

    def search_handout_name(self):
        mydoc = mycol_handout.find().sort("mtime", -1).limit(1)
        for x in mydoc:
            if 'handout_file_name' in x.keys():
                self.name = x['handout_file_name']
            else:
                self.name = x['name']
            #print(self.name + '1')
        return self.name

    def search_handout_class_name(self):
        mydoc = mycol_handout.find().sort("mtime", -1).limit(1)
        for x in mydoc:
            self.class_name_num = x['grade']
            if self.class_name_num == 33:
                self.class_name = '年级：初三'
            elif self.class_name_num == 32:
                self.class_name = '年级：初二'
            else:
                self.class_name = '年级：初一'

            list = [self.class_name, ]
        return self.class_name

    def search_handout_attribute(self):
        mydoc = mycol_handout.find().sort("mtime", -1).limit(1)
        for x in mydoc:
            #讲义年级
            self.class_name_num = x['grade']
            if self.class_name_num == 33:
                self.class_name = '年级：初三'
            elif self.class_name_num == 32:
                self.class_name = '年级：初二'
            else:
                self.class_name = '年级：初一'
            #讲义名
            if 'handout_file_name' in x.keys():
                self.name = x['handout_file_name']
            else:
                self.name = x['name']
            #年
            self.year = '年份：' + str(x['year'])
            # 讲义类型
            self.type_name_num = x['classtype']
            if self.type_name_num == 1:
                self.type_name = '类型：短期班'
            elif self.type_name_num == 2:
                self.type_name = '类型：长期班'
            else:
                self.type_name = '类型：公开课'
            # 讲义学季
            self.season_name_num = x['season']
            if self.season_name_num == 1:
                self.season_name = '学季：春季班'
            elif self.season_name_num == 2:
                self.season_name = '学季：暑假班'
            elif self.season_name_num == 3:
                self.season_name = '学季：秋季班'
            else:
                self.season_name = '学季：寒假班'
            # 讲义分校
            self.schoolid = x['division']
            self.school = '所属分校：' + Mongo_Data.school(self, self.schoolid)
            # 讲义创建人
            self.createman = '创建人：' + x['cname']
            self.list = [self.name, self.class_name, self.year, self.type_name, self.season_name, self.school, self.createman]
        return self.list

    def questionbasket(self):
        str = "5e017d1258b4bf000be228e0"
        mydoc = mycol_ItemCart.find({"_id":ObjectId(str)})
        for x in mydoc:
            self.list = x['itemids']
            if self.list:
                self.element = "empty_questionbasket_haveyes"
            else:
                self.element = "empty_questionbasket_yes"
        return self.element

    def school(self, str):
        mydb1 = mycol_division.find({"_id":ObjectId(str)})
        schoolname = ''
        for x in mydb1:
            schoolname = x['name']
        return schoolname

    def handoutid(self):
        # mydoc = mycol_handout.find({},{ "grade", 33})
        list = mycol_handout.find({}, {'deleted':False})
        # count = mycol_handout.find({}, {'deleted':False}).count()
        # newlist = list['deleted':False]
        # print(count)
        for x in list:
            # newlist = x['deleted':False]
            id = x['_id']
            print(id)
        myclient.close()