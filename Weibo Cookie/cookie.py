from time import sleep

from selenium import webdriver

class Cookie(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        url_login = 'https://passport.weibo.cn/signin/login'
        self.driver.get(url_login)
        sleep(1)
        username_element = self.driver.find_element_by_xpath('//*[@id="loginName"]')
        username_element.send_keys(username)
        password_element = self.driver.find_element_by_xpath('//*[@id="loginPassword"]')
        password_element.send_keys(password)
        button = self.driver.find_element_by_xpath('//*[@id="loginAction"]').click()

    def get_cookies(self):
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)
        return cookiestr