# python3
import random

x, p = 31, 263
a, b = random.randint(1, p), random.randint(0, p)



def hash_func(string):
    hash = 0
    i = len(string) - 1
    while i >= 0:
        hash = (hash * x + ord(string[i])) % p
        i -= 1
    return hash

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_precompute(pattern, text):
    H = [None] * (len(text) - len(pattern) + 1)
    H[-1] = hash_func(text[len(text) - len(pattern):])
    y = 1
    for i in range(len(pattern)):
        y = (y * x) % p
    i = len(text) - len(pattern) - 1
    while i >= 0:
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p
        i -= 1
    return H


def get_occurrences(pattern, text):
    H = hash_precompute(pattern, text)
    H_ = hash_func(pattern)
    result = []
    for i in range(0, len(text) - len(pattern) + 1):
        if H_ == H[i]:
            if text[i: i+len(pattern)] == pattern:
                result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
