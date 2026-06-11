import requests

url = "http://localhost:8080/api/users/login"

payload = {}

# auth=("Angelita_Batz@gmail.com","1234_Abcd")
# response = requests.request("GET", url, auth=("Angelita_Batz@gmail.com","1234_Abcd"), data=payload)
response = requests.get(url, auth= ("Constance_Kuhic60@yahoo.com","1234_Abcd"))

print(response.text)

