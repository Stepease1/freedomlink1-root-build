#!/usr/bin/env python3
"""Wrapper: build_merkle_tree.py -> calls existing merkle-tree.py
"""
import sys
import subprocess

def main(argv):
    args = ["python3", "scripts/merkle-tree.py"] + argv
    return subprocess.call(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
