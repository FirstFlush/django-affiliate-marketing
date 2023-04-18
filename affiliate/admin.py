from django.contrib import admin
from .models import AffiliatePlan, AffiliatePartner, PartnerWebsite#, ReferralSignUp, ReferralClick, ReferralPurchase


class AffiliatePlanAdmin(admin.ModelAdmin):

    list_display = [
        'plan_name',
        'cookie_expiration',
        'payout_threshold',
        'payout_date',
    ]


class AffiliatePartnerAdmin(admin.ModelAdmin):

    list_display = [
        'user_id',
        'plan_id',
        'amount_payable',
        'total_paid',
        'partnership_active',
        'partnership_began',
    ]


class PartnerWebsiteAdmin(admin.ModelAdmin):

    list_display = [
        'affiliate_id',
        'site_url',
    ]

# class ClickAdmin(admin.ModelAdmin):
#     list_display = [
#         affiliate_id
#     ]


# class SignUpAdmin(admin.ModelAdmin):
#     list_display = [
        
#     ]




# class AffiliatePurchaseAdmin(admin.ModelAdmin):
#     list_display = [
        
#     ]



admin.site.register(AffiliatePlan, AffiliatePlanAdmin)
admin.site.register(AffiliatePartner, AffiliatePartnerAdmin)
admin.site.register(PartnerWebsite, PartnerWebsiteAdmin)
# admin.site.register(Click, ClickAdmin)
# admin.site.register(SignUp, SignUpAdmin)
# admin.site.register(AffiliatePurchase, AffiliatePurchaseAdmin)
