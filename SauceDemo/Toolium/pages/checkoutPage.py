from SeleniumFramework.base.BasePage import BaseClass


class CheckoutPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Login Page
    _checkoutButton = 'checkout'  # id
    _giveFirstName = 'first-name'  # id
    _giveLastName = 'last-name'  # id
    _givePostalCode = 'postal-code'  # id
    _clickContinueToCheckout = 'continue'  # id
    _finishButton = 'finish'

    def clickOnCheckoutButton(self):
        self.clickOnElement(self._checkoutButton, 'id')

    def giveCheckoutInfo(self):
        self.sendText('Vinayashree', self._giveFirstName, 'id')
        self.sendText('Naganuri', self._giveLastName, 'id')
        self.sendText('591221', self._givePostalCode, 'id')

    def clickOnContinueToCheckout(self):
        self.scrollTo(self._clickContinueToCheckout, 'id')
        self.clickOnElement(self._clickContinueToCheckout, 'id')

    def clickOnFinishButton(self):
        self.clickOnElement(self._finishButton, 'id')
