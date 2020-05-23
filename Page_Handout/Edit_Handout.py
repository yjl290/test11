from Page_SerachQuestion import Search_Question
from Page_Handout import Method_Handout
from Util import Get_Element
from Util import Browser_Controller
from Util import MongoDB_Data
from time import sleep

driver = None
mongo = MongoDB_Data.Mongo_Data()


class Edit_Handout():

    def __init__(self, driver):
        self.driver = driver
        self.edit_handout = Get_Element.Search_Page_Elements(self.driver)
        self.method_handout = Method_Handout.Method_Handout(self.driver)
        # self.keyword = "复制"

    def add_points(self):
        # self.search_handout.click_button("handout", "new_handout_edit")
        # self.search_handout.switch_new_page()
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_points")
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_inputclick")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_input")
        self.edit_handout.backspace_input("handout", "new_edit_handout_addpoints_input")
        self.edit_handout.input_string('测试知识点', "handout", "new_edit_handout_addpoints_input")
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_select")
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_select")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_select1")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_select2")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_select3")
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_selectyes")

        self.edit_handout.move_mouse("handout", "new_edit_handout_addpoints_editor")
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_edit")
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe('ueditor_0')
        self.driver.find_element('tag name', 'body').send_keys('12364852')
        self.iframe.switch_to_default_content()
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addpoints_edityes")

    def add_text(self):
        self.edit_handout.click_button("handout", "new_edit_handout_addother")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addtext")
        self.edit_handout.click_button("handout", "new_edit_handout_addtext_inputclick")
        self.edit_handout.backspace_input("handout", "new_edit_handout_addtext_input")
        self.edit_handout.input_string('测试知识点', "handout", "new_edit_handout_addtext_input")
        self.edit_handout.move_mouse("handout", "new_edit_handout_addtext_editor")
        self.edit_handout.click_button("handout", "new_edit_handout_addtext_edit")
        self.iframe = Browser_Controller.Browser_Controller(self.driver)
        self.iframe.switch_to_iframe('ueditor_1')
        self.driver.find_element('tag name', 'body').send_keys('12364852')
        self.iframe.switch_to_default_content()
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_addtext_edityes")

    # def add_example(self):
    #     self.method_handout.currency_method("handout", "new_edit_handout_addother1", "new_edit_handout_addexample",
    #                                         "new_edit_handout_addexample_subject",
    #                                         "new_edit_handout_addexample_subject_use",
    #                                         "new_edit_handout_addexample_subject_useyes",
    #                                         "new_edit_handout_addexample_subject_popupadd",
    #                                         "new_edit_handout_addexample_subject_popupclose")
    def add_example(self):
        self.method_handout.addexmple("handout", "new_edit_handout_addother1", "new_edit_handout_addexample",
                                                "new_edit_handout_addexample_subject",
                                                "new_edit_handout_addexample_draft",
                                                "new_edit_handout_addexample_draftlist",
                                                "new_edit_handout_addexample_draftlist_name",
                                                "new_edit_handout_addexample_subject_use1",
                                                "new_edit_handout_addexample_subject_use2",
                                                "new_edit_handout_addexample_subject_use3",
                                                "new_edit_handout_addexample_subject_useyes1")

    def add_exercises(self):
        self.method_handout.currency_method("handout", "new_edit_handout_addother2", "new_edit_handout_addexercises",
                                            "new_edit_handout_addexercises_subject",
                                            "new_edit_handout_addexample_subject_use",
                                            "new_edit_handout_addexample_subject_useyes",
                                            "new_edit_handout_addexample_subject_popupadd",
                                            "new_edit_handout_addexample_subject_popupclose")

    def add_consolidate(self):
        self.method_handout.currency_method("handout", "new_edit_handout_addother3", "new_edit_handout_addconsolidate",
                                            "new_edit_handout_addconsolidate_subject",
                                            "new_edit_handout_addconsolidate_subject_use",
                                            "new_edit_handout_addconsolidate_subject_useyes",
                                            "new_edit_handout_addconsolidate_subject_popupadd",
                                            "new_edit_handout_addconsolidate_subject_popupclose")
    def add_expand(self):
        self.method_handout.currency_method("handout", "new_edit_handout_addother4", "new_edit_handout_addexpand",
                                            "new_edit_handout_addexpand_subject",
                                            "new_edit_handout_addexpand_subject_use",
                                            "new_edit_handout_addexpand_subject_useyes",
                                            "new_edit_handout_addexpand_subject_popupadd",
                                            "new_edit_handout_addexpand_subject_popupclose")

    def other(self):
        self.edit_handout.click_button("handout", "new_edit_handout_addmodule")
        self.edit_handout.click_button("handout", "new_edit_handout_addtask_delete")
        self.edit_handout.click_button("handout", "new_edit_handout_addtask")
        self.edit_handout.click_button("handout", "new_edit_handout_addtask_delete")

    def tree(self):
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_treemodule_open")
        self.edit_handout.move_top()
        self.edit_handout.click_button("handout", "new_edit_handout_treemodule")
        self.edit_handout.click_button("handout", "new_edit_handout_treepoints")
        self.edit_handout.click_button("handout", "new_edit_handout_treetest")
        self.edit_handout.click_button("handout", "new_edit_handout_treeexample")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_treeexample1")
        self.edit_handout1 = Method_Handout.Method_Handout(self.driver)
        self.edit_handout1.update_question()
        self.edit_handout1.replace_question()
        self.edit_handout1.insert_question()
        self.edit_handout1.delete_question()
        self.edit_handout1.adaptation_question()
        self.edit_handout1.correction_question()
        self.edit_handout1.details_question()
        self.edit_handout1.resemble_question()
        self.edit_handout1.open_question()
        self.edit_handout1.source_question_input()
        self.edit_handout1.source_question()
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_treemodule_open")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_treeexercises")
        #
        # self.driver.find_element_by_css_selector(
        #     ".ant-tree-treenode-switcher-close:nth-child(4) > .ant-tree-switcher svg").click()
        try:
            self.driver.find_element_by_css_selector(
                ".ant-tree-treenode-switcher-open:nth-child(4) .ant-tree-title > span").click()
        except:
            self.edit_handout.click_button("handout", "new_edit_handout_treeexercises1")

        self.edit_handout.click_button("handout", "new_edit_handout_treeconsolidate")
        sleep(1)
        # self.edit_handout.click_button("handout", "new_edit_handout_treeconsolidate1")
        self.edit_handout.click_button("handout", "new_edit_handout_treeconsolidate11")
        sleep(1)
        self.driver.find_element_by_css_selector(
            ".ant-tree-treenode-selected > .ant-tree-switcher path").click()
        self.edit_handout.move_top()
        self.edit_handout.click_button("handout", "new_edit_handout_pointsoutline")
        sleep(1)
        self.edit_handout.click_button("handout", "new_edit_handout_pointsoutline_delete")
        #完成编辑
        self.edit_handout.click_button("handout", "new_edit_handout_completeedit")
        # self.edit_handout.switch_page_close()


