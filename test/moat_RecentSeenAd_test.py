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

class MoatRecentSearchAdsTest(BaseTestAction, unittest.TestCase):

    def setUp(self):
        super(MoatRecentSearchAdsTest, self).setUp()
        self.navigate_to_page(Moat_Constants['Base_URL'])

    def test_MoatRecentSeenAdCheck(self):

    	recentSeen = MoatHomePage(self.driver)
    	recentSeen.grab_recent_seen_ad_list_time()

    def tearDown(self):
        super(MoatRecentSearchAdsTest, self).tearDown()

if __name__ == "__main__":
    nose.main()
