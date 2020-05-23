from Util import MongoDB_Data
from Util import ParseExcel
import unittest

class Search_Page(unittest.TestCase):


    def test_alogin_page(self):
       self.name =  MongoDB_Data.Mongo_Data()
       # self.list = self.name.questionbasket()
       # print(self.list)
       # self.list = self.name.questionbasket()
       # print(self.list)
       self.name.handoutid()
    # def test_alogin_page(self):
    #     self.testexcel = ParseExcel.ParserExcel()
    #     self.testexcel.readExel()
    #     self.testexcel.writeExcel()



if __name__ == "__main__":
    unittest.main()