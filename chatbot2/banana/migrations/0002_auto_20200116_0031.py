# Generated by Django 3.0.2 on 2020-01-15 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nick', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('male', '남성'), ('female', '여성')], default='male', max_length=10)),
                ('diary_open', models.CharField(choices=[('yes', 'open'), ('no', 'close')], default='yes', max_length=3)),
                ('center_exp', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3)),
                ('about', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('emotion', models.CharField(choices=[('기쁨', '기쁨'), ('혐오', '혐오'), ('두려움', '두려움'), ('분노', '분노'), ('슬픔', '슬픔'), ('기타', '기타')], default='기쁨', max_length=3)),
                ('other', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('score', models.IntegerField()),
                ('detail', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, choices=[('elementary', '초등학교 졸업'), ('middle', '중학교 졸업'), ('high', '고등학교 졸업'), ('college', '대학교(2년제)졸업'), ('university', '대학교(4년제)졸업'), ('graduate', '대학원 졸업 이상'), ('others', '기타')], default='elementary', max_length=10, null=True)),
                ('school_others', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('parent', models.CharField(blank=True, max_length=2, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('sibling', models.CharField(blank=True, max_length=10, null=True)),
                ('marriage', models.CharField(blank=True, max_length=3, null=True)),
                ('child', models.CharField(blank=True, max_length=3, null=True)),
                ('child_num', models.CharField(default='0', max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='userId',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='banana.User_Chat'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
