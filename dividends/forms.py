from django import forms

from .models import Dividend

class DividendForm(forms.ModelForm):
    class Meta:
        model = Dividend
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
