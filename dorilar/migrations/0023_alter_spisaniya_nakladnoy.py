# Generated by Django 3.2.12 on 2022-03-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar', '0022_spisaniya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spisaniya',
            name='nakladnoy',
            field=models.BigIntegerField(),
        ),
    ]
