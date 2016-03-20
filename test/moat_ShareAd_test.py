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

class MoatAdSharingTest(BaseTestAction, unittest.TestCase):

    def setUp(self):
        super(MoatAdSharingTest, self).setUp()
        self.navigate_to_page(Moat_Constants['Base_URL'])

    # def test_MoatAdResultMouseMoveToAnyOne(self):

    # 	searching = MoatHomePage(self.driver)
    # 	searching.submit_search_request()

    # 	search_result = MoatResultPage(self.driver)
    # 	search_result.check_search_result_ad_name()
    # 	search_result.mouse_move_to_random_one()

    # 	time.sleep(3)

    def test_MoatAdSharingFeature(self):

        searching = MoatHomePage(self.driver)
        searching.submit_search_request()

        search_result = MoatResultPage(self.driver)
        search_result.check_search_result_ad_name()
        search_result.mouse_move_to_random_one()
        search_result.share_ad()
        self.assertEqual(rp.share_ad_url, rp.fancy_highlight_url)
        time.sleep(3)

    def tearDown(self):
        super(MoatAdSharingTest, self).tearDown()

if __name__ == "__main__":
    nose.main()
