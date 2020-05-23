from Page_NewQuestion import Method_NewQuestion
from Util import Get_Element, ParseExcel


class Method_Omega():

    def __init__(self, driver):
        self.driver = driver
        self.model = ParseExcel.ParseExcel()
        self.value = self.model.getquestion_value()


    def choice_question(self):
        # 题干
        self.method_newquestion = Method_NewQuestion.Method_NewQuestion(self.driver)
        self.method_newquestion.currency_method_stem_picture("NewQuestion", "new_stem_editor", "new_stem_edit",
                                                             "new_stem_html",
                                                             "new_answering_position", "new_upload_pictures",
                                                             "new_option_yesedits", 'ueditor_0', 'A.菱形的对角线互相平分且相等'
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
        self.method_newquestion.currency_method("NewQuestion", "new_remarks_editor", "new_remarks_edit",
                                                     "new_remarks_yesedit",
                                                     "new_remarks_html", 'ueditor_4',
                                                     self.value['choice_remarks'])
        self.new_question = Get_Element.Search_Page_Elements(self.driver)
        self.new_question.click_button("NewQuestion", "new_question_save_omega")
