from SeleniumFramework.base.BasePage import BaseClass

class FilterPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    _selectFilterByOptionValue = 'select'   #tag
    _selectFilterByOptionIndex = 'select'   #tag
    _selectFilterByOptionText = 'select'    #tag

    def selectFilterByDropDownUsingOptionValue(self):
        self.select_option_in_dropdown(self._selectFilterByOptionValue,'tag',optionValue='hilo')

    def selectFilterByDropDownUsingOptionIndex(self):
        self.select_option_in_dropdown(self._selectFilterByOptionIndex,'tag',optionIndex=1)

    def selectFilterByDropDownUsingOptionText(self):
        self.select_option_in_dropdown(self._selectFilterByOptionText,'tag',optionText='Price (low to high)')













