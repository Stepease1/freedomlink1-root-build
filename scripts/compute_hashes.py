#!/usr/bin/env python3
"""Wrapper: compute_hashes.py -> calls existing hashing.py
"""
import sys
import subprocess

def main(argv):
    args = ["python3", "scripts/hashing.py"] + argv
    return subprocess.call(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
