from django.db import models


# Create your models here.
class Person(models.Model):
    gender = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=255,)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    timezone_offset = models.CharField(max_length=255)
    timezone_description = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    login_uuid = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    password_salt = models.CharField(max_length=255)
    password_md5 = models.CharField(max_length=255)
    password_sha1 = models.CharField(max_length=255)
    password_sha256 = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    days_to_birthday = models.IntegerField(default=0)
    registered_date = models.CharField(max_length=255)
    registered_age = models.IntegerField(default=0)
    phone = models.CharField(max_length=255)
    cell = models.CharField(max_length=255)
    id_name = models.CharField(max_length=255)
    id_value = models.CharField(max_length=255, null=True)
    # picture_large = models.CharField(max_length=255)
    # picture_medium = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    nat = models.CharField(max_length=255)

    # def __str__(self):
    #     full_name = (self.first, self.last)
    #     return full_name
