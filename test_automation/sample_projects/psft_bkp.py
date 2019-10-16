from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException


class PeoplesoftTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_search_login_test(self):
        self.driver.get("http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/EMPLOYEE/ERP/?cmd=login")
        self.driver.find_element_by_id('userid').send_keys('VP1')
        self.driver.find_element_by_id('pwd').send_keys('FinSit#92')
        self.driver.find_element_by_name('Submit').click()
        print('<b><font color="green">Able to login into Application </font></b>')

    def test_search_gateway_test(self):
        self.driver.get("http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/EMPLOYEE/ERP/?cmd=login")
        self.driver.find_element_by_id('userid').send_keys('VP1')
        self.driver.find_element_by_id('pwd').send_keys('FinSit#92')
        self.driver.find_element_by_name('Submit').click()
        self.driver.get(
            "http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/EMPLOYEE/ERP/c/IB_PROFILE.IB_GATEWAY.GBL?PORTALPARAM_PTCNAV=PT_IB_GATEWAY_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=IB_CONFIGURATION_FLD&EOPP.SCLabel=Configuration&EOPP.SCPTfname=IB_CONFIGURATION_FLD&FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.IB_CONFIGURATION_FLD.PT_IB_GATEWAY_GBL&IsFolder=false")
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_id("#ICSearch").click()
        current_window = self.driver.current_window_handle
        self.driver.find_element_by_id('PTIB_ADMIN_WRK_IB_PINGGATE').click()
        sleep(4)

        handles = self.driver.window_handles
        size = len(handles)
        sleep(2)
        self.driver.switch_to.window(handles[1])
        self.driver.find_element_by_id("PING_STATUS")
        element = self.driver.find_element_by_id("PING_STATUS")
        if element.text == 'ACTIVE':
            print('<b><font color="green"> Gateway Status is : </font></b>'+element.text)
        else:
            print('<b><font color="red"> Gateway Status is : </font></b>' + element.text)
            assert element.text == 'ACTIVE'


    def test_search_PingNode_test(self):
        node=['FINSIT92','HSB_OFFICE_DEPOT','HSB_VENDOR_PO_SEND']
        result = []

        self.driver.get("http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/?cmd=login&languageCd=ENG&")
        self.driver.find_element_by_id('userid').send_keys('VP1')
        self.driver.find_element_by_id('pwd').send_keys('FinSit#92')
        self.driver.find_element_by_name('Submit').click()


        for x in range(len(node)):
            sleep(3)
            self.driver.get(
                "http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/EMPLOYEE/ERP/c/IB_PROFILE.IB_NODE.GBL?FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.PT_IB_INTEGRATION.PT_IB_NODE_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder")
            sleep(2)
            self.driver.switch_to.frame(0)
            self.driver.find_element_by_id("PSMSGNODEDEFN_MSGNODENAME").send_keys(node[x])
            self.driver.find_element_by_id("#ICSearch").click()

            sleep(4)
            self.driver.find_element_by_id("ICTAB_1").click()
            #elem1 = self.driver.find_element_by_xpath('//*[@id="ICTAB_1"]/span')

            #self.driver.find_element_by_xpath('//*[@id="ICTAB_1"]/span').click()
            self.driver.find_element_by_id("PTIB_ADMIN_WRK_PINGNODE_BTN").click()
            self.driver.switch_to.default_content()
            sleep(5)
            self.driver.switch_to.frame(self.driver.find_element_by_name('ptModFrame_0'))
            sleep(2)

            element = self.driver.find_element_by_id("MESSAGE_TEXT$0")
            result.append(element.text)

            if element.text == 'Success (117,73)' or element.text == 'success (117,73)':

                print('<b><font color="green"> Node '+node[x]+' Status is : </font></b>' + element.text+'<br><br>')


            else:

                print('<b><font color="red"> Node '+node[x]+' Status is : </font></b>' + element.text+'<br><br>')



        for i in range(len(result)):

            assert result[i] == 'Success (117,73)' or element.text == 'success (117,73)'
    def test_search_Vertex_connection(self):
        global noelement
        self.driver.get("http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/?cmd=login&languageCd=ENG&")
        self.driver.find_element_by_id('userid').send_keys('VP1')
        self.driver.find_element_by_id('pwd').send_keys('FinSit#92')
        self.driver.find_element_by_name('Submit').click()
        self.driver.get('http://cvgs060166.am.munichre.com:8050/psp/FINSIT92/EMPLOYEE/ERP/c/DEFINE_GENERAL_OPTIONS.TAX_PROV_INFO.GBL')
        self.driver.switch_to.frame(0)


        self.driver.find_element_by_id('TAX_WRK_TEST_TAX_PB').click()
        sleep(3)
        try:
            element = self.driver.find_element_by_id('TAX_WRK_GEO_CODE')
            if element.text != '':
                print(
                    '<b><font color="green"> Connection Established with vertex server, Geocode returend is:  </font></b>' + element.text + '<br><br>')
                noelement=0
            else:
                print('<b><font color="red"> Connection not Established to vertex server <br><br>')
                noelement=1

        except NoSuchElementException:
            noelement=1
            print('<b><font color="red"> Connection not Established to vertex server <br><br>')
        if noelement==1:
            assert 1==2

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/py/projects/test_automation/HTML'))