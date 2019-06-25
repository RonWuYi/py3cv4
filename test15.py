import os
import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)

print(type(json_str))
with open(os.path.join('/home/hdc/Downloads/project/py3cv4/jsonData', 'data3.json'), 'w') as f:
    json.dump(data, f)
