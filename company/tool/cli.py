#!/usr/bin/env python
# coding: utf-8

# files creator V1
# inputs: 1- RunID, 2- number of flows

import os
import sys
import argparse

from company.tool.shared import item


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Tool to do something"
    )
    parser.add_argument(
        'param_integer',
        type=int,
        help="param_integer to use"
    )
    parser.add_argument(
        'param_str',
        help="string param to use"
    )
    parser.add_argument(
        '-w', '--workdir',
        help="Folder to work in",
        default=os.getcwd()
    )
    if args is None:
        args = sys.argv[1:]
    return parser.parse_args(args=args)


def main():
    params = parse_args(sys.argv[1:])
    item.shared_function(params.param_integer)
    item.shared_function(params.param_str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
