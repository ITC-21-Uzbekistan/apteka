# Generated by Django 3.2.9 on 2022-02-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar', '0016_alter_nakladnoy_date_dobavlen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nakladnoy',
            name='date_dobavlen',
            field=models.DateField(auto_now_add=True),
        ),
    ]
