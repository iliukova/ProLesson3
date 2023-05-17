# Task 2
# Модифікуйте друге домашнє завдання (Дисконт),
# додавши перевірки в методи класів та обробку виключних ситуацій.
# При спробі встановити знижку не в межах 0-100 % треба викликати виняткову ситуацію,
# тип якої реалізувати самостійно.

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-10s %(levelname)-8s %(message)s')

filehandler = logging.FileHandler(f'log.txt')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

class Discount:
    def __init__(self, rate: float = 0):
        self.__rate = rate

    def discount(self):
        return self.__rate


class RegularDiscount(Discount):
    def __init__(self, rate=1.1):
        super().__init__(rate)


class SilverDiscount(Discount):
    def __init__(self, rate=0.2):
        super().__init__(rate)


class GoldDiscount(Discount):
    def __init__(self, rate=0.3):
        super().__init__(rate)

class PriceError(Exception):
    def __init__(self, price, msg):
        self.price = price
        self.msg = msg
class Product:
    def __init__(self, title: str, price: float | int):
        if not isinstance(price, int | float):
            raise TypeError()
        if price <= 0:
            raise PriceError(price, 'Price must be gt zero!')

        self.title = title
        self.price = price

    def __str__(self):
        return self.title
    def __str__(self):
        return f'{self.name}: {self.price:.2f}'


class Cart:

    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product, quantity=1):
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        res = ''
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн\n'
        return res

class DiscountError(Exception):
    def __init__(self, discount, msg):
        self.discount = discount
        self.msg = msg

class Client:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount

    def __init__(self, name: str, discount: Discount):
        if not isinstance(discount, Discount):
            raise TypeError()
        if discount > 1:
            raise DiscountError(discount*100, 'Discount can`t be more than 100!')

    def get_total_price(self, order: Cart):
        return order.total() * (1 - self.discount.discount())

cart = Cart()
pr_1 = Product('banana', 10)
pr_2 = Product('apple', 20)
pr_3 = Product('orange', 30)

cart.add_product(pr_1)
cart.add_product(pr_2, 3)
cart.add_product(pr_3, 2)

client = Client('User 1', RegularDiscount())
print(client.get_total_price(cart))