# Generated by Django 3.0.2 on 2022-09-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20220824_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='В цій категорії зібрано новини про', max_length=200, verbose_name='Опис'),
        ),
    ]
