# from Configuration import ConstantConfig
from selenium import webdriver
import unittest
import time
import logging
import traceback
import ddt
from Util.ParseExcel import ParserExcel
excelPath = u"C:\\Users\\Dell\\PycharmProjects\\jiaoyan\\PageElementLocator\\testcase.xlsx"
sheetName =u"Sheet1"

#@ddt.ddt
class TestDataDrivenByExcel(unittest.TestCase):
    #def setUp(self):
        #self.driver = webdriver.Chrome()
   # @ddt.data(* excel.getDataFromSheet())
    def test_dataDrivenByExcel(self):
        self.excel = ParserExcel(excelPath, sheetName).getDataFromSheet()
        #test_data, expect_data = tuple(data)
        for i in self.excel:
            print(i)