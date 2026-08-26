#!/usr/bin/env python3
"""Wrapper: verify_signature.py -> calls existing signature-verification.py
"""
import sys
import subprocess

def main(argv):
    args = ["python3", "scripts/signature-verification.py"] + argv
    return subprocess.call(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
