# Generated by Django 2.0 on 2018-02-11 22:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('readin', '0043_auto_20180211_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='method_reg',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('DT', 'Decision Tree'), ('BR', 'Bayesian Ridge'), ('SVR', 'Support Vector Regression'), ('LR', 'Linear Regression'), ('AdaR', 'Ensembled Ada Boost Regressor'), ('BR', 'Ensembled Bagging Regressor'), ('ETR', 'Ensembled Extra Trees Regressor'), ('GBR', 'Ensembled Gradient Boosting Regressor'), ('RFR', 'Ensembled Random Forest Regressor')], max_length=32),
        ),
    ]