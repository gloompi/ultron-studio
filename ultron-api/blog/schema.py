import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Article

class ArticleType(DjangoObjectType):
  class Meta:
    model = Article

class Query(graphene.ObjectType):
  articles = graphene.List(ArticleType, search=graphene.String())

  def resolve_articles(self, info, search=None):
    filter = (
      Q(id__icontains=search) |
      Q(title__icontains=search) |
      Q(content__icontains=search)
    )

    if search:
      return Article.objects.filter(filter)

    return Article.objects.all()
