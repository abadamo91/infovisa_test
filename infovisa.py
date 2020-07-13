import platform
from selenium import webdriver
import unittest

if 'Windows' in platform.platform():
    PATH = 'C:\\Users\\anthony\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver_win32\\chromedriver.exe'
elif 'Linux' in platform.platform():
    PATH = '/usr/lib/chromium-browser/chromedriver'

class infovisaAutomationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.infovisa.com/contact-us')

    def test_name_field_required(self):
        self.name = self.driver.find_element_by_name('submitted[name]')
        self.assertTrue(self.name.get_attribute('required'))

    def test_email_field_required(self):
        self.email = self.driver.find_element_by_name('submitted[email]')
        self.assertTrue(self.email.get_attribute('required'))

    def test_email_format(self):
        self.email = self.driver.find_element_by_name('submitted[email]')
        self.assertEqual(self.email.get_attribute('type'), "email")

    def test_company_required(self):
        self.company = self.driver.find_element_by_name('submitted[company___organization]')
        self.assertTrue(self.company.get_attribute('required'))

    def test_phone_numeric(self):
        self.phone = self.driver.find_element_by_name('submitted[phone]')
        self.assertIn("form-number", self.phone.get_attribute('class'))

    def test_phone_only_letters(self):
        self.name = self.driver.find_element_by_name('submitted[name]')
        self.name.send_keys("test")
        self.email = self.driver.find_element_by_name('submitted[email]')
        self.email.send_keys("test@test.com")
        self.company = self.driver.find_element_by_name('submitted[company___organization]')
        self.company.send_keys("test")
        self.comment = self.driver.find_element_by_name('submitted[comments]')
        self.comment.send_keys("QA engineer interview test")
        self.phone = self.driver.find_element_by_name('submitted[phone]')
        self.phone.send_keys("test phone")
        self.submit = self.driver.find_element_by_name('op')
        self.submit.click()
        error_message = self.driver.find_element_by_xpath('//*[@id="center"]/div[1]').text
        self.assertEqual(error_message,
                         "ERROR MESSAGE\nPhone field value must format numbers as \"12,345.6789\".")

    def test_comment_required(self):
        self.comment = self.driver.find_element_by_name('submitted[comments]')
        self.assertTrue(self.comment.get_attribute('required'))

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)



