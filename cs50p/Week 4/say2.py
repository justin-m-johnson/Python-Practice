import sys

#pulls from sayins.py (my own library)
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])