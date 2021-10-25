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