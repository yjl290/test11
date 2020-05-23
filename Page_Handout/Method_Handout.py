from Util import Get_Element
from Util import Browser_Controller
from Page_SerachQuestion import Search_Question
from Page_SerachQuestion import Method_Question
from Page_NewQuestion import New_Question
from Util import MongoDB_Data
from time import sleep

mongo = MongoDB_Data.Mongo_Data()


class Method_Handout():

    def __init__(self, driver):
        self.driver = driver

    def currency_method(self, model, elm1, elm2, elm3, elm4, elm5, elm6, elm7):
        self.edit_handout = Get_Element.Search_Page_Elements(self.driver)
        self.edit_handout.click_button(model, elm1)
        sleep(1)
        self.edit_handout.click_button(model, elm2)
        # sleep(1)
        self.edit_handout.click_button(model, elm3)
        sleep(1)
        element = mongo.questionbasket()
        if element == "empty_questionbasket_haveyes":
            self.edit_handout.click_button(model, elm4)
            # sleep(1)
            self.edit_handout.click_button(model, elm5)
        else:
            #  sleep(1)
            self.edit_handout.click_button(model, elm6)
            self.edit_handout.switch_page_three()
            #  sleep(1)
            self.question = Search_Question.Search_Question(self.driver)
            self.question.join_questionbasket()
            self.edit_handout.switch_page_close3_return2()
            # sleep(1)
            self.edit_handout.click_button(model, elm7)
            # sleep(1)
            self.edit_handout.click_button(model, elm3)
            sleep(1)
            self.edit_handout.click_button(model, elm4)
            # sleep(1)
            self.edit_handout.click_button(model, elm5)
        # sleep(2)

    def addexmple(self, model, elm1, elm2, elm3, elm4, elm5, elm6, elm7, elm8, elm9, elm10):
        self.edit_handout = Get_Element.Search_Page_Elements(self.driver)
        self.edit_handout.click_button(model, elm1)
        sleep(1)
        self.edit_handout.click_button(model, elm2)
        # sleep(1)
        self.edit_handout.click_button(model, elm3)
        sleep(1)
        self.edit_handout.click_button(model, elm4)
        sleep(2)
        self.edit_handout.click_button(model, elm5)
        sleep(2)
        self.edit_handout.click_button(model, elm6)
        sleep(2)
        self.edit_handout.click_button(model, elm7)
        self.edit_handout.move_between()
        self.edit_handout.click_button(model, elm8)
        self.edit_handout.move_bottom()
        self.edit_handout.click_button(model, elm9)
        self.edit_handout.click_button(model, elm10)

    # 更新试题
    def update_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        state = self.driver.find_element_by_css_selector("i.anticon.anticon-redo > svg").is_displayed()
        # state = self.question_operation.element_state("handout", "new_edit_handout_question_update")
        print(state)

    # 输入的出处
    def source_question_input(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        sleep(1)
        self.question_operation.click_button("handout", "new_edit_handout_question_source")
        sleep(1)
        self.question_operation.click_button("handout", "new_edit_handout_question_source_display")
        self.question_operation.input_string("测试出处", "handout", "new_edit_handout_question_source_input")
        self.question_operation.click_button("handout", "new_edit_handout_question_source_ok")

    # 出处
    def source_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        sleep(1)
        self.question_operation.click_button("handout", "new_edit_handout_question_source1")
        sleep(1)
        self.question_operation.click_button("handout", "new_edit_handout_question_source_display")
        self.question_operation.click_button("handout", "new_edit_handout_question_source_name")
        self.question_operation.click_button("handout", "new_edit_handout_question_source_ok")

    # 替换试题
    def replace_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_replace")
        # try:
        #     self.question_operation.click_button("handout", "new_edit_handout_question_replace")
        # except:
        #     print("replace")
        self.method_newquestion = Method_Question.Method_AddQuestion(self.driver)
        self.method_newquestion.new_omegaPaper_add("handout", "new_edit_handout_addexample_subject_use",
                                                   "new_edit_handout_addexample_subject_useyes",
                                                   "new_edit_handout_addexample_subject_popupadd",
                                                   "new_edit_handout_addexample_subject_popupclose",
                                                   "new_edit_handout_question_replace")

    # 插入试题
    def insert_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_insert")
        self.method_newquestion = Method_Question.Method_AddQuestion(self.driver)
        self.method_newquestion.new_omegaPaper_add("handout", "new_edit_handout_addexample_subject_use",
                                                   "new_edit_handout_addexample_subject_useyes",
                                                   "new_edit_handout_addexample_subject_popupadd",
                                                   "new_edit_handout_addexample_subject_popupclose",
                                                   "new_edit_handout_question_insert")

    # 删除试题
    def delete_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_delete")

    # 改编
    def adaptation_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        sleep(1)
        self.question_operation.click_button("handout", "new_edit_handout_question_adaptation")
        self.question_operation.switch_page_three()
        # self.newquestion = New_Question.New_Question(self.driver)
        # state_choice = self.question_operation.radio_state("NewQuestion", "new_choice_question")
        # state_completion = self.question_operation.radio_state("NewQuestion", "new_completion_question")
        # state_answer = self.question_operation.radio_state("NewQuestion", "new_answer_question")
        # if state_choice == True:
        #     self.newquestion.choice_question()
        # elif state_completion == True:
        #     self.newquestion.omega_completion_question()
        # else:
        #     try:
        #         self.newquestion.adaptation_answer_question()
        #     except Exception:
        #         print("解答题暂未兼容存量题")
        self.question_operation.switch_page_close3_return2()
        sleep(2)

    # 改编真题试卷
    def omega_adaptation_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_adaptation")
        self.question_operation.switch_page_three()
        self.newquestion = New_Question.New_Question(self.driver)
        state_choice = self.question_operation.radio_state("NewQuestion", "new_choice_question")
        state_completion = self.question_operation.radio_state("NewQuestion", "new_completion_question")
        state_answer = self.question_operation.radio_state("NewQuestion", "new_answer_question")
        if state_choice == True:
            self.newquestion.choice_question()
        elif state_completion == True:
            self.newquestion.completion_question()
        else:
            self.newquestion.omegapaper_adaptation_answer_question()
        self.question_operation.switch_page_close3_return2()

    # 纠错
    def correction_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_correction")
        self.question_operation.switch_page_three()
        self.question_operation.switch_page_close3_return2()
        sleep(2)

    # 详情
    def details_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        self.question_operation.click_button("handout", "new_edit_handout_question_details")
        self.question_operation.switch_page_three()
        self.question_operation.switch_page_close3_return2()
        sleep(2)

    # 相似
    def resemble_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        state = self.question_operation.operation_state("handout", "new_edit_handout_question_resemble")
        print(state)
        # self.question_operation.click_button("handout", "new_edit_handout_question_resemble")
        # self.question_operation.switch_page_three()
        # self.question_operation.switch_page_close3_return2()

    # 展开试题信息
    def open_question(self):
        self.question_operation = Get_Element.Search_Page_Elements(self.driver)
        # sleep(10)
        # self.question_operation.click_button("handout", "new_edit_handout_question_open")
        # self.question_operation.click_button("handout", "new_edit_handout_question_open")
        self.driver.find_element_by_css_selector("i.anticon.anticon-down > svg").click()
        sleep(1)
        self.driver.find_element_by_css_selector("i.anticon.anticon-up > svg").click()


