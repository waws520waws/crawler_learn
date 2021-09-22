import requests
from lxml import etree
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

# ua = UserAgent()

headers = {
    # 'user-agent': ua.random,
    'referer': 'https://fmovies.to/film/supergirl.rw28m/8nkqrmy'
}
params = {
    'page': None
}
url = 'https://fmovies.to/film/supergirl.rw28m/1r2jkjp'

# response = requests.get(url, headers=headers, params=params)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("referer='https://fmovies.to/film/supergirl.rw28m/8nkqrmy'")
# options.add_argument("User-Agent='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'")


options = FirefoxProfile()

# options.add_argument("referer='https://fmovies.to/film/supergirl.rw28m/8nkqrmy'")

# driver = webdriver.Chrome(executable_path='./selenium/chromedriver', options=options)
driver = webdriver.Firefox(executable_path='./small_spider/selenium/geckodriver.exe')

# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => false
#     })
#   """
# })

# cookies1 = {
#     'domain': 'fmovies.to',
#     'name': '_ga',
#     'value': 'GA1.2.646825441.1629796282'
# }
# cookies2 = {
#     'domain': 'fmovies.to',
#     'name': 'session',
#     'value': '07057c787e3df5f59bb3f07bee5a43fda5b75566'
# }
# cookies3 = {
#     'domain': 'fmovies.to',
#     'name': '_gid',
#     'value': 'GA1.2.595016377.1630478187'
# }
# cookies4 = {
#     'domain': 'fmovies.to',
#     'name': '__atuvc',
#     'value': '74%7C34%2C33%7C35'
# }
# cookies5 = {
#     'domain': 'fmovies.to',
#     'name': '__atuvs',
#     'value': '612f1f6acb28ed2c002'
# }
# cookies6 = {
#     'domain': 'fmovies.to',
#     'name': 'AdskeeperStorage',
#     'value': '%7B%220%22%3A%7B%22svspr%22%3A%22%22%2C%22svsds%22%3A2%2C%22TejndEEDj%22%3A%22YOke5XTeB%22%7D%2C%22C910092%22%3A%7B%22page%22%3A5%2C%22time%22%3A1630479089927%7D%7D'
# }
#
# driver.get('https://fmovies.to/tv-series')
# driver.add_cookie(cookies1)
# # driver.add_cookie(cookies2)
# driver.add_cookie(cookies3)
# driver.add_cookie(cookies4)
# # driver.add_cookie(cookies5)
# driver.add_cookie(cookies6)


driver.get(url)

time.sleep(60)
# driver.implicitly_wait(40)

iframe = driver.find_element_by_xpath("//div[@id='player']//iframe")
driver.switch_to.frame(iframe)

time.sleep(3)
total_time = driver.find_element_by_class_name('jw-icon jw-icon-inline jw-text jw-reset jw-text-duration')
print(total_time.text)

# //*[@id="player"]/iframe