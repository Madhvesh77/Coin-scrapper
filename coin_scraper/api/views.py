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
        tasks_data = []
        for coin in coins:
            task = Task.objects.create(job=job, coin=coin)
            print("jbjkbjk"+str(task))
            scrape_coin_data.delay(coin, str(job.job_id))
            task.refresh_from_db()
            tasks_data.append({'coin': coin, 'task_id': str(task.id), 'output': str(task.output), 'status': str(task.status)})
        # for task_data in tasks_data:
        #     task = Task.objects.get(id=task_data['task_id'])
        #     # while task.output is None:
        #     #     task.refresh_from_db()
        #     task_data['output'] = task.output 
        return Response({'job_id': str(job.job_id), 'tasks': tasks_data})

    @action(detail=True, methods=['get'])
    def scraping_status(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)
        return Response(serializer.data)
