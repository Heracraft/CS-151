import sys

def in_virtualenv():
    return sys.prefix != sys.base_prefix

if in_virtualenv():
    print("Python is running inside a virtual environment.")
else:
    print("Python is NOT running inside a virtual environment.")