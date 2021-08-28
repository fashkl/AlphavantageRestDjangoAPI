from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse

from .models import BitcoinToUSDRates
from .exchange_rate_method import get_bitcoin_usd_exchange_rate


class BitcoinToUSDView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BitcoinToUSDView, self).dispatch(*args, **kwargs)

    def get(self, request):
        query_set = BitcoinToUSDRates.objects.all().order_by('-last_refreshed')

        items_data = []
        for item in query_set:
            items_data.append({
                'price': item.exchange_rate,
                'date': item.last_refreshed,
            })

        if items_data:
            data = {"Rates": items_data}
        else:
            data = {"Rates": "Sorry! No listed rates for the requested currencies"}

        return JsonResponse(data)

    def post(self, request):
        response = get_bitcoin_usd_exchange_rate()
        if response:
            data = {"message": "Success, force requesting of the price from alphaVantage API"}
        else:
            data = {"message": "Sorry! force requesting of the price from alphaVantage API"}

        return JsonResponse(data, status=201)
