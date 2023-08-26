# Generated by Django 4.2.1 on 2023-07-22 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gas_app', '0004_chats'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gas_app.chats')),
            ],
        ),
    ]