import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.BaseClass import BaseClass


class Confir(BaseClass):
    
    
    # constructor for driver
    def __init__(self,driver):
        self.driver=driver
        
        
    def confirmItem(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']").click()       
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID,"country").send_keys("Ind")
        # wait = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifylinkprsent("India")
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        successText=self.driver.find_element(By.CSS_SELECTOR,".alert-success").text
        assert "Success! Thank you" in successText
        print("pass")    