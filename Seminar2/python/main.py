from Classes.market import Market
from Classes.ordinary_client import OrdinaryClient
from Classes.special_client import SpecialClient
from Classes.tax_inspector import TaxInspector


magnit = Market()

client1 = OrdinaryClient("boris")
client2 = SpecialClient("prezident", 1)
client3 = TaxInspector()

magnit.acceptToMarket(client1)
magnit.acceptToMarket(client2)
magnit.acceptToMarket(client3)

magnit.update()