# Generated by Django 2.2 on 2022-04-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220408_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoryId',
            field=models.IntegerField(default=0),
        ),
    ]
