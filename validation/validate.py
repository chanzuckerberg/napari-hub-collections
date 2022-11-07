#!/usr/bin/env python

import click
import yaml
import glob

from schema import CollectionSchema

@click.command()
@click.argument('collection_path', nargs=1)
def validate(collection_path):

    collections = glob.glob(f"{collection_path}/*.yml")

    for collection in collections:

        # load the Collection
        with open(collection, "r") as stream:
            try:
                in_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        # validate it
        # try:
        #     CollectionSchema().load(in_data)
        # except ValidationError as err:
        #     pprint(err.messages)

        print(f"validating {collection}")
        parsed = CollectionSchema.parse_obj(in_data)
        print(parsed)


if __name__ == '__main__':
    validate()
