import graphene
from graphene_django import DjangoObjectType
from .models import Feature, Tariff

class TariffType(DjangoObjectType):
  class Meta:
    model = Tariff

class FeatureType(DjangoObjectType):
  class Meta:
    model = Feature

class Query(graphene.ObjectType):
  tariffs = graphene.List(TariffType)
  features = graphene.List(FeatureType)

  def resolve_tarrifs(self, info):
    return Tariff.objects.all()

  def resolve_features(self, info):
    return Feature.objects.all()