# Generated by Django 2.2.7 on 2019-11-18 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobiernoapp', '0003_auto_20191118_0605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['reg_name'], 'verbose_name_plural': 'Regions'},
        ),
    ]
