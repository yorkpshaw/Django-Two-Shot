from django.contrib import admin
from receipts.models import Receipt


# Register your models here.
class ReceiptAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipt, ReceiptAdmin)
