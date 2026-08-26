#!/usr/bin/env python3
"""Wrapper: compare_root.py -> calls existing root-comparison.py
"""
import sys
import subprocess

def main(argv):
    args = ["python3", "scripts/root-comparison.py"] + argv
    return subprocess.call(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
