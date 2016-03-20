from selenium                                   import webdriver
from Motivation.BaseTestAction                  import BaseTestAction
from Motivation.page.PageCommon                 import PageCommon
from Motivation.ConstantsDictionary             import Moat_Constants
from Motivation.page.HomePage                   import MoatHomePage
from Motivation.page.ResultPage                 import MoatResultPage
import Motivation.page.HomePage                 as hp
import Motivation.page.ResultPage               as rp
import unittest
import time
import nose

class MoatTryTheseAdTest(BaseTestAction, unittest.TestCase):

    def setUp(self):
        super(MoatTryTheseAdTest, self).setUp()
        self.navigate_to_page(Moat_Constants['Base_URL'])

    def test_MoatTryTheseAdE2E(self):
        trythese_search = MoatHomePage(self.driver)
        trythese_search.submit_random_ad_of_try_these_list()

        trythese_result = MoatResultPage(self.driver)
        trythese_result.check_search_result_ad_name()

        self.assertEqual(hp.optionValue.lower(), rp.searchResultAdNameValue)
        print "Search reault Ad brand name is same with selected tryThese Ad brand name."

        time.sleep(2)

    # def test_MoatTryTheseAdsRandom(self):
    #     trythese_search = MoatHomePage(self.driver)
    #     trythese_search.grab_try_these_list_ads_name_sss()
    #     tryTheseNo1 = hp.elfun.text

    #     time.sleep(1)
    #     driver.refresh()
    #     trythese_search.grab_try_these_list_ads_name_sss()
    #     tryTheseNo2 = hp.elfun.text

    #     print tryTheseNo1, tryTheseNo2

    def tearDown(self):
        super(MoatTryTheseAdTest, self).tearDown()

if __name__ == "__main__":
    nose.main()
