from django.urls import include, path

from .views import BitcoinToUSDView

urlpatterns = [
    path('quotes', BitcoinToUSDView.as_view()),
]
