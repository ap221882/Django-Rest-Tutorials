import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = ''


responseJoMila = requests.get(BASE_URL+ENDPOINT)
print(type(responseJoMila.json())) #converts to python readable form idhar hi
print(responseJoMila.json()) #converts to python readable form idhar hi
data = responseJoMila.json()
print('Data from django application:')
print('#'*15)
print('Employee Id: ', data['emp'] )
print('Employee Name: ', data['ename'] )
print('Employee Sallery: ', data['empsal'] )
print('Employee Location: ', data['empaddr'] )