from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from time import sleep


class Test_psft():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_1_search_login_test(self,test_setup):
        driver.get("http://cvgs060160:8000/psp/FSM92DMO/?cmd=login&languageCd=ENG")
        driver.find_element_by_id('userid').send_keys('VP1')
        driver.find_element_by_id('pwd').send_keys('TstHsb#92')
        driver.find_element_by_name('Submit').click()
        print("Able to login into Application")

    def test_search_gateway_test(self,test_setup):
        driver.get("http://cvgs060160:8000/psp/FSM92DMO/?cmd=login&languageCd=ENG")
        driver.find_element_by_id('userid').send_keys('VP1')
        driver.find_element_by_id('pwd').send_keys('TstHsb#92')
        driver.find_element_by_name('Submit').click()
        driver.get(
            "http://cvgs060160:8000/psp/FSM92DMO/EMPLOYEE/ERP/c/IB_PROFILE.IB_GATEWAY.GBL?PORTALPARAM_PTCNAV=PT_IB_GATEWAY_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=IB_CONFIGURATION_FLD&EOPP.SCLabel=Configuration&EOPP.SCPTfname=IB_CONFIGURATION_FLD&FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.IB_CONFIGURATION_FLD.PT_IB_GATEWAY_GBL&IsFolder=false")
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        driver.find_element_by_id("#ICSearch").click()
        current_window = driver.current_window_handle
        driver.find_element_by_id('PTIB_ADMIN_WRK_IB_PINGGATE').click()
        sleep(4)
        handles = driver.window_handles
        size = len(handles)
        sleep(2)
        driver.switch_to.window(handles[1])
        driver.find_element_by_id("PING_STATUS")
        element = driver.find_element_by_id("PING_STATUS")
        print("Gateay Status is : " + element.text)

# def test_teardown():
#    driver.close()
#    driver.quit()
#    print("Test Completed")


