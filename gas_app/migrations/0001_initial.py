# Generated by Django 4.2.3 on 2023-07-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('passwords', models.CharField(max_length=50)),
                ('number', models.IntegerField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
