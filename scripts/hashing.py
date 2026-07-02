#!/usr/bin/env python3
"""
FreedomLink1 Hashing Module

Computes canonical hashes for all documents using SHA-256.
Supports batch processing and canonical form enforcement.

Usage:
    python hashing.py [--file FILEPATH] [--directory DIR] [--verify]
"""

import hashlib
import json
import os
import sys
from pathlib import Path


def canonicalize(content):
    """Create canonical representation of content."""
    if isinstance(content, bytes):
        content = content.decode('utf-8')
    
    # Normalize line endings
    content = content.replace('\\r\\n', '\\n')
    
    # Strip trailing whitespace from lines
    lines = [line.rstrip() for line in content.split('\\n')]
    
    # Remove trailing empty lines
    while lines and not lines[-1]:
        lines.pop()
    
    canonical = '\\n'.join(lines) + '\\n'
    return canonical.encode('utf-8')


def hash_content(content):
    \"\"\"Compute SHA-256 hash of content.\"\"\"
    if isinstance(content, str):
        content = canonicalize(content)
    return hashlib.sha256(content).hexdigest()


def hash_file(filepath):
    \"\"\"Compute hash of a file.\"\"\"
    filepath = Path(filepath)
    
    if not filepath.exists():
        return {'error': f'File not found: {filepath}'}
    
    with open(filepath, 'rb') as f:\n        content = f.read()
    
    canonical = canonicalize(content)\n    hash_value = hashlib.sha256(canonical).hexdigest()
    
    return {\n        'file': str(filepath),\n        'hash': hash_value,\n        'size': len(content),\n        'algorithm': 'SHA-256'\n    }


def hash_directory(dirpath, extension=None):
    \"\"\"Compute hashes for all files in directory.\"\"\"
    dirpath = Path(dirpath)\n    results = {}
    
    if extension:\n        files = dirpath.rglob(f'*{extension}')\n    else:\n        files = dirpath.rglob('*')
    
    for filepath in sorted(files):
        if filepath.is_file():
            results[str(filepath)] = hash_file(filepath)
    
    return results


def main():
    \"\"\"Main entry point.\"\"\"
    if len(sys.argv) < 2:
        print(\"FreedomLink1 Hashing Module\")
        print(\"Usage: python hashing.py --file <path> | --directory <path>\")
        return
    
    if '--file' in sys.argv:
        idx = sys.argv.index('--file')
        if idx + 1 < len(sys.argv):
            result = hash_file(sys.argv[idx + 1])
            print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
