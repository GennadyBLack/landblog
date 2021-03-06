# Generated by Django 3.1 on 2020-08-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='poster',
            field=models.ImageField(null=True, upload_to='articles/', verbose_name='Постер'),
        ),
    ]
