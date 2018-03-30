from django.db import models
from django.contrib.postgres.fields import JSONField
from django.forms import ModelForm
from django.urls import reverse
from captcha.fields import ReCaptchaField
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django import forms


class Space(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)

    # In the form, we want to auto-fill lat/long from address or map using
    # google: https://developers.google.com/maps/documentation/geocoding/start
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    # address fields inspired by https://help.wufoo.com/articles/en_US/kb/Address
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    country = CountryField(max_length=20, null=True, blank=True)
    additional_directions = models.CharField(max_length=255, null=True, blank=True)
    # public_trans = EnumField(PublicTransAccess, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)

    website = models.CharField(max_length=255, null=True, blank=True)
    date_opened = models.DateField(null=True, blank=True)
    date_closed = models.DateField(null=True, blank=True)
    short_description = models.CharField(max_length=140, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)
    data_credit = models.CharField(max_length=100, null=True, blank=True)

    residencies = models.NullBooleanField(null=True, blank=True)
    membership = models.IntegerField(null=True, blank=True)
    users = models.IntegerField(null=True, blank=True)
    size_in_sq_meters = models.IntegerField(null=True, blank=True)
    wheelchair_accessibility = models.NullBooleanField(null=True, blank=True)
    business_model = models.CharField(max_length=1000, null=True, blank=True)
    

    IN_OPERATION = 'OP'
    PLANNED = 'PL'
    CLOSED = 'CL'
    UNKNOWN = 'UK'
    STATUS_OPTIONS = (
        (IN_OPERATION, 'In Operation'),
        (PLANNED, 'Planned'),
        (CLOSED, 'Closed'),
        (UNKNOWN, 'Unknown Operation Status'),
    )
    operational_status = models.CharField(
        max_length=2,
        choices=STATUS_OPTIONS,
        default=UNKNOWN,
    )

    VERIFIED = 'VE'
    FLAGGED = 'FL'
    VALIDATION_OPTIONS = (
        (VERIFIED, 'Verified'),
        (FLAGGED, 'Flagged'),
        (UNKNOWN, 'Unknown Data Status'),
    )
    validation_status = models.CharField(
        max_length=2,
        choices=VALIDATION_OPTIONS,
        default=UNKNOWN,
    )

    PRIVATE_SECTOR = "PRI"
    NON_PROFIT = "NON"
    EDU_PRIMARY = "EP"
    EDU_SECONDARY = "ES"
    EDU_UNI = "EU"
    EDU_VOCATIONAL = "EV"
    GOV_LOCAL = "GL"
    GOV_PROV = "GP"
    GOV_NATIONAL = "GN"
    UNINCORPORATED = "UN"
    LIBRARY = "LIB"
    OWNERSHIP_OPTIONS = (
        (PRIVATE_SECTOR, "Private Sector: a for-profit business, " + \
            "corporation, or startup"),
        (NON_PROFIT, "Non-Profit: a registered non-profit organization"),
        (EDU_PRIMARY, "Educational: primary school"),
        (EDU_SECONDARY, "Educational: secondary school"),
        (EDU_UNI, "Educational: university"),
        (EDU_VOCATIONAL, "Educational: vocational school"),
        (GOV_LOCAL, "Government: Local or Municipal"),
        (GOV_PROV, "Government: Provincial"),
        (GOV_NATIONAL, "Government: National"),
        (UNINCORPORATED, "Unincorporated"),
        (LIBRARY, "Library"),
    )

    ownership_type = MultiSelectField(choices=OWNERSHIP_OPTIONS, 
                                        null=True, blank=True)


    COOPERATIVE = "COOP"
    DEMOCRATIC = "DEM"
    COMPANY = "COM"
    SATELLITE = "SAT"
    
    GOVERNANCE_OPTIONS = (
        (COOPERATIVE, "Cooperative: members make decisions collectively"),
        (DEMOCRATIC, "Democratic: member-elected board makes decisions"),
        (COMPANY, "Company: founders and/or hired staff make decisions"),
        (SATELLITE, "Satellite: decisions are made by an external organization"),
    )

    governance_type = MultiSelectField(choices=GOVERNANCE_OPTIONS, 
                                        null=True, blank=True)



    other_data = JSONField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('space_profile', kwargs={'id':self.id})

class SpaceForm(ModelForm):
    
    captcha = ReCaptchaField()

    class Meta:
        model = Space
        fields = '__all__'
