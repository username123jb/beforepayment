# Generated by Django 2.2.2 on 2019-07-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_auto_20190708_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(),
        ),
    ]
