#!/usr/bin/env python3
"""
FreedomLink1 Canonicalization Module

Creates canonical representations of documents for deterministic hashing.
Normalizes formatting, line endings, and whitespace.

Usage:
    python canonicalization.py [--file FILEPATH] [--directory DIR]
"""

import sys
from pathlib import Path


def canonicalize_text(text):
    """
    Create canonical text representation.
    
    - Normalize line endings to LF
    - Remove trailing whitespace
    - Ensure final newline
    - UTF-8 encoding
    """
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    
    # Strip trailing whitespace from each line
    lines = [line.rstrip() for line in text.split('\n')]
    
    # Remove trailing empty lines
    while lines and not lines[-1]:
        lines.pop()
    
    # Ensure final newline
    canonical = '\n'.join(lines) + '\n'
    
    return canonical


def canonicalize_file(filepath):
    """
    Canonicalize a file.
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    canonical = canonicalize_text(content)
    return canonical


def canonicalize_directory(dirpath):
    """
    Canonicalize all files in directory.
    """
    dirpath = Path(dirpath)
    
    for filepath in sorted(dirpath.rglob('*')):
        if filepath.is_file() and filepath.suffix in ['.md', '.txt', '.json', '.yaml', '.py']:
            try:
                content = canonicalize_file(filepath)
                print(f"# {filepath}")
                print(content)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")


def main():
    """
    Main entry point.
    """
    if '--file' in sys.argv:
        idx = sys.argv.index('--file')
        if idx + 1 < len(sys.argv):
            content = canonicalize_file(sys.argv[idx + 1])
            if content:
                print(content)
    
    elif '--directory' in sys.argv:
        idx = sys.argv.index('--directory')
        if idx + 1 < len(sys.argv):
            canonicalize_directory(sys.argv[idx + 1])
    
    else:
        print("FreedomLink1 Canonicalization Module")
        print("Usage: python canonicalization.py --file <path> | --directory <path>")


if __name__ == '__main__':
    main()
