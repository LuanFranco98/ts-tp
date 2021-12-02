import unittest, time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
      #Required to run Seleniun on Repl.it

      self.driver = webdriver.Chrome(os.path.join('../venv/' ,'chromedriver'))
      self.base_url = "http://127.0.0.1:5000/"

    def tearDown(self):
        self.driver.quit()


    # def test_h1_text_homePage(self):
    #     self.driver.get(self.base_url)
    #     element = self.driver.find_element_by_tag_name('h1')
    #     self.assertEqual(element.text, "Home Page!")


    # def test_home_and_slash_equals(self):
    #     self.driver.get(self.base_url)
    #     slash = self.driver.page_source
    #     self.driver.get(self.base_url + 'home')
    #     home = self.driver.page_source

    #     self.assertEqual(slash, home)

