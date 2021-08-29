import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from .exchange_rate_method import get_bitcoin_usd_exchange_rate


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_bitcoin_usd_exchange_rate, 'interval', hours=1)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
