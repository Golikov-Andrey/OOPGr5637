from typing import List
from Domain.product import Product

from Services.coin_dispenser import CoinDispenser
from Services.display import Display
from Services.holder import Holder

class VendingMachine:
    def __init__(self, holder: Holder, dispenser: CoinDispenser, assort: List[Product], display: Display):
        self.holder = holder
        self.dispenser = dispenser
        self.assort = assort
        self.display = display


    def getProducts(self):
        return self.assort

    def buyProduct(self, p: Product, price):
        if p in self.assort and self.holder.getBalance() >= price:
            if self.dispenser.dispense(price):
                self.releaseProduct(p, self.holder)
                self.display.print("You have successfully bought " + p.getName() + ".")
        else:
            self.display.print("Product not available or insufficient balance.")

    def releaseProduct(self, p: Product, h: Holder):
        h.release(0, 0)
        self.assort.remove(p)

    def cancel(self):
        self.dispenser.giveChahge(0, 0)

    def getHolder(self):
        return self.holder

    def getDispenser(self):
        return self.dispenser

    def getAssort(self):
        return self.assort

    def getDisplay(self):
        return self.display