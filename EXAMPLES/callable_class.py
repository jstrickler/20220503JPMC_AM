#!/usr/bin/env python

class TagWrapper():
    def __init__(self, tag):
        self._tag = tag

    def wrap(self, text):
        return '<{0}>{1}</{0}>'.format(self._tag, text)

class HTMLWrapper():

    def __init__(self, tag):
        self._tag = tag

    def __call__(self, text):  # <1>
        return '<{0}>{1}</{0}>'.format(self._tag, text)

if __name__ == '__main__':
    # non-callable class
    t = TagWrapper('h1')
    print(t.wrap('foo'))
    print(t.wrap('bar'))
    print()

    # callable class
    h1 = HTMLWrapper('h1')  # <2>
    print(h1('spam'))  # <3>
    div = HTMLWrapper('div')
    print(div('ham'))
    print(div('toast'))
    print(div('jam'))
