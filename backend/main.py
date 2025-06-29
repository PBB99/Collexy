
from models.product import new_product,get_all_products
from models.unique_keys import get_unique_keys
from datetime import datetime
#test_get_unique_keys=get_unique_keys("MY_PRODUCTS")
#test_product=new_product("Carta Pokémon Charizard", 1,1,"NM",True, 2,1500.00,1200.00,"https://ejemplo.com/producto/charizard","Primera edición, condición excelente")
test_product=get_all_products()
print(test_product)



