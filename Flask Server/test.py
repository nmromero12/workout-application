import requests

BASE = "http://127.0.0.1:5000/"

data = {
    "name": "pushups",
    "sets": 3,
    "reps": 15,
    "date": "2025-03-17",
    "weight": 45
}
response = requests.put(BASE + "workout/1", json=data)
print(response.json())
input()
response = requests.delete(BASE + "workout/delete/1")

print(response)


