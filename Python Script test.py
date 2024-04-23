import json
import requests
import urllib3  # this disables warning about self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://restcountries.com/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response)  # response object
print(response.status_code)  # status code, success:200
countries = response.text
data_python = json.loads(countries)  # transfer to python format
country = input("enter country name, Capitalize the first letter: ")
for i in range(len(data_python)):
    if data_python[i]["name"] == country:
        print("It is the number " + str(i) + " in the countries list")
        print("The population is " + str(data_python[i]["population"]))
        print(data_python[i])
        break  # Force to quit from loop.
else:
    i += 1
if i == len(data_python):
    print("no this country")
