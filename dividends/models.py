from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Dividend(models.Model):
    symbol = models.CharField(max_length=255, verbose_name=_("symbol"))
    company_name = models.CharField(max_length=255, verbose_name=_("company_name"))
    fiscal_year = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        verbose_name=_("fiscal_year"),
    )
    meeting_date = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        verbose_name=_("meeting_date"),
    )
    number_of_shares = models.PositiveBigIntegerField(
        verbose_name=_("number_of_shares")
    )
    capital = models.PositiveBigIntegerField(verbose_name=_("capital"))
    eps = models.PositiveIntegerField(verbose_name=_("eps"))
    dps = models.PositiveIntegerField(verbose_name=_("dps"))
    total_dividend = models.PositiveBigIntegerField(verbose_name=_("total_dividend"))
    payment_schedule = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        verbose_name=_("payment_schedule"),
    )
    comments = models.TextField(blank=True, verbose_name=_("comments"))
    latest_actual_payment_date = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10)],
        null=True,
        blank=True,
        verbose_name=_("latest_actual_payment_date"),
    )
    latest_payment_amount = models.PositiveBigIntegerField(null=True, blank=True, verbose_name=_("latest_payment_amount"))
    created_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name="dividends",
        default=1,
        verbose_name=_("created_by"),
    )
    updated_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        related_name="updated_dividends",
        null=True,
        blank=True,
        verbose_name=_("updated_by"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated_at"))
