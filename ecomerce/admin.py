from itertools import product
from django.contrib import admin

from ecomerce.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Shoes)
admin.site.register(Clothes)
admin.site.register(Laptop)
admin.site.register(Electronic)
admin.site.register(MobilePhone)

# Test

# admin.site.register(Book)
# admin.site.register(CategoryBook)
# admin.site.register(Brand)
# admin.site.register(MobilePhone)
# admin.site.register(Clothes)
# admin.site.register(Shoes)
# admin.site.register(Electronics)

