# Generated by Django 4.2.2 on 2023-10-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_product_image_category_image_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Product_Image',
        ),
        migrations.AddField(
            model_name='products',
            name='Product_Image2',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='Product_Image3',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='Product_Image4',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
        migrations.AddField(
            model_name='products',
            name='Product_Image_Main',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
    ]
