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
#         'name': 'Akshay',
#         'rollno': 105,
#         'marks': 89,
#         'gf': 'Kangna',
#         'bf': 'Abhishek'
#     }
#     resp = requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())


# def update_resource(id):
#     new_emp = {
#         'id': id,
#         'gf': 'Twinkle Khanna',
#         'marks': 1
#     }
#     resp = requests.put(BASE_URL+END_POINT, data=json.dumps(new_emp))
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
delete_resource(5)

# create_resource()


# get_resource(100)
# # get_all()
# # id = input('Enter some ID: ')
# # get_resource(id)

# # STATUS_CODES
# # 1xx - Informational
# # 2xx- Successfull
# # 3xx - Redirectional
# # 4xx- Client Error
# # 5xx- Server Error
