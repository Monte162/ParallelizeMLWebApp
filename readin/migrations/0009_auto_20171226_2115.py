# Generated by Django 2.0 on 2017-12-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0008_auto_20171226_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.CharField(max_length=500, null=True),
        ),
    ]