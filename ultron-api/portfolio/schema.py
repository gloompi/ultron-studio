import graphene
from graphene_django import DjangoObjectType
from .models import Portfolio, Work, Category, Tech, Image

class PortfolioType(DjangoObjectType):
  class Meta:
    model = Portfolio

class WorkType(DjangoObjectType):
  class Meta:
    model = Work

class CategoryType(DjangoObjectType):
  class Meta:
    model = Category

class TechType(DjangoObjectType):
  class Meta:
    model = Tech

class ImageType(DjangoObjectType):
  class Meta:
    model = Image

class Query(graphene.ObjectType):
  portfolio = graphene.Field(PortfolioType)
  works = graphene.List(WorkType, id=graphene.String())
  categories = graphene.List(CategoryType)
  technologies = graphene.List(TechType)
  images = graphene.List(ImageType)

  def resolve_portfolio(self, info):
    return Portfolio.objects.get(id=1)

  def resolve_works(self, info, id=None):
    if id:
      return Work.objects.filter(id=id)

    return Work.objects.all()

  def resolve_categories(self, info):
    return Category.objects.all()

  def resolve_technologies(self, info):
    return Tech.objects.all()

  def resolve_images(self, info):
    return Image.objects.all()
