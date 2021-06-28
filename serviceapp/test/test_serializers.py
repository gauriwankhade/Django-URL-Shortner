from django.test import TestCase
from django.forms.models import model_to_dict  
from nose.tools import eq_, ok_
from .factories import *
from ..serializers import *


class TestLinkSerializer(TestCase):

    def setUp(self):
        self.link_data = model_to_dict(LinkFactory())

    def test_serializer_with_empty_data(self):
        serializer = LinkSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = LinkSerializer(data=self.link_data)
        ok_(serializer.is_valid())


