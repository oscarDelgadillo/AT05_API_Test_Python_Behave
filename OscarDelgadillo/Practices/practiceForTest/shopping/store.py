from practiceForTest.shopping.product import Product
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Test_Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Shopping:
    def __init__(self):
        self.list_items = []

    def add_item(self, item, price, amount):
        prod = Product(item, price, amount)
        self.list_items.append(prod)
        logger.debug('Adding product to store')

    def display_products(self):
        print("List Products")
        print("ITEMS \t | PRICES \t | AMOUNT")
        for prod in self.list_items:
            prod.show_product()
        logger.info('Show products of store')

    def exist_item(self, item):
        for prod in self.list_items:
            if prod.item == item:
                return True
        return False

    def available_amount(self, amount, item):
        for prod in self.list_items:
            if prod.item == item and int(prod.amount) >= int(amount):
                logger.info('item {0} available for sell'.format(prod.item))
                return True
        return False

    def get_product(self, item):
        for prod in self.list_items:
            if prod.item == item:
                logger.info('Get item: {0}'.format(prod.item))
                return prod

    def sell_item(self, item, amount):
        for prod in self.list_items:
            if prod.item == item and prod.amount >= int(amount):
                prod.set_amount(prod.get_amount() - int(amount))
                logger.debug('Product {0} was sold'.format(prod.item))
