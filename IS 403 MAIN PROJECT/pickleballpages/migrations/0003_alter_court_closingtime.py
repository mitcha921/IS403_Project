# Generated by Django 4.1.2 on 2022-11-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickleballpages', '0002_rename_courts_court_alter_court_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='closingtime',
            field=models.TimeField(null=True),
        ),
    ]
