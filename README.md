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

Here we created a dummy stream with a list of chunks.
```python
from truncjson import Stream

chunks = [
    'Here yo',
    'u go {"k1":"v1","k2":2',
    '0.5,"k3":[12,34,"56",tr',
    'ue,{"k31":"v31","k32":false,"k33":n',
    'ull}]}\nAnd ano',
    'ther one {"k',
    'ey":1.',
    '12} {"a',
    'b":"cd"}'
]

stream = Stream()
for chunk in chunks:
    print(stream.extract(chunk))

# Output:
# []
# ['{"k1":"v1","k2":2}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true]}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"k":null}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.0}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.12}', '{"a":null}']
# ['{"k1":"v1","k2":20.5,"k3":[12,34,"56",true,{"k31":"v31","k32":false,"k33":null}]}', '{"key":1.12}', '{"ab":"cd"}']
```

## ChatGPT Usage

```python
import openai
import json
from truncjson import Stream

openai.api_key = '###'

chat = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a intelligent assistant.'},
        {'role': 'user', 'content': 'Return 3 different random JSON objects each has more than 500 characters.'},
    ],
    stream=True
)

stream = Stream()
for chunk_obj in chat:
    chunk_content = chunk_obj['choices'][0]['delta'].get('content', '')
    for obj in stream.extract(chunk_content):
        print(json.loads(obj))
```