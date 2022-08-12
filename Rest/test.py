import requests

BASE="http://127.0.0.1:5000/"


data=[ {"name":"Ashish","likes":10,"views":123},
       {"name":"prafull","likes":10,"views":123},
       {"name":"vikas","likes":10,"views":123}]
       
for i in range(len(data)):
    response=requests.put(BASE+ "/video/"+str(i),data[i])
    print(response.json())

input()
response=requests.get(BASE+ "/video/2" )
print(response.json())

input()
response=requests.delete(BASE+ "/video/2" )
print(response)

input()
response=requests.get(BASE+ "/video/0" )
print(response.json())