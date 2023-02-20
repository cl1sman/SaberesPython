import string

def copy_list(n):
    new_list = []
    for i in range(len(n) - 1, 0, -1): # because, repete the center line
        new_list.append(n[i])
    return new_list

def print_rangoli(n):
    alphabet = string.ascii_lowercase
    final_line = []
    for i in range(n):
        line_pattern = '-'.join(alphabet[i:n]) # n=5; first line: a-b-c-d-e
        line_pattern_invert = line_pattern[::-1] # e-d-c-b-a
        line_pattern_invert = line_pattern_invert[:-1] # -d-c-b-a
        final_line.append(line_pattern_invert + line_pattern)
    final_line_invert = copy_list(final_line)

    width_center_line = len(final_line[0])

    for i in range(len(final_line_invert)):
        print(final_line_invert[i].center(width_center_line, '-'))
    for i in range(len(final_line)):
        print(final_line[i].center(width_center_line, '-'))
print_rangoli(5)