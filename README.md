# truncjson
Truncated JSON completer

# Usage

```
from truncjson import complete

complete('{"k1":"v1","k2":20.5,"k3":[12')

# Output: {"k1":"v1","k2":20.5,"k3":[12]}
```