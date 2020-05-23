from selenium import webdriver
class Browser_Controller:

    def __init__(self, driver):
        self.driver = driver

    def driver_browser(self, browser_type, base_url):
        if browser_type.lower() == "firefox":
            driver = webdriver.Firefox()
        elif browser_type.lower() == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    #浏览器后退
    def back(self):
        self.driver.back()

    #浏览器前进
    def forward(self):
        self.driver.forward()

    #打开Url
    def open_url(self, url):
        self.driver.get(url)

    #退出浏览器
    def quit_browser(self):
        self.driver.quit()

    #设置浏览器宽高
    def set_browser_window(self, weight, high):
        self.driver.set_window_size(weight, high)

    #进入iframe控件
    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    #从控件回到主页页面
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    #进入Alert控件
    def switch_to_alert(self):
        pop_dailog = self.driver.switch_to.alert
        return pop_dailog

