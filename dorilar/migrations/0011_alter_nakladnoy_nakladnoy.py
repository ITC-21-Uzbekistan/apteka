# Generated by Django 3.2.9 on 2022-02-03 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar', '0010_firma_nakladnoy_nakladnoyno_tiptovara_tovar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nakladnoy',
            name='nakladnoy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorilar.nakladnoyno'),
        ),
    ]
