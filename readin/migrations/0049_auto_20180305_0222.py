# Generated by Django 2.0 on 2018-03-05 02:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0048_auto_20180212_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='method_clust',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('KM', 'K-Means Clustering'), ('SC', 'Spectral Clustering'), ('AC', 'Agglomerative Clustering'), ('BC', 'Birch Clustering')], max_length=11),
        ),
    ]