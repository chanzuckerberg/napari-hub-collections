#!/usr/bin/env python

import click
import yaml

from pprint import pprint
from marshmallow import ValidationError

from schema import CollectionSchema

@click.command()
@click.argument('collection', nargs=1)
def validate(collection):

    # load the Collection
    with open(f"../collections/{collection}.yml", "r") as stream:
        try:
            print("loading...")
            in_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

        try:
            CollectionSchema().load(in_data)
        except ValidationError as err:
            pprint(err.messages)

    # validate it


if __name__ == '__main__':
    validate()
