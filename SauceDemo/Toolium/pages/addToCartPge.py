from Toolium.base.BasePage import BaseClass


class AddToCartPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Login Page
    _scrollEle = '//*[@id="item_3_title_link"]/div'  # xpath
    _productToAddToCart = 'item_3_img_link'   #id
    _addToCartButton = 'add-to-cart-test.allthethings()-t-shirt-(red)' #id
    _shoppingCartLink = 'shopping_cart_link'    #class

    def scrollElement(self):
        self.scrollTo(self._scrollEle,'xpath')

    def clickOnProductAddToCart(self):
        self.clickOnElement(self._productToAddToCart,'id')

    def clickOnAddToCartButton(self):
        self.clickOnElement(self._addToCartButton,'id')

    def clickOnShoppingCartLink(self):
        self.clickOnElement(self._shoppingCartLink,'class')












