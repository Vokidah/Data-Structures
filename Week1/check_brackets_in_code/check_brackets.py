# python3

import sys

def Match(bracket_type, c):
    if bracket_type == '[' and c == ']':
        return True
    if bracket_type == '{' and c == '}':
        return True
    if bracket_type == '(' and c == ')':
        return True
    return False

def check(text):
    opening_brackets_stack = []
    for i, char in enumerate(text):
        if char == '[' or char == '(' or char == '{':
            opening_brackets_stack.append((char, i + 1))
        elif char == ')' or char == ']' or char == '}':
            if not opening_brackets_stack or not Match(opening_brackets_stack.pop(-1)[0], char):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[-1][1]
    else:
        return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    text = text[:-1]
    print(check(text))