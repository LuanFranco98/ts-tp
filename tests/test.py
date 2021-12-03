import unittest, time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.path.insert(0, '../')
from flaskblog import db
from flaskblog.models import Post, User

class Test(unittest.TestCase):

    def setUp(self):
      # self.driver = webdriver.Chrome(os.path.join('../venv/' ,'chromedriver'))
      self.driver = webdriver.Chrome()
      self.base_url = "http://127.0.0.1:5000/"
      

    def tearDown(self):
      self.driver.quit()


    # def test_h1_text_homePage(self):
    #   self.driver.get(self.base_url)
    #   element = self.driver.find_element_by_tag_name('h1')
    #   self.assertEqual(element.text, "Home Page!")


    def test_home_and_slash_equals(self):
      self.driver.get(self.base_url)
      slash = self.driver.page_source
      self.driver.get(self.base_url + 'home')
      home = self.driver.page_source

      self.assertEqual(slash, home)

    def test_post_empty_after_drop_all(self):
      db.drop_all()
      db.create_all()
      self.assertEqual([], Post.query.all())

    def test_user_empty_after_drop_all(self):
      db.drop_all()
      db.create_all()
      db.session.commit()
      self.assertEqual([], User.query.all())

    def test_user_insertion_on_db(self):
      db.drop_all()
      db.create_all()
      user_1 = User(username='Luan', email='a@a.com', password='password')
      db.session.add(user_1)
      db.session.commit()
      query_user = User.query.filter_by(username='Luan').first()
      self.assertEqual(user_1,query_user )

    def test_post_insertion_on_db(self):
      db.drop_all()
      db.create_all()
      user_1 = User(username='Luan', email='a@a.com', password='password')
      db.session.add(user_1)
      db.session.commit()
      query_user = User.query.filter_by(username='Luan').first()
      post_1 = Post(title='titulo', content='conteudo', user_id = query_user.id)
      db.session.add(post_1)
      db.session.commit()
      query_post = Post.query.first()
      self.assertEqual(post_1,query_post )



