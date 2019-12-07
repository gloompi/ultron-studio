import graphene
from graphene_django import DjangoObjectType

from .models import Slide

class SlideType(DjangoObjectType):
  class Meta:
    model = Slide

class Query(graphene.ObjectType):
  slides = graphene.List(SlideType)

  def resolve_slides(self, info):
    return Slide.objects.all()