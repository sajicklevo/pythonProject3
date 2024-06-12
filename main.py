class Goods:
    def __init__(self, item_name, store_name, price):
        self.__item_name = item_name
        self.__store_name = store_name
        self.__price = price

    def get_item_name(self):
        return self.__item_name

    def get_store_name(self):
        return self.__store_name

    def get_price(self):
        return self.__price

    def set_price(self, price2):
        self.__price = price2
        return self.__price


class Warehouse:
    def __init__(self):
        self.__tovars = []

    def add_product(self, product):
        self.__tovars.append(product)

    def print_product_by_index(self, index):
        if index < len(self.__tovars):
            print("Item Name: {}, Store Name: {}, Price: {}".format(self.__tovars[index].get_item_name(),
                                                                    self.__tovars[index].get_store_name(),
                                                                    self.__tovars[index].get_price()))
        else:
            print("Index out of range")

    def print_product_by_name(self, name):
        for product in self.__tovars:
            if product.get_item_name() == name:
                print("Item Name: {}, Store Name: {}, Price: {}".format(product.get_item_name(),
                                                                        product.get_store_name(),
                                                                        product.get_price()))

    def sort_goods_by_name(self):
        self.__tovars.sort(key=lambda x: x.get_item_name())

    def sort_goods_by_store(self):
        self.__tovars.sort(key=lambda x: x.get_store_name())

    def sort_goods_by_price(self):
        self.__tovars.sort(key=lambda x: x.get_price())

    def add(self, other):
        total_price = sum([good.get_price() for good in self.__tovars]) + sum(
            [good.get_price() for good in other.__tovars])
        return total_price
