import json

data  = {[
    {
    'name':'Surskit',
    'cp':161,
    'hp':491,
    'dust':8001
},
    {
    'name':'Surskit',
    'cp':160,
    'hp':49,
    'dust':800
}
]}

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

json_str = json.dumps(data)

changed_data = json.loads(json_str, object_hook=JSONObject)

for i in changed_data.pet:
    print(i.name)
# print(changed_data.pet)
# print(json_str.)