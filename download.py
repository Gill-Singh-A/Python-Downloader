import requests, sys
web_file = requests.get(sys.argv[1])
with open(sys.argv[2], 'wb') as file:
    file.write(web_file.content)