import graphene
from graphene_django import DjangoObjectType
from .models import SkillsSection, Skill

class SkillsSectionType(DjangoObjectType):
  class Meta:
    model = SkillsSection

class SkillType(DjangoObjectType):
  class Meta:
    model = Skill

class Query(graphene.ObjectType):
  skills_section = graphene.Field(SkillsSectionType)
  skills = graphene.List(SkillType, id=graphene.String())

  def resolve_skills_section(self, info):
    return SkillsSection.objects.get(id=1)

  def resolve_skill(self, info, id=None):
    if id:
      return Skill.objects.filter(id=id)

    return Skill.objects.all()