from PageCommon                                    	import PageCommon
from PageCommon                                    	import IncorrectPageException
from Motivation.UiMap                              	import HomePageMap
from selenium.webdriver.common.keys             	import Keys
from selenium.webdriver.common.action_chains    	import ActionChains
import random
import time
import re

class MoatHomePage(PageCommon):

    def __init__(self, driver):
        super(MoatHomePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, 
                                             "xpath", 
                                             HomePageMap['searchAdEngineNameXpath']
                )
        except:   
              raise IncorrectPageException
    
    def submit_search_request(self):
        try:
            searchList = ['Honda', 'Neiman Marcus', 'P&G', 'Johnson & Johnson', 'Coca-Cola', 'Bank of America', 'Tiffany & Co.', 'Yahoo!', 'JP Morgan Chase & Co.', 'match.com']

            global randSearchItem
            randSearchItem = random.choice(searchList)
            print "The random entered Ad name is %s." % randSearchItem

            searchFieldElement = self.find_element("id",
                                                   HomePageMap['searchFieldId']
                )
            actions = ActionChains(self.driver)
            actions.send_keys_to_element(searchFieldElement, randSearchItem)
            actions.send_keys_to_element(searchFieldElement, Keys.ENTER)
            actions.perform()
        except:
            raise IncorrectPageException

    def submit_random_ad_of_try_these_list(self):
        try:
            tryTheseAdsOptions = self.driver.find_elements_by_xpath(HomePageMap['tryTheseAds'])
            for el in tryTheseAdsOptions:
                print el.text
            time.sleep(2)

            option = random.choice(tryTheseAdsOptions)
            global optionValue
            optionValue = option.text
            print "The random selected Ad nmae from try these list is %s." % optionValue
            option.click()
        except:
            raise IncorrectPageException

    def grab_try_these_list_ads_name_sss(self):
    	try:
    		tryTheseFirstAd = self.driver.find_elements_by_xpath(HomePageMap['tryTheseAdsFun'])
    		for elfun in tryTheseFirstAd:
    			print elfun.text
    	except:
    		raise IncorrectPageException

    def grab_recent_seen_ad_list_time(self):
    	try:
    		recentSeenAdsList = self.driver.find_elements_by_css_selector(HomePageMap['resentSeenAdsCss'])
    		numberOfRecentAds = len(recentSeenAdsList)
    		print "number is %s" % numberOfRecentAds
            # Log.info("number is %s" % numberOfRecentAds)

    		adsList = []
    		for el in range(1, numberOfRecentAds+1):
    			recentSeenAdChild = self.driver.find_element_by_xpath(".//*[@id='search-bar']/div/div[2]/ul/li[%s]/h4" % el)
    			recentSeenAdText = recentSeenAdChild.text
    			print recentSeenAdText
    			adsList.append(recentSeenAdText)

    		adsString = ' '.join(adsList)
    		print adsString

    		adsNumbers = re.findall('\d+', adsString)
    		if all(x <= 30 for x in adsNumbers):
    			print "All resent seen Ads are no more than 30 mins old"
    		else:
    			print "Some of or all resent seen Ads are more than 30 mins old"
    		print ' '.join(adsNumbers)
    	except:
    		raise IncorrectPageException





