def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # <1>

mary_in = trimmed('../DATA/mary.txt')

line1 = next(mary_in)
line2 = next(mary_in)

for trimmed_line in mary_in:  # next(mary_in)
    print(trimmed_line)
