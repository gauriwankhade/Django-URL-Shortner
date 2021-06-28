from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def valid_url(url):
    url_validator = URLValidator()
    try:
        url_validator(url)
    except:
        raise ValidationError("Invalid URL")
        
    return url