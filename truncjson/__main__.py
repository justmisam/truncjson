import json
import time
from truncjson import complete
from truncjson import Stream


if __name__ == '__main__':
    print(json.loads(complete('{"k1":"v1","k2":20.5,"k3":[12')))

    chunks = [
        '{"k1":"v1","k2":2',
        '0.5,"k3":[12,34,"56",tr',
        'ue,{"k31":"v31","k32":false,"k33":n'
    ]
    stream = Stream()
    for chunk in chunks:
        print(json.loads(stream.extract(chunk)[0]))

    repeats = 100000
    test_case = '{"k1":"v1","k2":20.5,"k3":[12'
    start_time = time.time()
    for _ in range(repeats):
        complete(test_case)
    end_time = time.time()
    print(f"Elapsed time for {repeats} repeats x {len(test_case)} chars: {end_time - start_time} seconds")
