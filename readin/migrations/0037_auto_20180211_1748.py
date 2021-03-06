# Generated by Django 2.0 on 2018-02-11 17:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0036_auto_20180209_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='method_class',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('DT', 'Decision Tree'), ('SVM', 'Support Vector Machine'), ('NN', 'Neural Network'), ('LR', 'Logistic Regression')], max_length=12),
        ),
    ]
