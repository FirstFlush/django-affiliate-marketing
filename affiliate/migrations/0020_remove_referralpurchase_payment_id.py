# Generated by Django 4.0.3 on 2023-04-18 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0019_referralsignup_click_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referralpurchase',
            name='payment_id',
        ),
    ]