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
    yaml_error_list = []
    schema_error_list = []

    for collection in collections:
        with open(collection, "r") as stream:
            try:
                in_data = yaml.safe_load(stream)
                CollectionSchema.parse_obj(in_data)
            except yaml.YAMLError as err:
                yaml_error_list.append(f'{err.problem} {err.problem_mark}')
                continue
            except ValidationError as err:
                schema_error_list.append(f'{err} in {collection}')

    if len(yaml_error_list) == 0 and len(schema_error_list) == 0:
        print("All collections have been validated successfully")
        return

    if len(yaml_error_list) > 0:
        print('Yaml Error List')
        print(*yaml_error_list, sep='\n')
    else:
        print('No Yaml Errors')

    print("-" * 40)

    if len(schema_error_list) > 0:
        print("Schema Error List")
        print(*schema_error_list, sep='\n')
    else:
        print("No Schema Errors")

    sys.exit(1)


if __name__ == '__main__':
    validate('/Users/klai/Documents/napari-hub-collections/collections')
