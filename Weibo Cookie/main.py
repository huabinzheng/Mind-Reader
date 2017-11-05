from cookie import Cookie
import configparser
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('login.ini')
    username = config['DEFAULT']['username']
    password = config['DEFAULT']['password']
    browser = Cookie()
    browser.login(username, password)
    cookies = browser.get_cookies()
    file = open('cookie.txt','w')
    file.write(cookies)
    file.close()