# Generated by Django 3.2.6 on 2021-10-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('feedback', models.TextField(max_length=100)),
            ],
        ),
    ]