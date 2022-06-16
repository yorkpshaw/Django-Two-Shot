from django import forms
from receipts.models import Account, Receipt, ExpenseCategory


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "number"]


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["vendor", "total", "tax", "date", "category", "account"]
