# Data Structure & Algorithms
## Palindrome Check
**Registration# 200901013**
### Explanation
```
from collections import deque
```
Importing deque from collections to use it for making stack.

```
string = input("Enter any string: ")
```
Taking expression as input from user and storing it in `string` variable.

```
rev = ""
```
Making `rev` variable to store the reverse string for later comparison with original string

```
stack = deque()
```
Creating stack using deque instead of list

```
for ch in string:
```
Iterating through every character in the variable `string` and storing it in variable `ch` using for loop

```
stack.append(ch)
```
Appending every character in stack from entered string.

```
for i in range(0, len(stack)):
```
Iterating till the end of the stack

```
rev = rev + stack.pop()
```
Storing reversed string by poping up every character from stack and combining it with `rev` variable and storing it in it.

```
if rev.lower() == string.lower():
```
Here we convert every character stored in `string` and `rev` variable in lowercase to implement a palindrome check as in ASCII lowercase and uppercase letter have different values but in general both have same meaning.

```
    print("Entered string is palindrome!")
else:
    print("Entered string is not palindrome!")
```
If both reversed and entered string are same then `Entered string is palindrome!` will be printed else `Entered string is not palindrome!` will be printed.

---

**Registration# 200901013**

**Assignment**
