#!/usr/bin/env python3
import argparse
from  modgen.cmod_generator import CModGenerator


def parse_arguments():
    parser = argparse.ArgumentParser(description='Create a module based on the specified template')
    parser.add_argument('name', help='name of the module to create')
    parser.add_argument('type', help='type of module to create')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    module_type = args.type.lower()
    if args.type == 'c':
        generator = CModGenerator(args.name, '../templates/cmodule.template')
    else:
        print('Module of type {} is not supported'.format(args.type))

    generator.generate()

