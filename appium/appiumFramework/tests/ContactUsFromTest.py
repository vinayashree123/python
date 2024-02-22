import time

from appiumFramework.base.DriverClass import Driver
import appiumFramework.utilities.CustomLogger as cl
from appiumFramework.base.BasePage import BasePage
from appiumFramework.pages.contactusFormPage import contactFormPage

d1 = Driver()
log = cl.customLogger()

driver=d1.getDriverMethod()
log.info("Launching app")

# bp = BasePage(driver)
# bp.screenshots('launchapp')
# # element = bp.WaitForElement('com.code2lead.kwad:id/EnterValue','id')
# # element.click()
# # time.sleep(2)
# # element = bp.WaitForElement(6,'index')
# # element.click()
# element = bp.isDisplayed('com.code2lead.kwad:id/EnterValue','id')
# print(element)
# bp.clickElement('com.code2lead.kwad:id/EnterValue','id')
# bp.sendText('vina','com.code2lead.kwad:id/Et1','id')
# bp.screenshots('sendtextpage')

cf = contactFormPage(driver)
cf.clickcontactformbutton()
cf.verifypagetitle()
cf.enterName()
cf.enterEmail()
cf.enterMobileNo()
cf.enterAddress()
cf.clickSubmit()
cf.screenshots('register')
