import ipdb

from jackpot import *

g1 = Gambler("Alex")
g2 = Gambler("James")

d1 = Dealer("GS")
d2 = Dealer("MS")
d3 = Dealer("JP")

b1 = Bid(g1,d1, 500)
b2 = Bid(g1,d2,1000)
b3 = Bid(g2, d1, 100)
b4 = Bid(g2, d2, 200)




ipdb.set_trace()

