# Generated by Django 2.0 on 2017-12-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0014_auto_20171227_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='algorithm_choice',
            field=models.CharField(blank=True, choices=[('S', 'Supervised'), ('U', 'Unsupervised')], max_length=2),
        ),
    ]
