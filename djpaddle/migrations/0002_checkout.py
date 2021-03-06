# Generated by Django 3.1a1 on 2020-05-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djpaddle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('completed', models.NullBooleanField()),
                ('passthrough', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
