from django.shortcuts import render
from django.views.generic.list import ListView
from receipts.models import Receipt
from django.views.generic.base import RedirectView


class ReceiptListView(ListView):
    model = Receipt
    template_name = "receipts/list.html"
    context_object_name = "receiptlist"
