# Generated by Django 4.2.2 on 2023-10-15 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_city_country_order_state_orderitem_order_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=80)),
                ('address1', models.TextField()),
                ('address2', models.TextField(null=True)),
                ('pincode', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
