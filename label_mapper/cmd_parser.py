# coding=utf-8
"""Argument parsers for the label mapper"""

# Import module argparse
from argparse import ArgumentParser


def parse_args():
    """
    Sets up the parser for the label mapper and parses the arguments
    :return: the parsed arguments
    """
    parser = ArgumentParser(prog="label_mapper.py", usage="label_mapper.py <log path> <model path> <out_path>")

    # add arguments to parser
    parser.add_argument('log', nargs='?', help="relative path to the event log")
    parser.add_argument('model', nargs='?', help="relative path to the xml model")
    parser.add_argument('out', nargs='?', help="relative path to which the remapped graph is written")


    # return the parsed arguments
    return parser.parse_args()
