from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Candie(models.Model):
    id = fields.IntField(pk=True)
    candie = fields.CharField(max_length=250)
    ingredients = fields.CharField(max_length=250)

    class PydanticMeta:
        ...                  # i'm not going to exclude or compute data for the path 

# User_Pydantic = pydantic_model_creator(Candie, name="User")
# UserIn_Pydantic = pydantic_model_creator(Candie, name="UserIn", exclude_readonly=True)

Candie_Pydantic = pydantic_model_creator(Candie, name="Candie")
CandieIn_Pydantic = pydantic_model_creator(Candie, name="CandieIn",exclude_readonly=True)   # response model
