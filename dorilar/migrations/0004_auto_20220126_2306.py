# Generated by Django 3.2.9 on 2022-01-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar', '0003_auto_20220126_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nakladnoyno',
            name='id',
        ),
        migrations.AlterField(
            model_name='nakladnoyno',
            name='nakladnoy_nom',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
