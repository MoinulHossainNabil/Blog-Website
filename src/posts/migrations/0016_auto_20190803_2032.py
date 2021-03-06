# Generated by Django 2.2.1 on 2019-08-04 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20190802_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='view_count',
        ),
        migrations.CreateModel(
            name='PostViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
            ],
        ),
    ]
