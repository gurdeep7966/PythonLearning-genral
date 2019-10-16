from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import HtmlTestRunner

class PeoplesoftTest(unittest.TestCase):

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print("into setup class")

    def login_test(self):
        self.driver.get("http://cvgs060160:8000/psp/FSM92DMO/?cmd=login&languageCd=ENG")
        self.driver.find_element_by_id('userid').send_keys('VP1')
        self.driver.find_element_by_id('pwd').send_keys('TstHsb#92')
        self.driver.find_element_by_name('Submit').click()

    def gateway_test(self):
        self.driver.get(
            "http://cvgs060160:8000/psp/FSM92DMO/EMPLOYEE/ERP/c/IB_PROFILE.IB_GATEWAY.GBL?PORTALPARAM_PTCNAV=PT_IB_GATEWAY_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=IB_CONFIGURATION_FLD&EOPP.SCLabel=Configuration&EOPP.SCPTfname=IB_CONFIGURATION_FLD&FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.IB_CONFIGURATION_FLD.PT_IB_GATEWAY_GBL&IsFolder=false")
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_id("#ICSearch").click()
        current_window = self.driver.current_window_handle
        self.driver.find_element_by_id('PTIB_ADMIN_WRK_IB_PINGGATE').click()
        sleep(4)

        handles = self.driver.window_handles
        size = len(handles)
        print(size)
        sleep(2)
        self.driver.switch_to.window(handles[1])
        self.driver.find_element_by_id("PING_STATUS")
        #element = self.driver.find_element_by_id("PING_STATUS")
        #print(element.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/py/projects/test_automation/HTML'))














