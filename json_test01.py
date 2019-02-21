import json

data = {'pet':[{
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
},{
    'name' : 'ACM',
    'shares' : 10,
    'price' : 54.23
}]}

json_str = json.dumps(data)


print(json_str.pet)