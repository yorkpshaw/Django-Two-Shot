from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from receipts.forms import AccountForm, ExpenseCategoryForm, ReceiptForm
from receipts.models import Account, ExpenseCategory, Receipt


# class AccountCreateView(LoginRequiredMixin, CreateView):
#     model = Account
#     template_name = "accounts/create.html"
#     fields = ["name", "number"]

#     def form_valid(self, form):
#         item = form.save(commit=False)
#         item.owner = self.request.user
#         item.save()
#         return redirect("list_accounts")


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("list_accounts")
    else:
        form = AccountForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/create.html", context)


# class AccountListView(LoginRequiredMixin, ListView):
#     model = Account
#     template_name = "accounts/list.html"

#     def get_queryset(self):
#         return Account.objects.filter(owner=self.request.user)


@login_required
def show_accounts(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "account_list": accounts,
    }
    return render(request, "accounts/list.html", context)


# class ExpenseCategoryCreateView(LoginRequiredMixin, CreateView):
#     model = ExpenseCategory
#     template_name = "expense_categories/create.html"
#     fields = ["name"]

#     def form_valid(self, form):
#         item = form.save(commit=False)
#         item.owner = self.request.user
#         item.save()
#         return redirect("list_categories")


@login_required
def create_expense_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            expense_category = form.save(commit=False)
            expense_category.owner = request.user
            expense_category.save()
            return redirect("list_categories")
    else:
        form = ExpenseCategoryForm()
    context = {
        "form": form,
    }
    return render(request, "expense_categories/create.html", context)


# class ExpenseCategoryListView(LoginRequiredMixin, ListView):
#     model = ExpenseCategory
#     template_name = "expense_categories/list.html"

#     def get_queryset(self):
#         return ExpenseCategory.objects.filter(owner=self.request.user)


@login_required
def show_expense_categories(request):
    expense_categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expensecategory_list": expense_categories,
    }
    return render(request, "expense_categories/list.html", context)


# class ReceiptCreateView(LoginRequiredMixin, CreateView):
#     model = Receipt
#     template_name = "receipts/create.html"
#     fields = ["vendor", "total", "tax", "date", "category", "account"]

#     def form_valid(self, form):
#         item = form.save(commit=False)
#         item.purchaser = self.request.user
#         item.save()
#         return redirect("home")


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


# class ReceiptListView(LoginRequiredMixin, ListView):
#     model = Receipt
#     template_name = "receipts/list.html"

#     def get_queryset(self):
#         return Receipt.objects.filter(purchaser=self.request.user)


@login_required
def show_receipts(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/list.html", context)
