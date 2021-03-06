import json

import requests

class RestManager():
    def __init__(self, url=None):
        if url!=None:
            self.url = url

    def Post(self, data):
        return requests.post(data["url"], json=data["js"])

    def Get(self, data):
        data["url"] += data["apiParams"]
        return requests.get(data["url"], params=data["params"])

    def Put(self, data):
        pass

    def Delete(self, data):
        headers = {'content-type': 'application/json'}
        return requests.delete(data["url"], data=json.dumps(data["js"]), headers=headers)