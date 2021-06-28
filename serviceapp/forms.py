from django import forms
from .validators import valid_url

class UrlForm(forms.Form):
    url = forms.CharField(label="Enter URL",
                          validators=[valid_url],
                          widget= forms.TextInput(attrs={"placeholder":"Long URL",
                                                         "class":"form-control"}))
