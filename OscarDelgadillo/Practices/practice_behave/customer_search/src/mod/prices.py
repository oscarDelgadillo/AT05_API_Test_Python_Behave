class Prices:
    def __init__(self):
        self.list_prices = {}
        self.set_list_prices()

    def get_list_prices(self):
        return self.list_prices

    def set_list_prices(self):
        self.list_prices.update({"ID001": 123.4})
        self.list_prices.update({"ID002": 8450.4})
        self.list_prices.update({"ID003": 454.0})
        self.list_prices.update({"ID004": 10.5})

    def get_price_by_id(self, id):
        return self.list_prices.get(id)
