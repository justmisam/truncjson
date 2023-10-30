# truncjson
Truncated JSON completer

# Simple Usage
```python
from truncjson import complete

complete('{"k1":"v1","k2":20.5,"k3":[12')

# Output: {"k1":"v1","k2":20.5,"k3":[12]}
```

# Stream Usage
```python
from truncjson import Stream

chunks = [
    '{"k1":"v1","k2":2',
    '0.5,"k3":[12,34,"56",tr',
    'ue,{"k31":"v31","k32":false,"k33":n'
]
stream = Stream()
for chunk in chunks:
    print(json.loads(stream.complete(chunk)))

# Output:
# {'k1': 'v1', 'k2': 2}
# {'k1': 'v1', 'k2': 20.5, 'k3': [12, 34, '56', True]}
# {'k1': 'v1', 'k2': 20.5, 'k3': [12, 34, '56', True, {'k31': 'v31', 'k32': False, 'k33': None}]}
```
