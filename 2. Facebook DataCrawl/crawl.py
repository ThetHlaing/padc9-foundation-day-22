from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from key import EMAIL,PASSWORD

browser = webdriver.Chrome('./drivers/chromedriver')
browser.get('http://www.facebook.com')

email = browser.find_element_by_id('email')
email.send_keys(EMAIL)

password = browser.find_element_by_id('pass')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)


browser.get("https://web.facebook.com/groups/378369752669659/")

posts = browser.find_elements_by_css_selector('.userContentWrapper')

for post in posts:
    postContent = post.find_element_by_css_selector('.userContent')
    print(postContent.text)    