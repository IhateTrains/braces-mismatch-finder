import glob
import sys


def remove_comments(line, sep):
    for s in sep:
        i = line.find(s)
        if i >= 0:
            line = line[:i]
    return line.strip()


# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = './'

errors_found = False
for filename in glob.iglob(root_dir + '**/*.txt', recursive=True):
    print('Checking file: ' + filename + '...')
    opening_bracket_count = 0
    closing_bracket_count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = remove_comments(line, '#')
                opening_bracket_count += cleaned_line.count('{')
                closing_bracket_count += cleaned_line.count('}')
    except Exception as e:
        print(filename, e)

    if opening_bracket_count != closing_bracket_count:
        errors_found = True
        print(filename, 'contains', opening_bracket_count, 'opening ({) vs', closing_bracket_count, 'closing (}) braces')

if errors_found:
    sys.exit(1)