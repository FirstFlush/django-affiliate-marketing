from datetime import datetime, timedelta
import hashlib

from .models import AffiliatePartner, ReferralClick


class ReferralCookieMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.set_cookie = False


    def __call__(self, request):
        if request.GET.get('ref') != None:
            self.ref_code = request.GET['ref']
            self.partner = self._get_partner()
            if self.partner != None:
                cookie_value = self._create_cookie_value(request.session.session_key)
                self.click_object = self._create_click_object(cookie_value)
                if self._check_for_ref_cookie(request) == False:
                    self.set_cookie = True
        # code that is executed after the view is called:
        response = self.get_response(request)
        if self.set_cookie == True:
            self._set_cookie(response)

        return response


    def _get_partner(self) -> AffiliatePartner:
        """Retrieves the AffiliatePartner who the reference code belongs to."""
        try:
            partner = AffiliatePartner.objects.get(ref_code=self.ref_code)
        except (AffiliatePartner.DoesNotExist, AffiliatePartner.MultipleObjectsReturned):
            partner = None
        return partner


    def _create_click_object(self, cookie_value:str):
        """Creates a Click object pointing to the appropriate AffiliatePartner"""
        click_object = ReferralClick.objects.create(
            affiliate_id=self.partner,
            cookie_value=cookie_value,
        )
        return click_object


    def _check_for_ref_cookie(self, request) -> bool:
        """Returns True or False depending on if the 'ref' cookie exists."""
        cookie = request.COOKIES.get('ref')
        return bool(cookie)    


    def _create_cookie_value(self, session_key:str):
        """Create a unique cookie value by hashing a string of the following values:
        -AffiliatePartner's cookie_signer
        -session key
        -timestamp
        """
        cookie_str = f"{self.partner.cookie_signer}{session_key}{datetime.utcnow().timestamp()}"
        cookie_value = hashlib.md5(cookie_str.encode()).hexdigest()
        return cookie_value


    def _set_cookie(self, response):
        """Set the cookie on the response object"""
        cookie_expiry = datetime.utcnow() + timedelta(days=15)
        response.set_cookie('ref', self.click_object.cookie_value, expires=cookie_expiry)
