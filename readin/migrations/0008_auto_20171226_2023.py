# Generated by Django 2.0 on 2017-12-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0007_auto_20171226_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='algorithm_choice',
            field=models.CharField(choices=[('S', 'Supervised'), ('U', 'Unsupervised')], default='S', max_length=2),
        ),
    ]