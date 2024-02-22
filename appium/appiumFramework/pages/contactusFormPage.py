from Amazon.base.BasePage import BasePage

class contactFormPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    _contactusFormButton = 'com.code2lead.kwad:id/ContactUs' #id
    _pagetitle = 'Contact Us form' #text
    _enterName = 'Enter Name'
    _enterEmail = 'Enter Email'
    _enterAddress = 'Enter Address'
    _entermobno = 'Enter Mobile No'
    _submitButton = 'SUBMIT'

    def clickcontactformbutton(self):
        self.clickElement(self._contactusFormButton,'id')
    def verifypagetitle(self):
        self.isDisplayed(self._pagetitle,'text')
    def enterName(self):
        self.sendText('vinaya',self._enterName,'text')
    def enterEmail(self):
        self.sendText('vinayashree@gmail.com',self._enterEmail,'text')
    def enterAddress(self):
        self.sendText('banshankari nagar hosur',self._enterAddress,'text')
    def enterMobileNo(self):
        self.sendText('8494889325',self._entermobno,'text')
    def clickSubmit(self):
        self.clickElement(self._submitButton,'text')
