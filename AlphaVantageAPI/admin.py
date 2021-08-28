from django.contrib import admin
from .models import BitcoinToUSDRates


# Register your models here.
class BitcoinToUSDRatesAdmin(admin.ModelAdmin):
    class Meta:
        model = BitcoinToUSDRates

    readonly_fields = ["currencies", "post_date"]


admin.site.register(BitcoinToUSDRates, BitcoinToUSDRatesAdmin)

