import requests

def BertQA2(question):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = "Delhi"
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    #print(format_add['temp'])
    return format_add['temp']

def BertQA1(question):
    api_address = 'http://52.172.51.143:8897/bertqa'
    headers = {
        'content-type': "application/json"
    }
    payload = {"question": question}
    response = requests.post(url=api_address, json=payload)
    return response.text

def BertQA(question):
    api_address = 'http://52.172.51.143:8896/bertqa'
    headers = {
        'content-type': "application/json"
    }
    payload = {"question": question}
    response = requests.post(url=api_address, json=payload)
    return response.text

#print(BertQA("who are you"))
