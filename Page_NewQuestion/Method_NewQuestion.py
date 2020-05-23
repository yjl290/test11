import os
from Util import Get_Element
from Util import Browser_Controller
from Util import MongoDB_Data
from time import sleep
from selenium.common.exceptions import ElementNotInteractableException
driver =None
from selenium.webdriver.common.action_chains import ActionChains
parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(parent_directory_path)
picture_file = parent_directory_path + u"\\picture\\1.jpg"

class Method_NewQuestion():
    def __init__(self, driver):
        self.driver = driver
        # self.new_question = Get_Element.Search_Page_Elements(self.driver)
        #self.keyword = "复制"

    def currency_method_answer(self, model, elm1, elm2, elm3, elm4, iframe, str):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.move_mouse(model, elm1)
        self.new_question.click_button(model, elm2)
        try:
            self.new_question.click_button(model, elm2)
        except ElementNotInteractableException:
            print(1)
        sleep(1)
        self.new_question.click_button(model, elm3)
        sleep(1)
        self.new_question.click_button(model, elm3)
        sleep(1)
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe(iframe)
        self.driver.find_element('tag name', 'body').send_keys(str)
        self.iframe.switch_to_default_content()
        sleep(1)
        try:
            self.new_question.click_button(model, elm4)
        except ElementNotInteractableException:
            print(2)

    # 备注+保存
    def currency_method_save(self, model, elm1, elm2, elm3, elm4, elm5, elm6, iframe, str):
        Method_NewQuestion.currency_method(self, model, elm1, elm2, elm3, elm4, iframe, str)
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.click_button(model, elm5)
        self.new_question.click_button(model, elm6)

    # 备注+保存+截图
    def currency_method_save_cut(self, model, elm1, elm2, elm3, elm4, elm5, elm6, elm7, elm8, iframe, str):
        Method_NewQuestion.currency_method(self, model, elm1, elm2, elm3, elm4, iframe, str)
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.click_button(model, elm5)
        self.new_question.click_button(model, elm6)
        #排版
        typesetting_name = self.new_question.get_page_element_name(model, elm7)
        sleep(3)
        self.new_question.cut('试题'+typesetting_name)
        self.new_question.click_button(model, elm8)
        #详情
        details_name = self.new_question.get_page_element_name(model, elm8)
        self.new_question.cut('试题'+details_name)
        sleep(1)


    # 选择答案
    def currency_method(self, model, elm1, elm2, elm3, elm4, iframe, str):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.move_mouse(model, elm1)
        sleep(1)
        self.new_question.move_mouse(model, elm1)
        self.new_question.click_button(model, elm2)
        try:
            self.new_question.click_button(model, elm2)
        except ElementNotInteractableException:
            print(3)
        sleep(1)
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe(iframe)
        self.driver.find_element('tag name', 'body').send_keys(str)
        self.iframe.switch_to_default_content()
        sleep(1)
        # try:
        #     self.new_question.click_button(model, elm3)
        # except ElementNotInteractableException:
        #     print(4)

    # 题干、选项
    def currency_method_stem_option(self, model, elm1, elm2, elm3, elm4, elm5, iframe, str, ):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.move_mouse(model, elm1)
        self.new_question.click_button(model, elm2)
        try:
            self.new_question.click_button(model, elm2)
        except ElementNotInteractableException:
            print(5)
        sleep(1)
        try:
            self.new_question.click_button(model, elm3)
        except:
            self.new_question.click_button("NewQuestion", "new_stem_html")
        sleep(1)
        try:
            self.new_question.click_button(model, elm3)
        except:
            self.new_question.click_button("NewQuestion", "new_stem_html")
        sleep(1)
        self.new_question.click_button(model, elm4)
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe(iframe)
        self.driver.find_element('tag name', 'body').send_keys(str)
        self.iframe.switch_to_default_content()
        sleep(1)
        try:
            self.new_question.click_button(model, elm5)
        except ElementNotInteractableException:
            print(6)

    # 题干、选项-上传图片
    def currency_method_stem_picture(self, model, elm1, elm2, elm3, elm4, elm5, elm6,iframe, str):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.move_mouse(model, elm1)
        self.new_question.click_button(model, elm2)
        try:
            self.new_question.click_button(model, elm2)
        except ElementNotInteractableException:
            print(5)
        sleep(1)
        self.new_question.click_button(model, elm3)
        sleep(1)
        self.new_question.click_button(model, elm3)
        sleep(1)
        self.new_question.click_button(model, elm4)

        # self.new_question.click_button(model, elm5)
        self.new_question.input_string(picture_file, model, elm5)
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe(iframe)
        self.driver.find_element('tag name', 'body').send_keys(str)
        self.iframe.switch_to_default_content()
        sleep(1)
        try:
            self.new_question.click_button(model, elm6)
        except ElementNotInteractableException:
            print(6)

    # 选题题干
    def currency_method_stemswitch(self, model, elm1, elm2, elm3, elm4, elm5, elm6,iframe, str):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.click_button(model, elm6)
        Method_NewQuestion.currency_method_stem_option(self, model, elm1, elm2, elm3, elm4, elm5, iframe, str)

    # 录入-新建试题
    def page_switch(self, model, elm1, elm2):
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.move_mouse(model, elm1)
        sleep(1)
        self.new_question.click_button(model, elm2)

