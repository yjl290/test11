from Util import Get_Element
from time import sleep

driver =None

class Login():

    def __init__(self, driver):
        self.driver = driver

    def test_search(self, loginname, password):
        login_page = Get_Element.Search_Page_Elements(self.driver)
        try:
            login_page.input_string(loginname, "login", "search_loginname")
            login_page.input_string(password, "login", "search_password")
            # login_page.click_button("login", "button_remember")
            # login_page.click_button("login", "button_remember")
            # login_page.click_button("login", "button_class_subject")
            # sleep(1)
            # login_page.click_button("login", "button_class")
            # sleep(1)
            # login_page.click_button("login", "button_subject")
            login_page.click_button("login", "button_login")
            sleep(1)
            login_page.move_bottom()
            login_page.click_button("login", "button_class_subject")
            login_page.click_button("login", "button_enter")
            sleep(1)

        except AssertionError as e:
            raise e

        #return chrome_driver.page_source
        #Search_Handout.Handout().screen_condition(login_page)