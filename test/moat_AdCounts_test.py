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

class MoatAdCountTest(BaseTestAction, unittest.TestCase):

    def setUp(self):
        super(MoatAdCountTest, self).setUp()
        self.navigate_to_page(Moat_Constants['Base_URL'])

    def test_MoatAdCountSinglePage(self):

    	searching = MoatHomePage(self.driver)
    	searching.submit_search_request()

    	search_result = MoatResultPage(self.driver)
    	search_result.check_search_result_ad_name()
      	search_result.fetch_count_of_search_results_single_page()

      	print "randSearchItemValue is %s " % hp.randSearchItem.lower()
        print "searchResultAdNameValue is %s " % rp.searchResultAdNameValue
        self.assertEqual(hp.randSearchItem.lower(), rp.searchResultAdNameValue)

    def test_MoatAdTotalCount(self):

        searching = MoatHomePage(self.driver)
        searching.submit_search_request()

        search_result = MoatResultPage(self.driver)
        search_result.check_search_result_ad_name()
        search_result.grab_printed_total_search_number()
        search_result.fetch_total_count()

        time.sleep(3)

    def tearDown(self):
        super(MoatAdCountTest, self).tearDown()

if __name__ == "__main__":
    nose.main()
