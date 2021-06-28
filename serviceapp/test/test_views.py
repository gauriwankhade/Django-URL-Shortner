from django.urls import reverse
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from django.test import TestCase
from django.forms.models import model_to_dict
from rest_framework import status
from faker import Faker
import factory
from ..models import *
from .factories import  *
import urllib


class TestCreateLinkTestCase(APITestCase):
    """
    Tests /Link create operation.
    """

    def setUp(self):
        self.url = reverse('create')

        #create Link object, not saving Link object
        link_build = LinkFactory.build()
        self.link_data = model_to_dict(link_build)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.link_data)
        eq_(response.status_code, status.HTTP_201_CREATED)


class TestRetriveLinkTestCase(APITestCase):
    """
    Tests /Link retrive operation.
    """
   
    def setUp(self):
        #create Link object, not saving Link object
        self.link_object = LinkFactory()
         
    def test_get_request_with_invalid_data_fails(self):
        url = reverse('retrive', kwargs={'short_url': 'z'})
        response = self.client.get(url)
        eq_(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_request_with_valid_data_succeeds(self):
        url = reverse('retrive', kwargs={'short_url': self.link_object.short_url})
        response = self.client.get(url)
        eq_(response.status_code, status.HTTP_200_OK)


class TestRedirectView(TestCase):
    def setUp(self):
        #create Link object, not saving Link object
        self.link_object = LinkFactory()

    def test_get_request_with_valid_data_succeeds(self):
        response = self.client.get(reverse('redirect', kwargs={'url': self.link_object.short_url}))
        self.assertEqual(response.status_code, 302)

    def test_get_request_with_invalid_data_fails(self):
        response = self.client.get(reverse('redirect', kwargs={'url': 'uix'}))
        self.assertEqual(response.status_code, 200)

    

    