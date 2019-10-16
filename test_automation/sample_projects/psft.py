from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,WebDriverException
import os

class PeoplesoftTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_search_login_test(self):
        global loginme
        global host
        global site
        global user
        global pwd
        global nodes
        host = os.environ.get("TEST_HOST")
        site=os.environ.get("SITE_NAME")
        user=os.environ.get("USER_ID")
        pwd = os.environ.get("USER_PWD")
        nodes = os.environ.get("NODE_NAMES")

        try:
            self.driver.get(host+"/psp/"+site+"/EMPLOYEE/ERP/?cmd=login")
            self.driver.find_element_by_id('userid').send_keys(user)
            self.driver.find_element_by_id('pwd').send_keys(pwd)
            self.driver.find_element_by_name('Submit').click()
            assert "Homepage" in self.driver.title
            print('<b><font color="green">Able to login into Application </font></b>')
            loginme=0
        except Exception as e:
            #print (format(e))
            print('<b><font color="red">URL or UserID/Password is wrong </font></b>')
            loginme=1
        if loginme==1:
            assert 1==2


    def test_search_gateway_test(self):
        global isgateway
        try:
            self.driver.get(host+"/psp/"+site+"/EMPLOYEE/ERP/?cmd=login")
            self.driver.find_element_by_id('userid').send_keys(user)
            self.driver.find_element_by_id('pwd').send_keys(pwd)
            self.driver.find_element_by_name('Submit').click()
            assert "Homepage" in self.driver.title
            loginme=0
        except Exception as e:
            print('<b><font color="red">URL or UserID/Password is wrong </font></b>')
            loginme=1
        if loginme==1:
            assert 1==2
        self.driver.get(
            host+"/psp/"+site+"/EMPLOYEE/ERP/c/IB_PROFILE.IB_GATEWAY.GBL?PORTALPARAM_PTCNAV=PT_IB_GATEWAY_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=IB_CONFIGURATION_FLD&EOPP.SCLabel=Configuration&EOPP.SCPTfname=IB_CONFIGURATION_FLD&FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.IB_CONFIGURATION_FLD.PT_IB_GATEWAY_GBL&IsFolder=false")
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(0)
        try:
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
                isgateway=0
            else:
                print('<b><font color="red"> Gateway Status is : </font></b>' + element.text)
                isgateway=1
        except NoSuchElementException:
            print('<b><font color="red"> Issue in searching Gateway Please check manually  </font></b><br><br>')
            isgateway = 1
        if isgateway==1:
            assert 1==2


    def test_search_PingNode_test(self):
        if nodes is None:
            assert 1 == 1
            print('<b><font color="green"> No Node defined for this test </font></b><br><br>')
        else:
            node=nodes.split(",")
        #node=['FINSIT92','HSB_OFFICE_DEPOT','HSB_VENDOR_PO_SEND']
            result = []

            try:
                self.driver.get(host+"/psp/"+site+"/EMPLOYEE/ERP/?cmd=login")
                self.driver.find_element_by_id('userid').send_keys(user)
                self.driver.find_element_by_id('pwd').send_keys(pwd)
                self.driver.find_element_by_name('Submit').click()
                assert "Homepage" in self.driver.title
                loginme=0
            except Exception as e:
                print('<b><font color="red">URL or UserID/Password is wrong </font></b>')
                loginme=1
            if loginme==1:
                assert 1==2


            for x in range(len(node)):
                global nonode
                sleep(3)
                self.driver.get(
                    host+"/psp/"+site+"/EMPLOYEE/ERP/c/IB_PROFILE.IB_NODE.GBL?FolderPath=PORTAL_ROOT_OBJECT.PT_PEOPLETOOLS.PT_IB_PROFILE.PT_IB_INTEGRATION.PT_IB_NODE_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder")
                sleep(2)
                self.driver.switch_to.frame(0)
                try:
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
                        nonode=0

                    else:

                        print('<b><font color="red"> Node '+node[x]+' Status is : </font></b>' + element.text+'<br><br>')
                        nonode=1

                except NoSuchElementException:
                    print('<b><font color="red"> Node '+node[x]+' Not Found : </font></b><br><br>')
                    nonode=1



            for i in range(len(result)):
                assert result[i] == 'Success (117,73)' or element.text == 'success (117,73)'
            if nonode==1:
                assert 1==2


    def test_search_Vertex_connection(self):
        global noelement
        try:
            self.driver.get(host + "/psp/" + site + "/EMPLOYEE/ERP/?cmd=login")
            self.driver.find_element_by_id('userid').send_keys(user)
            self.driver.find_element_by_id('pwd').send_keys(pwd)
            self.driver.find_element_by_name('Submit').click()
            assert "Homepage" in self.driver.title
            loginme = 0
        except Exception as e:
            print('<b><font color="red">URL or UserID/Password is wrong </font></b>')
            loginme = 1
        if loginme == 1:
            assert 1 == 2
        self.driver.get(host+"/psp/"+site+"/EMPLOYEE/ERP/c/DEFINE_GENERAL_OPTIONS.TAX_PROV_INFO.GBL")
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
    html_output = "C:/py/projects/test_automation/HTML"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_output))