from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap
import uuid

@shared_task
def scrape_coin_data(job_id, coins):
    coinmarketcap = CoinMarketCap()
    job = Job.objects.get(job_id=job_id)
    for coin in coins:
        data = coinmarketcap.get_coin_data(coin)
        Task.objects.create(job=job, coin=coin, output=data)
