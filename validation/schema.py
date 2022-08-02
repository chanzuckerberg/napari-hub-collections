import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, ConstrainedStr, HttpUrl

# Fields
Visibility = Literal['public', 'hidden', 'disabled']


class Comment(ConstrainedStr):
    max_length = 300


class Title(ConstrainedStr):
    max_length = 500

    
# Models
class LinksetSchema(BaseModel):
    orcid: str
    twitter: Optional[str]
    github: Optional[str]
    website: Optional[HttpUrl]


class InstitutionSchema(BaseModel):
    institution: str
    website: HttpUrl


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
    visibility: Visibility = 'public'
