# Generated by Django 3.2.9 on 2022-02-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dorilar', '0014_auto_20220219_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Nakladnoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_dobavlen', models.DateTimeField(auto_created=True)),
                ('olingan_soni', models.IntegerField()),
                ('ishlab_chiqaruvchi', models.CharField(max_length=300)),
                ('dori_sertifikati', models.CharField(max_length=200)),
                ('srok', models.DateField()),
                ('olingan_narxi', models.FloatField()),
                ('ustiga_foiz', models.FloatField()),
                ('sotiladigan_narx', models.FloatField()),
                ('max_sena', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipTovara',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shtrixKod', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('shtukPachke', models.IntegerField()),
                ('tip_tovara', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorilar.tiptovara')),
            ],
        ),
        migrations.CreateModel(
            name='Pereotsenka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorilar.nakladnoy')),
            ],
        ),
        migrations.CreateModel(
            name='NakladnoyNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nakladnoy_nom', models.BigIntegerField(unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('postavshik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorilar.firma')),
            ],
        ),
        migrations.AddField(
            model_name='nakladnoy',
            name='nakladnoy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorilar.nakladnoyno'),
        ),
        migrations.AddField(
            model_name='nakladnoy',
            name='tovar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorilar.tovar'),
        ),
    ]