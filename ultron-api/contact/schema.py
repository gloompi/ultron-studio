import graphene
from graphene_django import DjangoObjectType
from .models import Contact

class ContactType(DjangoObjectType):
  class Meta:
    model = Contact

class Query(graphene.ObjectType):
  contacts = graphene.List(ContactType)

  def resolve_contacts(self, info):
    return Contact.objects.all()