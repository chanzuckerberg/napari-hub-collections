import datetime
from typing import Optional, List
from typing_extensions import Literal

from pydantic import BaseModel, HttpUrl, ConstrainedStr, Field

# Fields
Visibility = Literal['public', 'hidden', 'disabled']


class Comment(ConstrainedStr):
    max_length = 300


class Title(ConstrainedStr):
    max_length = 500


class HttpsUrl(HttpUrl):
    allowed_schemes = {'https'}


# Models
class LinksetSchema(BaseModel):
    orcid: str
    twitter: Optional[str]
    github: Optional[str]
    website: Optional[HttpsUrl]


class InstitutionSchema(BaseModel):
    institution: str
    website: HttpsUrl


class CuratorSchema(BaseModel):
    name: str
    title: str
    affiliation: InstitutionSchema
    links: LinksetSchema


class PluginSchema(BaseModel):
    name: str
    comment: Comment


class CollectionSchema(BaseModel):
    title: Title
    cover_image: str
    summary: str
    description: str
    plugins: List[PluginSchema]
    updated_date: datetime.date
    curator: CuratorSchema
    visibility: Visibility = Field('public')
