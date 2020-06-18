import factory
from uuid import uuid4

from apps.dealer.models import Country, City, Dealer

class CountryFactory(factory.DjangoModelFactory):
    name = factory.django.CharField(name='Ukrain')

    class Meta:
        model = Country

class CityFactory(factory.DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    name = factory.django.CharField(name='Chernigiv')

    class Meta:
        model = City

class DealerFactory(factory.DjangoModelFactory):
    city = factory.SubFactory(CityFactory)


    class Meta:
        model = Dealer