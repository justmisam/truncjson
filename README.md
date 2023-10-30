# truncjson
A library to complete truncated JSON strings.

## Use Cases
1. When you possess a JSON file that is truncated, and you wish to parse its current content.
2. When you are receiving JSON content as a stream from services like ChatGPT. This allows you to parse the JSON content each time you receive a new chunk.

## Simple Usage
```python
from truncjson import complete

result = complete('{"k1":"v1","k2":20.5,"k3":[12')
print(result)

# Output: {"k1":"v1","k2":20.5,"k3":[12]}
```

## Stream Usage
```python
import json
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
