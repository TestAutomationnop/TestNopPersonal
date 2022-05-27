import time

import pytest

from pageObjects.LoginPage import LoginPage1
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import readProerty
from Utilities.customLogger import loggen
from Utilities import ExcelUtils

class Test_002_Login:
    baseUrl = readProerty.getApplicationUrl()
    path = "./TestCases/TestData/Book1.xlsx"

    loggers = loggen()

    @pytest.mark.regression
    def test_Login(self):
        # self.driver = setup
        self.loggers.info("*******************  Login test started **********************")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)

        self.lp = LoginPage1(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        exp_reslt = []

        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path,'Sheet1',r,2)
            self.exe = ExcelUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exe == "pass":
                    self.loggers.info("******************** test passed*****")
                    time.sleep(20)
                    self.lp.clickLogout()
                    exp_reslt.append("Pass")
                elif self.exe == "Fail":
                    self.loggers.info("test failed")
                    time.sleep(20)
                    self.lp.clickLogout()
                    exp_reslt.append("Fail")
            elif act_title != exp_title:
                if self.exe == "pass":
                    self.loggers.info("******************** test failed*****")
                    time.sleep(20)
                    #self.lp.clickLogout()
                    exp_reslt.append("Fail")
                elif self.exe == "Fail":
                    self.loggers.info("test pass")
                    time.sleep(20)
                    #self.lp.clickLogout()
                    exp_reslt.append("Pass")

        if "Fail" not in exp_reslt:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
        self.driver.close()
