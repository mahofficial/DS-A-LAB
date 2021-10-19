"""
Program Name:   Expression Balancing using Counters
By:             Aqib Hussain
Reg#:           200901013
"""
exp = input("Enter any expression: ")
dic = {
    '(': ')',
    '[': ']',
    '{': '}'
}
result = 1
for o, c in dic.items():
    if not exp.count(o) is exp.count(c):
        result = 0
        break
if result:
    print("Equation is Balanced!")
else:
    print("Equation is Unbalanced!")