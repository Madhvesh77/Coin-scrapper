# Generated by Django 5.0.6 on 2024-06-10 15:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
