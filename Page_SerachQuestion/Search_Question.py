from Util import Get_Element
from Util import MongoDB_Data
from time import sleep
driver =None


class Search_Question():

    def __init__(self, driver):
        self.driver = driver
        self.search_question= Get_Element.Search_Page_Elements(self.driver)
        #self.keyword = "复制"

    #清空试题篮，并加入三道题
    def join_questionbasket(self):

        self.search_question.move_mouse("Question", "move_mouse_questionbasket")
        sleep(1)
        self.search_question.click_button("Question", "in_questionbasket")
        sleep(1)
        self.search_question.click_button("Question", "empty_questionbasket")
        sleep(1)
        self.mongo = MongoDB_Data.Mongo_Data()
        self.element = self.mongo.questionbasket()
        self.search_question.click_button("Question", self.element)
        self.search_question.click_button("Question", "return_questionbasket")
        sleep(1)
        self.search_question.click_button("Question", "difficulty_question")
        self.search_question.click_button("Question", "search_question")
        self.search_question.click_button("Question", "join_questionbasket1")
        self.search_question.click_button("Question", "join_questionbasket2")
        self.search_question.click_button("Question", "join_questionbasket3")
        self.search_question.click_button("Question", "join_questionbasket4")