from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Dividend


class DividendList(generic.ListView):
    model = Dividend
    template_name = "list.html"
    context_object_name = "dividends"
    queryset = Dividend.objects.order_by("-id")
    paginate_by = 50



class DividendCreate(LoginRequiredMixin, generic.CreateView):
    model = Dividend
    template_name = "create.html"
    fields = [
        "symbol",
        "company_name",
        "fiscal_year",
        "meeting_date",
        "number_of_shares",
        "capital",
        "eps",
        "dps",
        "total_dividend",
        "payment_schedule",
        "comments",
        "latest_actual_payment_date",
        "latest_payment_amount",
    ]
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DividendUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Dividend
    template_name = "update.html"
    fields = [
        "symbol",
        "company_name",
        "fiscal_year",
        "meeting_date",
        "number_of_shares",
        "capital",
        "eps",
        "dps",
        "total_dividend",
        "payment_schedule",
        "comments",
        "latest_actual_payment_date",
        "latest_payment_amount",
    ]
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class DividendDelete(LoginRequiredMixin, generic.DeleteView):
    model = Dividend
    template_name = "delete.html"
    context_object_name = "dividend"
    success_url = reverse_lazy("list")
