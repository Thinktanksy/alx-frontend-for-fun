#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

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

def convert_md_to_html(input_file, output_file):
    # Read the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = []
    for line in md_content:
        # Check if the line is a heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            h_level = len(match.group(1))
            h_content = match.group(2)
            html_content.append('<h{0}>{1}</h{0}>\n'.format(h_level, h_content))
        else:
            html_content.append(line)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
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

    # Convert the markdown file to HTML
    convert_md_to_html(args.input_file, args.output_file)

