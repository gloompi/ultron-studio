# Generated by Django 2.2.3 on 2019-08-01 16:57

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantagesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Advatages Section',
                'verbose_name_plural': 'Advatages Section',
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(max_length=25, upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advantages_section', to='advantages.AdvantagesSection')),
            ],
        ),
    ]
