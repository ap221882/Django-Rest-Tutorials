import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_resource(id):
    resp = requests.get(BASE_URL+END_POINT+id+'/')
    print(resp.status_code)
    print(resp.json())


def get_all():
    resp = requests.get(BASE_URL+END_POINT)
    print(resp.status_code)
    print(resp.json())


get_resource('302')
get_all()
# id = input('Enter some ID: ')
# get_resource(id)

# STATUS_CODES
# 1xx - Informational
# 2xx- Successfull
# 3xx - Redirectional
# 4xx- Client Error
# 5xx- Server Error
