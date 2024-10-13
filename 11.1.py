import requests
r = requests.put('https://api.github.com/events', data={'key': 'value'})
b = requests.get('https://api.github.com/events')

print(b)
print(r)