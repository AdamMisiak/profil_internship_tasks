from django.db import models


# Create your models here.
class Person(models.Model):
    gender = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255, blank=True)
    street_name = models.IntegerField(blank=True, default=0)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postcode = models.IntegerField(blank=True, default=0)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)
    timezone_offset = models.CharField(max_length=255, blank=True)
    timezone_description = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    login_uuid = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    password_salt = models.CharField(max_length=255, blank=True)
    password_md5 = models.CharField(max_length=255, blank=True)
    password_sha1 = models.CharField(max_length=255, blank=True)
    password_sha256 = models.CharField(max_length=255, blank=True)
    dob = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True, default=0)
    registered_date = models.CharField(max_length=255, blank=True)
    registered_age = models.IntegerField(blank=True, default=0)
    phone = models.CharField(max_length=255, blank=True)
    cell = models.CharField(max_length=255, blank=True)
    id_name = models.CharField(max_length=255, blank=True)
    id_value = models.CharField(max_length=255, blank=True)
    picture_large = models.CharField(max_length=255, blank=True)
    picture_medium = models.CharField(max_length=255, blank=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    nat = models.CharField(max_length=255, blank=True)

    def __str__(self):
        full_name = (self.first, self.last)
        return full_name
