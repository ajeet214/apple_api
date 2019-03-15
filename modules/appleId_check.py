from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from config import Config


from time import sleep


class AppleId:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")

        # self.driver = webdriver.Chrome(chrome_options=options)

        # remote webdriver
        self.driver = webdriver.Remote(
            command_executor='http://'+Config.SELENIUM_CONFIG['host']+':'+Config.SELENIUM_CONFIG['port']+'/wd/hub',
            desired_capabilities=options.to_capabilities(),
        )
        self.EMAILFIELD = (By.TAG_NAME, "email-input email-input-wrapper ")

    def id_check(self, id):

        url = 'https://appleid.apple.com/account#!&page=create'
        self.driver.get(url)
        sleep(0.1)
        self.driver.find_element_by_xpath('//div[@class="email-input-wrapper email-input"]/idms-textbox/idms-error-wrapper/div/div/input').send_keys(id)
        sleep(0.1)
        self.driver.find_element_by_xpath('*//div[@class="intro text-centered"]').click()
        sleep(1)
        try:
            e = self.driver.find_element_by_xpath('//div[@class="idms-error"]/div/span')
            # print(e.text)
            self.driver.quit()
            return {'profileExists': True,
                    'profile_id': id}
        except NoSuchElementException:

            self.driver.quit()
            return {'profileExists': False}


if __name__ == '__main__':
    obj = AppleId()
    print(obj.id_check('jaqsoms43@gmail.com'))

# jaqsoms43@gmail.com