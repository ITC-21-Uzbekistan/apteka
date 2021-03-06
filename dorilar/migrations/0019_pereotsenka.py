# Generated by Django 3.2.12 on 2022-03-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorilar', '0018_delete_pereotsenka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pereotsenka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tovar_id', models.BigIntegerField()),
                ('eski_protsent', models.FloatField()),
                ('eski_narx', models.FloatField()),
                ('yengi_foiz', models.FloatField()),
                ('yengi_narx', models.FloatField()),
                ('changed_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
