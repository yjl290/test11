from time import sleep
from Util import Get_Element


class LeHandout():

    def __init__(self, driver):
        self.driver = driver
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.keyword = "自动测试讲义名"


    def screen_condition(self):
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.search_handout.move_top()
        self.search_handout.move_mouse("Navigation", "move_mouse_lejiaoyan")
        sleep(1)
        self.search_handout.click_button("Navigation", "move_mouse_lehandout")
        sleep(2)

    def keyword_search(self):
        self.search_handout.input_string("自动", "lejiaoyan", "lejiaoyan_keyword")
        sleep(1)
        self.search_handout.click_button("lejiaoyan", "lejiaoyan_search")

    def look_handout(self):
        self.search_handout.click_button("lejiaoyan", "lejiaoyan_handoutsetname")
        self.search_handout.switch_new_page()
        self.search_handout.click_button("lejiaoyan", "lejiaoyan_handoutname")
        self.search_handout.switch_page_three()
        self.search_handout.move_bottom()
        state = self.search_handout.isElementExist("lejiaoyan", "lejiaoyan_expandname")
        print(state)
        if state == True:
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look1")
            class_value1 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look1_value").get_attribute('class')
            print(class_value1)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look1_open")
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look2")
            class_value2 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look2_value").get_attribute('class')
            print(class_value2)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look3")
            class_value3 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look3_value").get_attribute('class')
            print(class_value3)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look4")
            class_value4 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look4_value").get_attribute('class')
            print(class_value4)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look5")
            class_value5 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look5_value").get_attribute('class')
            print(class_value5)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look6")
            class_value6 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look6_value").get_attribute('class')
            print(class_value6)
            self.search_handout.click_button("lejiaoyan", "lejiaoyan_look7")
            class_value7 = self.search_handout.get_page_element("lejiaoyan",
                                                                "lejiaoyan_look7_value").get_attribute('class')
            print(class_value7)
            self.search_handout.switch_page_close3_return2()
            self.search_handout.switch_page_close()
            dict = {'state': state, 'class_value1': class_value1, 'class_value2': class_value2, 'class_value3': class_value3,
                 'class_value4': class_value4, 'class_value5': class_value5, 'class_value6': class_value6, 'class_value7': class_value7}
            return dict
        else:
            self.search_handout.switch_page_close3_return2()
            self.search_handout.switch_page_close()
            dict = state
            return dict


