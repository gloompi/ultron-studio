import graphene
import users.schema
import slider.schema
import blog.schema
import about.schema
import advantages.schema
import contact.schema
import portfolio.schema
import pricing.schema
import professional_skills.schema

class Query(
  users.schema.Query,
  slider.schema.Query,
  blog.schema.Query,
  about.schema.Query,
  advantages.schema.Query,
  contact.schema.Query,
  portfolio.schema.Query,
  pricing.schema.Query,
  professional_skills.schema.Query,
  graphene.ObjectType,
):
  pass

schema = graphene.Schema(query=Query)