# Generated by Django 3.2.3 on 2021-05-20 07:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210519_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Полное описание'),
        ),
    ]
