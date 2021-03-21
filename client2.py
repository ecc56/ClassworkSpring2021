import requests

patient = {"name": "Emma", "id": 1, "blood_type": "O+"}

r = requests.post("http://127.0.0.1:5000/", json=patient)
print(r.status_code)
print(r.text)