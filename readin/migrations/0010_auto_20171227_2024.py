# Generated by Django 2.0 on 2017-12-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0009_auto_20171226_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='algorithm_choice',
            field=models.CharField(choices=[('N', 'None'), ('S', 'Supervised'), ('U', 'Unsupervised')], default='N', max_length=2),
        ),
    ]
