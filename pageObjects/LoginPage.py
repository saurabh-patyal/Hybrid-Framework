from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    text_username_id="Email"
    text_Password_id="Password"
    Login_btn_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    Logout_btn_linktext="Logout"

    def __init__(self,driver):  ##########python constructor,to invoke object of this class######
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID,self.text_username_id).send_keys(username)

    def setUserPassword(self,password):
        self.driver.find_element(By.ID,self.text_Password_id).clear()
        self.driver.find_element(By.ID,self.text_Password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.Login_btn_xpath).click()

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.Logout_btn_linktext).click()