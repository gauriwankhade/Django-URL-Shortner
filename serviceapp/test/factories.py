import factory, factory.fuzzy
import string


class LinkFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "serviceapp.Link"
        django_get_or_create = ('id', )

    id = factory.fuzzy.FuzzyInteger(1, 100)
    long_url = factory.Faker('uri')
    short_url = factory.fuzzy.FuzzyText(length=4, chars=string.ascii_letters)
    created_at = factory.Faker('date')


