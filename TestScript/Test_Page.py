from time import sleep

from selenium import webdriver
from Page_Login import Login_Page
from Page_Handout import Search_Handout, Method_Handout
from Page_SerachQuestion import Search_Question
from Util import MongoDB_Data
from Util import ParseExcel
from Page_NewQuestion import New_Question
from Page_NewQuestion import Method_NewQuestion
from Page_RecordPaper import New_OmegaPaper
import unittest

class Search_Page(unittest.TestCase):

    def setUp(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()  # 最大化浏览器窗口
        self.chrome_driver.implicitly_wait(8)
        self.value = ParseExcel.ParseExcel()
        value = self.value.getlogin_value()
        self.chrome_driver.get(value['url'])
        self.loginname = value['loginname']
        self.password = value['password']


    def test_handout_page(self):
        #登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)

        # js1 = "document.documentElement.scrollTop"
        # a = self.chrome_driver.execute_script(js1)
        # print(a)

        # self.assertTrue("yangjunlin@lexue.com" in self.chrome_driver.page_source)
        #self.assertTrue("yngjunlin@lexue.com" in self.login)

        # # #录试卷-真题试卷-插入试题
        # self.recordpaper = New_OmegaPaper.New_OmegaPaper(self.chrome_driver)
        # self.recordpaper.switch_omegaPaper()
        # # self.recordpaper.new_omegaPaper()
        # self.recordpaper.edit_omegaPaper()
        # # self.recordpaper.new_omegaPaper_add()
        # self.edit_handout1 = Method_Handout.Method_Handout(self.chrome_driver)
        # # self.edit_handout1.insert_question()
        # # self.edit_handout1.replace_question()
        # # self.edit_handout1.delete_question()
        # # self.edit_handout1.adaptation_question()
        # # self.edit_handout1.correction_question()
        # # self.edit_handout1.details_question()
        # # # self.edit_handout1.resemble_question()
        # self.edit_handout1.open_question()
        #
        # self.recordpaper.edit_omegaPaper_batch()

        # 操作试题篮
        # self.newquestion = Search_Question.Search_Question(self.chrome_driver)
        # self.newquestion.join_questionbasket()

        # # 新建试题
        # self.newquestion = New_Question.New_Question(self.chrome_driver)
        # self.newquestion.page_Navigation()
        # self.newquestion.choice_question_next()
        # # self.newquestion.completion_question_next()
        # # self.newquestion.answer_question_next()
        # # self.newquestion.answer_questionlong()
        # # self.newquestion.choice_question()

        # 我的讲义
        self.handout = Search_Handout.Handout(self.chrome_driver)
        self.handout.screen_condition()

        self.handout.screen_button_nanjing()
        sleep(5)
        # # self.handout_name = self.handout.get_handout_name()
        # self.mongo_handout_name = MongoDB_Data.Mongo_Data().search_handout_name()
        # # self.assertEqual(self.mongo_handout_name, self.handout_name)
        # # self.class_name = self.handout.get_class_name()
        # # self.mongo_handout_class_name = MongoDB_Data.Mongo_Data().search_handout_class_name()
        # # self.assertEqual(self.mongo_handout_class_name, self.class_name)
        # # self.handout.update_time_handout()
        # # self.handout.update_time_handout()
        # # self.handout.attribute_handout()
        # # self.handout.copy_handout()
        # # self.handout.delete_handout()
        # # self.handout.add_handout()
        # self.handout.screen_search_input()
        # self.handout.button_search()
        # self.handout.edit_handout()


    def tearDown(self):
        self.chrome_driver.quit()


if __name__ == "__main__":
    unittest.main()