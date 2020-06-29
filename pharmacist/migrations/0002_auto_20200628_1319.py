# Generated by Django 3.0.5 on 2020-06-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicineissued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ws_pat_id', models.IntegerField()),
                ('ws_med_id', models.IntegerField()),
                ('ws_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicinemaster',
            fields=[
                ('ws_med_id', models.AutoField(primary_key=True, serialize=False)),
                ('ws_med_name', models.CharField(max_length=255)),
                ('ws_qty', models.IntegerField()),
                ('ws_price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Medicinestock',
        ),
    ]
