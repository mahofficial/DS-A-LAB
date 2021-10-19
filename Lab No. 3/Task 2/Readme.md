# Data Structure & Algorithms
## Expression Balancing
*Registration# 200901013*
### Explanation
`from collections import deque`
Importing deque from collections to use it for making stack.

`exp = input("Enter any equation: ")`
Taking expression as input from user and storing it in `exp` variable.

`stack = deque()`
Creating stack using deque instead of list

`dic = {
    '{': '}',
    '[': ']',
    '(': ')'
}`
Making dictionary for parenthesis to easily check the opening and closing brackets.

`result = 1`
This variable by default stores 1 (True) in it. It is later used in the code to store 0 (false) if the expression is invalid or unbalanced.

`for i in exp:`
Iterating through every character in the variable `exp` and storing it in variable `i` using for loop

`if i in dic.keys():`
Check if the character is present as key in dictionary (if the character is opening brackets)

`stack.append(i)`
If the character is present as key in dictionary then it will push it into the stack.

`elif i in dic.values():`
If the character is not present in dictionary as key then this condition will check that whether it is present as value of any key in dictionary or not (closing bracket is present or not)

`if not stack:`
if the closing bracket is present as value of any key in dictionary then it will check that whether the stack is empty or not

`result = 0
break`
if the stack is empty then 0 (false) will be stored in variable `result` and it will break the loop and transfers the control to the end of the loop

`elif i not in dic[stack[-1]]:`
If the stack is not empty then this condition will check if the character is the value of the key in stored on the top of stack.

`result = 0
break`
If the character iterated is not the value of the key in dictionary stored on the top of stack then 0 (false) will be stored in the variable `result` and break the loop

`stack.pop()`
if above both conditions are false then the character will be poped from the stack (the bracked stored on the top of stack as it will match the closing bracket)

`if result:
    print("Valid Expression!")
else:
    print("Invalid Expression!")`
This code checks if the value of variable `result` is true or false. If it is true then `Valid Expression!` will be printed on the screen else `Invalid Expression!` will be printed on the screen
---
*Registration# 200901013*
*Assignment*
