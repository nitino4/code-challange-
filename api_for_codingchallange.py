import requests

#SEND STRING
payload = {"status": "on/off"}
send_data = requests.post("https://httpbin.org/post", data=payload)

#SET STATUS
status_payload = {"status": "on"}
check_status = requests.put("https://httpbin.org/put", data=status_payload)

#check status
response = requests.get("https://httpbin.org/get", params=status_payload)
print(response.text)
print(type(response.text))

#update status
payload_update = {"status": "off"}
response_modify = requests.put("https://httpbin.org/put", data=payload_update)
print(response_modify.text)
