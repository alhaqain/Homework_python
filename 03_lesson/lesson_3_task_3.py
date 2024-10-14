from address import Address
from mailing import Mailing

track = 2345678901
from_address = Address("450001", "г. Уфа", "ул. Ленина", 20, 10)
to_address = Address("450012", "г. Уфа", "ул. Ульяновых", 36, 2)
cost = 455

mailing = Mailing(track, from_address, to_address, cost)
print(mailing)
