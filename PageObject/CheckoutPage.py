from selenium.webdriver.common.by import By
from PageObject.ConfirmPage import Confir


class CheckOut:
    
    def __init__(self,driver):
        self.driver=driver
        
        
        
    products = (By.CSS_SELECTOR,"div[class='card h-100']")
    
        
    def checkoutItem(self):
        products = self.driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")
        for product in products:
            ProductName = product.find_element(By.XPATH,"div/h4/a").text
            if ProductName =="Blackberry":
                product.find_element(By.XPATH,"div/button").click()  
                ConfirmPages=Confir(self.driver)
                return ConfirmPages       
        
        