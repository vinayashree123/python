import time
from SeleniumFramework.base.DriverClass import WebDriverClass
from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.pages.loginPage import LoginPage

wd = WebDriverClass()
driver = wd.getWebDriver('edge')

bp = BaseClass(driver)
# driver.get('http://www.dummypoint.com/')
log = cl.customLogger()
log.info('web page launched')


lp = LoginPage(driver)

bp.launchWebPage("https://www.saucedemo.com/", "Swag Labs")



lp.clickOnUserName()
lp.enterUserName()
lp.clickOnPassword()
lp.enterPassword()
lp.clickOnLoginButton()
time.sleep(2)
driver.quit()
