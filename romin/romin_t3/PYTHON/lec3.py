import lec3_module
lec3_module.add(3,5)

import lec3_module as m
m.product(3,5)

from lec3_module import x,product
print(x)
product(1,0)

from lec3_module import*
print(x)
lec3_module.product(9,8)
lec3_module.add(9,8)