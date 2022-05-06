from random import choice

class RandomWord:

    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._words = words_in.read().splitlines()

    def __call__(self):
        return choice(self._words)

if __name__ == '__main__':
    rw = RandomWord()
    for i in range(10):
        print(rw())  #  RandomWord.__call__()
    print()
