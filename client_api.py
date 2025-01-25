import requests

response = requests.get("http://127.0.0.1:8000/weather/simple")
print(response.reason)
print(response.content)
print(response.encoding)

print(response.headers)
print(response.url)
print(response.elapsed)

print(response.request.method)
print(response.request.url)
print(response.request.headers)
print(response.request.body)


#print(response.text)
#print(response.json())