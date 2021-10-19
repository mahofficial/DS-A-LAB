"""
Project Name:   Expression Balancing using Stack
By:             Aqib Hussain
Reg#:           200901013
"""
from collections import deque

exp = input("Enter any equation: ")
stack = deque()
dic = {
    '{': '}',
    '[': ']',
    '(': ')'
}
result = 1
for i in exp:
    if i in dic.keys():
        stack.append(i)
    elif i in dic.values():
        if not stack:
            result = 0
            break
        elif i not in dic[stack[-1]]:
            result = 0
            break
        stack.pop()
if result:
    print("Valid Expression!")
else:
    print("Invalid Expression!")
