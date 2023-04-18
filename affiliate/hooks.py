import decimal
from datetime import datetime, timedelta

from django.db.utils import IntegrityError

from .models import ReferralClick, ReferralSignUp, ReferralPurchase


class SignUpHook:

    def __init__(self, cookies:dict, user):

        self.user = user
        self.cookies = cookies
        self.cookie_value = self._cookie_value()
        if self.cookie_value is not None:
            self.click = self._click()
            if self.click is not None:
                self._sign_up()


    def _click(self):
        """Grab the ReferralClick object this cookie is related to."""
        try:
            click = ReferralClick.objects.get(cookie_value=self.cookie_value)
        except ReferralClick.DoesNotExist:
            click = None
        return click


    def _cookie_value(self):
        """Checks the request.cookies and if the 'ref' cookie exists then
        this return's the ref cookie's value. If it does not exist,
        method returns None.
        """
        if 'ref' in self.cookies:
            cookie_value = self.cookies['ref']
        else:
            cookie_value = None
        return cookie_value


    def _sign_up(self):
        """Create the ReferralSignUp instance, appropriately crediting 
        our AffiliatePartner.
        """
        try:
            ReferralSignUp.objects.create(
                user_id = self.user,
                affiliate_id = self.click.affiliate_id,
                click_id = self.click,
            )
        except IntegrityError:
            pass

        return
    


class PurchaseHook:

    def __init__(self, amount_paid:decimal.Decimal, user):

        self.amount_paid = amount_paid
        self.user = user
        self.referral_signup = self._referral_signup()
        if self.referral_signup is not None:
            self.partner = self.referral_signup.affiliate_id
            if self._check_time() == True:
                self._create_purchase()


    def _referral_signup(self):
        """Check if the user making the purchase was referred by one of our
        AffiliatePartners or not. If the user is indeed a referral then
        this method returns a ReferralSignUp object.
        """
        try:
            referral = self.user.referralsignup
        except AttributeError:
            referral = None
        return referral


    def _check_time(self) -> bool:
        """Checks to make sure this purchase is being made within the appropriate
        timeframe, as defined in the AffiliatePartner's AffiliatePlan.
        Partners will only receive commission on sales made within their plan's
        designated timeframe.
        """
        number_of_days = self.referral_signup.affiliate_id.plan_id.cookie_expiration
        cookie_issued = self.referral_signup.click_id.date_clicked
        td = datetime.utcnow() - cookie_issued
        is_valid = td < timedelta(days=number_of_days)

        return is_valid


    def _create_purchase(self):
        """Create the ReferralPurchse object and credit the AffiliatePartner."""
        ReferralPurchase.objects.create(
            affiliate_id = self.partner,
            amount_paid = self.amount_paid,
        )
        
        return


