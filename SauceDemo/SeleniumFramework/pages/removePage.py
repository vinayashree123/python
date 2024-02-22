from SeleniumFramework.base.BasePage import BaseClass


class RemovePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    _selectFilter = 'select'    #tag
    _productToAddToCart1 = 'item_5_img_link'    #id
    _addToCartButton1 = 'add-to-cart-sauce-labs-fleece-jacket'
    _shoppingCartLink = 'shopping_cart_link'    #class
    _cartQuality = 'cart_quantity' #class
    _removeButton = 'remove-sauce-labs-fleece-jacket' #id


    def selectFilterByDropDown(self):
        self.select_option_in_dropdown(self._selectFilter,'tag',optionValue='hilo')

    def clickOnProduct(self):
        self.clickOnElement(self._productToAddToCart1,'id')

    def clickOnAddToCartButton1(self):
        self.clickOnElement(self._addToCartButton1,'id')

    def clickOnShoppingCartLink(self):
        self.clickOnElement(self._shoppingCartLink,'class')

    def clickOnRemoveButton(self):
        self.clickOnElement(self._removeButton,'id')







