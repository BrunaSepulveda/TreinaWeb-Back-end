# Generated by Django 3.2.4 on 2021-06-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210619_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
