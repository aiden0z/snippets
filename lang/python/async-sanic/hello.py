from sanic import Sanic
from sanic.response import json

app = Sanic(name="test")


@app.route('/')
def test(request):
    return json({'hello': 'owrld'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, auto_reload=True)
