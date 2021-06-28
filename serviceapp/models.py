from django.db import models
from django.conf import settings
import string

# Create your models here.

class Link(models.Model):

    long_url = models.TextField()
    short_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now=True, null=True) 

    def save(self, *args,**kwargs):
        if self.short_url is None or self.short_url == '':
            self.short_url = get_shorturl()
        super(Link, self).save(*args, **kwargs)

    def get_url(self):
        return settings.HOST_URL + self.short_url


class UniqueKey(models.Model):

    key = models.CharField(max_length=255, blank=True, null=True)
    used = models.BooleanField(default=False, blank=True, null=True)
   
def get_shorturl():
    if not UniqueKey.objects.filter(used=False):
        add_unique_key()
        
    key_instance = UniqueKey.objects.filter(used=False).first()
    short_url = key_instance.key

    #update UniqueKey instance
    key_instance.used = True
    key_instance.save()
    return short_url

""" 
insert new entries into UniqueKey
auto-generate multiple unique-keys at one go
"""
def add_unique_key(limit=50):
    objects_count = UniqueKey.objects.filter(used=False).count()
    if objects_count < limit:
        limit = limit - objects_count
        while(limit>0):
            instance = UniqueKey.objects.create(used=False)
            instance.save()

            #genrate unique key
            key = generate_uniquekey(instance)
            instance.key = key
            instance.save()
            limit -= 1

def generate_uniquekey(instance):
    if not instance.key or instance.key == '':
        key = b62_encode(instance.id)
        return key
    print('key already exists')

    
def b62_encode(number):
    base = string.digits+string.ascii_letters
    base62 = []

    while number != 0:
        number, i = divmod(number, 62)
        base62.append(base[i])
    return ''.join(reversed(base62))