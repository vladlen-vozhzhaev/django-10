# Generated by Django 5.1 on 2024-08-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
        ),
    ]
