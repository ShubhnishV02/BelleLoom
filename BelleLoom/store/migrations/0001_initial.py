# Generated by Django 4.2.2 on 2023-10-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('Product_Name', models.CharField(max_length=150)),
                ('Product_Image', models.ImageField(null=True, upload_to='store/images')),
                ('Product_Desc', models.TextField(max_length=2000)),
                ('status', models.BooleanField(default=False, help_text='0=default , 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default , 1=Trending')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keyword', models.CharField(max_length=150)),
                ('meta_description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
