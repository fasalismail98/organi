from django.contrib import admin
from .models import *



# Register your models here.

admin.site.register(CustomUser)
admin.site.register(product)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(blog)
admin.site.register(checkout)
admin.site.register(profile)
