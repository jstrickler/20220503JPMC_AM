#!/usr/bin/env python

from itertools import groupby

with open('../DATA/words.txt') as words_in:  # <1>
    all_words = (w.rstrip() for w in words_in)  # <2>

    g = groupby(all_words, key=lambda e: e[0])  # <3>

    counts = {letter: len(list(wlist)) for letter, wlist in g}  # <4>

sorted_letters = sorted(counts.items(), key=lambda e: e[1], reverse=True)  # <5>
for letter, count in sorted_letters:  # <6>
    print(letter, count)

print()
print("Total words counted:", sum(counts.values()))  # <7>

with open('../DATA/presidents.txt') as pres_in:
    data = []
    for line in pres_in:
        fields = line.rstrip().split(':')
        record = fields[1], fields[2], fields[-1]
        data.append(record)
print("data: {}".format(data))

def by_party(pres):
    return pres[-1]

sorted_data = sorted(data, key=by_party)

g = groupby(sorted_data, key=by_party)
for party, pres_list in g:
    print(party, list(pres_list))
    print('-' * 60)