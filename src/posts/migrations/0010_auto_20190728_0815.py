# Generated by Django 2.2.1 on 2019-07-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190728_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='featured',
            field=models.BooleanField(),
        ),
    ]
