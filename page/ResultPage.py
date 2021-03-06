from PageCommon                					        import PageCommon
from PageCommon                					        import IncorrectPageException
from PageCommon                                         import TimeoutException
from selenium.common.exceptions                         import NoSuchElementException
from Motivation.UiMap          					        import ResultPageMap
from selenium.webdriver.common.keys                     import Keys
from selenium.webdriver.common.action_chains            import ActionChains
import random
import time
import re

class MoatResultPage(PageCommon):

    def __init__(self, driver):
        super(MoatResultPage, self).__init__(driver)
  
    def _verify_page(self):
        try:
            self.wait_for_element_visibility(10, 
                                             "xpath", 
                                             ResultPageMap['searchResultNumberXpath']
            )
        except:   
            raise IncorrectPageException

    def check_search_result_ad_name(self):
        try:
            searchResultAdName = self.find_element("xpath",
                                                   ResultPageMap['searchResultAdNameXpath']
            )
            global searchResultAdNameValue
            searchResultAdNameValue = searchResultAdName.text
            print "The Ad name in search result is %s." % searchResultAdNameValue
        except:
            raise IncorrectPageException

    def print_search_result_page_title(self):
        try:
            searchResultPageTitle = self.driver.title
            print "The search result page title is %s. " % searchResultPageTitle
        except:
            raise IncorrectPageException

    def fetch_count_of_search_results_single_page(self):
        try:
            searchResultsInColumn = self.driver.find_elements_by_css_selector(ResultPageMap['searchResultAdContainerCss'])
            # for el in searchResultsInColumn:
            #     print el.get_attribute("creativeid")
            print "The count of the single page is %s ." % len(searchResultsInColumn)
            
        except:
            raise IncorrectPageException

    def grab_printed_total_search_number(self):
        try:
            printedTotalNumberMsg = self.find_element("cssSelector",
                                                      ResultPageMap['searchResultPrintedTotalNumberMsgCss']
            ).text
            print "Query summary message is %s ." % printedTotalNumberMsg
            
            removeText = ' ads for ' + searchResultAdNameValue
            print removeText
            
            global printedQuerySummaryNumber
            printedQuerySummaryNumber = int(printedTotalNumberMsg.strip(removeText).replace(',',''))
            print "The printed total search number is %s ." % printedQuerySummaryNumber
        except:
            raise IncorrectPageException

    def fetch_total_count(self):
        try:
            pages = int(printedQuerySummaryNumber) // 100
            print "Pages = %s " % pages

            i = 0
            while i < pages:
                time.sleep(2)
                nextButton = self.find_element('cssSelector',
                                               ResultPageMap['searchNext100ButtonCss']
                )
                print "Next 100 ads button is there - No. %s " % i
                nextButton.click()
                print "Clicking the next 100 ads button - No. %s " % i
                i += 1

                if i == pages:
                    break

            time.sleep(2)
            ads = self.driver.find_elements_by_xpath("*//div[@class='adcontainer']")
            totalNumberOfAds = int(len(ads))
            print "The count of the single page is %s ." % totalNumberOfAds  
        except:
            raise IncorrectPageException

    def fetch_random_one_from_results_list(self):
        try:
            searchResultsInColumn_s = self.driver.find_elements_by_css_selector(ResultPageMap['searchResultAdContainerCss'])
            results_random = random.choice(searchResultsInColumn_s)

            random_one_creativeid = results_random.get_attribute("creativeid")
            print "The random selected one from the results list is %s." % random_one_creativeid
        except:
            raise IncorrectPageException

    def mouse_move_to_random_one(self):
        try:
            searchResultsInColumn_ss = self.driver.find_elements_by_css_selector(ResultPageMap['searchResultAdContainerCss'])
            results_random_ss = random.choice(searchResultsInColumn_ss)
            global random_one_creativeid_ss
            random_one_creativeid_ss = results_random_ss.get_attribute("creativeid")
            print "The random selected one from the results list is %s." % random_one_creativeid_ss

            self.wait_for_element_visibility(5,
                                             "cssSelector",
                                             ".adcontainer[creativeid='" + random_one_creativeid_ss + "']"
            )
            random_one = self.find_element("cssSelector",
                                           ".adcontainer[creativeid='" + random_one_creativeid_ss + "']"
            )

            actions = ActionChains(self.driver)
            actions.move_to_element(random_one)
            print "actions - move mouse to element"
            actions.click(random_one)
            print "actions - click the element"
            actions.perform()
            print "actions - done"
        except:
            raise IncorrectPageException

    def share_ad(self):
        try:
            self.click(5,
                       "xpath",
                       ".//*[@id='popup-container-" + random_one_creativeid_ss + "']/tbody/tr[2]/td[2]/div[2]/div[7]/a"
            )
            global share_ad_url
            share_ad_url = self.find_element("xpath",
                                             ".//*[@id='share-this-ad-" + random_one_creativeid_ss + "']"
            ).get_attribute('value')
            print "The Ad URL for sharing is %s. " % share_ad_url

            self.driver.get(share_ad_url)
            print "open the shared url"
            self.wait_for_element_visibility(5,
                                             "xpath",
                                             ".//*[@id='fancybox-outer']"
            )
            print "fancy box is there"
            self.click(5,
                       "xpath",
                       ".//*[@id='popup-container-hilight-" + random_one_creativeid_ss + "']/tbody/tr[2]/td[2]/div[2]/div[7]/a"
            )
            global fancy_highlight_url
            fancy_highlight_url = self.find_element("xpath",
                                                    ".//*[@id='share-this-ad-hilight-" + random_one_creativeid_ss + "']"
            ).get_attribute('value')
            print "The shared URL for the AD is %s. " % fancy_highlight_url
            
        except:
            raise IncorrectPageException
