from celery import shared_task
from .coinmarketcap import CoinMarketCap
from .models import Job, Task

@shared_task
def scrape_coin_data(coin, job_id):
    coinmarketcap = CoinMarketCap()
    data = coinmarketcap.get_coin_data(coin)
    task = Task.objects.get(job_id=job_id, coin=coin)
    task.output = data
    task.status = 'COMPLETED' if data else 'FAILED'
    task.save()

