# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
# from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from utilities import XLUtils
# import pytest
import time

class Test_001_Login:
    baseUrl="https://admin-demo.nopcommerce.com"#ReadConfig.getApplicationUrl()
    username="admin@yourstore.com"#ReadConfig.getUserName()
    password="admin"#ReadConfig.getUserPassword()
    # workbook=ReadConfig.getWorkbook()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.logger.info("============Succefully Initialize Browser=============")
        time.sleep(5)
        self.logger.info("============test_homePageTitle starts=============")
        siteTitle=self.driver.title
        if siteTitle=="Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("============Successfuly Passed=============")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTittle.png")
            self.driver.close()
            self.logger.error("============test_homePageTitle Fails=============")
            assert False
            

    def test_Login(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(1)
        self.lp=LoginPage(self.driver)
        self.driver.maximize_window()
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        act_tittle=self.driver.title
        
        if act_tittle=="Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
            

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_successfully_Loggedin_failed.png")
            self.driver.close()
            assert False
            