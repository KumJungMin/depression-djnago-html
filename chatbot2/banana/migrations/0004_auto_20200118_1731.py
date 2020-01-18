# Generated by Django 3.0.2 on 2020-01-18 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banana', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='additional',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='diary',
            name='situation',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='reserve',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]