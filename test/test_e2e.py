import time
import pytest
from selenium.webdriver.common.by import By

from PageObject.HomePages import Homepage
from PageObject.CheckoutPage import CheckOut
from PageObject.ConfirmPage import Confir
from utilities.BaseClass import BaseClass




class TestOne(BaseClass):
    
    def test_e2e(self):
        # time.sleep(2)
        log = self.getLogger()
        HomePages = Homepage(self.driver)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.maximize_window()
        CheckoutPage = HomePages.shopItem()
        log.info("Getting all cards titles")
        ConfirmPages =CheckoutPage.checkoutItem()
        ConfirmPages.confirmItem()
        