# Generated by Django 4.0.3 on 2023-04-17 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0037_mailgunapifailure_to_email'),
        ('affiliate', '0012_rename_signup_referralsignup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AffiliatePurchase',
            new_name='ReferralPurchase',
        ),
    ]
