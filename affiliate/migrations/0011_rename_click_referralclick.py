# Generated by Django 4.0.3 on 2023-04-17 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('affiliate', '0010_click_session_id_alter_affiliatepartner_cookie_value'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Click',
            new_name='ReferralClick',
        ),
    ]