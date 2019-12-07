import graphene
from graphene_django import DjangoObjectType
from .models import AdvantagesSection, Advantage

class AdvantageSectionType(DjangoObjectType):
  class Meta:
    model = AdvantagesSection

class AdvantageType(DjangoObjectType):
  class Meta:
    model = Advantage

class Query(graphene.ObjectType):
  advantage_section = graphene.Field(AdvantageSectionType)
  advantages = graphene.List(AdvantageType)

  def resolve_advantage_section(self, info):
    return AdvantagesSection.objects.get(id=1)

  def resolve_advantages(self, info):
    return Advantage.objects.all()