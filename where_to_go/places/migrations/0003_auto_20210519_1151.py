# Generated by Django 3.2.3 on 2021-05-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='sort_order',
            field=models.IntegerField(default=0, verbose_name='Sort'),
        ),
    ]
