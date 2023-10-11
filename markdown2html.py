#!/usr/bin/python
"""
This is a script to convert a Markdown file to HTML with support for various custom syntax.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import re
import sys
import os
import hashlib

def convert_md_to_html(input_file, output_file):
    # Read the contents of the input file
    with open(input_file) as f:
        md_content = f.read()

    # Define a regular expression pattern to match [[text]] for MD5 hashing
    md5_pattern = r'\[\[(.*?)\]\]'
    
    # Use re.sub to replace [[text]] with its MD5 hash (lowercase)
    def md5_replace(match):
        content = match.group(1)
        return hashlib.md5(content.encode()).hexdigest().lower()

    html_content = re.sub(md5_pattern, md5_replace, md_content)

    # Define a regular expression pattern to match ((text)) for case-insensitive content replacement
    replace_pattern = r'\(\((.*?)\)\)'
    
    # Use re.sub to remove all 'c' characters (case-insensitive) from the content
    def replace_content(match):
        content = match.group(1)
        return content.replace('c', '', flags=re.IGNORECASE)

    html_content = re.sub(replace_pattern, replace_content, html_content)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html_content)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML with support for various custom syntax')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')

    args = parser.parse_args()

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py [input_file] [output_file]\n")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.isfile(args.input_file):
        sys.stderr.write('Missing {0}\n'.format(args.input_file))
        sys.exit(1)

    # Convert the markdown file to HTML with custom syntax handling
    convert_md_to_html(args.input_file, args.output_file)

