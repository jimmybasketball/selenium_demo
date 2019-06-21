import json

s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print (s)
print(s.keys())