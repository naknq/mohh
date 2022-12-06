import requests
import json

#https://rapidapi.com/rohan-patra/api/breachdirectory/pricing

#https://hashtoolkit.com/decrypt-hash/?hash=


user = input('username/Email: ')
url = "https://breachdirectory.p.rapidapi.com/"
querystring = {"func":"auto","term":""+user+""}
headers = {
	"X-RapidAPI-Key": "834670c200mshce353b6916ca399p13c22cjsn6ec017e033d8",
	"X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
info = json.loads(response.text)
print(info)
