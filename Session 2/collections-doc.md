# Documentation for Collections in Python

### Import Collections
To use the modules of Collections Library, Use code
```python
import collections as col
```

---

### namedtuple()
Named tuples assign name to each value in a tuple. It take these arguments:
`typename` defines the type of data
`field_names` assign the name to each value
`rename=False` if True then invalid field_names will be replaced automatically with the _index of value.
`defaults=None` set the default (enetered) value to the fieldnames in tuple (optional).
`__module__` if module is defined then this is set to the particular value

##### Example
```python
import collections as c
Point = c.namedtuple('int', ['x', 'y']) #making named tuple
p = Point(11, y=22) #initializing values
print(p[0] + p[1]) #named tuple is indexable
# Output = 33

x, y = p #values can be stored in other variables (unpacking)
print(x, y)
# Output = 11 22

print(p.x + p.y) #values can be accessed by name 
# Output = 33

print(p)
# Example taken from official docs
```

##### Basic Syntax
```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

##### Methods of namedtuple()
`_make(iterable)` Make a new instance from an existing sequence
`_asdict()` convert named tuple to dictionary
`_replace(**kwargs)` Replace specified fields with new values and return new instance of the named tuple
`_fields` Show the name of fields
`_field_defaults` convert field name to key of dictionary and default value as value of the key

---

### deque()
Deque stands for double-ended queues and can be used for the implementation of stack and queues with time complexity of bigO(1) because at the backend of deque linked-list is being used.

##### Example
```python
# Stack implementation using deque
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
```

##### Basic Syntax
```python
collections.deque([iterable[, maxlen]])
```

##### Methods of deque()
`append(x)` Add x to the right side of the deque
`appendleft(x)` Add x to the left side of the deque
`pop()` Fetch and Remove element from the right side of the deque.
`popleft()` Fetch and Remove element from the left side of the deque.
`clear()` Remove all elements from the deque leaving it with length 0.
`copy()` Create a shallow copy of the deque
`count(x)` Count the number of deque elements equal to x
`extend(iterable)` Extend the right side of the deque with the iterable values
`extendleft(iterable)` Extend the left side of the deque with the iterable values
`insert(p,x)` Insert deque into the x at position p
`remove(value)` Remove the first occurence of value
`rotate(n=1)` Rotate the deque n steps to the right, if n is negative rotate to the left
`reverse()` Reverse the elements of the deque

---

