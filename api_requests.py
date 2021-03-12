import requests


def get_branches():
    r = requests.get("https://api.github.com/repos/ecc56/ClassworkSpring2021/branches")
    print(r)
    print(type(r))
    print(r.status_code)
    print(r.text)
    branches = r.json
    print(branches)
    for branch in branches:
       print(branch["name"])


def countries():
    server = "http://vcm-7631.vm.duke.edu:5000"
    r = requests.get(server+"/countries")
    print(r.status_code)
    print(r.text)
    
    my_countries = {"one": "Austria", "two": "Argentina"}
    r = requests.post(server+"/compare", json=my_countries)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


def id_num():
    info = {"name": "Emma Cooper", "net_id": "ecc56", "e-mail": "ecc56@duke.edu"}
    server = "http://vcm-6764.vm.duke.edu:5000/student"
    r = requests.post(server+"/compare", json=info)
    print(r.status_code)
    print(r.text)
    data = r.json()
    print(data)


if __name__ == '__main__':
    #get_branches()
    #countries()
    id_num()

