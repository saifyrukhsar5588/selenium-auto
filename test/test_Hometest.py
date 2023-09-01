import time
import pytest
from selenium.webdriver.common.by import By
from testData.HomePageData import homgpagedata
from utilities.BaseClass import BaseClass
from PageObject.HomePages import Homepage

class TestHomeDtaPage(BaseClass):
    
    def test_formsubmittion(self,getData):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        time.sleep(2)
        self.driver.maximize_window()
        log = self.getLogger()
        home=Homepage(self.driver)
        log.info("FirstName is"+getData["FirstName" ])
        home.getname().send_keys(getData["FirstName" ])
        home.getemail().send_keys(getData["email"])
        home.getpassword().send_keys("hello")
        home.getcheck().click()
        home.EmploymentStatu().click()
        self.selectOptionBytext(home.getgender(),getData["gender"])
        home.EmployeeText()
        home.getformsubmit().click()
        home.getSuccessmessage()
        self.driver.refresh()
        
        
    # @pytest.fixture(params=[("Amir","aamir@gmail.com","Male"),("Sone","sonu@gmail.com","Female")])
    @pytest.fixture(params=homgpagedata.gettestdata("TestCase1"))
    def getData(self,request):
        return request.param   