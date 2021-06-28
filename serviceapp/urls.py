from django.conf.urls import url
from .views import URLCreateView, URLRetrieveView

urlpatterns = [   
    url(r'^$',URLCreateView.as_view(),name='create'),
	url(r'^(?P<short_url>[\w-]+)/$',URLRetrieveView.as_view(),name='retrive'),    
]
