import json
from pprint import pprint

test_data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(type(test_data))
print(test_data)
pprint(test_data)