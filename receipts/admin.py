from django.contrib import admin
from receipts.models import Receipt, ExpenseCategory, Account


# Register your models here.
class ReceiptAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipt, ReceiptAdmin)


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)
