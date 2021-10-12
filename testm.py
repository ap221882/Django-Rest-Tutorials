import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

# 13:56


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id
        }
    resp = requests.get(BASE_URL+END_POINT, data=json.dumps(data))
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


# def create_resource():
#     new_emp = {
#         'eno': 890,
#         'ename': 'David',
#         'esal': 7000,
#         'eaddr': 'Gurugram',
#     }
#     resp = requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())


# def update_resource(id):
#     new_emp = {
#         # 'id': id,
#         'eaddr': 'Delhi'
#     }
#     resp = requests.put(BASE_URL+END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())


# update_resource(80)

def delete_resource(id):
    data = {
        'id': id,
    }
    resp = requests.delete(BASE_URL+END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


# # update_resource(8)
delete_resource(8)

# create_resource()


# get_resource()
# # get_all()
# # id = input('Enter some ID: ')
# # get_resource(id)

# # STATUS_CODES
# # 1xx - Informational
# # 2xx- Successfull
# # 3xx - Redirectional
# # 4xx- Client Error
# # 5xx- Server Error
