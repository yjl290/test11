from Page_LeHandout import Search_LeHandout


class Method_LeHandout():

    def __init__(self, driver):
        self.driver = driver

    def looklehandout(self):
        self.lehandout = Search_LeHandout.LeHandout(self.driver)
        self.lehandout.screen_condition()
        self.lehandout.keyword_search()
        dict = self.lehandout.look_handout()
        return dict