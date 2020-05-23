from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from Util import ParseElementLocator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
driver =None
parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(parent_directory_path)
page_elements_file = parent_directory_path + u"\\PageElementLocator\\page_elements.ini"

class Search_Page_Elements():

    def __init__(self, driver):
        self.location_file = page_elements_file
        self.driver = driver
        self.get_element = ParseElementLocator.ParseConfigFile(self.driver, self.location_file)
        self.actions = ActionChains(self.driver)

    #获取元素
    def get_page_element(self, section_name, option_name):
        self.page_element = self.get_element.get_element_location(section_name, option_name, 10)
        return self.page_element

    #script点击
    def click_script(self, section_name, option_name):
        element = Search_Page_Elements.get_page_element(self, section_name, option_name)
        self.driver.execute_script("arguments[0].click();", element)

    # script输入
    def input_script(self, section_name, option_name):
        element = Search_Page_Elements.get_page_element(self, section_name, option_name)
        self.driver.execute_script("arguments[0].send_keys(1);", element)

    # 获取元素文案
    def get_page_element_name(self, section_name, option_name):
        self.page_element = self.get_element.get_element_location(section_name, option_name, 10)
        self.name = self.page_element.text
        return self.name

    #输入
    def input_string(self, string, section_name, option_name):
        page_string = Search_Page_Elements(self.driver)
        page_string.get_page_element(section_name, option_name).send_keys(string)

    #点击
    def click_button(self, section_name, option_name):
        button = Search_Page_Elements(self.driver)
        try:
            button.get_page_element(section_name, option_name).click()
        except:
            button.get_page_element(section_name, option_name).click()

    #单选框状态
    def radio_state(self, section_name, option_name):
        page_string = Search_Page_Elements(self.driver)
        state = page_string.get_page_element(section_name, option_name).is_selected()
        return state

    # 元素显示状态
    def element_state(self, section_name, option_name):
        page_string = Search_Page_Elements(self.driver)
        state = page_string.get_page_element(section_name, option_name).is_displayed()
        return state

    # 元素点击状态
    def operation_state(self, section_name, option_name):
        page_string = Search_Page_Elements(self.driver)
        state = page_string.get_page_element(section_name, option_name).is_enabled()
        return state

    def isElementExist(self, section_name, option_name):
        flag = True
        try:
            Search_Page_Elements.get_page_element(self, section_name, option_name)
            return flag
        except:
            flag = False
            return flag

    # 清空文本框内容
    def clear_input(self, section_name, option_name):
        button = Search_Page_Elements(self.driver)
        button.get_page_element(section_name, option_name).clear()

    # backspace清空文本框内容
    def backspace_input(self, section_name, option_name):
        button = Search_Page_Elements(self.driver)
        button.get_page_element(section_name, option_name).send_keys(Keys.BACK_SPACE)

    # 回车清空文本框内容
    def enter_input(self, section_name, option_name):
        button = Search_Page_Elements(self.driver)
        button.get_page_element(section_name, option_name).send_keys(Keys.ENTER)

    # 鼠标悬停
    def move_mouse(self, section_name, option_name):
        page_mouse = Search_Page_Elements(self.driver)
        element = page_mouse.get_page_element(section_name, option_name)
        # self.actions.__init__(self.driver)
        self.actions.move_to_element(element).perform()


    # 拖动滚动条至底部
    def move_bottom(self):
        js1 = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js1)

    # 拖动滚动条至底部
    def move_between(self):
        js1 = "document.documentElement.scrollTop=600"
        self.driver.execute_script(js1)

    # 拖动滚动条至顶部
    def move_top(self):
        js2 = "document.documentElement.scrollTop=0"
        self.driver.execute_script(js2)

    #截图
    def cut(self,name):
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(picture_time)
        try:
            picture_url = self.driver.get_screenshot_as_file(parent_directory_path + u'\\Screenshot\\' + name + picture_time +'.png')
            print("%s：截图成功！！！" % picture_url)
        except BaseException as msg:
            print(msg)


    #切到第二页
    def switch_new_page(self):
        # windows = self.driver.current_window_handle  # 定位当前页面句柄
        all_handles = self.driver.window_handles  # 获取全部页面句柄
        # for handle in all_handles:  # 遍历全部页面句柄
            # print(handle)
            # print(windows)
            #if handle != windows:  # 判断条件
        self.driver.switch_to.window(all_handles[1])  # 切换到新页面

    #切到第一页，关闭第二页
    def switch_page_close(self):
        all_handles = self.driver.window_handles  # 获取全部页面句柄
        self.driver.close()
        self.driver.switch_to.window(all_handles[0])  # 切换到新页面

    # 切到第2页，关闭第3页
    def switch_page_close3_return2(self):
        all_handles = self.driver.window_handles  # 获取全部页面句柄
        self.driver.close()
        self.driver.switch_to.window(all_handles[1])  # 切换到新页面

    # 切换页面，到第三页
    def switch_page_three(self):
        all_handles = self.driver.window_handles  # 获取全部页面句柄
        self.driver.switch_to.window(all_handles[2])  # 切换到新页面

    #刷新
    def Refresh(self):
        self.driver.refresh()

     #下拉菜单
    def select_by_index(self, element, index):
        Select(element).select_by_index(index)

    #下拉菜单
    def select_by_value(self, element, index):
        Select(element).select_by_value(index)

    #下拉菜单
    def select_by_text(self, element, index):
        Select(element).select_by_visible_text(index)