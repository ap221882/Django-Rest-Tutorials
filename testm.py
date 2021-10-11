import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_resource(id):
    resp = requests.get(BASE_URL+END_POINT+id+'/')
    # if resp.status_code in range(200, 300):
    print(resp.status_code)
    print(resp.json())
    # if resp.status_code == requests.codes.ok:
    #     print(resp.status_code)
    #     print(resp.json())
    # else:
    #     print('Something goes wrong.')


def get_all():
    resp = requests.get(BASE_URL+END_POINT)
    print(resp.status_code)
    print(resp.json())


def create_resource():
    new_emp = {
        'eno': 420,
        'ename': 'Katrina',
        'esal': 40000,
        'eaddr': 'Mumbai',
    }
    resp = requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


create_resource()


# get_resource('3')
# get_all()
# id = input('Enter some ID: ')
# get_resource(id)

# STATUS_CODES
# 1xx - Informational
# 2xx- Successfull
# 3xx - Redirectional
# 4xx- Client Error
# 5xx- Server Error
