import requests
import json


url = "https://pokeapi.co/api/v2/pokemon/"

payload = {}
headers = {}

response = json.loads(requests.request("GET", 
                            url, headers=headers, 
                            data=payload).text)

# A função json.loads():

# Converte uma string JSON (vinda de .text)

# Para um dicionário Python



print(response["results"])


