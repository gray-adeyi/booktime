# Generated by Django 3.2 on 2021-05-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_productimage_producttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='product-thumbnails'),
        ),
    ]
