# Generated by Django 3.0.5 on 2020-06-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deskexecutive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstore',
            name='ws_rtype',
            field=models.CharField(max_length=30),
        ),
    ]
