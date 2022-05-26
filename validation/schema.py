from marshmallow import Schema, fields, validate

class LinksetSchema(Schema):
    orcid = fields.Str(required=True)
    twitter = fields.Str()
    github = fields.Str()
    website = fields.URL(schemes=['https'])

class InstitutionSchema(Schema):
    institution = fields.Str(required=True)
    website = fields.URL(required=True, schemes=['https'])

class CuratorSchema(Schema):
    name = fields.Str(required=True)
    title = fields.Str(required=True)
    affiliation = fields.Nested(InstitutionSchema(),required=True)
    links = fields.Nested(LinksetSchema(), required=True)

class PluginSchema(Schema):
    name = fields.Str(required=True)
    comment = fields.Str(validate=validate.Length(max=300))

class CollectionSchema(Schema):
    title = fields.Str(required=True,validate=validate.Length(max=500))
    cover_image = fields.Str(required=True)
    summary = fields.Str(required=True)
    description = fields.Str(required=True)
    plugins = fields.List(
        fields.Nested(PluginSchema()),
        required=True
        )
    updated_date = fields.Date(required=True)
    curator = fields.Nested(CuratorSchema(), required=True)
