from argparse import ArgumentParser
import importlib

parser = ArgumentParser()
parser.add_argument('year', type=int)
parser.add_argument('day', type=int)
args = parser.parse_args()

module = importlib.import_module(f'{args.year}.{args.day}', package=None)
