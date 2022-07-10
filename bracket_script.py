import glob


def remove_comments(line, sep):
    for s in sep:
        i = line.find(s)
        if i >= 0:
            line = line[:i]
    return line.strip()


# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = './'
for filename in glob.iglob(root_dir + '**/*.txt', recursive=True):
    opening_bracket_count = 0
    closing_bracket_count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = remove_comments(line, '#')
                opening_bracket_count += cleaned_line.count('{')
                closing_bracket_count += cleaned_line.count('}')
        if opening_bracket_count != closing_bracket_count:
            print(filename, 'contains', opening_bracket_count, 'opening ({) vs', closing_bracket_count, 'closing (}) braces')
    except Exception as e:
        print(filename, e)
