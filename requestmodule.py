import requests

x = requests.get('https://www.google.co.in/')

print(x.text)

print(x.cookies)