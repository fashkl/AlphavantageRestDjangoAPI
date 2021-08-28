from django.db import models


class BitcoinToUSDRates(models.Model):
    currencies = models.CharField(max_length=60, default='BTC/USD', )
    exchange_rate = models.DecimalField(decimal_places=8, max_digits=60)
    last_refreshed = models.CharField(max_length=60)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s=%s @ %s' % (self.currencies, self.exchange_rate, self.last_refreshed)

