from Util import Get_Element
from Page_Handout import Edit_Handout
from Page_Handout import Method_Handout
from time import sleep

driver = None


class Handout():

    def __init__(self, driver):
        self.driver = driver
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.keyword = "自动测试讲义名"

    # 搜索按钮
    def button_search(self):
        try:
            self.search_handout.click_button("handout", "button_search")
        except:
            self.search_handout.click_script("handout", "button_search")

    # 重置按钮
    def button_reset(self):
        self.search_handout.click_button("handout", "button_reset")

    # 我的讲义
    def screen_condition(self):
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.search_handout.move_top()
        self.search_handout.move_mouse("Navigation", "move_mouse_my")
        sleep(1)
        self.search_handout.click_button("Navigation", "button_myhandout")
        sleep(1)

    def screen_class_31(self):
        self.search_handout.click_button("handout", "button_class_31")

    def screen_class_32(self):
        self.search_handout.click_button("handout", "button_class_32")

    def screen_class_33(self):
        self.search_handout.click_button("handout", "button_class_33")

    def screen_class_all(self):
        self.search_handout.click_button("handout", "button_class_all")

    def screen_year_2021(self):
        self.search_handout.click_button("handout", "button_year_2021")

    def screen_year_2020(self):
        self.search_handout.click_button("handout", "button_year_2020")

    def screen_year_2019(self):
        self.search_handout.click_button("handout", "button_year_2019")

    def screen_year_2018(self):
        self.search_handout.click_button("handout", "button_year_2018")

    def screen_year_2017(self):
        self.search_handout.click_button("handout", "button_year_2017")

    def screen_year_2016(self):
        self.search_handout.click_button("handout", "button_year_2016")

    def screen_year_2015(self):
        self.search_handout.click_button("handout", "button_year_2015")

    def screen_year_2014(self):
        self.search_handout.click_button("handout", "button_year_2014")

    def screen_year_2013(self):
        self.search_handout.click_button("handout", "button_year_2013")

    def screen_year_2012(self):
        self.search_handout.click_button("handout", "button_year_2012")

    def screen_year_all(self):
        self.search_handout.click_button("handout", "button_year_all")

    def screen_type_short(self):
        self.search_handout.click_button("handout", "button_type_short")

    def screen_type_long(self):
        self.search_handout.click_button("handout", "button_type_long")

    def screen_type_public(self):
        self.search_handout.click_button("handout", "button_type_public")

    def screen_type_all(self):
        self.search_handout.click_button("handout", "button_type_all")

    def screen_Season_spring(self):
        self.search_handout.click_button("handout", "button_Season_spring")

    def screen_Season_summer(self):
        self.search_handout.click_button("handout", "button_Season_summer")

    def screen_Season_Autumn(self):
        self.search_handout.click_button("handout", "button_Season_Autumn")

    def screen_Season_winter(self):
        self.search_handout.click_button("handout", "button_Season_winter")

    def screen_Season_all(self):
        self.search_handout.click_button("handout", "button_Season_all")
        # search_handout.click_button("handout", "button_date")
        # search_handout.click_button("handout", "button_before_year")
        # search_handout.click_button("handout", "button_after_year")
        # search_handout.click_button("handout", "button_february")

    def screen_button_nanjing(self):
        self.search_handout.click_button("handout", "button_school")
        sleep(3)
        # element = self.search_handout.get_page_element("handout", "button_school")
        # self.search_handout.select_by_index(element, '1')
        # self.search_handout.click_button("handout", "button_nanjing")

    # 关键字
    def screen_search_input(self):
        self.search_handout.clear_input("handout", "search_input")
        self.search_handout.input_string(self.keyword, "handout", "search_input")

    # 添加讲义
    def add_handout(self):
        self.search_handout.click_button("handout", "handout_add")
        self.search_handout.input_string('自动测试讲义名', "handout", "handout_add_name")
        sleep(1)
        self.search_handout.click_script("handout", "handout_add_class")
        sleep(1)
        self.search_handout.click_button("handout", "handout_add_class31")
        self.search_handout.click_script("handout", "handout_add_school")
        sleep(1)
        self.search_handout.click_button("handout", "handout_add_school1")
        self.search_handout.click_script("handout", "handout_add_year")
        sleep(1)
        self.search_handout.click_button("handout", "handout_add_year1")
        self.search_handout.click_script("handout", "handout_add_type")
        sleep(1)
        self.search_handout.click_button("handout", "handout_add_type1")
        self.search_handout.click_script("handout", "handout_add_season")
        sleep(1)
        self.search_handout.click_button("handout", "handout_add_season1")
        self.search_handout.click_button("handout", "handout_add_ok")
        sleep(1)
        # 编辑添加讲义
        self.search_handout.switch_new_page()
        self.search_handout.click_button("handout", "new_edit_handout_name")
        sleep(1)
        self.search_handout.input_string('自测', "handout", "new_edit_handout_nameinput")
        self.search_handout.click_button("handout", "new_edit_handout_modulename")
        sleep(1)
        self.search_handout.input_string('自测', "handout", "new_edit_handout_modulenameinput")
        # 添加删除知识点
        self.search_handout.click_button("handout", "new_edit_handout_points")
        self.search_handout.click_button("handout", "new_edit_handout_points_delete")
        sleep(1)
        self.search_handout.click_button("handout", "new_edit_handout_points_deleteyes")

        self.search_handout.click_button("handout", "new_edit_handout_text")
        self.search_handout.click_button("handout", "new_edit_handout_text_delete")
        sleep(1)
        self.search_handout.click_button("handout", "new_edit_handout_text_deleteyes")

        self.search_handout.click_button("handout", "new_edit_handout_example")
        self.search_handout.click_button("handout", "new_edit_handout_example_delete")

        self.search_handout.click_button("handout", "new_edit_handout_exercises")
        self.search_handout.click_button("handout", "new_edit_handout_exercises_delete")

        self.search_handout.click_button("handout", "new_edit_handout_consolidate")
        self.search_handout.click_button("handout", "new_edit_handout_consolidate_delete")
        self.search_handout.switch_page_close()
        # edit_handout = Edit_Handout.Edit_Handout(self.driver)
        # edit_handout.add_points()
        # edit_handout.add_text()

    # 获取讲义名称
    def get_handout_attribute(self):
        self.handoutname = self.search_handout.get_page_element_name("handout", "new_handout_name")
        self.classes = self.search_handout.get_page_element_name("handout", "new_handout_classes")
        self.year = self.search_handout.get_page_element_name("handout", "new_handout_year")
        self.type = self.search_handout.get_page_element_name("handout", "new_handout_type")
        self.season = self.search_handout.get_page_element_name("handout", "new_handout_season")
        self.school = self.search_handout.get_page_element_name("handout", "new_handout_school")
        self.createman = self.search_handout.get_page_element_name("handout", "new_handout_createman")
        self.list = [self.handoutname, self.classes, self.year, self.type, self.season, self.school, self.createman]
        return self.list

    # 获取讲义列表年级名称
    def get_class_name(self):
        self.class_name = self.search_handout.get_page_element_name("handout", "handout_class_name")
        return self.class_name

    # 更新时间
    def update_time_handout(self):
        self.search_handout.click_button("handout", "handout_update_time")

    # 属性
    def attribute_handout(self):
        self.search_handout.move_between()
        self.search_handout.click_button("handout", "handout_attribute")
        # self.search_handout.clear_input("handout", "handout_attribute_name")
        # self.search_handout.input_string('测试讲义名', "handout", "handout_attribute_name")
        # self.search_handout.click_button("handout", "handout_attribute_class")
        # sleep(1)
        # self.search_handout.click_button("handout", "handout_attribute_school")
        # sleep(1)
        # self.search_handout.click_button("handout", "handout_attribute_year")
        # sleep(1)
        # self.search_handout.click_button("handout", "handout_attribute_type")
        # sleep(1)
        # self.search_handout.click_button("handout", "handout_attribute_season")
        sleep(1)
        self.search_handout.click_button("handout", "handout_attribute_ok")
        sleep(1)

    # 复制
    def copy_handout(self):
        self.search_handout.click_button("handout", "handout_copy")
        sleep(1)

    # 删除
    def delete_handout(self):
        # self.search_handout.move_top()
        # Handout.button_reset(self)
        # self.search_handout.input_string("自动测试讲义名1", "handout", "search_input")
        sleep(2)
        # Handout.button_search(self)
        # self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        self.search_handout.click_button("handout", "handout_delete")
        try:
            self.search_handout.click_button("handout", "handout_delete")
        except:
            print()
        sleep(1)
        self.search_handout.click_button("handout", "handout_delete_yes")

        # Handout.screen_search_input()

    # 其他操作-移动
    def other_handout(self):
        self.search_handout.move_mouse("Navigation", "move_mouse_handout_other")
        sleep(1)
        self.search_handout.click_button("Navigation", "handout_move")
        sleep(1)

    # 学生版排版
    def student_handout(self):
        sleep(2)
        self.search_handout.move_between()
        try:
            sleep(1)
            self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
        except:
            self.search_handout.move_mouse("handout", "move_mouse_handout_other")
        self.search_handout.click_button("handout", "handout_student")
        self.search_handout.switch_new_page()
        sleep(3)
        self.search_handout.click_script("handout", "handout_student_points_addBlank")
        self.search_handout.click_script("handout", "handout_student_yes")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        state1 = self.search_handout.isElementExist("handout", "handout_student_points_Blank2")
        print(state1)
        self.search_handout.click_script("handout", "handout_student_points_deleteBlank")
        self.search_handout.click_script("handout", "handout_student_yes")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        state2 = self.search_handout.isElementExist("handout", "handout_student_points_Blank2")
        print(state2)
        # self.search_handout.input_string(5, "handout", "handout_student_points_input")
        # self.search_handout.enter_input("handout", "handout_student_points_input")
        # self.search_handout.click_script("handout", "handout_student_yes")
        # self.search_handout.Refresh()
        # self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        # sleep(3)
        self.search_handout.move_between()

        try:
            question_class = self.search_handout.get_page_element("handout", "handout_student_question2").get_attribute('class')
        except:
            question_class = self.search_handout.get_page_element("handout", "handout_student_question21").get_attribute('class')
        print(question_class)
        sleep(10)
        question_id = question_class.split('_')[2]
        element = '//*[@id="'+ question_id +'_0"]'

        # class_value1 = self.search_handout.get_page_element("handout", element).get_attribute('class')
        class_value1 = self.driver.find_element_by_xpath(element).get_attribute('class')
        print(class_value1)
        # self.search_handout.click_script("handout", element)
        elements = self.driver.find_element_by_xpath(element)
        self.driver.execute_script("arguments[0].click();", elements)
        self.search_handout.click_script("handout", "handout_student_yes")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        self.search_handout.move_between()
        # class_value2 = self.search_handout.get_page_element("handout", element).get_attribute('class')
        class_value2 = self.driver.find_element_by_xpath(element).get_attribute('class')
        print(class_value2)
        # self.search_handout.click_script("handout",element)
        elements = self.driver.find_element_by_xpath(element)
        self.driver.execute_script("arguments[0].click();", elements)
        self.search_handout.click_script("handout", "handout_student_yes")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        self.search_handout.move_between()
        # class_value3 = self.search_handout.get_page_element("handout", element).get_attribute('class')
        class_value3 = self.driver.find_element_by_xpath(element).get_attribute('class')
        print(class_value3)
        # self.search_handout.click_script("handout", element)
        elements = self.driver.find_element_by_xpath(element)
        self.driver.execute_script("arguments[0].click();", elements)
        self.search_handout.click_script("handout", "handout_student_yes")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        self.search_handout.move_between()
        # class_value4 = self.search_handout.get_page_element("handout", element).get_attribute('class')
        class_value4 = self.driver.find_element_by_xpath(element).get_attribute('class')
        print(class_value4)
        state = self.search_handout.get_page_element_name("handout", "handout_student_page")
        print(state == "第1页")
        self.search_handout.click_script("handout", "handout_student_page_hide")
        pagestate1 = self.search_handout.get_page_element_name("handout", "handout_student_page")
        print(pagestate1 == "")
        background = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
            'style')
        print(background)
        self.search_handout.click_script("handout", "handout_student_template")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        background1 = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
            'style')
        print(background1)
        # self.search_handout.cut("学生版排版-普通模板")
        self.search_handout.click_script("handout", "handout_student_odd_even")
        sleep(1)
        self.search_handout.click_script("handout", "handout_student_template_odd_even")
        self.search_handout.Refresh()
        self.search_handout = Get_Element.Search_Page_Elements(self.driver)
        sleep(3)
        background2 = self.search_handout.get_page_element("handout", "handout_student_background").get_attribute(
            'style')
        print(background2)
        self.search_handout.move_between()
        # self.search_handout.cut("学生版排版-奇偶模板")
        self.search_handout.switch_page_close()
        # true  false  true、col-xs-12  3  6  12、""
        dict = {'blank1': state1, 'blank2': state2, 'example_option1': class_value1, 'example_option2': class_value2,
                'example_option3': class_value3, 'example_option4': class_value4, 'page': pagestate1,
                'background': background,'background1': background1, 'background2': background2}
        return dict
        # 归档
    def file_handout(self):
        sleep(2)
        Handout.screen_search_input(self)
        Handout.button_search(self)
        self.search_handout.move_between()
        self.search_handout.move_mouse("handout", "move_mouse_handout_other")
        self.search_handout.click_button("handout", "handout_file")
        sleep(1)
        self.search_handout.input_string("自动", "handout", "handout_file_input")
        self.search_handout.click_button("handout", "handout_file_search")
        sleep(1)
        self.search_handout.click_button("handout", "handout_file_file")
        sleep(1)
        try:
            self.search_handout.click_button("handout", "handout_file_file_yes")
        except Exception:
            print(1)
        sleep(2)
        self.search_handout.click_button("handout", "handout_file_file_file")
        handout_list = Handout.get_file_handout_attribute(self)
        lehandout_list = Handout.get_file_lehandout_attribute(self)
        sleep(1)
        self.search_handout.click_button("handout", "handout_file_file_file_yes")
        return {'handout_list':handout_list, 'lehandout_list':lehandout_list}

    def update_file_handout(self):
        Handout.screen_search_input(self)
        Handout.button_search(self)
        self.search_handout.move_between()
        self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
        self.search_handout.click_button("handout", "handout_file")
        sleep(1)
        self.search_handout.click_button("handout", "handout_file_updatefile")
        sleep(1)
        try:
            self.search_handout.click_button("handout", "handout_file_updatefile_yes")
        except Exception:
            print(1)
        sleep(2)

    def delete_file_handout(self):
        Handout.screen_search_input(self)
        Handout.button_search(self)
        self.search_handout.move_between()
        self.search_handout.move_mouse("handout", "move_mouse_handout_other1")
        self.search_handout.click_button("handout", "handout_file")
        sleep(1)
        self.search_handout.click_button("handout", "handout_file_delete")
        state = self.search_handout.isElementExist("handout", "handout_file_file_file")
        print(state)

    def get_file_handout_attribute(self):
        self.handoutname = self.search_handout.get_page_element_name("handout", "file_verification_handout_name")
        self.classes = self.search_handout.get_page_element_name("handout", "file_verification_handout_classes")
        self.year = self.search_handout.get_page_element_name("handout", "file_verification_handout_year")
        self.type = self.search_handout.get_page_element_name("handout", "file_verification_handout_type")
        self.season = self.search_handout.get_page_element_name("handout", "file_verification_handout_season")
        self.school = self.search_handout.get_page_element_name("handout", "file_verification_handout_school")
        self.createman = self.search_handout.get_page_element_name("handout", "file_verification_handout_createman")
        self.list = [self.handoutname, self.classes, self.year, self.type, self.season, self.school, self.createman]
        return self.list

    def get_file_lehandout_attribute(self):
        self.handoutname = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_name")
        self.classes = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_classes")
        self.year = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_year")
        self.type = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_type")
        self.season = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_season")
        self.school = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_school")
        self.createman = self.search_handout.get_page_element_name("handout", "file_verification_lehandout_createman")
        self.list = [self.handoutname, self.classes, self.year, self.type, self.season, self.school, self.createman]
        return self.list