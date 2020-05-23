from Util import Get_Element
from time import sleep
from Page_NewQuestion import Method_NewQuestion
from Util import ParseExcel
driver = None

class New_Question():

    def __init__(self, driver):
        self.driver = driver
        self.new_question1 = Get_Element.Search_Page_Elements(self.driver)
        self.method_newquestion = Method_NewQuestion.Method_NewQuestion(self.driver)
        self.model = ParseExcel.ParseExcel()
        self.value = self.model.getquestion_value()
        # self.keyword = "复制"

    def page_Navigation(self):
        self.method_newquestion.page_switch("Navigation", "move_mouse_input", "button_newquestions", )

    # 录入-新建试题-选择题录新题
    def choice_question_next(self):
        # 题干
        self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_option_yesedit",
                                                           "new_choice_question", 'ueditor_0', 'A.菱形的对角线互相平分且相等'
                                                                                               'B.矩形的对角线互相垂直平分'
                                                                                               'C.对角线相等且垂直的四边形是正方形'
                                                                                               'D.对角线互相平分的四边形是平行四边形.')

        self.method_newquestion.currency_method_stem_option("NewQuestion", "new_option_editor", "new_option_edit",
                                                            "new_option_html", "new_insert_options",
                                                            "new_option_yesedit", 'ueditor_1', 'A.菱形的对角线互相平分且相等'
                                                                                               'B.矩形的对角线互相垂直平分'
                                                                                               'C.对角线相等且垂直的四边形是正方形'
                                                                                               'D.对角线互相平分的四边形是平行四边形.')

        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                "new_answer_yesedit",
                                                "new_answer_yesedit", 'ueditor_2', 'a')
        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit", 'ueditor_3',
                                                       '12364852')

        # 备注
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit", "new_question_preview",
                                                     "new_question_savenew", 'ueditor_4',
                                                     '12364852')

    # 录入-新建试题-选择题
    def choice_question(self):
        # 题干
        self.method_newquestion.currency_method_stem_picture("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_upload_pictures",
                                                           "new_option_yesedit", 'ueditor_0', 'A.菱形的对角线互相平分且相等'
                                                                                               'B.矩形的对角线互相垂直平分'
                                                                                               'C.对角线相等且垂直的四边形是正方形'
                                                                                               'D.对角线互相平分的四边形是平行四边形.')
        # self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
        #                                                    "new_stem_html",
        #                                                    "new_answering_position", "new_option_yesedit",
        #                                                    "new_choice_question", 'ueditor_0', 'A.菱形的对角线互相平分且相等'
        #                                                                                        'B.矩形的对角线互相垂直平分'
        #                                                                                        'C.对角线相等且垂直的四边形是正方形'
        #                                                                                        'D.对角线互相平分的四边形是平行四边形.')

        self.method_newquestion.currency_method_stem_option("NewQuestion", "new_option_editor", "new_option_edit",
                                                            "new_option_html", "new_insert_options",
                                                            "new_option_yesedit", 'ueditor_1',
                                                            self.value['choice_option'])

        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                "new_answer_yesedit",
                                                "new_answer_yesedit", 'ueditor_2', self.value['choice_answer'])
        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit", 'ueditor_3',
                                                       self.value['choice_analysis'])

        # 备注
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit", "new_question_preview",
                                                     "new_question_save", 'ueditor_4',
                                                     self.value['choice_remarks'])

    # 录入-新建试题-选择题-截图
    def choice_question_cut(self):
        # 题干
        self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_option_yesedits",
                                                           "new_choice_question", 'ueditor_0', 'A.菱形的对角线互相平分且相等'
                                                                                               'B.矩形的对角线互相垂直平分'
                                                                                               'C.对角线相等且垂直的四边形是正方形'
                                                                                               'D.对角线互相平分的四边形是平行四边形.')

        self.method_newquestion.currency_method_stem_option("NewQuestion", "new_option_editor", "new_option_edit",
                                                            "new_option_html", "new_insert_options",
                                                            "new_option_yesedit", 'ueditor_1', 'A.菱形的对角线互相平分且相等'
                                                                                               'B.矩形的对角线互相垂直平分'
                                                                                               'C.对角线相等且垂直的四边形是正方形'
                                                                                               'D.对角线互相平分的四边形是平行四边形.')

        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                "new_answer_yesedit",
                                                "new_answer_yesedit", 'ueditor_2', 'a')
        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit", 'ueditor_3',
                                                       '12364852')

        # 备注
        self.method_newquestion.currency_method_save_cut("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                         "new_remarks_html",
                                                         "new_remarks_yesedit", "new_question_preview",
                                                         "new_question_save", "new_typesetting", "new_details",
                                                         'ueditor_4',
                                                         '12364852')

    # 录入-新建试题-填空题录新题
    def completion_question_next(self):
        sleep(1)
        # 题干
        self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_stem_yesedit",
                                                           "new_completion_question", 'ueditor_10',
                                                           '下列命题中，真命题是[[nn]]')

        # 答案
        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                       "new_option_html",
                                                       "new_answer_yesedit", 'ueditor_11',
                                                       'a')

        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html1",
                                                       "new_analysis_yesedit", 'ueditor_12',
                                                       '12364852')

        # 备注
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_html1",
                                                     "new_remarks_yesedit", "new_question_preview",
                                                     "new_question_savenew", 'ueditor_13',
                                                     '12364852')

    # 录入-新建试题-填空题
    def completion_question(self):
        # 题干
        self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_stem_yesedit",
                                                           "new_completion_question", 'ueditor_5',
                                                           '下列命题中，真命题是[[nn]]')

        # 答案
        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                       "new_option_html",
                                                       "new_answer_yesedit", 'ueditor_6',
                                                       'a')

        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html1",
                                                       "new_analysis_yesedit", 'ueditor_7',
                                                       '12364852')

        # 备注
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_html1",
                                                     "new_remarks_yesedit", "new_question_preview",
                                                     "new_question_save", 'ueditor_8',
                                                     '12364852')

        # 录入-新建试题-填空题

    def omega_completion_question(self):
        # 题干
        self.method_newquestion.currency_method_stemswitch("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                           "new_stem_html",
                                                           "new_answering_position", "new_stem_yesedit",
                                                           "new_completion_question", 'ueditor_0',
                                                           '下列命题中，真命题是[[nn]]')

        # 答案
        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor", "new_answer_edit",
                                                       "new_option_html",
                                                       "new_answer_yesedit", 'ueditor_1',
                                                       'a')

        # 解析
        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor", "new_analysis_edit",
                                                       "new_analysis_html1",
                                                       "new_analysis_yesedit", 'ueditor_2',
                                                       '12364852')

        # 备注
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_html1",
                                                     "new_remarks_yesedit", "new_question_preview",
                                                     "new_question_save", 'ueditor_3',
                                                     '12364852')

    # 录入-新建试题-解答题录新题
    def answer_question_next(self):
        # 题干
        sleep(1)
        self.new_question4 = Get_Element.Search_Page_Elements(self.driver)
        self.new_question4.click_button("NewQuestion", "new_answer_question")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        sleep(1)
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")

        self.method_newquestion.currency_method_answer("NewQuestion", "new_stem_editor1", "new_stem_edit1",
                                                       "new_stem_html",
                                                       "new_stem_yesedit1", 'ueditor_5',
                                                       '下列命题中，真命题是[[nn]]')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor1", "new_answer_edit1",
                                                       "new_analysis_html1",
                                                       "new_answer_yesedit1", 'ueditor_6',
                                                       'a')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor1", "new_analysis_edit1",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit1", 'ueditor_7',
                                                       '12364852')

        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor1", "new_remarks_edit1",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit1", "new_question_preview",
                                                     "new_question_savenew", 'ueditor_8',
                                                     '12364852')

    # 录入-新建试题-解答题多小题
    def answer_questionlong(self):
        # 主题干
        self.new_question5 = Get_Element.Search_Page_Elements(self.driver)
        sleep(1)
        self.new_question5.click_button("NewQuestion", "new_answer_question")
        sleep(1)
        self.new_question5.click_button("NewQuestion", "new_addsmall")
        self.new_question5.click_button("NewQuestion", "new_addsmall")
        self.new_question5.click_button("NewQuestion", "new_addsmall")
        self.new_question5.click_button("NewQuestion", "new_addsmall")
        sleep(1)

        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor2", "new_stem_edit2",
                                                "new_stem_html", "new_stem_yesedit2", 'ueditor_9', '下列命题中，真命题是[[nn]]')

        # 1小题题干
        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor1small", "new_stem_edit1small",
                                                "new_stem_html", "new_stem_yesedit1small", 'ueditor_5',
                                                '下列命题中，真命题是[[nn]]')
        # # 答案
        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor1small", "new_answer_edit1small",
                                                "new_option_html", "new_answer_yesedit1small", 'ueditor_6', 'a')
        # # 解析
        self.method_newquestion.currency_method("NewQuestion", "new_analysis_editor1small", "new_analysis_edit1small",
                                                "new_analysis_html", "new_analysis_yesedit1small", 'ueditor_7',
                                                '12364852')
        # # 备注
        self.method_newquestion.currency_method("NewQuestion", "new_remarks_editor1small", "new_remarks_edit1small",
                                                "new_remarks_html", "new_remarks_yesedit1small", 'ueditor_8',
                                                '12364852')

        # 2小题题干
        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor1small2", "new_stem_edit1small2",
                                                "new_stem_html",
                                                "new_stem_edit1small2", 'ueditor_10', '下列命题中，真命题是[[nn]]')
        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor1small2", "new_answer_edit1small2",
                                                "new_option_html",
                                                "new_answer_yesedit1small2", 'ueditor_11', 'a')
        self.method_newquestion.currency_method("NewQuestion", "new_analysis_editor1small2", "new_analysis_edit1small2",
                                                "new_analysis_html",
                                                "new_analysis_yesedit1small2", 'ueditor_12', '12364852')
        self.method_newquestion.currency_method("NewQuestion", "new_remarks_editor1small2", "new_remarks_edit1small2",
                                                "new_remarks_html",
                                                "new_remarks_yesedit1small2", 'ueditor_13', '12364852')

        # 3小题题干
        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor1small3", "new_stem_edit1small3",
                                                "new_stem_html",
                                                "new_stem_yesedit1small3", 'ueditor_14', '下列命题中，真命题是[[nn]]')
        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor1small3", "new_answer_edit1small3",
                                                "new_option_html",
                                                "new_answer_yesedit1small3", 'ueditor_15', 'a')
        self.method_newquestion.currency_method("NewQuestion", "new_analysis_editor1small3", "new_analysis_edit1small3",
                                                "new_analysis_html",
                                                "new_analysis_yesedit1small3", 'ueditor_16', '12364852')
        self.method_newquestion.currency_method("NewQuestion", "new_remarks_editor1small3", "new_remarks_edit1small3",
                                                "new_remarks_html",
                                                "new_remarks_yesedit1small3", 'ueditor_17', '12364852')

        # 4小题题干
        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor1small4", "new_stem_edit1small4",
                                                "new_stem_html",
                                                "new_stem_yesedit1small4", 'ueditor_18', '下列命题中，真命题是[[nn]]')
        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor1small4", "new_answer_edit1small4",
                                                "new_option_html",
                                                "new_answer_yesedit1small4", 'ueditor_19', 'a')
        self.method_newquestion.currency_method("NewQuestion", "new_analysis_editor1small4", "new_analysis_edit1small4",
                                                "new_analysis_html",
                                                "new_analysis_yesedit1small4", 'ueditor_20', '12364852')
        self.method_newquestion.currency_method("NewQuestion", "new_remarks_editor1small4", "new_remarks_edit1small4",
                                                "new_remarks_html",
                                                "new_remarks_yesedit1small4", 'ueditor_21', '12364852')

        # 5小题题干
        self.method_newquestion.currency_method("NewQuestion", "new_stem_editor1small5", "new_stem_edit1small5",
                                                "new_stem_html",
                                                "new_stem_yesedit1small5", 'ueditor_22', '下列命题中，真命题是[[nn]]')
        self.method_newquestion.currency_method("NewQuestion", "new_answer_editor1small5", "new_answer_edit1small5",
                                                "new_option_html",
                                                "new_answer_yesedit1small5", 'ueditor_23', 'a')
        self.method_newquestion.currency_method("NewQuestion", "new_analysis_editor1small5", "new_analysis_edit1small5",
                                                "new_analysis_html",
                                                "new_analysis_yesedit1small5", 'ueditor_24', '12364852')
        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor1small5",
                                                     "new_remarks_edit1small5", "new_remarks_html",
                                                     "new_remarks_yesedit1small5", "new_question_preview",
                                                     "new_question_save", 'ueditor_25', '12364852')

    # 录入-新建试题-解答题
    def answer_question(self):
        # 题干
        self.new_question4 = Get_Element.Search_Page_Elements(self.driver)
        self.new_question4.click_button("NewQuestion", "new_answer_question")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        self.new_question4.click_button("NewQuestion", "new_addsmall")
        sleep(1)
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")
        self.new_question4.click_button("NewQuestion", "new_deletesmall")

        self.method_newquestion.currency_method_answer("NewQuestion", "new_stem_editor1", "new_stem_edit1",
                                                       "new_stem_html",
                                                       "new_stem_yesedit1", 'ueditor_5',
                                                       '下列命题中，真命题是[[nn]]')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor1", "new_answer_edit1",
                                                       "new_analysis_html1",
                                                       "new_answer_yesedit1", 'ueditor_6',
                                                       'a')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor1", "new_analysis_edit1",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit1", 'ueditor_7',
                                                       '12364852')

        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor1", "new_remarks_edit1",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit1", "new_question_preview",
                                                     "new_question_save", 'ueditor_8',
                                                     '12364852')

    # 录入-改编试题-解答题
    def adaptation_answer_question(self):
        # 题干
        self.new_question4 = Get_Element.Search_Page_Elements(self.driver)
        self.new_question4.click_button("NewQuestion", "new_answer_question")
        self.method_newquestion.currency_method_answer("NewQuestion", "new_stem_editor1", "new_stem_edit1",
                                                       "new_stem_html",
                                                       "new_stem_yesedit1", 'ueditor_0',
                                                       '下列命题中，真命题是[[nn]]')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor1", "new_answer_edit1",
                                                       "new_analysis_html1",
                                                       "new_answer_yesedit1", 'ueditor_1',
                                                       'a')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor1", "new_analysis_edit1",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit1", 'ueditor_2',
                                                       '12364852')

        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor1", "new_remarks_edit1",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit1", "new_question_preview",
                                                     "new_question_save", 'ueditor_3',
                                                     '12364852')

    # 录入-改编试题-解答题
    def omegapaper_adaptation_answer_question(self):
        # 题干
        self.new_question4 = Get_Element.Search_Page_Elements(self.driver)
        self.new_question4.click_button("NewQuestion", "new_answer_question")
        self.method_newquestion.currency_method_answer("NewQuestion", "new_stem_editor1", "new_analysis_html1",
                                                       "new_stem_html",
                                                       "new_stem_yesedit1", 'ueditor_0',
                                                       '下列命题中，真命题是[[nn]]')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_answer_editor1", "new_remarks_html1",
                                                       "new_analysis_html1",
                                                       "new_answer_yesedit1", 'ueditor_1',
                                                       'a')

        self.method_newquestion.currency_method_answer("NewQuestion", "new_analysis_editor1", "new_remarks_html",
                                                       "new_analysis_html",
                                                       "new_analysis_yesedit1", 'ueditor_2',
                                                       '12364852')

        self.method_newquestion.currency_method_save("NewQuestion", "new_remarks_editor1", "new_remarks_html_omega",
                                                     "new_remarks_html",
                                                     "new_remarks_yesedit1", "new_question_preview",
                                                     "new_question_save", 'ueditor_3',
                                                     '12364852')
