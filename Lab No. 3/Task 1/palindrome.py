from collections import deque
string = input("Enter any string: ")
rev = ""
stack = deque()
for ch in string:
    stack.append(ch)

for i in range(0, len(stack)):
    rev = rev + stack.pop()

if rev.lower() == string.lower():
    print("Entered string is palindrome!")
else:
    print("Entered string is not palindrome!")