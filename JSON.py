import json
inf = open(r'D:\input.txt', 'r')
todos = json.loads(inf.read())
inf.close()
print(sorted(todos,key=lambda x: (x['event_id'], x['item_id'])))