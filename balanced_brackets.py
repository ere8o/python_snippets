def isBalanced(s):
    balance = []

    try:
        for c in s:
            uni_c = ord(c)
            if uni_c in [41, 93, 125]:
                if balance.pop() not in [uni_c-1, uni_c-2]:
                    raise Exception
            else:
                balance.append(uni_c)
        return 'YES' if len(balance) == 0 else 'NO'
    except:
        return 'NO'

string = '()()()'
print('YES', isBalanced(string))

string = '()())'
print('NO', isBalanced(string))

string = '({[[{}]]})'
print('YES', isBalanced(string))

string = '('
print('NO', isBalanced(string))
