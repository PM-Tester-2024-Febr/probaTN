from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestRectangle(object):
    def setup_method(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get('https://high-flyer.hu/hetihazi/feladat1_teglalap.html')

#    def teardown_method(self):
#        self.browser.quit()


    def test_rectangle_positive(self):
        a_side = self.browser.find_element(By.ID,'a')
        a_side.send_keys('74')
        b_side = self.browser.find_element(By.ID,'b')
        b_side.send_keys('32')
        calculate = self.browser.find_element(By.ID,'submit')
        calculate.click()
        result = self.browser.find_element(By.ID,'result')
        assert result.text == '212'

    def test_rectangle_word(self):
        a_side = self.browser.find_element(By.ID,'a')
        a_side.send_keys('kiskutya')
        b_side = self.browser.find_element(By.ID,'b')
        b_side.send_keys('32')
        calculate = self.browser.find_element(By.ID,'submit')
        calculate.click()
        result = self.browser.find_element(By.ID,'result')
        assert result.text == 'NaN'

    def test_rectangle_empty(self):
        a_side = self.browser.find_element(By.ID, 'a')
        a_side.send_keys('')
        b_side = self.browser.find_element(By.ID, 'b')
        b_side.send_keys('')
        calculate = self.browser.find_element(By.ID, 'submit')
        calculate.click()
        result = self.browser.find_element(By.ID, 'result')
        assert result.text == 'NaN'

