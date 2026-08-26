#!/usr/bin/env python3
"""Wrapper: canonicalize_json.py -> calls existing canonicalization.py
"""
import sys
import subprocess

def main(argv):
    args = ["python3", "scripts/canonicalization.py"] + argv
    return subprocess.call(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
