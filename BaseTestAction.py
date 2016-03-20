from selenium                         import webdriver
from Motivation.ConstantsDictionary   import Moat_Constants
import unittest

class BaseTestAction(object):

  def setUp(self):
      if Moat_Constants['Browser'].lower() == "firefox":
      	 self.driver = webdriver.Firefox()
         self.driver.maximize_window()
      elif Moat_Constants['Browser'].lower() == "chrome":
      	 self.driver = webdriver.Chrome()
         self.driver.maximize_window()
      elif Moat_Constants['Browser'].lower() == "Safari": 
         self.driver = webdriver.Safari()
         self.driver.maximize_window()
      elif Moat_Constants['Browser'].lower() == "IE":
         self.driver = webdriver.IE()
         self.driver.maximize_window()
      else:
      	raise Exception("This browser is not supported at the moment.")

  def navigate_to_page(self, url):
      self.driver.get(url)

  def tearDown(self):
  	  self.driver.quit()