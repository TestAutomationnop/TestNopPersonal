import pytest

from pageObjects.LoginPage import LoginPage1
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import readProerty
from Utilities.customLogger import loggen


class Test_001_Login:
    baseUrl = readProerty.getApplicationUrl()
    username = readProerty.getApplicationUsername()
    password = readProerty.getApplicationpassword()
    loggers = loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self):
        # self.driver = setup
        self.loggers.info("*******************  Test_001_Login  **********************")
        self.loggers.info("*******************  Page Title verification started  **********************")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.loggers.info("*******************  Title verification completed successfully  **********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.loggers.info("*******************  Title verification failed  **********************")
            assert False

    @pytest.mark.regression
    def test_Login(self):
        # self.driver = setup
        self.loggers.info("*******************  Login test started **********************")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseUrl)

        self.lp = LoginPage1(self.driver)

        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.loggers.info("*******************  Login test completed successfully  **********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.loggers.info("*******************  Login test failed with title name exception  **********************")
            assert False
