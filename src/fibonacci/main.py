from bottle import Bottle, request, response, run
#
from .fibonacci_math import get_fibonacci_value


app = Bottle()


@app.route('/api/fibonacci/<index>', method='GET')
def get_result(index: int):
    return {'value': get_fibonacci_value(int(index))}


def main():
    run(app, host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()
