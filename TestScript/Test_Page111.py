from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from Page_Login import Login_Page
from Page_Handout import Search_Handout
from Page_SerachQuestion import Search_Question
from Util import MongoDB_Data
from Util import ParseExcel
from Page_NewQuestion import New_Question
from Page_NewQuestion import Method_NewQuestion
import unittest
from selenium.webdriver.common.by import By

class Search_Page(unittest.TestCase):

    def setUp(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()  # 最大化浏览器窗口
        self.chrome_driver.implicitly_wait(8)
        self.value = ParseExcel.ParseExcel()
        value = self.value.getlogin_value()
        self.chrome_driver.get(value['url'])
        self.loginname = value['loginname']
        self.password = value['password']

    def test_handout_page(self):
        #登录
        self.login = Login_Page.Login(self.chrome_driver)
        self.login.test_search(self.loginname, self.password)
        self.assertTrue("yangjunlin@lexue.com" in self.chrome_driver.page_source)

        self.newquestion = New_Question.New_Question(self.chrome_driver)
        self.newquestion.page_Navigation()
        element = self.chrome_driver.find_element_by_xpath('//*[@id="testPriviewdesc=0"]')
        self.actions = ActionChains(self.chrome_driver)
        self.actions.move_to_element(element).perform()
        sleep(5)
        self.chrome_driver.find_element_by_xpath('//*[@id="testPriviewBoxdesc=0"]/button[1]').click()
        try:
            self.chrome_driver.find_element_by_xpath('//*[@id="testPriviewBoxdesc=0"]/button[1]').click()
        except ElementNotInteractableException:
            print(5)
        self.chrome_driver.find_element_by_xpath('//div[3]/div[2]/div/div/div/div/div[3]/div/div/div/div').click()
        sleep(5)
        # self.chrome_driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div/div[2]/input').click()
        self.chrome_driver.find_element_by_xpath('//div[2]/div/div/div[2]/label').send_keys(r'C:\Users\Dell\PycharmProjects\jiaoyan\picture\1.jpg')

def tearDown(self):
        self.chrome_driver.quit()


if __name__ == "__main__":
    unittest.main()