# Generated by Django 4.0.3 on 2023-04-18 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0018_rename_cookie_value_affiliatepartner_cookie_signer'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralsignup',
            name='click_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='affiliate.referralclick'),
        ),
    ]