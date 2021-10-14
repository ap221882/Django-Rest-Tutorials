import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


# def get_resource(id=None):
#     data = {}
#     if id is not None:
#         data = {
#             'id': id
#         }
#     resp = requests.get(BASE_URL+END_POINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())


# def get_all():
#     resp = requests.get(BASE_URL+END_POINT)
#     print(resp.status_code)
#     print(resp.json())


# def create_resource():
#     new_emp = {
#         'eno': 400,
#         'ename': 'Akshay',
#         'esal': 8900,
#         'eaddr': 'Kanpur',
#     }
#     resp = requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())


# def update_resource(id):
#     new_data = {
#         'id': id,
#         'esal': 2300,
#         'eaddr': 'England'
#     }
#     resp = requests.put(BASE_URL+END_POINT, data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())


# update_resource(4)

def delete_resource(id):
    data = {
        'id': id,
    }
    resp = requests.delete(BASE_URL+END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


# # # update_resource(8)
delete_resource(4)

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
