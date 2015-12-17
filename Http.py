# Higher level access to a server
# using a built in protocol handler
import requests


with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()

