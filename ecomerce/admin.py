from itertools import product
from django.contrib import admin

from ecomerce.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)

# Test
admin.site.register(Test)

# admin.site.register(Book)
# admin.site.register(CategoryBook)
# admin.site.register(Brand)
# admin.site.register(MobilePhone)
# admin.site.register(Clothes)
# admin.site.register(Shoes)
# admin.site.register(Electronics)

