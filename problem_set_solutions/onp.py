import string


def go(exp):
    symbols = []
    parentesis = []
    var = []
    result = ''
    for i in exp:
        if i == '(':
            parentesis.append('(')
        if i == ')':
            parentesis.pop()
            result += symbols.pop()
        if i in string.letters:
            result += i
        if i in '+-*^%/':
            symbols.append(i)
    print result


n = input()

for i in range(n):
    go(raw_input())
