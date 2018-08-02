from sanic import Sanic
from sanic.request import Request as SanicRequest
from sanic.response import json


class ConfigStorage:

    def __init__(self):
        self._configs = {
            'aplha.json': {'Name': 'Alpha', 'Host': '127.0.0.1'},
            'beta.json': {'Name': 'Beta', 'Host': '127.0.0.1'},
            'gamma.json': {'Name': 'Gamma', 'Host': '127.0.0.1'},
        }

    def list(self):
        return self._configs.keys()

    def get(self, name):
        return self._configs.get(name)

    def save(self, name, body):
        self._configs[name] = body


app = Sanic()
storage = ConfigStorage()


@app.route('/configs/', methods=['GET'])
async def list_all(request):
    return json(storage.list())


@app.route('/configs/<name>/', methods=['GET'])
async def list_one(request: SanicRequest, name):
    return json(storage.get(name))


@app.route('/configs/<name>/', methods=['POST', 'PATCH'])
async def list_one(request: SanicRequest, name):
    storage.save(name, request.json)
    return json({'ok': 'ok :)'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
