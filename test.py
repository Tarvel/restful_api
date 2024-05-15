import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 500, 'name':'How to swim', "views":7300000},
        {"likes": 10, 'name':'Who made the food?', "views":6700000},
        {"likes": 12350, 'name':'the dragon legend', "views":9100000},
        {"likes": 900000, 'name':'Fastest car ever', "views":99991000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/1")
print(response)

input()
response = requests.get(BASE + "video/1")
print(response.json())


