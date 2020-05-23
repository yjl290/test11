from Util import Get_Element
from Page_Handout import Edit_Handout, Search_Handout

from time import sleep
driver =None


class Look_Handout():


    def __init__(self, driver):
        self.driver = driver
        self.look_handout= Get_Element.Search_Page_Elements(self.driver)
        self.keyword = "自动测试讲义名"

    def ppt(self):
        # Look_Handout.handout_look(self)
        self.look_handout.click_button("handout", "new_edit_handout_ppt")
        self.look_handout.switch_page_three()
        sleep(1)
        self.look_handout.click_button("handout", "new_edit_handout_ppt50")
        self.look_handout.click_button("handout", "new_edit_handout_ppt100")
        self.look_handout.click_button("handout", "new_edit_handout_ppt150")
        self.look_handout.click_button("handout", "new_edit_handout_ppt12")
        self.look_handout.click_button("handout", "new_edit_handout_ppt14")
        self.look_handout.click_button("handout", "new_edit_handout_ppt16")
        self.look_handout.click_button("handout", "new_edit_handout_ppt18")
        self.look_handout.click_button("handout", "new_edit_handout_ppt20")
        self.look_handout.click_button("handout", "new_edit_handout_pptwhite")
        self.look_handout.click_button("handout", "new_edit_handout_pptblack")
        self.look_handout.switch_page_close3_return2()
        # self.look_handout.click_button("handout", "new_handout_edit_save")

    # 查看
    def handout_look(self):
        self.handout = Search_Handout.Handout(self.driver)
        self.handout.screen_search_input()
        self.handout.button_search()
        self.look_handout.click_button("handout", "new_handout_name")
        self.look_handout.switch_new_page()
        Look_Handout.handout_edit(self)
        Look_Handout.ppt(self)
        self.look_handout.switch_page_close()

    # 编辑
    def handout_edit(self):
        # self.handout = Search_Handout.Handout(self.driver)
        # self.handout.screen_search_input()
        # self.handout.button_search()
        # self.edit_handout = Edit_Handout.Edit_Handout(self.driver)
        # sleep(1)
        # self.look_handout.click_button("handout", "new_handout_name")
        # self.look_handout.switch_new_page()
        self.edit_handout = Edit_Handout.Edit_Handout(self.driver)
        sleep(1)
        self.look_handout.click_button("handout", "new_handout_edit")
        self.edit_handout.add_points()
        self.edit_handout.add_text()
        self.edit_handout.add_example()
        self.edit_handout.add_exercises()
        self.edit_handout.add_consolidate()
        self.edit_handout.add_expand()
        self.edit_handout.other()
        self.edit_handout.tree()

        # self.search_handout.click_button("handout", "new_handout_edit")
        # self.search_handout.switch_new_page()
        # sleep(2)
        # print(self.search_handout.get_page_element_name("handout", "new_edit_handout_name"))
        # self.search_handout.click_button("handout", "new_handout_edit_save")
        # self.search_handout.switch_new_page_close()