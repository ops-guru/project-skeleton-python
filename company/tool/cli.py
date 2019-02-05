#!/usr/bin/env python
# coding: utf-8

# files creator V1
# inputs: 1- RunID, 2- number of flows

import os
import sys
import argparse

from company.tool.shared import thing


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Tool to do something"
    )
    parser.add_argument(
        'iparam',
        type=int,
        help="iparam to use"
    )
    parser.add_argument(
        'sparam',
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
    thing.shared_function(params.iparam)
    thing.shared_function(params.sparam)
    return 0


if __name__ == '__main__':
    sys.exit(main())
