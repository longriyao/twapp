from django.contrib import admin
from .models import project, projectColor, projectSize, projectSku, orderUser, orderaddress, SkuOrders, projectColorImages


admin.site.register(project)

admin.site.register(projectColor)
admin.site.register(projectSize)
admin.site.register(projectSku)
admin.site.register(orderUser)
admin.site.register(orderaddress)
admin.site.register(SkuOrders)
admin.site.register(projectColorImages)
# Register your models here.
