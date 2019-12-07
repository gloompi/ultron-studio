import graphene
from graphene_django import DjangoObjectType

from .models import About, Item

class AboutType(DjangoObjectType):
  class Meta:
    model = About

class ItemType(DjangoObjectType):
  class Meta:
    model = Item

class Query(graphene.ObjectType):
  about = graphene.Field(AboutType)
  items = graphene.List(ItemType)

  def resolve_about(self, info, **kwargs):
    return About.objects.get(id=1)
    
  def resolve_items(self, info, **kwargs):
    return Item.objects.all()