# Generated by Django 2.0 on 2017-12-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0002_auto_20171225_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]
