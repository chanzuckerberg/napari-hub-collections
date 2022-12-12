#!/usr/bin/env python

import sys

import click
import yaml
import glob

from pydantic import ValidationError

from schema import CollectionSchema


@click.command()
@click.argument('collection_path', nargs=1)
def validate(collection_path):
    collections = glob.glob(f"{collection_path}/*.yml")
    # list of .yml files that have errors
    yaml_error_list = []
    schema_error_list = []

    for collection in collections:

        # load the Collection
        with open(collection, "r") as stream:
            try:
                in_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                yaml_error_list.append((str(exc.problem) + str(exc.problem_mark)))
                continue

        # process the Collection
        try:
            CollectionSchema.parse_obj(in_data)
        except ValidationError as err:
            schema_error_list.append(str(err) + ' in ' + collection)

    if len(yaml_error_list) == 0 and len(schema_error_list) == 0:
        print("All collections have been validated successfully")
        return

    if len(yaml_error_list) > 0:
        print("Yaml Error List")
        for item in yaml_error_list:
            print(item)
    print("-" * 40)
    if len(schema_error_list) > 0:
        print("Schema Error List")
        for item in schema_error_list:
            print(item)
    sys.exit(1)


if __name__ == '__main__':
    validate()
