# Generated by Django 2.2.3 on 2019-08-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190801_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='work',
            field=models.ManyToManyField(related_name='categories', to='portfolio.Work'),
        ),
        migrations.RemoveField(
            model_name='tech',
            name='work',
        ),
        migrations.AddField(
            model_name='tech',
            name='work',
            field=models.ManyToManyField(related_name='technologies', to='portfolio.Work'),
        ),
    ]
