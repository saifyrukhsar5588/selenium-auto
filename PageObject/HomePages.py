import time
from selenium.webdriver.common.by import By
from PageObject.CheckoutPage import CheckOut

class Homepage:
    
    # constructor for driver
    def __init__(self,driver):
        self.driver=driver
        
        
    #  class variable   
    shop = (By.LINK_TEXT,"Shop")
    email = (By.NAME,"email")
    name = (By.NAME,"name")
    check=(By.ID,"exampleCheck1")
    gender=(By.XPATH,"//select[@id='exampleFormControlSelect1']")
    submit=(By.XPATH,"//input[@type= 'submit']")
    message=(By.CLASS_NAME, "alert-success")
    password=(By.ID,"exampleInputPassword1")
    EmploymentStatus=(By.CSS_SELECTOR,"#inlineRadio1")
    
    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        self.driver.execute_script("window.scroll(0,550)")
        time.sleep(2)
        CheckoutPage = CheckOut(self.driver)
        return CheckoutPage
        # CheckoutPage.checkoutItem()
        
    def getname(self):
        return self.driver.find_element(*Homepage.name)    
    
    def getemail(self):
        return self.driver.find_element(*Homepage.email)  
    
    def getcheck(self):
        return self.driver.find_element(*Homepage.check) 
    
    def getgender(self):
        return self.driver.find_element(*Homepage.gender) 
    
    def getformsubmit(self):
        return self.driver.find_element(*Homepage.submit) 
    
    def getSuccessmessage(self):
         message=self.driver.find_element(*Homepage.message).text
         print(message)
         assert "Success" in message
         print("pass")
    
    def getpassword(self):
        return self.driver.find_element(*Homepage.password)
    
    def EmploymentStatu(self):
        return self.driver.find_element(*Homepage.EmploymentStatus)
    
    def EmployeeText(self):
        self.driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
        self.driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello123")