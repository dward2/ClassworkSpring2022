import requests

# out_data = {
#    "name": "David Ward",
#    "net_id": "daw74",
#    "e-mail": "david.a.ward@duke.edu"
# }
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
# print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
