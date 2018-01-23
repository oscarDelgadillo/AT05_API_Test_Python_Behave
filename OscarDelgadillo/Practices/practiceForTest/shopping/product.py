import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Test_Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Product:
    def __init__(self, item, price, amount):
        self.item = item
        self.price = price
        self.amount = amount

    def set_amount(self, amount):
        self.amount = amount
        logger.debug('Set amount %s', self.amount)

    def get_amount(self):
        logger.info('Get amount %s', self.amount)
        return self.amount

    def get_price(self):
        logger.info('Get price %s', self.price)
        return self.price

    def show_product(self):
        print("{0} \t | {1} \t | {2}".format(self.item, self.price, self.amount))
