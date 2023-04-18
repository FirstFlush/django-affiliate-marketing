# Generated by Django 4.0.3 on 2023-04-15 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliatePartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliate_code', models.CharField(max_length=255, unique=True)),
                ('cookie_value', models.CharField(max_length=255, unique=True)),
                ('amount_payable', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_paid', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('partnership_active', models.BooleanField(default=True)),
                ('partnership_began', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AffiliatePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=255, unique=True)),
                ('payout_date', models.IntegerField(default=15)),
                ('payout_threshold', models.IntegerField(default=20)),
                ('cookie_expiry_days', models.IntegerField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.URLField(max_length=255)),
                ('affiliate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiliate.affiliatepartner')),
            ],
        ),
        migrations.AddField(
            model_name='affiliatepartner',
            name='plan_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='affiliate.affiliateplan'),
        ),
        migrations.AddField(
            model_name='affiliatepartner',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
