# Generated by Django 2.2.8 on 2019-12-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20190801_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(unique=True, upload_to=''),
        ),
    ]
