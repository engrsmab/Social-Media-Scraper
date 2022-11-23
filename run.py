from tkinter.tix import Form
import requests
ans = requests.get("http://azeementerprises.org/read_device_port/id=192100")
print(ans.text)