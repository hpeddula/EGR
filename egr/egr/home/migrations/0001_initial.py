# Generated by Django 2.0.3 on 2018-03-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
            ],
        ),
    ]
