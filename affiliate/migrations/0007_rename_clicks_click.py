# Generated by Django 4.0.3 on 2023-04-15 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0006_rename_affiliate_code_affiliatepartner_ref_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clicks',
            new_name='Click',
        ),
    ]