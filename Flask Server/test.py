import requests

BASE = "http://127.0.0.1:5000/"

data = {
    
}

data_two = {
    "name": "pullups",
    "sets": 4,
    "reps": 50,
    "date": "2025-03-18",
    "weight": 100
}
# response = requests.put(BASE + "workout/1", json=data)
# print(response.json())
# input()


response = requests.get(BASE + "workout/2004-12-29")


print(response.json())




# input()
# response = requests.get(BASE + "workout/delete/2025-03-17")

# print(response)


