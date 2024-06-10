from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Job, Task
from .serializers import JobSerializer
from .tasks import scrape_coin_data
import uuid

class JobViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def start_scraping(self, request):
        coins = request.data.get('coins', [])
        if not all(isinstance(coin, str) for coin in coins):
            return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

        job = Job.objects.create()
        for coin in coins:
            Task.objects.create(job=job, coin=coin)
            scrape_coin_data.delay(coin, str(job.job_id))
        return Response({'job_id': str(job.job_id)})

    @action(detail=True, methods=['get'])
    def scraping_status(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        return Response(serializer.data)
