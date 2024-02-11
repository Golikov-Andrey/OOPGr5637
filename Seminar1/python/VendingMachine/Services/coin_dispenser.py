class CoinDispenser:
    def __init__(self, nominal):
        self.nominal = nominal


    def __str__(self):
        return "Номинал монеты равен " + str(self.nominal)

    def getSumm(self, insertCoin, outCoin):
        summCoin = insertCoin + outCoin
        return summCoin

    def giveChahge(self, summCoin, price):
        if price < summCoin:
            change = summCoin - price
        elif price == summCoin:
            change = summCoin - price
        else:
            change = 0
        return change

    def dispense(self, price):
        return False