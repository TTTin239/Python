import requests
from win10toast import ToastNotifier
import json
import time
def Update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered : {data["recovered"]}'
    
    while True:
        t = ToastNotifier()
        t.show_toast("Covid 19 Update", text, duration = 20)
        time.sleep(160)    
Update()        