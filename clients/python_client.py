import requests

def get_url():
    return requests.get('http://127.0.0.1:8000/')

def post_url():
    resp = requests.post('http://127.0.0.1:8000/?name=gerry')
    return resp 

if __name__ == '__main__':
    print(get_url().json())