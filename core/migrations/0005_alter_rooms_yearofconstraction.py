# Generated by Django 5.0.2 on 2024-02-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_market_options_alter_rooms_yearofconstraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='yearofconstraction',
            field=models.DateField(verbose_name='Год постройки'),
        ),
    ]