from django.urls import path

from receipts.views import (
    show_accounts,
    show_expense_categories,
    show_receipts,
    create_account,
    create_expense_category,
    create_receipt,
)


urlpatterns = [
    path("", show_receipts, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("accounts/", show_accounts, name="list_accounts"),
    path(
        "accounts/create/",
        create_account,
        name="create_account",
    ),
    path(
        "categories/",
        show_expense_categories,
        name="list_categories",
    ),
    path(
        "categories/create/",
        create_expense_category,
        name="create_category",
    ),
]
