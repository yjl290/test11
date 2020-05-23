from Page_RecordPaper import OmegaMethod
from Util import Get_Element
from Util import MongoDB_Data
from Page_SerachQuestion import Search_Question
from Page_NewQuestion import New_Question
from Page_SerachQuestion import Method_Question
from time import sleep

driver = None
mongo = MongoDB_Data.Mongo_Data()


class New_OmegaPaper():

    def __init__(self, driver):
        self.driver = driver
        self.method_newquestion = Method_Question.Method_AddQuestion(self.driver)

    def switch_omegaPaper(self):
        self.OmegaPaper_page = Get_Element.Search_Page_Elements(self.driver)
        self.OmegaPaper_page.move_mouse("Navigation", "move_mouse_input")
        sleep(1)
        self.OmegaPaper_page.click_button("Navigation", "button_resordpaper")

    def new_omegaPaper(self):
        self.OmegaPaper_page = Get_Element.Search_Page_Elements(self.driver)
        self.OmegaPaper_page.move_mouse("Navigation", "move_mouse_input")
        sleep(1)
        self.OmegaPaper_page.click_button("Navigation", "button_resordpaper")
        sleep(1)
        self.OmegaPaper_page.move_mouse("RecordPaper", "recordpaper_new")
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper")
        sleep(1)
        self.OmegaPaper_page.input_string('自动测试真题试卷名', "RecordPaper", "new_omegapaper_name")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_class")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_class31")
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_year")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_year2021")
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_school")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_schoolall")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_schoolall_unified")
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_type")
        sleep(1)
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_type_midtermup")
        self.OmegaPaper_page.input_string('自动测试真题试卷名', "RecordPaper", "new_omegapaper_remarks")
        self.OmegaPaper_page.click_button("RecordPaper", "new_omegapaper_yes")
        sleep(1)
        self.OmegaPaper_page.switch_new_page()

    # 手动加题
    def new_omegaPaper_add(self):
        self.omegaPaper_page_add = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_add.click_button("RecordPaper", "new_omegapaper_add")
        self.method_newquestion.new_omegaPaper_add("RecordPaper", "new_edit_handout_addexample_subject_use",
                                                   "new_edit_handout_addexample_subject_useyes",
                                                   "new_edit_handout_addexample_subject_popupadd",
                                                   "new_edit_handout_addexample_subject_popupclose",
                                                   "new_omegapaper_add")

    # 录入新题
    def new_omegaPaper_new(self):
        self.omegaPaper_page_new = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_new.click_button("RecordPaper", "new_omegapaper_new")
        sleep(1)
        self.newquestion = OmegaMethod.Method_Omega(self.driver)
        self.newquestion.choice_question()
        New_OmegaPaper.similar(self)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_back")
        self.omegaPaper_page_new.switch_page_close()

    # 编辑真题试卷
    def edit_omegaPaper(self):
        self.omegaPaper_page_new = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_new.click_button("RecordPaper", "eidt_omegapaper")
        self.omegaPaper_page_new.switch_new_page()

    # 编辑真题试卷-录入新题
    def edit_omegaPaper_new(self):
        self.omegaPaper_page_new = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_new.click_button("RecordPaper", "edit_omegapaper_new")
        self.newquestion = OmegaMethod.Method_Omega(self.driver)
        self.newquestion.choice_question()
        # self.omegaPaper_page_new.click_button("RecordPaper", "edit_omegapaper_new")
        # self.newquestion.choice_question()
        # self.omegaPaper_page_new.click_button("RecordPaper", "edit_omegapaper_new")
        # self.newquestion.choice_question()
        New_OmegaPaper.similar(self)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_back")
        # self.omegaPaper_page_new.switch_page_close()


    # 编辑真题试卷-批量录入
    def edit_omegaPaper_batch(self):
        self.omegaPaper_page_new = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_new.click_button("RecordPaper", "new_omegapaper_batch")
        self.omegaPaper_page_new.input_string("5ea92bb9f2c315000bfbb4fd","RecordPaper", "new_omegapaper_batch_input")
        self.omegaPaper_page_new.move_bottom()
        sleep(1)
        self.omegaPaper_page_new.click_button("RecordPaper", "new_omegapaper_batchsave")
        sleep(3)

    def similar(self):
        self.omegaPaper_page_new = Get_Element.Search_Page_Elements(self.driver)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_similar")
        sleep(1)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_similar_use")
        sleep(1)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_similar")
        sleep(1)
        self.omegaPaper_page_new.click_button("RecordPaper", "omegapaper_similar_use1")
        sleep(1)