# Generated by Django 4.2.2 on 2023-11-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=30)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
