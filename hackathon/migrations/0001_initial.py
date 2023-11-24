# Generated by Django 4.2.2 on 2023-11-21 12:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('phone', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('image', models.ImageField(upload_to='uploads/products')),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hackathon.category')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='hackathon.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='hackathon.product')),
            ],
        ),
    ]