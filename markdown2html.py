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

import sys
import os
import re
import hashlib

# Check the number of arguments
if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py <Markdown_file> <Output_file>", file=sys.stderr)
    sys.exit(1)

# Extract the input and output filenames from the command line arguments
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# Regular expressions to match custom syntax
md5_pattern = re.compile(r'\[\[(.*?)\]\]')
remove_c_pattern = re.compile(r'\(\((.*?)\)\)')

# Function to convert custom syntax to HTML
def md5_to_html(match):
    content = match.group(1)
    md5_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
    return f'<p>{md5_hash}</p>'

def remove_c_to_html(match):
    content = match.group(1)
    content_without_c = content.replace('c', '', -1)
    return f'<p>{content_without_c}</p>'

# Read the Markdown file, process custom syntax, and write to the output file
with open(markdown_file, 'r') as markdown_input:
    markdown_content = markdown_input.read()

# Convert custom syntax to HTML
markdown_content = md5_pattern.sub(md5_to_html, markdown_content)
markdown_content = remove_c_pattern.sub(remove_c_to_html, markdown_content)

# Write the HTML content to the output file
with open(output_file, 'w') as html_output:
    html_output.write(markdown_content)

# Exit with code 0
sys.exit(0)

