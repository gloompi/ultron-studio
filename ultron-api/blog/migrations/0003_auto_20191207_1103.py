# Generated by Django 2.2.8 on 2019-12-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190731_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='background_image',
            field=models.ImageField(unique=True, upload_to=''),
        ),
    ]
