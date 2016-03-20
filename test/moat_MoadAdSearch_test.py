from selenium                                   import webdriver
from Motivation.BaseTestAction                  import BaseTestAction
from Motivation.ConstantsDictionary             import Moat_Constants
from Motivation.page.HomePage                   import MoatHomePage
from Motivation.page.ResultPage                 import MoatResultPage
import Motivation.page.HomePage                 as hp
import Motivation.page.ResultPage               as rp
import unittest
import time
import nose

class MoatPageElementTest(BaseTestAction, unittest.TestCase):

    def setUp(self):
        super(MoatPageElementTest, self).setUp()
        self.navigate_to_page(Moat_Constants['Base_URL'])

    # An E2E flow checking by entering a brand (randomly selecting from list)
    def test_MoatAdSearch(self):
        searchFieldId = "pro-landing-search-box" 

        moat_Search = MoatHomePage(self.driver)
        moat_Search.submit_search_request()

        moat_Result = MoatResultPage(self.driver)
        moat_Result.check_search_result_ad_name()

        print "randSearchItemValue is %s " % hp.randSearchItem.lower()
        print "searchResultAdNameValue is %s " % rp.searchResultAdNameValue
        self.assertEqual(hp.randSearchItem.lower(), rp.searchResultAdNameValue)
        print "Search reault Ad brand name is same with entered Ad brand name."
        
        self.assertIn("Moat Ad Search", self.driver.title)
        moat_Result.print_search_result_page_title()

        time.sleep(3)

    def tearDown(self):
        super(MoatPageElementTest, self).tearDown()

if __name__ == "__main__":
    nose.main()
