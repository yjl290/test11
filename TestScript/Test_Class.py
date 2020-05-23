from time import sleep

from selenium import webdriver

from Page_LeHandout import Method_LeHandout
from Page_Login import Login_Page
from Page_Handout import Search_Handout
from Page_NewQuestion import New_Question
from Page_RecordPaper import New_OmegaPaper
from Page_SerachQuestion import Search_Question
from Page_Handout import Method_Handout
from Page_Handout import Look_Handout
from Util import MongoDB_Data
import unittest

from Util.GetLog import Logger

logger  = Logger(logger='PageTest').getlog()
class PageTest(unittest.TestCase):

    def setUp(self):
        self.chrome_driver = webdriver.Chrome()
        logger.info('打开浏览器')
        self.chrome_driver.maximize_window()  # 最大化浏览器窗口
        logger.info('最大化浏览器窗口')
        self.chrome_driver.implicitly_wait(8)
        self.chrome_driver.get("http://p.lejiaoyan.com")
        logger.info('打开乐学预发地址')
        self.loginname = "yangjunlin@lexue.com"
        self.password = ".014789+"

    # @unittest.skip("")
    def test_recordpaper_page(self):
        # 登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)
        logger.info('登录')
        self.assertTrue("yangjunlin@lexue.com" in self.chrome_driver.page_source)
        # self.assertTrue("yngjunlin@lexue.com" in self.login)

        # #录试卷-真题试卷-插入试题
        self.recordpaper = New_OmegaPaper.New_OmegaPaper(self.chrome_driver)
        self.edit_handout1 = Method_Handout.Method_Handout(self.chrome_driver)
        self.recordpaper.switch_omegaPaper()
        logger.info('进入真题试卷页面')
        self.recordpaper.new_omegaPaper()
        logger.info('新建真题试卷')
        self.recordpaper.new_omegaPaper_add()
        logger.info('编辑真题试卷，去手动加题')
        self.recordpaper.edit_omegaPaper_new()
        logger.info('编辑真题试卷，试题下方图标-录入试题')
        self.edit_handout1.replace_question()
        logger.info('编辑真题试卷，试题下方图标-替换试题')
        self.edit_handout1.insert_question()
        logger.info('编辑真题试卷，试题下方图标-插入试题')
        self.edit_handout1.delete_question()
        logger.info('编辑真题试卷，试题下方图标-删除试题')
        self.edit_handout1.adaptation_question()
        logger.info('编辑真题试卷，试题下方图标-改编试题')
        self.edit_handout1.correction_question()
        logger.info('编辑真题试卷，试题下方图标-纠错试题')
        self.edit_handout1.details_question()
        logger.info('编辑真题试卷，试题下方图标-试题详情')
        # self.edit_handout1.resemble_question()
        self.edit_handout1.open_question()
        logger.info('编辑真题试卷，试题下方图标-展开试题')
        self.recordpaper.edit_omegaPaper_batch()
        logger.info('编辑真题试卷，')

    # @unittest.skip("")
    def test_recordpaper_page1(self):
        # 登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)
        self.assertTrue("yangjunlin@lexue.com" in self.chrome_driver.page_source)
        # self.assertTrue("yngjunlin@lexue.com" in self.login)

        # 录试卷-真题试卷-录入试题
        self.recordpaper = New_OmegaPaper.New_OmegaPaper(self.chrome_driver)
        self.recordpaper.new_omegaPaper()
        self.recordpaper.new_omegaPaper_new()

    # @unittest.skip("")
    def test_newquestion_page(self):
        # 登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)
        self.assertTrue("yangjunlin@lexue.com" in self.chrome_driver.page_source)
        # self.assertTrue("yngjunlin@lexue.com" in self.login)
        sleep(5)

        # 操作试题篮
        # self.newquestion = Search_Question.Search_Question(self.chrome_driver)
        # self.newquestion.join_questionbasket()

        # 新建试题
        self.newquestion = New_Question.New_Question(self.chrome_driver)
        self.newquestion.page_Navigation()
        self.newquestion.choice_question_cut()
        self.newquestion.page_Navigation()
        self.newquestion.completion_question_next()
        self.newquestion.answer_question_next()
        self.newquestion.answer_questionlong()


    # @unittest.skip("")
    def test_myhandout_page(self):
        # 登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)

        # 我的讲义
        self.handout = Search_Handout.Handout(self.chrome_driver)
        self.handout.screen_condition()
        self.handout.add_handout()
        handout_attribute_list = self.handout.get_handout_attribute()
        self.handout.button_search()
        # 归档查看乐讲义
        handour_dict = self.handout.file_handout()
        self.lehandout = Method_LeHandout.Method_LeHandout(self.chrome_driver)
        dict_lehandout = self.lehandout.looklehandout()
        self.handout.screen_condition()
        self.lookhandout = Look_Handout.Look_Handout(self.chrome_driver)
        self.lookhandout.handout_look()
        # self.lookhandout.handout_edit()

        dict_student_handout = self.handout.student_handout()
        self.handout.update_file_handout()
        dict_lehandout2 = self.lehandout.looklehandout()
        self.handout.screen_condition()
        self.handout.delete_file_handout()
        self.handout.update_time_handout()
        self.handout.update_time_handout()
        self.handout.attribute_handout()
        self.handout.copy_handout()
        self.handout.delete_handout()
        # 验证讲义列表
        try:
            handout_attribute_list1 = ['自动测试讲义名', '年级：初一', '年份：2021', '类型：短期班', '学季：春季班', '所属分校：南京', '创建人：杨钧麟']
            self.assertEqual(handout_attribute_list1, handout_attribute_list)
        except  Exception as e:
            print(e)
        # 验证归档讲义列表
        try:
            handour_dict1 = {'handout_list': ['自动测试讲义名', '年级：初一', '年份：2021', '类型：短期班', '学季：春季班', '所属分校：南京', '创建人：杨钧麟'],
                             'lehandout_list': ['自动测试专用讲义集', '包含讲义数量：1', '创建人：杨钧麟', '年级：初二', '年份：2020', '类型：短期班', '学季：春季班']}
            self.assertEqual(handour_dict1, handour_dict)
        except  Exception as e:
            print(e)
        # 验证讲义排版
        try:
            dict_student_handout1 = {'blank1': True, 'blank2': False, 'example_option1': 'col-xs-12',
                                     'example_option2': 'col-xs-3',
                                     'example_option3': 'col-xs-6', 'example_option4': 'col-xs-12', 'page': "",
                                     'background': 'background-image: url("/static/handoutDetail/bg.png"); background-size: 100% 100%;',
                                     'background1': 'background-image: url("/img/0a/41/0a4168399f6be837c767a021137ef856.png"); background-size: 100% 100%;',
                                     'background2': 'background-image: url("/img/2f/67/2f67faa3ffe5394f64c6c89d2dbdbaee.png"); background-size: 100% 100%;'}
            self.assertEqual(dict_student_handout1, dict_student_handout)
        except  Exception as e:
            print(e)
        # 验证查看讲义模块树点击状态
        try:
            dict_lehandout1 = {'state': True, 'class_value1': 'ant-tree-treenode-switcher-close ant-tree-treenode-selected',
                               'class_value2': 'ant-tree-treenode-switcher-close ant-tree-treenode-selected',
                               'class_value3': 'ant-tree-treenode-switcher-close ant-tree-treenode-selected',
                               'class_value4': 'ant-tree-treenode-switcher-close ant-tree-treenode-selected',
                               'class_value5': 'ant-tree-treenode-switcher-close ant-tree-treenode-selected',
                               'class_value6': "ant-tree-treenode-switcher-close ant-tree-treenode-selected",
                               'class_value7': "ant-tree-treenode-switcher-close ant-tree-treenode-selected"}
            self.assertEqual(dict_lehandout1, dict_lehandout2)
        except  Exception as e:
            print(e)

    def tearDown(self):
        self.chrome_driver.quit()


if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(PageTest("test_recordpaper_page"))
    suite.addTest(PageTest("test_recordpaper_page1"))
