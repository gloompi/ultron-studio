# Generated by Django 2.2.3 on 2019-08-01 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20190801_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='work',
            new_name='portfolio',
        ),
    ]
